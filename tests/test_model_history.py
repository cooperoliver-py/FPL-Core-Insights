import unittest
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd

from scripts import fpl_predictions as predictions


class ModelHistoryTests(unittest.TestCase):
    def test_copied_gw1_metadata_is_quarantined_without_removing_match_results(self):
        rows = pd.DataFrame({
            "season": ["2025-2026"] * 2, "gw": [1, 2], "player_code": [7, 7],
            "event_points": [13, 13], "minutes": [90, 90], "status": ["s", "a"],
            "news": ["Suspended until 20 Dec", ""], "now_cost": [5.7, 5.6],
            "chance_of_playing_next_round": [0, 100], "penalties_order": [1, 2], "ep_next": [99, 4],
        })
        result = predictions.build_lagged_features(rows, "player_code")
        self.assertEqual(result.iloc[1]["event_points_lag3"], 13)
        for name in ("availability_lag1", "news_lag1", "status_lag1", "now_cost_lag1", "penalties_order_lag1", "ep_next_lag"):
            self.assertTrue(pd.isna(result.iloc[1][name]), name)
        self.assertEqual(result.iloc[1]["now_cost"], 5.6)

    def test_new_form_features_are_shifted_and_summer_snapshots_are_reset(self):
        history = pd.DataFrame({
            "player_code": [10, 10, 10], "season": ["2025-2026", "2025-2026", "2026-2027"],
            "gw": [37, 38, 1], "minutes": [90, 90, 90], "expected_goals": [.2, .4, 99],
            "status": ["a", "i", "a"], "now_cost": [5., 5., 8.], "penalties_order": [1, 2, 3],
        })
        result = predictions.build_lagged_features(history, "player_code")
        self.assertAlmostEqual(result.iloc[-1]["expected_goals_per90"], .3)
        self.assertEqual(result.iloc[-1]["appearance_rate"], 1)
        self.assertTrue(pd.isna(result.iloc[-1]["availability_lag1"]))
        self.assertTrue(pd.isna(result.iloc[-1]["now_cost_lag1"]))
        self.assertTrue(pd.isna(result.iloc[-1]["penalties_order_lag1"]))
        self.assertEqual(result.iloc[1]["penalties_order_lag1"], 1)

    def test_elo_does_not_read_ratings_from_target_or_future_matches(self):
        matches = pd.DataFrame({
            "kickoff_time": pd.to_datetime(["2026-08-01", "2026-09-19"], utc=True),
            "finished": [True, True], "home_team": [1, 1], "away_team": [2, 2],
            "home_team_elo": [1600., 9999.], "away_team_elo": [1500., 9999.],
        })
        teams = pd.DataFrame({"code": [1, 2], "elo": [1450., 1400.]})
        with patch.object(predictions, "_read_csv", return_value=teams), \
             patch.object(Path, "is_file", return_value=True):
            ratings, _ = predictions._deadline_elo("2026-2027", matches, pd.Timestamp("2026-09-18", tz="UTC"))
        self.assertEqual(ratings, {1: 1600., 2: 1500.})

    def test_live_lags_share_training_logic_without_id_collisions_or_duplicate_rows(self):
        previous, current = predictions.TRAIN_SEASON, "2026-2027"
        history = pd.DataFrame({
            "season": [previous, previous, previous, current, current, current],
            "gw": [37, 38, 38, 1, 1, 3],
            "id": [1, 1, 2, 2, 1, 2],
            "player_id": [1, 1, 2, 2, 1, 2],
            "player_code": [100, 100, 200, 100, 200, 100],
            "event_points": [2, 4, 9, 8, 6, 900],
            "minutes": [90, 90, 90, 90, 60, 900],
            "expected_goals": [.1, .2, .9, .4, .3, 900],
        })
        catalog = pd.DataFrame({"player_id": [2, 1, 3], "player_code": [100, 200, 300]})
        duplicate = history.loc[history["season"].eq(current) & history["gw"].eq(1)].copy()
        duplicate["event_points"] = 1000  # Must not replace already-loaded training rows.
        new = pd.DataFrame({"season": [current], "gw": [2], "id": [2], "player_id": [2],
                            "player_code": [100], "event_points": [10], "minutes": [90], "expected_goals": [.5]})
        with patch.object(predictions, "_completed_current_history", return_value=pd.concat([duplicate, new])):
            actual = predictions._current_lags(catalog, history, current, 3).set_index("player_id")
        sentinel = catalog.assign(season=current, gw=3, _forecast_row=True)
        expected = predictions.build_lagged_features(pd.concat([
            history.loc[~(history["season"].eq(current) & history["gw"].ge(3))], new, sentinel,
        ], ignore_index=True), "player_code")
        expected = expected.loc[expected["_forecast_row"].eq(True)].set_index("player_id")
        columns = [column for column in (*predictions.LAG_COLUMNS, *predictions.RECENT_COLUMNS,
                                         *predictions.FORM_COLUMNS) if column in expected]
        pd.testing.assert_frame_equal(actual[columns], expected[columns], check_dtype=False)
        self.assertEqual(actual.loc[2, "history_count"], 4)
        self.assertEqual(actual.loc[2, "current_season_matches"], 2)
        self.assertAlmostEqual(actual.loc[2, "event_points_lag3"], 22 / 3)
        self.assertEqual(actual.loc[1, "event_points_lag3"], 7.5)
        self.assertEqual(actual.loc[3, "cold_start"], 1)

    def test_current_labels_use_stable_codes_and_only_completed_checked_gameweeks(self):
        previous, current = predictions.TRAIN_SEASON, "2026-2027"
        prior = pd.DataFrame({"season": [previous], "gw": [38], "id": [1], "player_id": [1],
                              "player_code": [100], "event_points": [4], "minutes": [90]})
        teams = pd.DataFrame({"code": [1, 2], "elo": [1500, 1400]})
        fixtures = pd.DataFrame({"home_team": [1], "away_team": [2], "home_team_elo": [1500],
                                 "away_team_elo": [1400], "kickoff_time": ["2026-08-21T19:00:00Z"]})
        summaries = pd.DataFrame({"id": [1, 2], "finished": [True, True], "data_checked": [True, False],
                                  "deadline_time": ["2026-08-21T17:30:00Z", "2026-08-28T17:30:00Z"]})
        players = pd.DataFrame({"player_id": [1, 2], "player_code": [200, 100],
                               "team_code": [1, 2], "position": ["Midfielder", "Forward"]})
        stats = pd.DataFrame({"id": [1, 2, 999], "gw": [1, 1, 1], "event_points": [6, 8, 0], "minutes": [60, 90, 0]})

        def read(path, required=()):
            return {"gameweek_summaries.csv": summaries, "teams.csv": teams, "fixtures.csv": fixtures,
                    "players.csv": players, "player_gameweek_stats.csv": stats}[Path(path).name].copy()

        with patch.object(predictions, "_read_csv", side_effect=read), \
             patch.object(predictions, "load_match_data", return_value=(None, None)), \
             patch.object(predictions, "_deadline_elo", return_value=({1: 1500, 2: 1400}, set())), \
             patch.object(predictions, "build_match_features", side_effect=lambda frame, *args: pd.DataFrame(index=frame.index)):
            result = predictions._load_training_data(current, 3, prior_history=prior)
        self.assertEqual(len(result), 3)
        self.assertFalse(result.duplicated(["season", "player_code", "gw"]).any())
        latest = result.loc[result["season"].eq(current)].set_index("player_code")
        self.assertEqual(latest.loc[100, "event_points_lag3"], 4)
        self.assertTrue(pd.isna(latest.loc[200, "event_points_lag3"]))

    def test_current_season_labels_enter_final_fit_but_never_historical_folds(self):
        training = pd.DataFrame({
            "season": [predictions.TRAIN_SEASON] * 3 + ["2026-2027"] * 2,
            "gw": [1, 31, 32, 1, 2], "event_points": [1, 3, 5, 100, 200],
            "minutes": [90] * 5, "fixture_count": [1] * 5, "position": ["Midfielder"] * 5,
            "event_points_lag5": [1] * 5, "ep_next_lag": [1] * 5,
        })
        labels = []

        class Model:
            def fit(self, features, target):
                labels.append(target.tolist())
                return self

            def predict(self, features):
                return np.ones(len(features))

        with patch.object(predictions, "_new_model", side_effect=Model):
            predictions._evaluate_and_fit(training)
        self.assertGreaterEqual(len(labels), 2)
        self.assertTrue(all(max(fold) < 100 for fold in labels[:-1]))
        self.assertEqual(labels[-1], [1, 3, 5, 100, 200])


if __name__ == "__main__":
    unittest.main()
