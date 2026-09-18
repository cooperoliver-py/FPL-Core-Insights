import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

from scripts.match_features import build_match_features, load_match_data


class MatchFeaturesTests(unittest.TestCase):
    def test_missing_workload_differs_from_an_observed_zero(self):
        matches = pd.DataFrame({"match_id": ["cup"], "finished": [True],
                                "kickoff_time": pd.to_datetime(["2026-09-16"], utc=True)})
        records = pd.DataFrame({"match_id": ["cup"], "player_id": [1], "minutes_played": [0],
                                "kickoff_time": matches.kickoff_time, "competition": ["EFL Cup"]})
        players = pd.DataFrame({"player_id": [1, 2]})
        result = build_match_features(players, (matches, records), "2026-09-18")
        self.assertEqual(result.loc[0, "workload_nonpl_minutes_7d"], 0)
        self.assertTrue(pd.isna(result.loc[1, "workload_nonpl_minutes_7d"]))
        self.assertEqual(result["workload_nonpl_records_14d"].tolist(), [1, 0])

    def test_canonical_deduplication_deadline_missingness_and_team_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rows = [
                ("Premier League", "pl", "2026-09-01T15:00:00Z", True, 1, 2, 2, 1, 90, 0.4, 0.2),
                ("EFL Cup", "cup", "2026-09-05T19:00:00Z", True, 2, 3, 1, 0, 60, np.nan, 0.5),
                ("Friendlies", "friendly", "2026-09-06T12:00:00Z", True, 2, 3, 1, 1, 30, 5, 5),
                ("Premier League", "ongoing", "2026-09-08T11:00:00Z", True, 1, 2, 99, 99, 90, 99, 99),
                ("Premier League", "unfinished", "2026-09-03T15:00:00Z", False, 1, 2, 99, 99, 90, 99, 99),
                ("Premier League", "future", "2026-09-09T15:00:00Z", True, 1, 2, 99, 99, 90, 99, 99),
            ]
            for competition, key, kickoff, finished, home, away, hxg, axg, minutes, xg, xa in rows:
                path = root / "By Tournament" / competition / f"GW{key}"
                path.mkdir(parents=True)
                fixture = pd.DataFrame([dict(match_id=key, kickoff_time=kickoff, finished=finished,
                                             home_team=home, away_team=away,
                                             home_expected_goals_xg=hxg, away_expected_goals_xg=axg)])
                stats = pd.DataFrame([dict(match_id=key, player_id=11, minutes_played=minutes, xg=xg, xa=xa)])
                fixture.to_csv(path / "fixtures.csv", index=False)
                stats.to_csv(path / "playermatchstats.csv", index=False)
                if key == "pl":
                    # Both a repeated canonical file and its By Gameweek projection exist.
                    for duplicate in (root / "By Tournament" / competition / "GWduplicate", root / "By Gameweek" / "GW1"):
                        duplicate.mkdir(parents=True)
                        fixture.to_csv(duplicate / "fixtures.csv", index=False)
                        stats.to_csv(duplicate / "playermatchstats.csv", index=False)
            match_data = load_match_data(root)
            self.assertEqual(len(match_data[0]), 6)
            self.assertEqual(len(match_data[1]), 6)
            # Current club is 2; historical appearances may have been for club 1.
            players = pd.DataFrame({"player_id": [11, 12], "player_code": [111, 112], "team_code": [2, 99]}, index=[5, 7])
            result = build_match_features(players, match_data, "2026-09-08T12:00:00Z")
            row = result.loc[5]
            self.assertEqual(result.index.tolist(), [5, 7])
            self.assertEqual(row["workload_all_minutes_14d"], 180)
            self.assertEqual(row["workload_all_minutes_7d"], 180)
            self.assertEqual(row["workload_nonpl_minutes_7d"], 90)
            self.assertEqual(row["workload_friendlies_minutes_28d"], 30)
            self.assertEqual(row["workload_days_since_last"], 2)
            self.assertEqual(row["workload_history_appearances"], 3)
            self.assertEqual(result.loc[7, "workload_history_appearances"], 0)
            # Future fixture results/dates and all post-cutoff match statistics are irrelevant.
            changed_matches, changed_stats = (frame.copy() for frame in match_data)
            changed_matches.loc[changed_matches["match_id"].eq("future"), "home_expected_goals_xg"] = 900
            changed_stats.loc[changed_stats["match_id"].eq("future"), "minutes_played"] = 900
            pd.testing.assert_frame_equal(result, build_match_features(players, (changed_matches, changed_stats), "2026-09-08T12:00:00Z"))

    def test_missing_match_exports_are_supported(self):
        with tempfile.TemporaryDirectory() as directory:
            data = load_match_data(Path(directory))
            players = pd.DataFrame({"player_id": [1], "team_code": [1]})
            result = build_match_features(players, data, "2026-09-08")
            self.assertEqual(result.loc[0, "workload_history_appearances"], 0)

    def test_conflicting_optional_records_are_omitted_and_league_conflicts_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = pd.DataFrame({"match_id": ["cup"], "kickoff_time": ["2026-09-01"], "finished": [True]})
            for gw, minutes in ((1, 60), (2, 90)):
                path = root / "By Tournament" / "EFL Cup" / f"GW{gw}"
                path.mkdir(parents=True)
                fixture.to_csv(path / "fixtures.csv", index=False)
                pd.DataFrame({"match_id": ["cup"], "player_id": [1], "minutes_played": [minutes]}).to_csv(path / "playermatchstats.csv", index=False)
            with self.assertWarnsRegex(UserWarning, "conflicting non-league"):
                _, appearances = load_match_data(root)
            self.assertTrue(appearances.empty)
            (root / "By Tournament" / "EFL Cup").rename(root / "By Tournament" / "Premier League")
            with self.assertRaisesRegex(ValueError, "Conflicting canonical Premier League"):
                load_match_data(root)


if __name__ == "__main__":
    unittest.main()
