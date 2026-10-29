"""Public forecast snapshots and private analysis using the existing FPL engine."""
from datetime import UTC, datetime
import hashlib
import json
import math
from pathlib import Path
import re

import pandas as pd
try:
    from scripts import fpl_predictions as engine
except ModuleNotFoundError:
    import fpl_predictions as engine

LIMITS = ["Predictions are estimates, not guarantees.", "No chips, transfer hits, predicted price changes or recursive future form.", "Live XI scores are measured before autosubs; frozen forecasts may use older model versions."]


def records(frame):
    return json.loads(frame.to_json(orient="records", date_format="iso"))


def write_snapshot(forecast, season, gameweeks, evaluation, context, freshness, performance, output_dir):
    # Public snapshots are built before any owner-specific projection changes.
    private = [c for c in forecast if c in {"excluded", "purchase_price", "selling_price", "bank", "current_squad", "recommended_squad"} or re.match(r"(?:current_)?GW\d+_(?:lineup|captain|vice_captain)$", c)]
    players = records(forecast.drop(columns=private))
    generated = datetime.now(UTC).isoformat()
    summary_path = engine.DATA / season / "gameweek_summaries.csv"
    summary = pd.read_csv(summary_path).set_index("id") if summary_path.exists() else pd.DataFrame()
    deadline = str(summary.loc[gameweeks[0], "deadline_time"]) if gameweeks[0] in summary.index else None
    snapshot = dict(schema_version=1, season=season, gameweeks=gameweeks, generated_at=generated,
                    deadline=deadline, weights=list(engine.HORIZON_WEIGHTS[:len(gameweeks)]), players=players,
                    evaluation=evaluation, evaluation_context=context, freshness=freshness,
                    performance=records(performance.drop(columns=["current_xi_captain_points"], errors="ignore")), limits=LIMITS,
                    methodology="Historical walk-forward evaluation. Forecasts combine lagged form, fixtures, availability and workload.",
                    model_version=engine.MODEL_VERSION, model_code_sha=engine._model_sha(), data_commit_sha=engine._data_sha())
    snapshot["id"] = hashlib.sha256(json.dumps(snapshot, sort_keys=True).encode()).hexdigest()[:24]
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    temporary = output_dir / ".latest.json.tmp"
    temporary.write_text(json.dumps(snapshot, allow_nan=False), encoding="utf-8")
    temporary.replace(output_dir / "latest.json")
    return snapshot


