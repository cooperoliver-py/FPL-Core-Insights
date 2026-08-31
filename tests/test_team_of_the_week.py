import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from scripts import team_of_the_week


class TeamOfTheWeekTests(unittest.TestCase):
    def test_only_completed_gameweeks_are_written_with_the_required_positions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = root / "data"
            season = data / "2026-2027"
            gameweek = season / "By Gameweek" / "GW1"
            output = root / "TeamOfTheWeek"
            gameweek.mkdir(parents=True)
            pd.DataFrame(
                {
                    "id": [1, 2],
                    "finished": [True, False],
                    "data_checked": [True, False],
                }
            ).to_csv(season / "gameweek_summaries.csv", index=False)

            positions = ["Goalkeeper"] * 3 + ["Defender"] * 6 + ["Midfielder"] * 6 + [
                "Forward"
            ] * 4
            player_ids = list(range(1, len(positions) + 1))
            pd.DataFrame(
                {
                    "id": player_ids,
                    "event_points": player_ids,
                    "minutes": [90] * len(player_ids),
                    "goals_scored": [0] * len(player_ids),
                    "assists": [0] * len(player_ids),
                    "clean_sheets": [0] * len(player_ids),
                    "bonus": [0] * len(player_ids),
                }
            ).to_csv(gameweek / "player_gameweek_stats.csv", index=False)
            pd.DataFrame(
                {
                    "player_id": player_ids,
                    "player_code": player_ids,
                    "first_name": ["Test"] * len(player_ids),
                    "second_name": [f"Player {value}" for value in player_ids],
                    "web_name": [f"Player {value}" for value in player_ids],
                    "team_code": [1] * len(player_ids),
                    "position": positions,
                }
            ).to_csv(gameweek / "players.csv", index=False)
            pd.DataFrame({"code": [1], "short_name": ["TST"]}).to_csv(
                gameweek / "teams.csv", index=False
            )

            with patch.object(team_of_the_week, "DATA", data):
                written = team_of_the_week.generate("2026-2027", output)

            self.assertEqual(len(written), 2)
            team = pd.read_csv(output / "GW1" / "team.csv")
            self.assertEqual(
                team["position"].value_counts().to_dict(),
                team_of_the_week.POSITION_COUNTS,
            )
            self.assertEqual(len(team), 15)
            self.assertEqual(set(team["player_id"]), set(player_ids) - {1, 4, 10, 16})
            self.assertFalse((output / "GW2").exists())


if __name__ == "__main__":
    unittest.main()
