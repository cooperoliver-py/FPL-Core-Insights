"""Pre-deadline form from canonical match exports, shared by training and forecasts.

Historical exports have no publication timestamps. Backtests assume the final
record was available three hours after kickoff; they cannot replay later source
corrections. Missing player-match rows mean unobserved workload, not proven rest.
"""

from pathlib import Path
import warnings

import numpy as np
import pandas as pd


WORKLOAD_COLUMNS = (
    "workload_all_minutes_7d", "workload_all_minutes_14d",
    "workload_nonpl_minutes_7d", "workload_nonpl_minutes_14d",
    "workload_friendlies_minutes_28d", "workload_days_since_last",
    "workload_recorded_appearances_14d", "workload_history_appearances",
)
_FIXTURE_COLUMNS = (
    "match_id", "kickoff_time", "finished", "home_team", "away_team",
    "home_team_elo", "away_team_elo",
)
_PLAYER_COLUMNS = ("match_id", "player_id", "minutes_played")


def load_match_data(season_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Read one season once; IDs in player-match files are season-local FPL IDs."""
    tables = []
    for filename, columns, keys in (
        ("fixtures.csv", _FIXTURE_COLUMNS, ["match_id"]),
        ("playermatchstats.csv", _PLAYER_COLUMNS, ["match_id", "player_id"]),
    ):
        parts = []
        for path in sorted((Path(season_dir) / "By Tournament").glob(f"*/GW*/{filename}")):
            frame = pd.read_csv(path, usecols=lambda column: column in columns)
            frame = frame.reindex(columns=columns)
            if filename == "fixtures.csv":
                frame["competition"] = path.parent.parent.name
            parts.append(frame)
        frame = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=columns)
        frame = frame.drop_duplicates()
        conflicting = frame.duplicated(keys, keep=False)
        if conflicting.any():
            fixtures = frame if filename == "fixtures.csv" else tables[0]
            league_ids = fixtures.loc[fixtures["competition"].eq("Premier League"), "match_id"]
            if frame.loc[conflicting, "match_id"].isin(league_ids).any():
                raise ValueError(f"Conflicting canonical Premier League {filename} records in {season_dir}")
            warnings.warn(f"Omitting {conflicting.sum()} conflicting non-league {filename} rows in {season_dir}", stacklevel=2)
            frame = frame.loc[~conflicting]
        tables.append(frame)
    matches, appearances = tables
    matches["kickoff_time"] = pd.to_datetime(matches["kickoff_time"], utc=True, errors="coerce")
    matches["finished"] = matches["finished"].astype(str).str.lower().eq("true")
    if "competition" not in matches:
        matches["competition"] = pd.Series(dtype=str)
    for frame, columns in (
        (matches, ("home_team", "away_team", "home_team_elo", "away_team_elo")),
        (appearances, ("player_id", "minutes_played")),
    ):
        for column in columns:
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
            frame.loc[~np.isfinite(frame[column]) | frame[column].lt(0), column] = np.nan
    appearances = appearances.merge(
        matches[["match_id", "kickoff_time", "finished", "competition"]],
        on="match_id", how="inner", validate="many_to_one",
    )
    return matches, appearances


def build_match_features(
    players: pd.DataFrame,
    match_data: tuple[pd.DataFrame, pd.DataFrame],
    as_of,
) -> pd.DataFrame:
    """Return features aligned to players; as_of is the actual information cutoff.

    Pass season-local player_id. Future fixtures never extend the observation
    cutoff. Friendlies inform workload, not competitive attacking form.
    """
    cutoff = pd.Timestamp(as_of)
    if pd.isna(cutoff):
        raise ValueError("Match features require a valid as_of timestamp")
    cutoff = cutoff.tz_localize("UTC") if cutoff.tzinfo is None else cutoff.tz_convert("UTC")
    matches, appearances = match_data
    # Conservative completion buffer also excludes an in-progress match's final export.
    history = matches.loc[matches["finished"] & (matches["kickoff_time"] + pd.Timedelta(hours=3) < cutoff)]
    observed = appearances.loc[appearances["match_id"].isin(history["match_id"]) & appearances["minutes_played"].gt(0)].copy()
    observed["age_days"] = (cutoff - observed["kickoff_time"]).dt.total_seconds() / 86400
    result = pd.DataFrame(np.nan, index=players.index, columns=WORKLOAD_COLUMNS)
    player_ids = pd.to_numeric(players["player_id"], errors="coerce")

    def assign(column, values, default=None):
        mapped = player_ids.map(values)
        result[column] = mapped if default is None else mapped.fillna(default)

    for days in (7, 14):
        recent = observed.loc[observed["age_days"].le(days)]
        assign(f"workload_all_minutes_{days}d", recent.groupby("player_id")["minutes_played"].sum(), 0)
        nonpl = recent.loc[recent["competition"].ne("Premier League")]
        assign(f"workload_nonpl_minutes_{days}d", nonpl.groupby("player_id")["minutes_played"].sum(), 0)
    assign("workload_days_since_last", observed.groupby("player_id")["age_days"].min())
    assign("workload_history_appearances", observed.groupby("player_id").size(), 0)
    assign("workload_recorded_appearances_14d", observed.loc[observed["age_days"].le(14)].groupby("player_id").size(), 0)
    recent = observed.loc[observed["age_days"].le(28)]
    friendly = recent["competition"].eq("Friendlies")
    assign("workload_friendlies_minutes_28d", recent.loc[friendly].groupby("player_id")["minutes_played"].sum(), 0)
    return result
