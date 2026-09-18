import unittest

import pandas as pd

from scripts.player_availability import availability_for_fixture, availability_for_gameweek, estimate_return_availability


class PlayerAvailabilityTests(unittest.TestCase):
    def test_expired_suspension_stays_eligible_but_stale_injury_does_not(self):
        frame = pd.DataFrame({"status": ["s", "i"], "chance_of_playing_next_round": [0, 0],
                              "news": ["Suspended until 22 Sep", "Expected back 22 Sep"]})
        before = availability_for_fixture(frame, "2026-09-24", "2026-09-18", injury_return_probability=.3)
        after = availability_for_fixture(frame, "2026-09-24", "2026-09-23", injury_return_probability=.3)
        self.assertEqual(before.tolist(), [1, .3])
        self.assertEqual(after.tolist(), [1, 0])

    def test_double_gameweek_averages_each_fixture_and_preserves_snapshot(self):
        frame = pd.DataFrame({
            "status_lag1": ["s", "a", "i"], "availability_lag1": [0., 1., 0.],
            "news_lag1": ["Suspended until 22 Sep", "", "Expected back 22 Sep"],
            "fixture_count": [2, 0, 2],
            "fixture_kickoffs": [("2026-09-20", "2026-09-24"), (), ("2026-09-20", "2026-09-24")],
        }, index=[8, 3, 10])
        actual = availability_for_gameweek(frame, "2026-09-18", injury_return_probability=.4)
        self.assertEqual(actual.tolist(), [.5, 0., .2])
        self.assertEqual(actual.index.tolist(), [8, 3, 10])
        frame["fixture_availability"] = actual
        pd.testing.assert_series_equal(actual, availability_for_gameweek(
            frame, "2026-09-18", injury_return_probability=.4
        ))

    def test_return_boundary_needs_empirical_prior_and_preserves_next_round(self):
        frame = pd.DataFrame({
            "status": ["i", "i", "s"],
            "news": ["Ankle injury - Expected back 19 Sep"] * 2 + ["Suspended until 19 Sep"],
            "chance_of_playing_next_round": [0, 0, 0],
        })
        dates = pd.Series(["2026-09-18", "2026-09-19", "2026-09-19"])
        self.assertEqual(availability_for_fixture(frame, dates, "2026-09-18").tolist(), [0, 0, 1])
        self.assertEqual(availability_for_fixture(
            frame, dates, "2026-09-18", injury_return_probability=0.3
        ).tolist(), [0, 0.3, 1])
        self.assertEqual(availability_for_fixture(
            frame, dates, "2026-09-18", injury_return_probability=0.3, is_next_round=True
        ).tolist(), [0, 0, 1])

    def test_unknown_injury_transfers_and_blanks_stay_unavailable(self):
        frame = pd.DataFrame({
            "status": ["i", "u", "n", "a"],
            "news": ["Unknown return date", "Expected back 19 Sep", "Expected back 19 Sep", ""],
            "fixture_count": [1, 1, 1, 0],
        })
        self.assertEqual(availability_for_fixture(
            frame, "2026-10-01", "2026-09-18", injury_return_probability=0.3
        ).tolist(), [0, 0, 0, 0])

    def test_stale_future_and_malformed_news_do_not_restore_fitness(self):
        frame = pd.DataFrame({
            "status": ["i"] * 5,
            "news": ["Expected back 17 Sep", "Expected back 19 Sep", "Expected back 31 Sep",
                     "Expected back 19 Sep", "Unknown return date"],
            "news_added": ["2026-09-01", "2026-09-20", None, "malformed", None],
        })
        self.assertEqual(availability_for_fixture(
            frame, "2026-10-01", "2026-09-18", injury_return_probability=0.3
        ).tolist(), [0] * 5)

    def test_year_rollover_and_explicit_year(self):
        frame = pd.DataFrame({
            "status": ["i", "i"],
            "news": ["Expected back 03 Jan", "Expected back 03 Jan 2028"],
        })
        self.assertEqual(availability_for_fixture(
            frame, "2027-01-03", "2026-12-29", injury_return_probability=0.3
        ).tolist(), [0.3, 0])

    def test_historical_rows_use_only_prior_snapshot_news(self):
        frame = pd.DataFrame({
            "availability_lag1": [0.0, 0.0],
            "status_lag1": ["i", "i"],
            "news_lag1": ["Expected back 19 Sep", "Unknown return date"],
            "status": ["u", "a"],
            "news": ["Unknown return date", "Expected back 19 Sep"],
        })
        self.assertEqual(availability_for_fixture(
            frame, "2026-09-20", "2026-09-18", injury_return_probability=0.3
        ).tolist(), [0.3, 0])

    def test_missing_fixture_date_keeps_snapshot_and_empty_frame_is_supported(self):
        frame = pd.DataFrame({"status": ["d"], "chance_of_playing_next_round": [25]})
        self.assertEqual(availability_for_fixture(frame, None, "2026-09-18").tolist(), [0.25])
        self.assertTrue(availability_for_fixture(frame.iloc[:0], None, "2026-09-18").empty)
        with self.assertRaises(ValueError):
            availability_for_fixture(frame, None, "2026-09-18", injury_return_probability=1.2)

    def test_recovery_prior_is_shifted_and_requires_enough_observed_outcomes(self):
        history = pd.DataFrame({
            "id": [1, 1, 2, 2],
            "kickoff_time": ["2026-09-12", "2026-09-20"] * 2,
            "status": ["i", "a", "i", "a"],
            "news": ["Expected back 19 Sep", "", "Expected back 19 Sep", ""],
            "minutes": [0, 90, 0, 0],
        })
        self.assertEqual(estimate_return_availability(history), {"probability": None, "samples": 2})
        self.assertEqual(estimate_return_availability(history, min_samples=2),
                         {"probability": 0.5, "samples": 2})
        history.loc[history["kickoff_time"].eq("2026-09-20"), ["news", "status"]] = [
            "Expected back 10 Oct", "i"
        ]
        self.assertEqual(estimate_return_availability(history, min_samples=2),
                         {"probability": 0.5, "samples": 2})


if __name__ == "__main__":
    unittest.main()
