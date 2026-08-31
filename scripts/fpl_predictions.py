#!/usr/bin/env python3
"""Leakage-safe FPL forecasts, legal squad selection, and one-transfer advice."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable

os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")

import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix
from scipy.stats import spearmanr
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TRAIN_SEASON = "2025-2026"
HORIZON_WEIGHTS = (1.0, 0.9, 0.8, 0.7, 0.6)
LAG_WINDOWS = (3, 5)
RECENT_EWM_ALPHA = 0.35
RECENT_EWM_METRICS = ("event_points", "minutes", "starts", "expected_goal_involvements")
POSITION_COUNTS = {
    "Goalkeeper": 2,
    "Defender": 5,
    "Midfielder": 5,
    "Forward": 3,
}
LINEUP_LIMITS = {
    "Goalkeeper": (1, 1),
    "Defender": (3, 5),
    "Midfielder": (2, 5),
    "Forward": (1, 3),
}
UNAVAILABLE = {"i", "u", "s"}
RAW_METRICS = (
    "event_points",
    "minutes",
    "starts",
    "goals_scored",
    "assists",
    "clean_sheets",
    "bonus",
    "bps",
    "expected_goals",
    "expected_assists",
    "expected_goal_involvements",
    "expected_goals_conceded",
    "influence",
    "creativity",
    "threat",
    "ict_index",
    "saves",
    "defensive_contribution",
)
LAG_COLUMNS = tuple(f"{metric}_lag{window}" for metric in RAW_METRICS for window in LAG_WINDOWS)
RECENT_COLUMNS = ("minutes_lag1",) + tuple(f"{metric}_ewm" for metric in RECENT_EWM_METRICS)
MODEL_COLUMNS = LAG_COLUMNS + RECENT_COLUMNS + (
    "history_count",
    "cold_start",
    "now_cost",
    "availability",
    "fixture_count",
    "home_share",
    "team_elo",
    "opponent_elo",
    "elo_diff",
    "promoted_elo_fallback",
    "position_goalkeeper",
    "position_defender",
    "position_midfielder",
    "position_forward",
)


def calculate_selling_price(purchase_price: float, current_price: float) -> float:
    """Return the official FPL selling price, in millions."""
    try:
        purchase = float(purchase_price)
        current = float(current_price)
    except (TypeError, ValueError) as exc:
        raise ValueError("purchase_price and current_price must be numbers") from exc
    if not math.isfinite(purchase) or not math.isfinite(current) or min(purchase, current) < 0:
        raise ValueError("purchase_price and current_price must be finite and non-negative")
    purchase_tenths, current_tenths = round(purchase * 10), round(current * 10)
    selling_tenths = (
        current_tenths
        if current_tenths <= purchase_tenths
        else purchase_tenths + (current_tenths - purchase_tenths) // 2
    )
    return selling_tenths / 10


def validate_squad(squad, catalog: pd.DataFrame | None = None) -> bool:
    """Validate a 15-player FPL squad; raise ValueError and otherwise return True."""
    bank = 0.0
    if isinstance(squad, dict):
        if "bank" not in squad or "players" not in squad:
            raise ValueError("squad JSON must contain 'bank' and 'players'")
        try:
            bank = float(squad["bank"])
        except (TypeError, ValueError) as exc:
            raise ValueError("squad bank must be a number") from exc
        frame = pd.DataFrame(squad["players"])
    elif isinstance(squad, pd.DataFrame):
        frame = squad.copy()
    else:
        frame = pd.DataFrame(squad)

    if not math.isfinite(bank) or bank < 0:
        raise ValueError("squad bank must be finite and non-negative")
    if "player_code" not in frame:
        raise ValueError("squad players must contain player_code")
    if len(frame) != 15:
        raise ValueError(f"squad must contain exactly 15 players, found {len(frame)}")
    if frame["player_code"].isna().any() or frame["player_code"].duplicated().any():
        raise ValueError("squad player_code values must be present and unique")

    if catalog is not None:
        required_catalog = {"player_code", "position", "team_code"}
        missing = required_catalog - set(catalog.columns)
        if missing:
            raise ValueError(f"catalog is missing columns: {', '.join(sorted(missing))}")
        metadata = catalog.drop_duplicates("player_code").set_index("player_code")
        unknown = sorted(set(frame["player_code"]) - set(metadata.index))
        if unknown:
            raise ValueError(f"unknown player_code values: {unknown}")
        for column in ("position", "team_code"):
            if column not in frame:
                frame[column] = frame["player_code"].map(metadata[column])

    missing = {"position", "team_code"} - set(frame.columns)
    if missing:
        raise ValueError(f"squad is missing columns: {', '.join(sorted(missing))}")
    if frame[["position", "team_code"]].isna().any().any():
        raise ValueError("squad position and team_code values must be present")
    actual_positions = frame["position"].value_counts().to_dict()
    if actual_positions != POSITION_COUNTS:
        raise ValueError(f"illegal position counts: {actual_positions}; expected {POSITION_COUNTS}")
    crowded = frame["team_code"].value_counts()
    if not crowded.empty and crowded.max() > 3:
        raise ValueError("squad may contain at most three players from one club")
    if "purchase_price" in frame:
        prices = pd.to_numeric(frame["purchase_price"], errors="coerce")
        if prices.isna().any() or (~np.isfinite(prices)).any() or (prices < 0).any():
            raise ValueError("every purchase_price must be finite and non-negative")
    return True


def _linear_constraint(
    variable_count: int,
    rows: Iterable[tuple[dict[int, float], float, float]],
) -> LinearConstraint:
    row_ids: list[int] = []
    columns: list[int] = []
    values: list[float] = []
    lower: list[float] = []
    upper: list[float] = []
    for row_id, (coefficients, low, high) in enumerate(rows):
        for column, value in coefficients.items():
            row_ids.append(row_id)
            columns.append(column)
            values.append(value)
        lower.append(low)
        upper.append(high)
    matrix = coo_matrix(
        (values, (row_ids, columns)), shape=(len(lower), variable_count), dtype=float
    ).tocsr()
    return LinearConstraint(matrix, np.asarray(lower), np.asarray(upper))


def best_lineup(squad: pd.DataFrame, points_column: str) -> tuple[list[object], object]:
    """Return legal XI index labels and captain index label using SciPy MILP."""
    if len(squad) != 15 or "position" not in squad or points_column not in squad:
        raise ValueError("best_lineup needs 15 players plus position and the points column")
    if squad["position"].value_counts().to_dict() != POSITION_COUNTS:
        raise ValueError("best_lineup received illegal squad position counts")
    points = pd.to_numeric(squad[points_column], errors="coerce").fillna(0).to_numpy(float)
    if not np.isfinite(points).all():
        raise ValueError(f"{points_column} must contain finite values")

    count = len(squad)
    # Variables are XI[0:n] and captain[n:2n]. A tiny stable tie-break is harmless.
    tie_break = (count - np.arange(count)) * 1e-10
    objective = -np.concatenate((points + tie_break, points + tie_break))
    rows: list[tuple[dict[int, float], float, float]] = []
    rows.append(({i: 1.0 for i in range(count)}, 11, 11))
    for position, (low, high) in LINEUP_LIMITS.items():
        indices = np.flatnonzero(squad["position"].to_numpy() == position)
        rows.append(({int(i): 1.0 for i in indices}, low, high))
    excluded = squad.get("excluded", pd.Series(False, index=squad.index)).fillna(False).astype(bool)
    eligible_counts = squad.loc[~excluded, "position"].value_counts()
    can_avoid_excluded = (
        eligible_counts.get("Goalkeeper", 0) >= 1
        and all(eligible_counts.get(position, 0) >= low for position, (low, _) in LINEUP_LIMITS.items())
        and sum(
            min(eligible_counts.get(position, 0), high)
            for position, (_, high) in LINEUP_LIMITS.items()
        )
        >= 11
    )
    if excluded.any() and not can_avoid_excluded:
        raise ValueError("current squad cannot form a legal XI without excluded players")
    rows.extend(
        ({int(i): 1.0}, 0, 0) for i in np.flatnonzero(excluded.to_numpy())
    )
    rows.append(({count + i: 1.0 for i in range(count)}, 1, 1))
    rows.extend(({count + i: 1.0, i: -1.0}, -np.inf, 0) for i in range(count))
    if (~excluded).any():
        rows.extend(
            ({count + int(i): 1.0}, 0, 0) for i in np.flatnonzero(excluded.to_numpy())
        )
    result = milp(
        objective,
        integrality=np.ones(2 * count),
        bounds=Bounds(0, 1),
        constraints=_linear_constraint(2 * count, rows),
        options={"presolve": True},
    )
    if not result.success or result.x is None:
        raise RuntimeError(f"lineup optimization failed: {result.message}")
    lineup_positions = np.flatnonzero(result.x[:count] > 0.5)
    captain_position = int(np.argmax(result.x[count:]))
    labels = squad.index.to_numpy()
    return labels[lineup_positions].tolist(), labels[captain_position]


def _vice_captain(
    squad: pd.DataFrame, lineup: list[object], captain: object, points_column: str
) -> object:
    candidates = squad.loc[[index for index in lineup if index != captain]].sort_values(
        [points_column, "player_code"], ascending=[False, True], kind="mergesort"
    )
    if candidates.empty:
        raise ValueError("a vice-captain requires another player in the starting XI")
    return candidates.index[0]


def build_lagged_features(frame: pd.DataFrame, identity: str = "id") -> pd.DataFrame:
    """Add strictly shifted 3/5-GW rolling features to a player-GW frame."""
    missing = {identity, "gw"} - set(frame.columns)
    if missing:
        raise ValueError(f"lag input is missing columns: {', '.join(sorted(missing))}")
    result = frame.copy().sort_values([identity, "gw"], kind="mergesort").reset_index(drop=True)
    for metric in RAW_METRICS:
        if metric not in result:
            continue
        result[metric] = pd.to_numeric(result[metric], errors="coerce")
        shifted = result.groupby(identity, sort=False)[metric].shift(1)
        for window in LAG_WINDOWS:
            result[f"{metric}_lag{window}"] = shifted.groupby(
                result[identity], sort=False
            ).transform(lambda values: values.rolling(window, min_periods=1).mean())
        if metric == "minutes":
            result["minutes_lag1"] = shifted
        if metric in RECENT_EWM_METRICS:
            result[f"{metric}_ewm"] = shifted.groupby(
                result[identity], sort=False
            ).transform(
                lambda values: values.ewm(
                    alpha=RECENT_EWM_ALPHA, adjust=False, min_periods=1
                ).mean()
            )
    result["history_count"] = result.groupby(identity, sort=False).cumcount()
    result["cold_start"] = (result["history_count"] == 0).astype(int)
    result["data_coverage"] = result["history_count"].clip(upper=5) / 5
    result["availability_lag1"] = _availability(result).groupby(
        result[identity], sort=False
    ).shift(1)
    if "now_cost" in result:
        result["now_cost_lag1"] = pd.to_numeric(
            result["now_cost"], errors="coerce"
        ).groupby(result[identity], sort=False).shift(1)
    if "ep_next" in result:
        result["ep_next_lag"] = result.groupby(identity, sort=False)["ep_next"].shift(1)
    else:
        result["ep_next_lag"] = np.nan
    return result


def _read_csv(path: Path, required: Iterable[str] = ()) -> pd.DataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"required data file not found: {path}")
    frame = pd.read_csv(path, low_memory=False)
    missing = set(required) - set(frame.columns)
    if missing:
        raise ValueError(f"{path} is missing columns: {', '.join(sorted(missing))}")
    return frame


def _season_path(season: str) -> Path:
    if not re.fullmatch(r"\d{4}-\d{4}", season):
        raise ValueError("season must use YYYY-YYYY, for example 2026-2027")
    path = DATA / season
    if not path.is_dir():
        raise FileNotFoundError(f"season directory not found: {path}")
    return path


def _latest_season() -> str:
    seasons = sorted(
        path.name
        for path in DATA.iterdir()
        if path.is_dir()
        and re.fullmatch(r"\d{4}-\d{4}", path.name)
        and (path / "players.csv").is_file()
        and (path / "teams.csv").is_file()
    )
    if not seasons:
        raise FileNotFoundError(f"no season data found under {DATA}")
    return seasons[-1]


def _fixture_file(season: str, gameweek: int) -> Path:
    return (
        DATA
        / season
        / "By Tournament"
        / "Premier League"
        / f"GW{gameweek}"
        / "fixtures.csv"
    )


def _next_unfinished_gameweek(season: str) -> int:
    summaries_path = DATA / season / "gameweek_summaries.csv"
    if summaries_path.is_file():
        summaries = _read_csv(summaries_path, ("id", "is_next", "deadline_time"))
        next_mask = summaries["is_next"].fillna(False).astype(str).str.lower().eq("true")
        if next_mask.any():
            return int(pd.to_numeric(summaries.loc[next_mask, "id"], errors="raise").min())
        deadlines = pd.to_datetime(summaries["deadline_time"], errors="coerce", utc=True)
        future = deadlines > pd.Timestamp.now(tz="UTC")
        if future.any():
            first_future = deadlines.loc[future].idxmin()
            return int(summaries.loc[first_future, "id"])
    for gameweek in range(1, 39):
        fixtures = _read_csv(_fixture_file(season, gameweek), ("finished",))
        finished = fixtures["finished"].fillna(False).astype(str).str.lower().eq("true")
        if fixtures.empty or not finished.all():
            return gameweek
    raise ValueError(f"all Premier League gameweeks are finished for {season}; pass --gameweek")


def _incomplete_source_gameweeks(season: str, target_gameweek: int) -> list[dict[str, object]]:
    teams = _read_csv(_season_path(season) / "teams.csv", ("code", "short_name"))
    team_names = dict(zip(teams["code"].astype(int), teams["short_name"].astype(str)))
    incomplete: list[dict[str, object]] = []
    for gameweek in range(1, target_gameweek + 1):
        fixtures = _read_csv(
            _fixture_file(season, gameweek), ("home_team", "away_team", "finished")
        )
        finished = fixtures["finished"].fillna(False).astype(str).str.lower().eq("true")
        if finished.all():
            continue
        if gameweek == target_gameweek and not finished.any():
            continue
        unfinished = fixtures.loc[~finished, ["home_team", "away_team"]]
        codes = pd.concat([unfinished["home_team"], unfinished["away_team"]]).dropna().astype(int)
        incomplete.append(
            {
                "gameweek": gameweek,
                "finished": int(finished.sum()),
                "total": len(fixtures),
                "deferred_teams": sorted(team_names.get(code, str(code)) for code in set(codes)),
                "is_target": gameweek == target_gameweek,
            }
        )
    return incomplete


def _availability(frame: pd.DataFrame) -> pd.Series:
    if "availability_lag1" in frame:
        return pd.to_numeric(frame["availability_lag1"], errors="coerce").fillna(1.0).clip(0, 1)
    chance = pd.to_numeric(
        frame.get("chance_of_playing_next_round", pd.Series(np.nan, index=frame.index)),
        errors="coerce",
    )
    status = frame.get("status", pd.Series("a", index=frame.index)).fillna("a").astype(str)
    fallback = status.map({"a": 1.0, "d": 0.75, "i": 0.0, "u": 0.0, "s": 0.0, "n": 0.0})
    return (chance / 100).where(chance.notna(), fallback).fillna(0.5).clip(0, 1)


def _fixture_context(
    fixtures: pd.DataFrame,
    fallback_elo: dict[int, float],
    promoted_codes: set[int] | None = None,
) -> pd.DataFrame:
    required = {"home_team", "away_team", "home_team_elo", "away_team_elo"}
    missing = required - set(fixtures.columns)
    if missing:
        raise ValueError(f"fixture data is missing columns: {', '.join(sorted(missing))}")
    promoted_codes = promoted_codes or set()
    known_elos = np.asarray([value for value in fallback_elo.values() if np.isfinite(value)])
    if known_elos.size == 0:
        raise ValueError("no finite team Elo values are available for fallback")
    league_low, league_median = float(known_elos.min()), float(np.median(known_elos))

    def elo(code: int, raw) -> tuple[float, bool]:
        numeric = pd.to_numeric(pd.Series([raw]), errors="coerce").iloc[0]
        if pd.notna(numeric):
            return float(numeric), False
        if code in fallback_elo and np.isfinite(fallback_elo[code]):
            return float(fallback_elo[code]), False
        return (league_low if code in promoted_codes else league_median), code in promoted_codes

    records: list[dict[str, float | int]] = []
    for fixture in fixtures.itertuples(index=False):
        home_code, away_code = int(fixture.home_team), int(fixture.away_team)
        home_elo, home_promoted = elo(home_code, fixture.home_team_elo)
        away_elo, away_promoted = elo(away_code, fixture.away_team_elo)
        records.extend(
            (
                {
                    "team_code": home_code,
                    "fixture_count": 1,
                    "home_share": 1.0,
                    "team_elo": home_elo,
                    "opponent_elo": away_elo,
                    "elo_diff": home_elo - away_elo,
                    "promoted_elo_fallback": int(home_promoted or away_promoted),
                },
                {
                    "team_code": away_code,
                    "fixture_count": 1,
                    "home_share": 0.0,
                    "team_elo": away_elo,
                    "opponent_elo": home_elo,
                    "elo_diff": away_elo - home_elo,
                    "promoted_elo_fallback": int(home_promoted or away_promoted),
                },
            )
        )
    if not records:
        return pd.DataFrame(
            columns=(
                "team_code",
                "fixture_count",
                "home_share",
                "team_elo",
                "opponent_elo",
                "elo_diff",
                "promoted_elo_fallback",
            )
        )
    context = pd.DataFrame(records)
    return context.groupby("team_code", as_index=False).agg(
        fixture_count=("fixture_count", "sum"),
        home_share=("home_share", "mean"),
        team_elo=("team_elo", "mean"),
        opponent_elo=("opponent_elo", "mean"),
        elo_diff=("elo_diff", "mean"),
        promoted_elo_fallback=("promoted_elo_fallback", "max"),
    )


def _team_elo_map(teams: pd.DataFrame) -> dict[int, float]:
    required = {"code", "elo"}
    missing = required - set(teams.columns)
    if missing:
        raise ValueError(f"teams data is missing columns: {', '.join(sorted(missing))}")
    result: dict[int, float] = {}
    for row in teams[["code", "elo"]].itertuples(index=False):
        value = pd.to_numeric(pd.Series([row.elo]), errors="coerce").iloc[0]
        if pd.notna(value):
            result[int(row.code)] = float(value)
    return result


def _load_training_data() -> pd.DataFrame:
    parts: list[pd.DataFrame] = []
    for gameweek in range(1, 39):
        base = DATA / TRAIN_SEASON / "By Gameweek" / f"GW{gameweek}"
        stats = _read_csv(base / "player_gameweek_stats.csv", ("id", "gw", "event_points"))
        players = _read_csv(
            base / "players.csv",
            ("player_id", "player_code", "team_code", "position"),
        )
        if players["player_id"].duplicated().any():
            raise ValueError(f"duplicate player_id values in {base / 'players.csv'}")
        merged = stats.merge(
            players[["player_id", "player_code", "team_code", "position"]],
            left_on="id",
            right_on="player_id",
            how="left",
            validate="many_to_one",
        )
        if merged[["player_code", "team_code", "position"]].isna().any().any():
            raise ValueError(f"unmapped player rows in {base / 'player_gameweek_stats.csv'}")
        teams = _read_csv(base / "teams.csv", ("code", "elo"))
        fixtures = _read_csv(_fixture_file(TRAIN_SEASON, gameweek))
        context = _fixture_context(fixtures, _team_elo_map(teams))
        merged = merged.merge(context, on="team_code", how="left", validate="many_to_one")
        merged["fixture_count"] = merged["fixture_count"].fillna(0)
        parts.append(merged)
    training = pd.concat(parts, ignore_index=True)
    if training.duplicated(["id", "gw"]).any():
        raise ValueError("training data contains duplicate player_id/gameweek rows")
    for metric in RAW_METRICS:
        if metric not in training:
            training[metric] = 0.0
    return build_lagged_features(training, "id")


def _model_frame(frame: pd.DataFrame) -> pd.DataFrame:
    prepared = frame.copy()
    prepared["availability"] = _availability(prepared)
    if "now_cost_lag1" in prepared:
        prepared["now_cost"] = pd.to_numeric(prepared["now_cost_lag1"], errors="coerce")
    for position, suffix in (
        ("Goalkeeper", "goalkeeper"),
        ("Defender", "defender"),
        ("Midfielder", "midfielder"),
        ("Forward", "forward"),
    ):
        prepared[f"position_{suffix}"] = (prepared["position"] == position).astype(int)
    for column in MODEL_COLUMNS:
        if column not in prepared:
            prepared[column] = np.nan
    return prepared.loc[:, MODEL_COLUMNS].apply(pd.to_numeric, errors="coerce")


def _new_model() -> HistGradientBoostingRegressor:
    return HistGradientBoostingRegressor(
        loss="squared_error",
        learning_rate=0.05,
        max_iter=200,
        max_leaf_nodes=15,
        min_samples_leaf=20,
        l2_regularization=0.1,
        random_state=42,
    )


def _served_prediction(frame: pd.DataFrame, prediction) -> np.ndarray:
    adjusted = np.maximum(np.asarray(prediction, dtype=float), 0)
    adjusted *= _availability(frame).to_numpy(float)
    fixture_count = pd.to_numeric(frame["fixture_count"], errors="coerce").fillna(0).to_numpy(float)
    adjusted[fixture_count == 0] = 0
    return adjusted


def _metrics(actual: np.ndarray, predicted: np.ndarray) -> dict[str, float | None]:
    actual, predicted = np.asarray(actual, float), np.asarray(predicted, float)
    mae = float(mean_absolute_error(actual, predicted))
    rmse = float(np.sqrt(np.mean(np.square(actual - predicted))))
    correlation: float | None = None
    if len(actual) > 1 and np.std(actual) > 0 and np.std(predicted) > 0:
        value = spearmanr(actual, predicted, nan_policy="omit").statistic
        correlation = float(value) if np.isfinite(value) else None
    return {"mae": mae, "rmse": rmse, "spearman": correlation}


def _evaluate_and_fit(training: pd.DataFrame):
    target = pd.to_numeric(training["event_points"], errors="coerce")
    valid = target.notna()
    test_gameweeks = sorted(training.loc[valid & training["gw"].ge(31), "gw"].unique())
    if not test_gameweeks or not (valid & training["gw"].lt(test_gameweeks[0])).any():
        raise ValueError("held-out evaluation requires historical GWs 1-38")
    actual_parts: list[np.ndarray] = []
    model_parts: list[np.ndarray] = []
    rolling_parts: list[np.ndarray] = []
    ep_next_parts: list[np.ndarray] = []
    played_parts: list[np.ndarray] = []
    top20_actual: list[float] = []
    pool_actual: list[float] = []
    for gameweek in test_gameweeks:
        train_mask = valid & training["gw"].lt(gameweek)
        test_mask = valid & training["gw"].eq(gameweek)
        evaluation_model = _new_model().fit(
            _model_frame(training.loc[train_mask]), target[train_mask]
        )
        rows = training.loc[test_mask]
        actual = target[test_mask].to_numpy(float)
        model_prediction = _served_prediction(
            rows, evaluation_model.predict(_model_frame(rows))
        )
        rolling = pd.to_numeric(rows["event_points_lag5"], errors="coerce").fillna(
            target[train_mask].mean()
        )
        ep_next = pd.to_numeric(rows["ep_next_lag"], errors="coerce").fillna(rolling)
        rolling_prediction = _served_prediction(rows, rolling)
        ep_next_prediction = _served_prediction(rows, ep_next)
        actual_parts.append(actual)
        model_parts.append(model_prediction)
        rolling_parts.append(rolling_prediction)
        ep_next_parts.append(ep_next_prediction)
        played_parts.append(pd.to_numeric(rows["minutes"], errors="coerce").fillna(0).gt(0).to_numpy())
        selectable = (_availability(rows).gt(0) & rows["fixture_count"].gt(0)).to_numpy()
        if selectable.any():
            selectable_actual = actual[selectable]
            selectable_prediction = model_prediction[selectable]
            amount = min(20, len(selectable_actual))
            top = np.argpartition(selectable_prediction, -amount)[-amount:]
            top20_actual.append(float(selectable_actual[top].mean()))
            pool_actual.append(float(selectable_actual.mean()))
    actual = np.concatenate(actual_parts)
    model_prediction = np.concatenate(model_parts)
    rolling_prediction = np.concatenate(rolling_parts)
    ep_next_prediction = np.concatenate(ep_next_parts)
    played = np.concatenate(played_parts)
    evaluation = {
        "HistGradientBoosting": _metrics(actual, model_prediction),
        "Rolling points (5 GW)": _metrics(actual, rolling_prediction),
        "Lagged FPL ep_next": _metrics(actual, ep_next_prediction),
    }
    context = {
        "rows": len(actual),
        "zero_actual_pct": float(np.mean(actual == 0) * 100),
        "played_rows": int(played.sum()),
        "played": _metrics(actual[played], model_prediction[played]),
        "top20_actual_mean": float(np.mean(top20_actual)),
        "pool_actual_mean": float(np.mean(pool_actual)),
    }
    final_model = _new_model().fit(_model_frame(training.loc[valid]), target[valid])
    return final_model, evaluation, context


def _current_catalog(season: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    base = _season_path(season)
    players = _read_csv(
        base / "players.csv",
        ("player_code", "player_id", "team_code", "position", "web_name"),
    )
    stats = _read_csv(base / "playerstats.csv", ("id", "status", "now_cost"))
    if "gw" in stats:
        stats = stats.sort_values(["id", "gw"], kind="mergesort")
    stats = stats.drop_duplicates("id", keep="last")
    teams = _read_csv(base / "teams.csv", ("code", "name", "short_name"))
    if players["player_code"].duplicated().any() or players["player_id"].duplicated().any():
        raise ValueError(f"duplicate player identities in {base / 'players.csv'}")
    # Player identity belongs to players.csv; avoid duplicate snapshot name columns.
    stats = stats[["id", *[column for column in stats if column != "id" and column not in players]]]
    catalog = players.merge(stats, left_on="player_id", right_on="id", how="left", validate="one_to_one")
    catalog = catalog.merge(
        teams[["code", "name", "short_name"]],
        left_on="team_code",
        right_on="code",
        how="left",
        validate="many_to_one",
    ).rename(columns={"name": "team", "short_name": "team_short_name"})
    if catalog[["status", "now_cost", "team"]].isna().any().any():
        raise ValueError("current players could not be joined to playerstats/teams")
    catalog["now_cost"] = pd.to_numeric(catalog["now_cost"], errors="coerce")
    if catalog["now_cost"].isna().any() or (catalog["now_cost"] <= 0).any():
        raise ValueError("current player prices must be positive numbers")
    return catalog, teams


def _completed_current_history(season: str, target_gameweek: int) -> pd.DataFrame:
    if season == TRAIN_SEASON or target_gameweek <= 1:
        return pd.DataFrame()
    parts: list[pd.DataFrame] = []
    for gameweek in range(1, target_gameweek):
        fixtures = _read_csv(
            _fixture_file(season, gameweek), ("home_team", "away_team", "finished")
        )
        finished = fixtures["finished"].fillna(False).astype(str).str.lower().eq("true")
        if fixtures.empty or not finished.any():
            continue
        team_fixtures = pd.concat(
            (
                pd.DataFrame({"team_code": fixtures["home_team"], "finished": finished}),
                pd.DataFrame({"team_code": fixtures["away_team"], "finished": finished}),
            ),
            ignore_index=True,
        ).dropna(subset=["team_code"])
        complete_teams = set(
            team_fixtures.assign(team_code=team_fixtures["team_code"].astype(int))
            .groupby("team_code")["finished"]
            .all()
            .loc[lambda values: values]
            .index
        )
        if not complete_teams:
            continue
        base = DATA / season / "By Gameweek" / f"GW{gameweek}"
        stats = _read_csv(base / "player_gameweek_stats.csv", ("id", "gw"))
        players = _read_csv(base / "players.csv", ("player_id", "player_code", "team_code"))
        history = stats.merge(
            players[["player_id", "player_code", "team_code"]],
            left_on="id",
            right_on="player_id",
            how="left",
            validate="many_to_one",
        )
        parts.append(history.loc[history["team_code"].isin(complete_teams)])
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def _current_lags(
    catalog: pd.DataFrame,
    training: pd.DataFrame,
    season: str,
    target_gameweek: int,
) -> pd.DataFrame:
    prior = training.sort_values(["player_code", "gw"], kind="mergesort")
    prior_groups = {int(code): group for code, group in prior.groupby("player_code", sort=False)}
    current_history = _completed_current_history(season, target_gameweek)
    current_groups = (
        {int(player_id): group for player_id, group in current_history.groupby("id", sort=False)}
        if not current_history.empty
        else {}
    )
    records: list[dict[str, float | int]] = []
    for player in catalog[["player_id", "player_code"]].itertuples(index=False):
        if season == TRAIN_SEASON:
            history = prior.loc[(prior["id"] == player.player_id) & (prior["gw"] < target_gameweek)]
            current_season_matches = len(history)
        else:
            pieces = []
            previous = prior_groups.get(int(player.player_code))
            if previous is not None:
                pieces.append(previous)
            this_season = current_groups.get(int(player.player_id))
            if this_season is not None:
                pieces.append(this_season)
            history = pd.concat(pieces, ignore_index=True) if pieces else pd.DataFrame()
            current_season_matches = 0 if this_season is None else len(this_season)
        record: dict[str, float | int] = {"player_id": int(player.player_id)}
        record["history_count"] = len(history)
        record["current_season_matches"] = current_season_matches
        record["cold_start"] = int(history.empty)
        record["data_coverage"] = min(len(history), 5) / 5
        for metric in RAW_METRICS:
            values = (
                pd.to_numeric(history.get(metric, pd.Series(dtype=float)), errors="coerce")
                if not history.empty
                else pd.Series(dtype=float)
            )
            for window in LAG_WINDOWS:
                record[f"{metric}_lag{window}"] = (
                    float(values.tail(window).mean()) if values.notna().any() else np.nan
                )
            if metric == "minutes":
                record["minutes_lag1"] = float(values.iloc[-1]) if values.notna().any() else np.nan
            if metric in RECENT_EWM_METRICS:
                record[f"{metric}_ewm"] = (
                    float(
                        values.ewm(
                            alpha=RECENT_EWM_ALPHA, adjust=False, min_periods=1
                        ).mean().iloc[-1]
                    )
                    if values.notna().any()
                    else np.nan
                )
        ep_next = (
            pd.to_numeric(history.get("ep_next", pd.Series(dtype=float)), errors="coerce")
            if not history.empty
            else pd.Series(dtype=float)
        )
        record["ep_next_lag"] = float(ep_next.iloc[-1]) if len(ep_next) and pd.notna(ep_next.iloc[-1]) else np.nan
        records.append(record)
    return pd.DataFrame(records)


def _forecast(
    model: HistGradientBoostingRegressor,
    training: pd.DataFrame,
    season: str,
    gameweeks: list[int],
) -> pd.DataFrame:
    catalog, current_teams = _current_catalog(season)
    lags = _current_lags(catalog, training, season, gameweeks[0])
    forecast = catalog.merge(lags, on="player_id", how="left", validate="one_to_one")
    previous_teams = _read_csv(DATA / TRAIN_SEASON / "teams.csv", ("code", "elo"))
    previous_elos = _team_elo_map(previous_teams)
    current_codes = set(pd.to_numeric(current_teams["code"], errors="raise").astype(int))
    promoted_codes = current_codes - set(previous_elos)
    promoted_flags: list[pd.Series] = []
    future_columns: dict[str, np.ndarray] = {}

    for gameweek in gameweeks:
        fixtures = _read_csv(_fixture_file(season, gameweek))
        context = _fixture_context(fixtures, previous_elos, promoted_codes)
        features = forecast.merge(context, on="team_code", how="left", validate="many_to_one")
        features["fixture_count"] = features["fixture_count"].fillna(0)
        features["promoted_elo_fallback"] = features["promoted_elo_fallback"].fillna(0)
        prediction = _served_prediction(features, model.predict(_model_frame(features)))
        future_columns[f"GW{gameweek}_predicted_points"] = prediction
        promoted_flags.append(features["promoted_elo_fallback"])
        future_columns[f"_GW{gameweek}_elo_diff"] = features["elo_diff"].to_numpy()
        future_columns[f"_GW{gameweek}_fixture_count"] = features["fixture_count"].to_numpy()

    forecast = pd.concat(
        (forecast, pd.DataFrame(future_columns, index=forecast.index)), axis=1
    ).copy()
    weights = np.asarray(HORIZON_WEIGHTS[: len(gameweeks)])
    point_columns = [f"GW{gameweek}_predicted_points" for gameweek in gameweeks]
    forecast["weighted_score"] = forecast[point_columns].to_numpy(float) @ weights
    forecast["predicted_value"] = forecast["weighted_score"] / forecast["now_cost"]
    availability = _availability(forecast)
    has_next_fixture = forecast[f"_GW{gameweeks[0]}_fixture_count"].gt(0)
    rolling_baseline = pd.to_numeric(forecast["event_points_lag5"], errors="coerce").fillna(0)
    forecast["baseline_rolling_points"] = rolling_baseline * availability * has_next_fixture
    forecast["baseline_ep_next"] = pd.to_numeric(forecast["ep_next_lag"], errors="coerce").fillna(
        rolling_baseline
    ) * availability * has_next_fixture
    forecast["baseline"] = forecast["baseline_rolling_points"]
    affected = pd.concat(promoted_flags, axis=1).max(axis=1).fillna(0).astype(int)
    confidence = forecast["data_coverage"].fillna(0) * (0.75 if gameweeks[0] == 1 else 1.0)
    confidence *= np.where(affected.astype(bool), 0.85, 1.0)
    forecast["confidence_score"] = confidence.clip(0, 1)
    forecast["confidence"] = pd.cut(
        forecast["confidence_score"],
        bins=[-np.inf, 0.5, 0.8, np.inf],
        labels=["low", "medium", "high"],
        right=False,
    ).astype(str)
    forecast["promoted_elo_fallback"] = affected
    mean_elo_diff = forecast[[f"_GW{gameweek}_elo_diff" for gameweek in gameweeks]].mean(axis=1)
    forecast["drivers"] = [
        f"5-GW avg pts {points:.2f}; mins {minutes:.0f}; xGI {xgi:.2f}; "
        f"current GWs {current}; fixture Elo diff {elo:+.0f}"
        for points, minutes, xgi, current, elo in zip(
            forecast["event_points_lag5"].fillna(0),
            forecast["minutes_lag5"].fillna(0),
            forecast["expected_goal_involvements_lag5"].fillna(0),
            forecast["current_season_matches"].fillna(0).astype(int),
            mean_elo_diff.fillna(0),
        )
    ]
    return forecast


def _apply_exclusions(
    forecast: pd.DataFrame, excluded_codes: set[int], gameweeks: list[int]
) -> pd.DataFrame:
    result = forecast.copy()
    result["excluded"] = result["player_code"].astype(int).isin(excluded_codes)
    mask = result["excluded"]
    projection_columns = [
        *[f"GW{gameweek}_predicted_points" for gameweek in gameweeks],
        "weighted_score",
        "predicted_value",
        "baseline",
        "baseline_rolling_points",
        "baseline_ep_next",
        "confidence_score",
    ]
    result.loc[mask, projection_columns] = 0.0
    result.loc[mask, "confidence"] = "excluded"
    result.loc[mask, "drivers"] = "Excluded in squad.json; projection forced to zero"
    return result


def _select_initial_squad(forecast: pd.DataFrame, gameweeks: list[int]) -> list[object]:
    candidates = forecast.loc[
        (~forecast["status"].astype(str).isin(UNAVAILABLE)) & (~forecast["excluded"])
    ].copy()
    candidates = candidates.sort_values("player_code", kind="mergesort")
    count = len(candidates)
    if count < 15:
        raise ValueError("fewer than 15 selectable players are available")
    cost = candidates["now_cost"].to_numpy(float)
    horizon = len(gameweeks)
    variable_count = count * (1 + 2 * horizon)
    objective = np.zeros(variable_count)
    # Squad, XI, and captain variables. Only the latter two score material points.
    objective[:count] = -candidates["weighted_score"].to_numpy(float) * 1e-8
    for horizon_index, (gameweek, weight) in enumerate(
        zip(gameweeks, HORIZON_WEIGHTS[:horizon])
    ):
        points = candidates[f"GW{gameweek}_predicted_points"].to_numpy(float)
        lineup_offset = count * (1 + horizon_index)
        captain_offset = count * (1 + horizon + horizon_index)
        objective[lineup_offset : lineup_offset + count] = -weight * points
        objective[captain_offset : captain_offset + count] = -weight * points
    objective[:count] += cost * 1e-10 + np.arange(count) * 1e-12
    rows: list[tuple[dict[int, float], float, float]] = []
    rows.append(({i: 1.0 for i in range(count)}, 15, 15))
    for position, required in POSITION_COUNTS.items():
        indices = np.flatnonzero(candidates["position"].to_numpy() == position)
        rows.append(({int(i): 1.0 for i in indices}, required, required))
    for _, indices in candidates.groupby("team_code", sort=True).indices.items():
        rows.append(({int(i): 1.0 for i in indices}, 0, 3))
    rows.append(({i: float(cost[i]) for i in range(count)}, 0, 100.0 + 1e-9))
    for horizon_index in range(horizon):
        lineup_offset = count * (1 + horizon_index)
        captain_offset = count * (1 + horizon + horizon_index)
        rows.append(({lineup_offset + i: 1.0 for i in range(count)}, 11, 11))
        for position, (low, high) in LINEUP_LIMITS.items():
            indices = np.flatnonzero(candidates["position"].to_numpy() == position)
            rows.append(({lineup_offset + int(i): 1.0 for i in indices}, low, high))
        rows.append(({captain_offset + i: 1.0 for i in range(count)}, 1, 1))
        for i in range(count):
            rows.append(({lineup_offset + i: 1.0, i: -1.0}, -np.inf, 0))
            rows.append(
                ({captain_offset + i: 1.0, lineup_offset + i: -1.0}, -np.inf, 0)
            )
    result = milp(
        objective,
        integrality=np.ones(variable_count),
        bounds=Bounds(0, 1),
        constraints=_linear_constraint(variable_count, rows),
        options={"presolve": True},
    )
    if not result.success or result.x is None:
        raise RuntimeError(f"initial squad optimization failed: {result.message}")
    selected = candidates.index.to_numpy()[result.x[:count] > 0.5].tolist()
    squad = forecast.loc[selected]
    validate_squad(squad)
    if squad["now_cost"].sum() > 100.0 + 1e-8:
        raise RuntimeError("optimizer returned a squad above the £100m budget")
    return selected


def _resolve_user_squad(
    path: Path, catalog: pd.DataFrame
) -> tuple[pd.DataFrame, float, set[int]]:
    if not path.is_file():
        raise FileNotFoundError(f"squad file not found: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid squad JSON in {path}: {exc}") from exc
    validate_squad(payload, catalog)
    excluded = payload.get("excluded_player_codes", [])
    if not isinstance(excluded, list) or any(
        isinstance(code, bool) or not isinstance(code, int) for code in excluded
    ):
        raise ValueError("excluded_player_codes must be a list of integer player_code values")
    excluded_codes = set(excluded)
    if len(excluded_codes) != len(excluded):
        raise ValueError("excluded_player_codes must not contain duplicates")
    bank = float(payload["bank"])
    selections = pd.DataFrame(payload["players"])
    if "purchase_price" not in selections:
        raise ValueError("every squad player must contain purchase_price")
    columns = [
        "player_code",
        "player_id",
        "web_name",
        "team_code",
        "team",
        "position",
        "status",
        "now_cost",
    ]
    resolved = selections.merge(
        catalog[columns], on="player_code", how="left", validate="one_to_one"
    )
    resolved["purchase_price"] = pd.to_numeric(resolved["purchase_price"], errors="raise")
    resolved["selling_price"] = [
        calculate_selling_price(purchase, current)
        for purchase, current in zip(resolved["purchase_price"], resolved["now_cost"])
    ]
    return resolved, bank, excluded_codes


def _exact_lineup_score(squad: pd.DataFrame, points_column: str) -> float:
    points = pd.to_numeric(squad[points_column], errors="coerce").fillna(0).to_numpy(float)
    positions = squad["position"].to_numpy()
    ranked = {
        position: np.sort(points[positions == position])[::-1]
        for position in POSITION_COUNTS
    }
    best = -np.inf
    for defenders in range(3, 6):
        for midfielders in range(2, 6):
            forwards = 10 - defenders - midfielders
            if not 1 <= forwards <= 3:
                continue
            formation = (
                ("Goalkeeper", 1),
                ("Defender", defenders),
                ("Midfielder", midfielders),
                ("Forward", forwards),
            )
            selected = [ranked[position][:amount] for position, amount in formation]
            total = float(sum(values.sum() for values in selected) + max(values[0] for values in selected))
            best = max(best, total)
    if not np.isfinite(best):
        raise ValueError("no legal starting XI can be formed")
    return best


def _transfer_options(
    user_squad: pd.DataFrame,
    bank: float,
    forecast: pd.DataFrame,
    gameweeks: list[int],
) -> pd.DataFrame:
    point_columns = [f"GW{gameweek}_predicted_points" for gameweek in gameweeks]
    columns = [
        "player_code",
        "web_name",
        "team_code",
        "position",
        "status",
        "excluded",
        "now_cost",
        *point_columns,
    ]
    pool = forecast[columns].copy().set_index("player_code", drop=False)
    squad = user_squad.drop(columns=[column for column in point_columns if column in user_squad]).merge(
        forecast[["player_code", *point_columns]], on="player_code", how="left", validate="one_to_one"
    )
    weights = HORIZON_WEIGHTS[: len(gameweeks)]
    base_score = sum(
        weight * _exact_lineup_score(squad, column) for weight, column in zip(weights, point_columns)
    )
    squad_codes = set(squad["player_code"])
    club_counts = Counter(squad["team_code"])
    options: list[dict[str, float | int | str]] = []
    for outgoing_index, outgoing in squad.iterrows():
        selling_price = calculate_selling_price(outgoing["purchase_price"], outgoing["now_cost"])
        funds = bank + selling_price
        incoming_pool = pool.loc[
            (~pool.index.isin(squad_codes))
            & (pool["position"] == outgoing["position"])
            & (~pool["status"].astype(str).isin(UNAVAILABLE))
            & (~pool["excluded"])
            & (pool["now_cost"] <= funds + 1e-9)
        ].sort_index(kind="mergesort")
        for incoming in incoming_pool.itertuples(index=False):
            counts = club_counts.copy()
            counts[outgoing["team_code"]] -= 1
            counts[incoming.team_code] += 1
            if counts[incoming.team_code] > 3:
                continue
            replacement = squad.copy()
            for column in columns:
                replacement.at[outgoing_index, column] = getattr(incoming, column)
            new_score = sum(
                weight * _exact_lineup_score(replacement, column)
                for weight, column in zip(weights, point_columns)
            )
            options.append(
                {
                    "out_player_code": int(outgoing["player_code"]),
                    "out": outgoing["web_name"],
                    "in_player_code": int(incoming.player_code),
                    "in": incoming.web_name,
                    "selling_price": selling_price,
                    "buy_price": float(incoming.now_cost),
                    "bank_after": funds - float(incoming.now_cost),
                    "weighted_gain": new_score - base_score,
                }
            )
    if not options:
        return pd.DataFrame(
            columns=(
                "out_player_code",
                "out",
                "in_player_code",
                "in",
                "selling_price",
                "buy_price",
                "bank_after",
                "weighted_gain",
            )
        )
    return pd.DataFrame(options).sort_values(
        ["weighted_gain", "out_player_code", "in_player_code"],
        ascending=[False, True, True],
        kind="mergesort",
    ).reset_index(drop=True)


def _data_sha() -> str:
    override = os.environ.get("FPL_DATA_SHA", "").strip()
    if override:
        return override
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def _markdown_table(headers: list[str], rows: Iterable[Iterable[object]]) -> str:
    def clean(value: object) -> str:
        if value is None or (isinstance(value, float) and np.isnan(value)):
            return "n/a"
        return str(value).replace("|", "\\|").replace("\n", " ")

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend("| " + " | ".join(clean(value) for value in row) + " |" for row in rows)
    return "\n".join(lines)


def _render_markdown(
    forecast: pd.DataFrame,
    evaluation: dict[str, dict[str, float | None]],
    season: str,
    gameweeks: list[int],
    recommended_codes: set[int],
    transfers: pd.DataFrame | None,
    evaluation_context: dict[str, object] | None = None,
    incomplete_source: list[dict[str, object]] | None = None,
    live_performance: pd.DataFrame | None = None,
) -> str:
    point_columns = [f"GW{gameweek}_predicted_points" for gameweek in gameweeks]
    lines = [
        f"# FPL predictions: {season}, GW{gameweeks[0]}",
        "",
        f"Last generated: {datetime.now(UTC):%Y-%m-%d %H:%M UTC}",
        "",
        f"Data commit: `{_data_sha()}`",
        "",
        "## Data freshness",
        "",
    ]
    if incomplete_source:
        lines.append("**⚠️ Some relevant Premier League fixtures are not complete.**")
        lines.append("")
        for progress in incomplete_source:
            deferred = ", ".join(progress["deferred_teams"])
            if progress.get("is_target"):
                lines.append(
                    f"- GW{progress['gameweek']}: {progress['finished']}/{progress['total']} fixtures "
                    "finished. This forecast targets a Gameweek already under way; played results "
                    "are not used because they were unavailable at its deadline."
                )
            else:
                lines.append(
                    f"- GW{progress['gameweek']}: {progress['finished']}/{progress['total']} fixtures "
                    f"finished. Completed clubs contribute current-season form; {deferred} are deferred."
                )
        lines.extend(
            (
                "",
                "Incomplete Gameweeks are not scored in live performance reporting until the "
                "official data is finished and checked.",
                "",
            )
        )
    else:
        lines.extend(
            (
                f"All scheduled Premier League fixtures before GW{gameweeks[0]} are complete.",
                "",
            )
        )
    lines.extend(
        (
        "The model is fitted on canonical 2025/26 data; completed 2026/27 results update strictly "
        "lagged 3/5-GW and exponentially weighted recent form. Five-GW forecast weights are "
        f"{list(HORIZON_WEIGHTS[:len(gameweeks)])}; price and availability are held constant.",
        "",
        "## Walk-forward evaluation (historical GWs 31-38)",
        "",
        _markdown_table(
            ["Method", "MAE", "RMSE", "Spearman"],
            (
                (
                    name,
                    f"{values['mae']:.3f}",
                    f"{values['rmse']:.3f}",
                    "n/a" if values["spearman"] is None else f"{values['spearman']:.3f}",
                )
                for name, values in evaluation.items()
            ),
        ),
        "",
        )
    )
    if evaluation_context:
        played = evaluation_context["played"]
        played_spearman = (
            "n/a" if played["spearman"] is None else f"{played['spearman']:.3f}"
        )
        lines.extend(
            (
                f"Evaluation covers {evaluation_context['rows']:,} player-Gameweeks; "
                f"{evaluation_context['zero_actual_pct']:.1f}% scored zero. Among "
                f"{evaluation_context['played_rows']:,} appearances, model MAE is "
                f"{played['mae']:.3f} and Spearman is {played_spearman}.",
                "",
                f"The predicted top 20 averaged {evaluation_context['top20_actual_mean']:.2f} "
                f"actual points versus {evaluation_context['pool_actual_mean']:.2f} for the "
                "selectable pool.",
                "",
            )
        )
    lines.extend(("## Live-season performance", ""))
    if live_performance is None or live_performance.empty:
        lines.extend(
            (
                "No completed archived Gameweek forecast is available yet. Forecasts are only "
                "scored after official data is finished and checked.",
                "",
            )
        )
    else:
        lines.extend(
            (
                _markdown_table(
                    ["GW", "MAE", "RMSE", "Spearman", "Top 20", "Pool", "XI + captain", "FPL avg"],
                    (
                        (
                            int(row.gameweek),
                            f"{row.model_mae:.3f}",
                            f"{row.model_rmse:.3f}",
                            "n/a" if pd.isna(row.model_spearman) else f"{row.model_spearman:.3f}",
                            f"{row.top20_actual_mean:.2f}",
                            f"{row.pool_actual_mean:.2f}",
                            f"{row.optimal_xi_captain_points:.0f}",
                            "n/a" if pd.isna(row.fpl_average) else f"{row.fpl_average:.0f}",
                        )
                        for row in live_performance.itertuples(index=False)
                    ),
                ),
                "",
                "XI + captain is measured before autosubs; archived exclusions are omitted from "
                "forecast-skill metrics.",
                "",
            )
        )
    if gameweeks[0] == 1:
        lines.extend(
            (
                "## GW1 confidence",
                "",
                "GW1 confidence is deliberately capped below `high`: returning players carry "
                "2025/26 history by `player_code`, while new players are marked cold starts. "
                "Blank current Elo uses 2025/26 club Elo; promoted clubs use the prior league-low "
                "Elo and are explicitly flagged.",
                "",
            )
        )
    top = forecast.loc[~forecast["excluded"]].sort_values(
        [point_columns[0], "player_code"], ascending=[False, True], kind="mergesort"
    ).head(20)
    lines.extend(
        (
            f"## Top GW{gameweeks[0]} player forecasts",
            "",
            _markdown_table(
                [
                    "Player",
                    "Club",
                    "Pos",
                    *[f"GW{gw}" for gw in gameweeks],
                    "5GW score",
                    "5GW value",
                    "Confidence",
                    "Raw drivers",
                ],
                (
                    (
                        row.web_name,
                        row.team_short_name,
                        row.position,
                        *[f"{getattr(row, column):.2f}" for column in point_columns],
                        f"{row.weighted_score:.2f}",
                        f"{row.predicted_value:.2f}",
                        row.confidence,
                        row.drivers,
                    )
                    for row in top.itertuples(index=False)
                ),
            ),
            "",
            "Raw drivers are descriptive inputs, not SHAP or causal attributions.",
            "",
        )
    )
    squads = [("ML-optimal £100m squad", forecast["player_code"].isin(recommended_codes), "")]
    if transfers is not None:
        squads.append(("Your current squad", forecast["current_squad"], "current_"))
    for title, selected, prefix in squads:
        squad = forecast.loc[selected].sort_values(
            ["position", "weighted_score", "player_code"],
            ascending=[True, False, True],
            kind="mergesort",
        )
        lines.extend(
            (
                f"## {title}",
                "",
                _markdown_table(
                    [
                        "Player",
                        "Club",
                        "Position",
                        "Cost",
                        "Weighted score",
                        "Starts",
                        "Captains",
                        "Vice-captains",
                    ],
                    (
                        (
                            row.web_name,
                            row.team_short_name,
                            row.position,
                            f"£{row.now_cost:.1f}m",
                            f"{row.weighted_score:.2f}",
                            ", ".join(
                                f"GW{gw}"
                                for gw in gameweeks
                                if getattr(row, f"{prefix}GW{gw}_lineup")
                            ) or "Bench",
                            ", ".join(
                                f"GW{gw}"
                                for gw in gameweeks
                                if getattr(row, f"{prefix}GW{gw}_captain")
                            ) or "—",
                            ", ".join(
                                f"GW{gw}"
                                for gw in gameweeks
                                if getattr(row, f"{prefix}GW{gw}_vice_captain")
                            ) or "—",
                        )
                        for row in squad.itertuples(index=False)
                    ),
                ),
                "",
                f"Squad cost: £{squad['now_cost'].sum():.1f}m.",
                "",
            )
        )
    if transfers is not None:
        lines.extend(("## One-transfer recommendation", ""))
        if transfers.empty or transfers.iloc[0]["weighted_gain"] <= 1e-9:
            lines.extend(("**HOLD** — no legal same-position swap has a positive projected gain.", ""))
        else:
            best = transfers.iloc[0]
            lines.extend(
                (
                    f"**{best['out']} → {best['in']}** (projected weighted XI+captain gain "
                    f"{best['weighted_gain']:.2f}).",
                    "",
                )
            )
        lines.extend(
            (
                _markdown_table(
                    ["Out", "In", "Sell", "Buy", "Bank after", "XI+captain gain"],
                    (
                        (
                            row.out,
                            row["in"],
                            f"£{row.selling_price:.1f}m",
                            f"£{row.buy_price:.1f}m",
                            f"£{row.bank_after:.1f}m",
                            f"{row.weighted_gain:.2f}",
                        )
                        for _, row in transfers.head(10).iterrows()
                    ),
                ),
                "",
            )
        )
    lines.extend(
        (
            "## Limits",
            "",
            "Predictions are estimates, not guarantees. The model does not use chips, transfer hits, "
            "price-change forecasts, recursive future form, or a UI.",
            "",
        )
    )
    return "\n".join(lines)


PERFORMANCE_COLUMNS = (
    "season",
    "gameweek",
    "data_commit_sha",
    "players",
    "appeared",
    "zero_actual_pct",
    "model_mae",
    "model_rmse",
    "model_spearman",
    "rolling_mae",
    "rolling_rmse",
    "rolling_spearman",
    "ep_next_mae",
    "ep_next_rmse",
    "ep_next_spearman",
    "appeared_model_mae",
    "appeared_model_spearman",
    "top20_actual_mean",
    "pool_actual_mean",
    "optimal_xi_captain_points",
    "current_xi_captain_points",
    "fpl_average",
)


def _truth(values: pd.Series) -> pd.Series:
    return values.fillna(False).astype(str).str.lower().eq("true")


def _squad_actual_points(frame: pd.DataFrame, prefix: str, gameweek: int) -> float | None:
    lineup_column = f"{prefix}GW{gameweek}_lineup"
    captain_column = f"{prefix}GW{gameweek}_captain"
    vice_column = f"{prefix}GW{gameweek}_vice_captain"
    if lineup_column not in frame or not _truth(frame[lineup_column]).any():
        return None
    lineup = _truth(frame[lineup_column])
    captain = frame.loc[_truth(frame[captain_column])]
    vice = frame.loc[_truth(frame[vice_column])]
    captain_bonus = 0.0
    if not captain.empty and float(captain.iloc[0]["minutes"]) > 0:
        captain_bonus = float(captain.iloc[0]["actual_points"])
    elif not vice.empty and float(vice.iloc[0]["minutes"]) > 0:
        captain_bonus = float(vice.iloc[0]["actual_points"])
    return float(frame.loc[lineup, "actual_points"].sum() + captain_bonus)


def _live_performance(output_dir: Path, season: str) -> pd.DataFrame:
    archive_dir = output_dir / "archive" / season
    summaries = _read_csv(
        _season_path(season) / "gameweek_summaries.csv",
        ("id", "finished", "data_checked", "average_entry_score"),
    ).set_index("id")
    records: list[dict[str, object]] = []
    for path in sorted(archive_dir.glob("GW*.csv")) if archive_dir.is_dir() else []:
        match = re.fullmatch(r"GW(\d+)\.csv", path.name)
        if not match:
            continue
        gameweek = int(match.group(1))
        if gameweek not in summaries.index:
            continue
        summary = summaries.loc[gameweek]
        if not _truth(pd.Series([summary["finished"]])).iloc[0] or not _truth(
            pd.Series([summary["data_checked"]])
        ).iloc[0]:
            continue
        archived = _read_csv(
            path,
            (
                "player_id",
                f"GW{gameweek}_predicted_points",
                "baseline_rolling_points",
                "baseline_ep_next",
            ),
        )
        actual = _read_csv(
            DATA / season / "By Gameweek" / f"GW{gameweek}" / "player_gameweek_stats.csv",
            ("id", "event_points", "minutes"),
        )[["id", "event_points", "minutes"]]
        scored = archived.merge(
            actual,
            left_on="player_id",
            right_on="id",
            how="inner",
            validate="one_to_one",
        ).rename(columns={"event_points": "actual_points"})
        excluded = _truth(scored["excluded"]) if "excluded" in scored else pd.Series(False, index=scored.index)
        skill = scored.loc[~excluded].copy()
        observed = pd.to_numeric(skill["actual_points"], errors="raise").to_numpy(float)
        model = pd.to_numeric(
            skill[f"GW{gameweek}_predicted_points"], errors="raise"
        ).to_numpy(float)
        rolling = pd.to_numeric(skill["baseline_rolling_points"], errors="raise").to_numpy(float)
        ep_next = pd.to_numeric(skill["baseline_ep_next"], errors="raise").to_numpy(float)
        model_metrics = _metrics(observed, model)
        rolling_metrics = _metrics(observed, rolling)
        ep_next_metrics = _metrics(observed, ep_next)
        appeared = pd.to_numeric(skill["minutes"], errors="coerce").fillna(0).gt(0).to_numpy()
        appeared_metrics = _metrics(observed[appeared], model[appeared])
        fixtures = _read_csv(_fixture_file(season, gameweek), ("home_team", "away_team"))
        fixture_teams = set(
            pd.concat([fixtures["home_team"], fixtures["away_team"]]).dropna().astype(int)
        )
        selectable = ~skill.get("status", pd.Series("a", index=skill.index)).astype(str).isin(
            UNAVAILABLE
        ) & pd.to_numeric(skill["team_code"], errors="coerce").isin(fixture_teams)
        pool = skill.loc[selectable]
        top = pool.nlargest(min(20, len(pool)), f"GW{gameweek}_predicted_points")
        records.append(
            {
                "season": season,
                "gameweek": gameweek,
                "data_commit_sha": str(archived.get("data_commit_sha", pd.Series(["unknown"])).iloc[0]),
                "players": len(skill),
                "appeared": int(appeared.sum()),
                "zero_actual_pct": float(np.mean(observed == 0) * 100),
                "model_mae": model_metrics["mae"],
                "model_rmse": model_metrics["rmse"],
                "model_spearman": model_metrics["spearman"],
                "rolling_mae": rolling_metrics["mae"],
                "rolling_rmse": rolling_metrics["rmse"],
                "rolling_spearman": rolling_metrics["spearman"],
                "ep_next_mae": ep_next_metrics["mae"],
                "ep_next_rmse": ep_next_metrics["rmse"],
                "ep_next_spearman": ep_next_metrics["spearman"],
                "appeared_model_mae": appeared_metrics["mae"],
                "appeared_model_spearman": appeared_metrics["spearman"],
                "top20_actual_mean": float(top["actual_points"].mean()),
                "pool_actual_mean": float(pool["actual_points"].mean()),
                "optimal_xi_captain_points": _squad_actual_points(scored, "", gameweek),
                "current_xi_captain_points": _squad_actual_points(scored, "current_", gameweek),
                "fpl_average": pd.to_numeric(summary["average_entry_score"], errors="coerce"),
            }
        )
    return pd.DataFrame(records, columns=PERFORMANCE_COLUMNS)


def _before_gameweek_deadline(
    season: str, gameweek: int, now: pd.Timestamp | None = None
) -> bool:
    summaries = _read_csv(
        _season_path(season) / "gameweek_summaries.csv", ("id", "deadline_time")
    )
    deadline = pd.to_datetime(
        summaries.loc[summaries["id"].eq(gameweek), "deadline_time"], errors="coerce", utc=True
    )
    current = now if now is not None else pd.Timestamp.now(tz="UTC")
    return len(deadline) == 1 and pd.notna(deadline.iloc[0]) and current < deadline.iloc[0]


def _write_outputs(
    forecast: pd.DataFrame,
    markdown: str,
    output_dir: Path,
    gameweeks: list[int],
    season: str,
    live_performance: pd.DataFrame,
) -> tuple[Path, Path]:
    identity = [
        "data_commit_sha",
        "player_code",
        "player_id",
        "first_name",
        "second_name",
        "web_name",
        "team_code",
        "team",
        "team_short_name",
        "position",
        "status",
        "excluded",
        "now_cost",
        "selected_by_percent",
    ]
    identity = [column for column in identity if column in forecast]
    point_columns = [f"GW{gameweek}_predicted_points" for gameweek in gameweeks]
    decision_columns = ["recommended_squad", "current_squad"]
    for gameweek in gameweeks:
        decision_columns.extend(
            (
                f"GW{gameweek}_lineup",
                f"GW{gameweek}_captain",
                f"GW{gameweek}_vice_captain",
                f"current_GW{gameweek}_lineup",
                f"current_GW{gameweek}_captain",
                f"current_GW{gameweek}_vice_captain",
            )
        )
    columns = identity + point_columns + [
        "weighted_score",
        "predicted_value",
        "confidence",
        "confidence_score",
        "data_coverage",
        "current_season_matches",
        "cold_start",
        "promoted_elo_fallback",
        "baseline",
        "baseline_rolling_points",
        "baseline_ep_next",
        "drivers",
        *decision_columns,
    ]
    output = forecast.loc[:, columns].sort_values(
        ["weighted_score", "player_code"], ascending=[False, True], kind="mergesort"
    )
    numeric = [
        *point_columns,
        "weighted_score",
        "predicted_value",
        "confidence_score",
        "data_coverage",
        "baseline",
        "baseline_rolling_points",
        "baseline_ep_next",
    ]
    output[numeric] = output[numeric].round(4)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path, markdown_path = output_dir / "latest.csv", output_dir / "latest.md"
    csv_temp, markdown_temp = output_dir / ".latest.csv.tmp", output_dir / ".latest.md.tmp"
    output.to_csv(csv_temp, index=False, lineterminator="\n")
    markdown_temp.write_text(markdown, encoding="utf-8", newline="\n")
    csv_temp.replace(csv_path)
    markdown_temp.replace(markdown_path)
    performance_path = output_dir / "performance.csv"
    performance_temp = output_dir / ".performance.csv.tmp"
    performance_output = live_performance.copy()
    performance_numeric = performance_output.select_dtypes(include="number").columns
    performance_output[performance_numeric] = performance_output[performance_numeric].round(4)
    performance_output.to_csv(performance_temp, index=False, lineterminator="\n")
    performance_temp.replace(performance_path)
    if _before_gameweek_deadline(season, gameweeks[0]):
        archive_dir = output_dir / "archive" / season
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_path = archive_dir / f"GW{gameweeks[0]:02d}.csv"
        archive_temp = archive_dir / f".GW{gameweeks[0]:02d}.csv.tmp"
        output.to_csv(archive_temp, index=False, lineterminator="\n")
        archive_temp.replace(archive_path)
    return csv_path, markdown_path


def run(
    season: str | None = None,
    gameweek: int | None = None,
    squad_path: Path | None = None,
    output_dir: Path = ROOT / "predictions",
) -> tuple[Path, Path]:
    latest_season = _latest_season()
    season = season or latest_season
    if season != latest_season:
        raise ValueError(
            "historical season replay is not supported; use the latest data season to avoid look-ahead bias"
        )
    _season_path(season)
    gameweek = _next_unfinished_gameweek(season) if gameweek is None else gameweek
    if not 1 <= gameweek <= 38:
        raise ValueError("gameweek must be between 1 and 38")
    gameweeks = list(range(gameweek, min(gameweek + 5, 39)))

    training = _load_training_data()
    model, evaluation, evaluation_context = _evaluate_and_fit(training)
    forecast = _forecast(model, training, season, gameweeks)
    user_squad = None
    bank = 0.0
    excluded_codes: set[int] = set()
    if squad_path is not None:
        user_squad, bank, excluded_codes = _resolve_user_squad(squad_path, forecast)
        user_squad["excluded"] = user_squad["player_code"].astype(int).isin(excluded_codes)
    forecast = _apply_exclusions(forecast, excluded_codes, gameweeks)
    selected_indices = _select_initial_squad(forecast, gameweeks)
    recommended = forecast.loc[selected_indices]
    recommended_codes = set(recommended["player_code"].astype(int))
    forecast["data_commit_sha"] = _data_sha()
    forecast["recommended_squad"] = forecast["player_code"].astype(int).isin(recommended_codes)
    forecast["current_squad"] = False
    for gameweek_value in gameweeks:
        column = f"GW{gameweek_value}_predicted_points"
        lineup, captain = best_lineup(recommended, column)
        vice_captain = _vice_captain(recommended, lineup, captain, column)
        lineup_codes = set(forecast.loc[lineup, "player_code"].astype(int))
        captain_code = int(forecast.at[captain, "player_code"])
        vice_captain_code = int(forecast.at[vice_captain, "player_code"])
        forecast[f"GW{gameweek_value}_lineup"] = forecast["player_code"].astype(int).isin(lineup_codes)
        forecast[f"GW{gameweek_value}_captain"] = forecast["player_code"].astype(int).eq(captain_code)
        forecast[f"GW{gameweek_value}_vice_captain"] = forecast["player_code"].astype(int).eq(
            vice_captain_code
        )
        forecast[f"current_GW{gameweek_value}_lineup"] = False
        forecast[f"current_GW{gameweek_value}_captain"] = False
        forecast[f"current_GW{gameweek_value}_vice_captain"] = False

    transfers = None
    if user_squad is not None:
        user_codes = set(user_squad["player_code"].astype(int))
        forecast["current_squad"] = forecast["player_code"].astype(int).isin(user_codes)
        user_squad = user_squad.merge(
            forecast[["player_code", *[f"GW{gw}_predicted_points" for gw in gameweeks]]],
            on="player_code",
            how="left",
            validate="one_to_one",
        )
        for gameweek_value in gameweeks:
            column = f"GW{gameweek_value}_predicted_points"
            lineup, captain = best_lineup(user_squad, column)
            vice_captain = _vice_captain(user_squad, lineup, captain, column)
            lineup_codes = set(user_squad.loc[lineup, "player_code"].astype(int))
            captain_code = int(user_squad.at[captain, "player_code"])
            vice_captain_code = int(user_squad.at[vice_captain, "player_code"])
            forecast[f"current_GW{gameweek_value}_lineup"] = forecast["player_code"].astype(int).isin(
                lineup_codes
            )
            forecast[f"current_GW{gameweek_value}_captain"] = forecast["player_code"].astype(int).eq(
                captain_code
            )
            forecast[f"current_GW{gameweek_value}_vice_captain"] = forecast[
                "player_code"
            ].astype(int).eq(vice_captain_code)
        transfers = _transfer_options(user_squad, bank, forecast, gameweeks)

    incomplete_source = _incomplete_source_gameweeks(season, gameweek)
    live_performance = _live_performance(output_dir, season)
    markdown = _render_markdown(
        forecast,
        evaluation,
        season,
        gameweeks,
        recommended_codes,
        transfers,
        evaluation_context=evaluation_context,
        incomplete_source=incomplete_source,
        live_performance=live_performance,
    )
    return _write_outputs(
        forecast, markdown, output_dir, gameweeks, season, live_performance
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--season", help="latest data season in YYYY-YYYY form (default: auto-detect)")
    parser.add_argument(
        "--gameweek", type=int, help="first gameweek to forecast (default: next editable/upcoming)"
    )
    parser.add_argument("--squad", type=Path, help="optional current-squad JSON file")
    parser.add_argument(
        "--output-dir", type=Path, default=ROOT / "predictions", help="output directory"
    )
    args = parser.parse_args(argv)
    if args.squad is None and (ROOT / "squad.json").is_file():
        args.squad = ROOT / "squad.json"
    try:
        csv_path, markdown_path = run(
            args.season, args.gameweek, args.squad, args.output_dir
        )
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        parser.error(str(exc))
    print(f"Wrote {csv_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
