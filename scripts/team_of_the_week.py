#!/usr/bin/env python3
"""Write the highest-scoring 15-player squad for each completed Gameweek."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = ROOT / "TeamOfTheWeek"
POSITION_COUNTS = {
    "Goalkeeper": 2,
    "Defender": 5,
    "Midfielder": 5,
    "Forward": 3,
}


def _truth(values: pd.Series) -> pd.Series:
    return values.fillna(False).astype(str).str.lower().eq("true")


def _latest_season() -> str:
    seasons = sorted(
        path.name
        for path in DATA.iterdir()
        if path.is_dir()
        and (path / "gameweek_summaries.csv").is_file()
        and (path / "By Gameweek").is_dir()
    )
    if not seasons:
        raise FileNotFoundError(f"no season data found under {DATA}")
    return seasons[-1]


def _completed_gameweeks(season: str) -> list[int]:
    summaries = pd.read_csv(DATA / season / "gameweek_summaries.csv")
    required = {"id", "finished", "data_checked"}
    missing = required - set(summaries)
    if missing:
        raise ValueError(f"gameweek summaries are missing: {', '.join(sorted(missing))}")
    completed = summaries.loc[_truth(summaries["finished"]) & _truth(summaries["data_checked"])]
    return sorted(pd.to_numeric(completed["id"], errors="raise").astype(int).tolist())


def _team(season: str, gameweek: int) -> pd.DataFrame:
    base = DATA / season / "By Gameweek" / f"GW{gameweek}"
    stats = pd.read_csv(base / "player_gameweek_stats.csv")
    players = pd.read_csv(base / "players.csv")
    teams = pd.read_csv(base / "teams.csv")
    stats_columns = {
        "id",
        "event_points",
        "minutes",
        "goals_scored",
        "assists",
        "clean_sheets",
        "bonus",
    }
    player_columns = {
        "player_id",
        "player_code",
        "first_name",
        "second_name",
        "web_name",
        "team_code",
        "position",
    }
    team_columns = {"code", "short_name"}
    for name, frame, required in (
        ("player stats", stats, stats_columns),
        ("players", players, player_columns),
        ("teams", teams, team_columns),
    ):
        missing = required - set(frame)
        if missing:
            raise ValueError(f"GW{gameweek} {name} are missing: {', '.join(sorted(missing))}")

    pool = stats[list(stats_columns)].merge(
        players[list(player_columns)],
        left_on="id",
        right_on="player_id",
        how="inner",
        validate="one_to_one",
    ).merge(
        teams[["code", "short_name"]],
        left_on="team_code",
        right_on="code",
        how="left",
        validate="many_to_one",
    )
    pool["event_points"] = pd.to_numeric(pool["event_points"], errors="raise")
    selected: list[pd.DataFrame] = []
    for position, count in POSITION_COUNTS.items():
        candidates = pool.loc[pool["position"].eq(position)].sort_values(
            ["event_points", "player_code"], ascending=[False, True], kind="mergesort"
        )
        if len(candidates) < count:
            raise ValueError(f"GW{gameweek} has only {len(candidates)} {position} players")
        chosen = candidates.head(count).copy()
        chosen["position_rank"] = range(1, count + 1)
        selected.append(chosen)

    result = pd.concat(selected, ignore_index=True).rename(
        columns={"event_points": "points", "short_name": "club"}
    )
    result.insert(0, "season", season)
    result.insert(1, "gameweek", gameweek)
    return result[
        [
            "season",
            "gameweek",
            "position",
            "position_rank",
            "player_code",
            "player_id",
            "first_name",
            "second_name",
            "web_name",
            "team_code",
            "club",
            "points",
            "minutes",
            "goals_scored",
            "assists",
            "clean_sheets",
            "bonus",
        ]
    ]


def _markdown(team: pd.DataFrame, season: str, gameweek: int) -> str:
    lines = [
        f"# Team of the Week: {season}, GW{gameweek}",
        "",
        f"Total points: **{int(team['points'].sum())}**",
        "",
        "The highest-scoring 2 goalkeepers, 5 defenders, 5 midfielders and 3 forwards. "
        "Ties are resolved by stable `player_code`; no budget constraint is applied.",
        "",
        "| Position | Player | Club | Points | Minutes | Goals | Assists | Clean sheets | Bonus |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in team.itertuples(index=False):
        lines.append(
            f"| {row.position} | {row.web_name} | {row.club} | {int(row.points)} | "
            f"{int(row.minutes)} | {int(row.goals_scored)} | {int(row.assists)} | "
            f"{int(row.clean_sheets)} | {int(row.bonus)} |"
        )
    return "\n".join(lines) + "\n"


def generate(season: str | None = None, output: Path = OUTPUT) -> list[Path]:
    season = season or _latest_season()
    written: list[Path] = []
    for gameweek in _completed_gameweeks(season):
        team = _team(season, gameweek)
        destination = output / f"GW{gameweek}"
        destination.mkdir(parents=True, exist_ok=True)
        csv_path, markdown_path = destination / "team.csv", destination / "team.md"
        csv_temp, markdown_temp = destination / ".team.csv.tmp", destination / ".team.md.tmp"
        team.to_csv(csv_temp, index=False, lineterminator="\n")
        markdown_temp.write_text(_markdown(team, season, gameweek), encoding="utf-8", newline="\n")
        csv_temp.replace(csv_path)
        markdown_temp.replace(markdown_path)
        written.extend((csv_path, markdown_path))
    return written


if __name__ == "__main__":
    paths = generate()
    print(f"Wrote {len(paths) // 2} completed Team of the Week report(s)")