def validate_snapshot(snapshot):
    """Reject incomplete or unusable public data before replacing a valid snapshot."""
    if not isinstance(snapshot, dict) or snapshot.get("schema_version") != 1:
        raise ValueError("Unsupported forecast snapshot")
    for key in ("id", "season", "generated_at", "methodology"):
        if not isinstance(snapshot.get(key), str) or not snapshot[key]:
            raise ValueError(f"Missing snapshot {key}")
    try:
        datetime.fromisoformat(snapshot["generated_at"].replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid forecast timestamp") from exc
    weeks = snapshot.get("gameweeks")
    if not isinstance(weeks, list) or not 1 <= len(weeks) <= 5 or any(type(gw) is not int or not 1 <= gw <= 38 for gw in weeks) or weeks != sorted(set(weeks)):
        raise ValueError("Invalid forecast Gameweeks")
    weights = snapshot.get("weights")
    if not isinstance(weights, list) or len(weights) != len(weeks) or any(type(w) not in (int, float) or not math.isfinite(w) or w < 0 for w in weights):
        raise ValueError("Invalid forecast weights")
    for key in ("evaluation", "evaluation_context"):
        if not isinstance(snapshot.get(key), dict):
            raise ValueError(f"Invalid snapshot {key}")
    for key in ("freshness", "performance", "limits"):
        if not isinstance(snapshot.get(key), list):
            raise ValueError(f"Invalid snapshot {key}")
    if any(not isinstance(row, dict) for key in ("freshness", "performance") for row in snapshot[key]) or any(not isinstance(limit, str) for limit in snapshot["limits"]):
        raise ValueError("Invalid snapshot report metadata")
    def finite(value, nullable=False):
        return (nullable and value is None) or (type(value) in (int, float) and math.isfinite(value))
    for method in snapshot["evaluation"].values():
        if not isinstance(method, dict) or any(not finite(method.get(key), key == "spearman") for key in ("mae", "rmse", "spearman")):
            raise ValueError("Invalid evaluation metrics")
    context = snapshot["evaluation_context"]
    if context:
        required = ("rows", "zero_actual_pct", "played_rows", "top20_actual_mean", "pool_actual_mean")
        played = context.get("played")
        if any(not finite(context.get(key)) for key in required) or not isinstance(played, dict) or any(not finite(played.get(key), key == "spearman") for key in ("mae", "rmse", "spearman")):
            raise ValueError("Invalid evaluation context")
    for row in snapshot["freshness"]:
        if any(type(row.get(key)) is not int for key in ("gameweek", "finished", "total")) or not isinstance(row.get("deferred_teams"), list) or any(not isinstance(team, str) for team in row["deferred_teams"]):
            raise ValueError("Invalid freshness metadata")
    for row in snapshot["performance"]:
        if type(row.get("gameweek")) is not int or any(not finite(row.get(key), True) for key in engine.PERFORMANCE_COLUMNS if key not in ("season", "gameweek", "data_commit_sha", "model_version", "current_xi_captain_points")):
            raise ValueError("Invalid live performance metrics")
    if snapshot.get("deadline") is not None:
        if not isinstance(snapshot["deadline"], str):
            raise ValueError("Invalid forecast deadline")
        try:
            datetime.fromisoformat(snapshot["deadline"].replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError("Invalid forecast deadline") from exc
    players = snapshot.get("players")
    if not isinstance(players, list) or not players:
        raise ValueError("Missing forecast players")
    seen = set()
    for player in players:
        if not isinstance(player, dict):
            raise ValueError("Invalid forecast player")
        for key in ("player_code", "player_id", "team_code"):
            if type(player.get(key)) is not int:
                raise ValueError(f"Invalid player {key}")
        if player["player_code"] in seen:
            raise ValueError("Duplicate forecast player")
        seen.add(player["player_code"])
        if player.get("position") not in engine.POSITION_COUNTS:
            raise ValueError("Invalid player position")
        for key in ("web_name", "team", "team_short_name", "status", "confidence", "drivers"):
            if not isinstance(player.get(key), str):
                raise ValueError(f"Invalid player {key}")
        for key in ("first_name", "second_name"):
            if key in player and not isinstance(player[key], str):
                raise ValueError(f"Invalid player {key}")
        for key in ("news", "recent_gameweek_points", "recent_points_breakdown"):
            if key in player and player[key] is not None and not isinstance(player[key], str):
                raise ValueError(f"Invalid player {key}")
        for key in ("recent_points_total", "recent_points_average", "recent_points_count", "data_coverage"):
            if key in player and not finite(player[key], True):
                raise ValueError(f"Invalid player {key}")
        for key in ("now_cost", "weighted_score", "predicted_value", "baseline", "baseline_rolling_points", "baseline_ep_next", "confidence_score", *[f"GW{gw}_predicted_points" for gw in weeks], *[f"GW{gw}_availability" for gw in weeks]):
            value = player.get(key)
            if type(value) not in (int, float) or not math.isfinite(value):
                raise ValueError(f"Invalid player {key}")
        if player["now_cost"] < 0 or not 0 <= player["confidence_score"] <= 1 or any(not 0 <= player[f"GW{gw}_availability"] <= 1 for gw in weeks):
            raise ValueError("Invalid player availability")
    return snapshot


def load_snapshot(path):
    return validate_snapshot(json.loads(Path(path).read_text()))


def squad_analysis(frame, gameweeks):
    lineups = {}
    weighted = 0.0
    for gw, weight in zip(gameweeks, engine.HORIZON_WEIGHTS):
        column = f"GW{gw}_predicted_points"
        starters, captain = engine.best_lineup(frame, column)
        vice = engine._vice_captain(frame, starters, captain, column)
        points = float(frame.loc[starters, column].sum() + frame.at[captain, column])
        lineups[str(gw)] = dict(starters=frame.loc[starters, "player_code"].astype(int).tolist(),
                               bench=frame.loc[~frame.index.isin(starters), "player_code"].astype(int).tolist(),
                               captain=int(frame.at[captain, "player_code"]), vice_captain=int(frame.at[vice, "player_code"]), points=points)
        weighted += weight * points
    return dict(players=frame.player_code.astype(int).tolist(), lineups=lineups, weighted_points=weighted)


def analyse(snapshot, draft):
    baseline = pd.DataFrame(snapshot["players"])
    user, bank, exclusions = engine.resolve_squad(draft, baseline)
    unknown = exclusions - set(baseline.player_code)
    if unknown:
        raise ValueError(f"Unknown excluded player codes: {sorted(unknown)}")
    weeks = snapshot["gameweeks"]
    forecast = engine._apply_exclusions(baseline, exclusions, weeks)
    points = [f"GW{gw}_predicted_points" for gw in weeks]
    user = user.merge(forecast[["player_code", *points]], on="player_code", validate="one_to_one")
    optimal = forecast.loc[engine._select_initial_squad(forecast, weeks, user, bank)]
    costs, available = engine._squad_budget(forecast, user, bank)
    transfers = records(engine._transfer_options(user, bank, forecast, weeks).head(10))
    return dict(snapshot_id=snapshot["id"], team=draft,
                budget=dict(bank=bank, selling_value=float(user.selling_price.sum()), available=available,
                            market_value=float(user.now_cost.sum()), optimal_bank=available-float(costs.loc[optimal.index].sum())),
                current=squad_analysis(user, weeks), optimal=squad_analysis(optimal, weeks),
                transfers=transfers, hold=not transfers or transfers[0]["weighted_gain"] <= 1e-9)


def private_report(snapshot, analysis):
    """Render the engine's report from the exact private analysis snapshot."""
    draft = analysis["team"]
    baseline = pd.DataFrame(snapshot["players"])
    user, bank, exclusions = engine.resolve_squad(draft, baseline)
    weeks = snapshot["gameweeks"]
    forecast = engine._apply_exclusions(baseline, exclusions, weeks)
    for name, value in (("data_commit_sha", snapshot.get("data_commit_sha")),
                        ("model_version", snapshot.get("model_version")),
                        ("model_code_sha", snapshot.get("model_code_sha")),
                        ("forecast_created_at", snapshot["generated_at"])):
        forecast[name] = value
    for section, prefix, membership in (("current", "current_", "current_squad"), ("optimal", "", "recommended_squad")):
        forecast[membership] = forecast.player_code.isin(analysis[section]["players"])
        for gw, lineup in analysis[section]["lineups"].items():
            forecast[f"{prefix}GW{gw}_lineup"] = forecast.player_code.isin(lineup["starters"])
            forecast[f"{prefix}GW{gw}_captain"] = forecast.player_code.eq(lineup["captain"])
            forecast[f"{prefix}GW{gw}_vice_captain"] = forecast.player_code.eq(lineup["vice_captain"])
    user = user.merge(forecast[["player_code", *[f"GW{gw}_predicted_points" for gw in weeks]]], on="player_code", validate="one_to_one")
    user["excluded"] = user.player_code.isin(exclusions)
    markdown = engine._render_markdown(
        forecast, snapshot["evaluation"], snapshot["season"], weeks, set(analysis["optimal"]["players"]),
        pd.DataFrame(analysis["transfers"]), evaluation_context=snapshot["evaluation_context"],
        incomplete_source=snapshot["freshness"], live_performance=pd.DataFrame(snapshot["performance"]),
        user_squad=user, bank=bank)
    return forecast, markdown
