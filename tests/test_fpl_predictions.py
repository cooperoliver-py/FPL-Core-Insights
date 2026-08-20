import os
import unittest
from unittest.mock import patch

import pandas as pd

from scripts import fpl_predictions as predictions
from scripts.fpl_predictions import (
    best_lineup,
    build_lagged_features,
    calculate_selling_price,
    validate_squad,
)


def legal_squad():
    positions = (
        ["Goalkeeper"] * 2
        + ["Defender"] * 5
        + ["Midfielder"] * 5
        + ["Forward"] * 3
    )
    return pd.DataFrame(
        {
            "player_code": range(1, 16),
            "position": positions,
            "team_code": [index % 5 for index in range(15)],
            "purchase_price": [5.0] * 15,
            "predicted_points": range(15, 0, -1),
        }
    )


class FPLPredictionsTests(unittest.TestCase):
    def test_official_selling_price_rounding(self):
        for current, expected in ((7.3, 7.1), (7.4, 7.2), (6.9, 6.9)):
            with self.subTest(current=current):
                self.assertEqual(calculate_selling_price(7.0, current), expected)

    def test_squad_constraints(self):
        squad = legal_squad()
        self.assertTrue(validate_squad(squad))

        squad.loc[squad["position"].eq("Defender").idxmax(), "position"] = "Midfielder"
        with self.assertRaises(ValueError):
            validate_squad(squad)

    def test_best_lineup_is_legal_and_captain_starts(self):
        squad = legal_squad()
        lineup, captain = best_lineup(squad, "predicted_points")
        vice_captain = predictions._vice_captain(squad, lineup, captain, "predicted_points")
        counts = squad.loc[lineup, "position"].value_counts()

        self.assertEqual(len(lineup), 11)
        self.assertEqual(len(set(lineup)), 11)
        self.assertEqual(counts["Goalkeeper"], 1)
        self.assertGreaterEqual(counts["Defender"], 3)
        self.assertGreaterEqual(counts["Midfielder"], 2)
        self.assertGreaterEqual(counts["Forward"], 1)
        self.assertIn(captain, lineup)
        self.assertIn(vice_captain, lineup)
        self.assertNotEqual(vice_captain, captain)

    def test_gameweek_points_are_not_used_in_same_gameweek_lags(self):
        original = pd.DataFrame(
            {"id": [1, 1, 1], "gw": [1, 2, 3], "event_points": [2, 4, 6]}
        )
        changed = original.copy()
        changed.loc[changed["gw"].eq(3), "event_points"] = 600

        before = build_lagged_features(original).query("gw == 3").iloc[0]
        after = build_lagged_features(changed).query("gw == 3").iloc[0]
        lag_columns = ["event_points_lag3", "event_points_lag5"]

        self.assertEqual(before["event_points_lag3"], 3.0)
        self.assertEqual(before[lag_columns].tolist(), after[lag_columns].tolist())

    def test_is_next_summary_wins_over_unfinished_current_gameweek(self):
        summaries = pd.DataFrame(
            {
                "id": [1, 2],
                "is_next": [False, True],
                "deadline_time": ["2026-08-15", "2026-08-22"],
            }
        )
        with (
            patch.object(predictions.Path, "is_file", return_value=True),
            patch.object(predictions, "_read_csv", return_value=summaries),
        ):
            self.assertEqual(predictions._next_unfinished_gameweek("2026-2027"), 2)

    def test_transfer_candidates_exclude_unavailable_players(self):
        squad = legal_squad().assign(
            web_name=[f"Player {code}" for code in range(1, 16)],
            status="a",
            now_cost=5.0,
        )
        columns = ["player_code", "web_name", "team_code", "position", "status", "now_cost"]
        forecast = squad[columns].copy()
        forecast["GW1_predicted_points"] = squad["predicted_points"]
        incoming = pd.DataFrame(
            {
                "player_code": [16, 17, 18, 19],
                "web_name": ["Available", "Injured", "Unavailable", "Suspended"],
                "team_code": [9] * 4,
                "position": ["Forward"] * 4,
                "status": ["a", "i", "u", "s"],
                "now_cost": [5.0] * 4,
                "GW1_predicted_points": [20.0] * 4,
            }
        )

        options = predictions._transfer_options(
            squad, 0.0, pd.concat([forecast, incoming], ignore_index=True), [1]
        )

        self.assertEqual(set(options["in_player_code"]), {16})

    def test_non_empty_transfer_table_renders_reserved_in_column(self):
        forecast = pd.DataFrame(
            {
                "player_code": [1],
                "web_name": ["Starter"],
                "team_short_name": ["TST"],
                "position": ["Forward"],
                "GW1_predicted_points": [5.0],
                "weighted_score": [5.0],
                "predicted_value": [1.0],
                "confidence": ["medium"],
                "drivers": ["synthetic"],
                "now_cost": [5.0],
                "GW1_lineup": [True],
                "GW1_captain": [True],
                "GW1_vice_captain": [False],
                "current_squad": [True],
                "current_GW1_lineup": [True],
                "current_GW1_captain": [False],
                "current_GW1_vice_captain": [True],
            }
        )
        transfers = pd.DataFrame(
            [
                {
                    "out": "Outgoing",
                    "in": "Incoming",
                    "selling_price": 5.0,
                    "buy_price": 5.0,
                    "bank_after": 0.0,
                    "weighted_gain": 1.0,
                }
            ]
        )
        with patch.object(predictions, "_data_sha", return_value="test"):
            markdown = predictions._render_markdown(
                forecast, {}, "2026-2027", [1], {1}, transfers
            )

        self.assertIn("**Outgoing → Incoming**", markdown)
        self.assertIn("| Outgoing | Incoming |", markdown)
        self.assertIn("## ML-optimal £100m squad", markdown)
        self.assertIn("## Your current squad", markdown)
        self.assertIn("| Starter | TST | Forward | £5.0m | 5.00 | GW1 | — | GW1 |", markdown)
        self.assertRegex(markdown, r"Last generated: \d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC")

    def test_workflow_data_revision_override_is_stable(self):
        with patch.dict(os.environ, {"FPL_DATA_SHA": "upstream-commit"}):
            self.assertEqual(predictions._data_sha(), "upstream-commit")

    def test_historical_season_replay_is_rejected(self):
        with patch.object(predictions, "_latest_season", return_value="2026-2027"):
            with self.assertRaisesRegex(ValueError, "look-ahead bias"):
                predictions.run(season="2025-2026")

    def test_gameweek_zero_is_rejected_instead_of_auto_selected(self):
        with (
            patch.object(predictions, "_latest_season", return_value="2026-2027"),
            patch.object(predictions, "_season_path"),
        ):
            with self.assertRaisesRegex(ValueError, "between 1 and 38"):
                predictions.run(gameweek=0)


if __name__ == "__main__":
    unittest.main()
