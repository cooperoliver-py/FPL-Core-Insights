#!/usr/bin/env python3
"""Compare models and frozen-origin forecast horizons on chronological folds."""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import HistGradientBoostingRegressor

if __package__:
    from . import fpl_predictions as p
else:
    import fpl_predictions as p


def legacy_features(rows):
    features = p._model_frame(rows).reindex(columns=p.BASE_MODEL_COLUMNS)
    for column in features:
        if f"legacy_{column}" in rows:
            features[column] = rows[f"legacy_{column}"].fillna(0) if column == "fixture_count" else rows[f"legacy_{column}"]
    return features


def summarize(rows, model, segment):
    result = {"model": model, "segment": segment, "rows": len(rows)}
    if rows.empty:
        return result
    result.update(p._metrics(rows["actual"], rows["prediction"]))
    result["mean_prediction"] = float(rows["prediction"].mean())
    result["mean_actual"] = float(rows["actual"].mean())
    top, captain = [], []
    for _, gameweek in rows.loc[rows["selectable"]].groupby("gw"):
        ranked = gameweek.sort_values(["prediction", "player_code"], ascending=[False, True])
        top.append(ranked.head(20)["actual"].mean())
        captain.append(ranked.iloc[0]["actual"])
    result["top20_actual"] = float(np.mean(top)) if top else None
    result["captain_actual"] = float(np.mean(captain)) if captain else None
    return result


def forecast_horizons(model, training, gameweek, fixtures_by_week, matches):
    """Freeze origin features; only fixture context and dated eligibility evolve."""
    origin = training.loc[training["gw"].eq(gameweek)].copy()
    as_of = origin["deadline_time"].iloc[0]
    ratings, promoted = p._deadline_elo(p.TRAIN_SEASON, matches, as_of)
    recovery = p.estimate_return_availability(training.loc[training["gw"].lt(gameweek)])
    results = []
    for target in range(gameweek, min(gameweek + 5, 39)):
        fixtures = fixtures_by_week[target]
        context = p._fixture_context(
            fixtures.assign(home_team_elo=np.nan, away_team_elo=np.nan), ratings, promoted
        )
        rows = origin.drop(columns=[column for column in context if column != "team_code"])
        rows = rows.merge(context, on="team_code", how="left", validate="many_to_one")
        rows["fixture_count"] = rows["fixture_count"].fillna(0)
        rows["promoted_elo_fallback"] = rows["promoted_elo_fallback"].fillna(0)
        rows = p._add_fixture_dates(rows, fixtures)
        rows["fixture_availability"] = p.availability_for_gameweek(
            rows, as_of, injury_return_probability=recovery["probability"],
            is_next_round=target == gameweek,
        )
        raw = model.predict(p._model_frame(rows))
        outcomes = training.loc[training["gw"].eq(target)].set_index("player_code")
        result = rows[["player_code", "fixture_count"]].copy()
        result["actual"] = result["player_code"].map(outcomes["event_points"])
        result["selectable"] = p._availability(rows).gt(0) & rows["fixture_count"].gt(0)
        result["origin_gameweek"], result["gw"], result["horizon"] = gameweek, target, target - gameweek + 1
        for name, scale in (("refined", True), ("refined_no_soft_scaling", False)):
            scored = result.assign(model=name, prediction=p._served_prediction(
                rows, raw, scale_availability=scale
            ))
            # Unobserved labels cannot be silently scored as a zero-point outcome.
            results.append(scored.dropna(subset=["actual"]))
    return pd.concat(results, ignore_index=True)


