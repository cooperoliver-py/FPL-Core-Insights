import os
import tempfile
import unittest
from pathlib import Path
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
        lag_columns = ["event_points_lag3", "event_points_lag5", "event_points_ewm"]

        self.assertEqual(before["event_points_lag3"], 3.0)
        self.assertEqual(before[lag_columns].tolist(), after[lag_columns].tolist())

    def test_recent_form_ewm_weights_newer_matches_more(self):
        frame = pd.DataFrame(
            {"id": [1, 1, 1, 1], "gw": [1, 2, 3, 4], "event_points": [1, 2, 10, 0]}
        )
        latest = build_lagged_features(frame).query("gw == 4").iloc[0]

        self.assertGreater(latest["event_points_ewm"], latest["event_points_lag3"])

    def test_historical_availability_and_price_use_the_prior_snapshot(self):
        original = pd.DataFrame(
            {
                "id": [1, 1],
                "gw": [1, 2],
                "event_points": [2, 4],
                "status": ["d", "a"],
                "chance_of_playing_next_round": [50, 100],
                "now_cost": [5.0, 9.0],
                "position": ["Midfielder", "Midfielder"],
            }
        )
        changed = original.copy()
        changed.loc[changed["gw"].eq(2), ["status", "chance_of_playing_next_round", "now_cost"]] = [
            "i",
            0,
            15.0,
        ]

        before = build_lagged_features(original).query("gw == 2")
        after = build_lagged_features(changed).query("gw == 2")

        self.assertEqual(predictions._availability(before).iloc[0], 0.5)
        self.assertEqual(predictions._availability(after).iloc[0], 0.5)
        self.assertEqual(predictions._model_frame(before)["now_cost"].iloc[0], 5.0)
        self.assertEqual(predictions._model_frame(after)["now_cost"].iloc[0], 5.0)

    def test_partial_gameweek_uses_only_clubs_with_every_fixture_finished(self):
        fixtures = pd.DataFrame(
            {
                "home_team": [1, 1, 3],
                "away_team": [2, 4, 5],
                "finished": [True, False, False],
            }
        )
        stats = pd.DataFrame({"id": [11, 12, 13, 14, 15], "gw": [1] * 5})
        players = pd.DataFrame(
            {
                "player_id": [11, 12, 13, 14, 15],
                "player_code": [101, 102, 103, 104, 105],
                "team_code": [1, 2, 3, 4, 5],
            }
        )

        def read(path, required=()):
            if path.name == "fixtures.csv":
                return fixtures
            if path.name == "player_gameweek_stats.csv":
                return stats
            return players

        with (
            patch.object(predictions, "_fixture_file", return_value=Path("fixtures.csv")),
            patch.object(predictions, "_read_csv", side_effect=read),
        ):
            history = predictions._completed_current_history("2026-2027", 2)

        self.assertEqual(history["player_code"].tolist(), [102])

    def test_in_progress_target_gameweek_is_reported(self):
        fixtures = pd.DataFrame(
            {
                "home_team": [1, 3],
                "away_team": [2, 4],
                "finished": [True, False],
            }
        )
        teams = pd.DataFrame(
            {"code": [1, 2, 3, 4], "short_name": ["ONE", "TWO", "THR", "FOU"]}
        )

        def read(path, required=()):
            return fixtures if path.name == "fixtures.csv" else teams

        with (
            patch.object(predictions, "_season_path", return_value=Path("season")),
            patch.object(predictions, "_fixture_file", return_value=Path("fixtures.csv")),
            patch.object(predictions, "_read_csv", side_effect=read),
        ):
            result = predictions._incomplete_source_gameweeks("2026-2027", 1)

        self.assertTrue(result[0]["is_target"])
        self.assertEqual(result[0]["finished"], 1)

    def test_exclusions_zero_projections_and_keep_player_out_of_lineup(self):
        forecast = legal_squad().assign(
            status="a",
            now_cost=5.0,
            GW1_predicted_points=lambda frame: frame["predicted_points"],
            weighted_score=lambda frame: frame["predicted_points"],
            predicted_value=1.0,
            baseline=1.0,
            baseline_rolling_points=1.0,
            baseline_ep_next=1.0,
            confidence_score=1.0,
            confidence="high",
            drivers="synthetic",
        )
        result = predictions._apply_exclusions(forecast, {1}, [1])
        lineup, captain = best_lineup(result, "GW1_predicted_points")
        vice = predictions._vice_captain(result, lineup, captain, "GW1_predicted_points")

        excluded = result.loc[result["player_code"].eq(1)].iloc[0]
        self.assertEqual(excluded["GW1_predicted_points"], 0)
        self.assertEqual(excluded["weighted_score"], 0)
        self.assertEqual(excluded["confidence"], "excluded")
        self.assertNotIn(excluded.name, lineup)
        self.assertNotEqual(excluded.name, captain)
        self.assertNotEqual(excluded.name, vice)

    def test_served_prediction_applies_availability_and_fixture_rules(self):
        frame = pd.DataFrame(
            {"status": ["a", "i", "a"], "fixture_count": [1, 1, 0]}
        )
        self.assertEqual(
            predictions._served_prediction(frame, [2.0, 2.0, 2.0]).tolist(),
            [2.0, 0.0, 0.0],
        )

    def test_captain_dnp_promotes_vice_captain_in_live_score(self):
        frame = pd.DataFrame(
            {
                "actual_points": [0, 5],
                "minutes": [0, 90],
                "GW1_lineup": [True, True],
                "GW1_captain": [True, False],
                "GW1_vice_captain": [False, True],
            }
        )
        self.assertEqual(predictions._squad_actual_points(frame, "", 1), 10)

    def test_archive_deadline_guard_freezes_post_deadline_forecast(self):
        summaries = pd.DataFrame(
            {"id": [3], "deadline_time": ["2026-09-04T17:30:00+00:00"]}
        )
        with (
            patch.object(predictions, "_season_path", return_value=Path("data/2026-2027")),
            patch.object(predictions, "_read_csv", return_value=summaries),
        ):
            self.assertTrue(
                predictions._before_gameweek_deadline(
                    "2026-2027", 3, pd.Timestamp("2026-09-04T17:29:00+00:00")
                )
            )
            self.assertFalse(
                predictions._before_gameweek_deadline(
                    "2026-2027", 3, pd.Timestamp("2026-09-04T17:31:00+00:00")
                )
            )

    def test_live_performance_scores_only_checked_archives(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = root / "data"
            season = data / "2026-2027"
            gameweek = season / "By Gameweek" / "GW1"
            archive = root / "predictions" / "archive" / "2026-2027"
            gameweek.mkdir(parents=True)
            archive.mkdir(parents=True)
            pd.DataFrame(
                {
                    "id": [1],
                    "finished": [True],
                    "data_checked": [True],
                    "average_entry_score": [50],
                }
            ).to_csv(season / "gameweek_summaries.csv", index=False)
            pd.DataFrame(
                {"id": [1, 2, 3], "event_points": [0, 5, 10], "minutes": [0, 90, 90]}
            ).to_csv(gameweek / "player_gameweek_stats.csv", index=False)
            pd.DataFrame(
                {
                    "player_id": [1, 2, 3],
                    "team_code": [1, 2, 3],
                    "status": ["a", "a", "a"],
                    "excluded": [False, False, True],
                    "data_commit_sha": ["test"] * 3,
                    "GW1_predicted_points": [5.0, 1.0, 99.0],
                    "baseline_rolling_points": [2.0, 2.0, 2.0],
                    "baseline_ep_next": [3.0, 3.0, 3.0],
                    "GW1_lineup": [True, True, False],
                    "GW1_captain": [True, False, False],
                    "GW1_vice_captain": [False, True, False],
                    "current_GW1_lineup": [False] * 3,
                    "current_GW1_captain": [False] * 3,
                    "current_GW1_vice_captain": [False] * 3,
                }
            ).to_csv(archive / "GW01.csv", index=False)
            fixture_path = season / "By Tournament" / "Premier League" / "GW1"
            fixture_path.mkdir(parents=True)
            pd.DataFrame({"home_team": [1], "away_team": [2]}).to_csv(
                fixture_path / "fixtures.csv", index=False
            )

            with patch.object(predictions, "DATA", data):
                result = predictions._live_performance(root / "predictions", "2026-2027")

            self.assertEqual(len(result), 1)
            self.assertEqual(result.iloc[0]["players"], 2)
            self.assertEqual(result.iloc[0]["optimal_xi_captain_points"], 10)

            summaries = pd.read_csv(season / "gameweek_summaries.csv")
            summaries["data_checked"] = False
            summaries.to_csv(season / "gameweek_summaries.csv", index=False)
            with patch.object(predictions, "DATA", data):
                self.assertTrue(
                    predictions._live_performance(root / "predictions", "2026-2027").empty
                )

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
        forecast["excluded"] = False
        forecast["GW1_predicted_points"] = squad["predicted_points"]
        incoming = pd.DataFrame(
            {
                "player_code": [16, 17, 18, 19, 20],
                "web_name": ["Available", "Injured", "Unavailable", "Suspended", "Excluded"],
                "team_code": [9] * 5,
                "position": ["Forward"] * 5,
                "status": ["a", "i", "u", "s", "a"],
                "excluded": [False, False, False, False, True],
                "now_cost": [5.0] * 5,
                "GW1_predicted_points": [20.0] * 5,
            }
        )

        options = predictions._transfer_options(
            squad, 0.0, pd.concat([forecast, incoming], ignore_index=True), [1]
        )

        self.assertEqual(set(options["in_player_code"]), {16})

    def test_excluded_player_is_not_selected_for_optimal_squad(self):
        forecast = legal_squad().assign(status="a", now_cost=5.0, excluded=False)
        forecast["weighted_score"] = forecast["predicted_points"]
        forecast["GW1_predicted_points"] = forecast["predicted_points"]
        excluded = pd.DataFrame(
            {
                "player_code": [16],
                "position": ["Forward"],
                "team_code": [9],
                "purchase_price": [5.0],
                "predicted_points": [100.0],
                "status": ["a"],
                "now_cost": [5.0],
                "excluded": [True],
                "weighted_score": [100.0],
                "GW1_predicted_points": [100.0],
            }
        )

        selected = predictions._select_initial_squad(
            pd.concat([forecast, excluded], ignore_index=True), [1]
        )

        selected_codes = set(
            pd.concat([forecast, excluded], ignore_index=True).loc[selected, "player_code"]
        )
        self.assertNotIn(16, selected_codes)

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
                "excluded": [False],
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
                forecast,
                {},
                "2026-2027",
                [1],
                {1},
                transfers,
                incomplete_source=[
                    {
                        "gameweek": 2,
                        "finished": 9,
                        "total": 10,
                        "deferred_teams": ["ARS", "AVL"],
                    }
                ],
            )

        self.assertIn("**Outgoing → Incoming**", markdown)
        self.assertIn("| Outgoing | Incoming |", markdown)
        self.assertIn("## ML-optimal £100m squad", markdown)
        self.assertIn("## Your current squad", markdown)
        self.assertIn("GW2: 9/10 fixtures finished", markdown)
        self.assertIn("ARS, AVL are deferred", markdown)
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
