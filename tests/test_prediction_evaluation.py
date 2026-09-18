import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from scripts import evaluate_predictions as evaluation
from scripts import fpl_predictions as p


class ForecastEvaluationTests(unittest.TestCase):
    def test_future_outcomes_and_snapshots_do_not_change_frozen_origin_features(self):
        history = pd.DataFrame({
            "season": [p.TRAIN_SEASON] * 6, "gw": range(15, 21), "player_code": [1] * 6,
            "player_id": [1] * 6, "team_code": [1] * 6, "position": ["Forward"] * 6,
            "event_points": [4] * 6, "minutes": [90] * 6, "now_cost": [6.] * 6,
            "status": ["s"] + ["a"] * 5, "chance_of_playing_next_round": [0] + [100] * 5,
            "news": ["Suspended until 25 Sep"] + [""] * 5,
            "deadline_time": pd.date_range("2025-09-12", periods=6, freq="7D", tz="UTC"),
        })
        history = p.build_lagged_features(history, "player_code")
        fixtures = {}
        for week in range(15, 21):
            date = pd.Timestamp("2025-09-13", tz="UTC") + pd.Timedelta(days=7 * (week - 15))
            fixtures[week] = pd.DataFrame({"home_team": [1], "away_team": [2],
                                           "home_team_elo": [1500.], "away_team_elo": [1400.],
                                           "kickoff_time": [date]})
            context = p._fixture_context(fixtures[week], {1: 1500., 2: 1400.}).set_index("team_code")
            for column in context:
                history.loc[history.gw.eq(week), column] = context.loc[1, column]
        history["kickoff_time"] = history.deadline_time + pd.Timedelta(days=1)
        history["fixture_availability"] = p.availability_for_gameweek(
            history, history.deadline_time, is_next_round=True
        )

        class Model:
            def __init__(self):
                self.inputs = []

            def predict(self, frame):
                self.inputs.append(frame.copy())
                return np.full(len(frame), 8.)

        first, changed = Model(), Model()
        with patch.object(p, "_deadline_elo", return_value=({1: 1500., 2: 1400.}, set())), \
             patch.object(p, "estimate_return_availability", return_value={"probability": .3}) as prior:
            result = evaluation.forecast_horizons(first, history, 16, fixtures, None)
            self.assertEqual(prior.call_args.args[0].gw.tolist(), [15])
            modified = history.copy()
            modified.loc[modified.gw.gt(16), ["event_points", "event_points_lag5", "now_cost_lag1", "minutes_lag1"]] = 999
            modified.loc[modified.gw.gt(16), ["status", "status_lag1"]] = "i"
            evaluation.forecast_horizons(changed, modified, 16, fixtures, None)
        for left, right in zip(first.inputs, changed.inputs):
            pd.testing.assert_frame_equal(left, right)
        pd.testing.assert_frame_equal(
            first.inputs[0], p._model_frame(history.loc[history.gw.eq(16)]).reset_index(drop=True),
            check_dtype=False,
        )
        refined = result.loc[result.model.eq("refined")]
        self.assertEqual(refined.prediction.tolist(), [0., 8., 8., 8., 8.])

    def test_calibration_ablation_keeps_hard_unavailability_and_blank_rules(self):
        frame = pd.DataFrame({"fixture_availability": [0., .5, 1., 1.], "fixture_count": [1, 1, 1, 0]})
        self.assertEqual(p._served_prediction(frame, [8.] * 4).tolist(), [0., 4., 8., 0.])
        self.assertEqual(p._served_prediction(frame, [8.] * 4, scale_availability=False).tolist(), [0., 8., 8., 0.])


if __name__ == "__main__":
    unittest.main()