def evaluate(split, output_dir):
    training = p._load_training_data()
    weeks = range(16, 31) if split == "development" else range(31, 39) if split == "holdout" else range(16, 39)
    fixtures = {gw: p._read_csv(p._fixture_file(p.TRAIN_SEASON, gw)) for gw in range(1, 39)}
    matches, _ = p.load_match_data(p.DATA / p.TRAIN_SEASON)
    scored, horizon_scores = [], []
    for gameweek in weeks:
        train = training.loc[training["gw"].lt(gameweek)]
        test = training.loc[training["gw"].eq(gameweek)]
        # v1 used season-local ID order: preserve its random early-stopping split.
        legacy_train = train.sort_values(["id", "gw"], kind="mergesort")
        legacy = HistGradientBoostingRegressor(
            loss="squared_error", learning_rate=0.05, max_iter=200, max_leaf_nodes=15,
            min_samples_leaf=20, l2_regularization=0.1, random_state=42,
        ).fit(legacy_features(legacy_train), legacy_train["event_points"])
        core = HistGradientBoostingRegressor(**legacy.get_params()).fit(
            p._model_frame(train)[list(p.BASE_MODEL_COLUMNS)], train["event_points"]
        )
        refined = p._new_model().fit(p._model_frame(train), train["event_points"])
        raw = refined.predict(p._model_frame(test))
        predictions = {
            "legacy_context": p._served_prediction(test, legacy.predict(legacy_features(test))),
            "deadline_core": p._served_prediction(test, core.predict(p._model_frame(test)[list(p.BASE_MODEL_COLUMNS)])),
            "refined": p._served_prediction(test, raw),
            "refined_no_soft_scaling": p._served_prediction(test, raw, scale_availability=False),
            "rolling_5gw": p._served_prediction(test, test["event_points_lag5"].fillna(train["event_points"].mean())),
        }
        for name, values in predictions.items():
            rows = test[["gw", "player_code", "position", "minutes", "fixture_count", "history_count"]].copy()
            rows["model"], rows["actual"], rows["prediction"] = name, test["event_points"], values
            rows["selectable"] = p._availability(test).gt(0) & test["fixture_count"].gt(0)
            scored.append(rows)
        horizon_scores.append(forecast_horizons(refined, training, gameweek, fixtures, matches))
        print(f"Evaluated GW{gameweek}", flush=True)
    scored = pd.concat(scored, ignore_index=True)
    summaries, weekly = [], []
    for model, rows in scored.groupby("model", sort=False):
        segments = {
            "all": rows, "appeared": rows.loc[rows["minutes"].gt(0)],
            "double_gameweek": rows.loc[rows["fixture_count"].eq(2)],
            "low_history": rows.loc[rows["history_count"].lt(5)],
            **{position: rows.loc[rows["position"].eq(position)] for position in p.POSITION_COUNTS},
        }
        summaries.extend(summarize(frame, model, name) for name, frame in segments.items())
        for gameweek, frame in rows.groupby("gw"):
            weekly.append({"gameweek": int(gameweek), **summarize(frame, model, "all")})
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(summaries).to_csv(output_dir / "metrics.csv", index=False)
    pd.DataFrame(weekly).to_csv(output_dir / "by_gameweek.csv", index=False)
    horizons = pd.concat(horizon_scores, ignore_index=True)
    horizon_summary = [
        {"horizon": int(horizon), **summarize(rows, model, "all")}
        for (model, horizon), rows in horizons.groupby(["model", "horizon"], sort=True)
    ]
    pd.DataFrame(horizon_summary).to_csv(output_dir / "by_horizon.csv", index=False)
    pd.DataFrame([
        {"origin_gameweek": int(origin), "horizon": int(horizon), **summarize(rows, model, "all")}
        for (model, origin, horizon), rows in horizons.groupby(["model", "origin_gameweek", "horizon"], sort=True)
    ]).to_csv(output_dir / "horizon_by_gameweek.csv", index=False)
    source_hashes = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in Path(__file__).parent.glob("*.py")}
    metadata = {
        "split": split, "gameweeks": list(weeks), "data_revision": p._data_sha(),
        "sklearn_version": sklearn.__version__, "model_parameters": p._new_model().get_params(),
        "features": list(p.MODEL_COLUMNS), "source_sha256": source_hashes,
        "scope": "Expanding-window fitting, plus 1-5 week frozen-origin forecasts using production fixture availability. No current-season labels in these folds.",
        "snapshot_quarantine": "2025-2026 GW1 price, availability, news, ep_next and set-piece metadata masked; copied GW15 metadata must not inform GW2.",
        "limitations": [
            "Historical exports have no publication timestamps; completed match details are assumed available three hours after kickoff.",
            "legacy_context is a comparison on sanitized inputs, not an exact replay of the original model; it retains fixture-time Elo.",
            "Historical non-PL detail coverage stops in February 2026; unobserved workload remains missing, with record-count features.",
            "Future fixture schedules are final exports, not archived schedules as known at each origin. Only players with observed target labels are scored.",
            "These folds do not validate summer cold starts, live current-season refitting, or the squad/transfer optimizer. Overlapping horizons are not independent samples.",
            "Later folds have previously been inspected and are retrospective diagnostics, not an untouched holdout.",
        ],
    }
    (output_dir / "metadata.json").write_text(json.dumps(metadata, indent=2, default=str) + "\n")
    print(pd.DataFrame(summaries).query("segment == 'all'").to_string(index=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--split", choices=("development", "holdout", "all"), default="development")
    parser.add_argument("--output-dir", type=Path, default=p.ROOT / "predictions" / "evaluation")
    args = parser.parse_args()
    evaluate(args.split, args.output_dir)
