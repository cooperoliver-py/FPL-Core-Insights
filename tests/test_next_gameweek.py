from contextlib import ExitStack
import hashlib
from pathlib import Path
from unittest.mock import patch
import json
import unittest

import pandas as pd

from scripts import fpl_predictions as engine
from scripts.fpml_data import analyse, private_report
from tests.test_fpml import fixture
from tests.test_fpl_predictions import legal_squad


class NextGameweekTests(unittest.TestCase):
    def test_complete_pool_ranks_before_truncation_and_preserves_horizon_order(self):
        squad = legal_squad().assign(status='a', now_cost=5., excluded=False,
                                    GW1_predicted_points=1., GW2_predicted_points=1.)
        squad['web_name'] = squad.player_code.astype(str)
        incoming = pd.concat([squad.iloc[[-1]]] * 12, ignore_index=True)
        incoming['player_code'] = range(100, 112)
        incoming['team_code'] = 99
        incoming['GW1_predicted_points'] = [2.] * 11 + [10.]
        incoming['GW2_predicted_points'] = [40.] * 11 + [1.]
        pool = pd.concat([squad, incoming], ignore_index=True)
        options = engine._transfer_options(squad, 0, pool, [1, 2], include_weekly_gains=True)
        legacy = engine._transfer_options(squad, 0, pool, [1, 2])
        pd.testing.assert_frame_equal(legacy, options[legacy.columns])
        self.assertNotIn(111, options.head(10).in_player_code.tolist())
        result = engine._next_gameweek_result(options, 1)
        self.assertEqual(result['transfers'][0]['in_player_code'], 111)
        self.assertFalse(result['hold'])
        self.assertEqual(options.iloc[0].in_player_code, 100)
        for row in options.itertuples():
            self.assertAlmostEqual(row.weighted_gain, row.weekly_gains['1'] + .9 * row.weekly_gains['2'])
            self.assertEqual(row.next_gw_gain, row.weekly_gains['1'])
            replacement = squad.copy()
            replacement.loc[replacement.player_code.eq(row.out_player_code), ['player_code', 'GW1_predicted_points', 'GW2_predicted_points']] = pool.loc[pool.player_code.eq(row.in_player_code), ['player_code', 'GW1_predicted_points', 'GW2_predicted_points']].iloc[0].to_numpy()
            expected_weighted = sum(weight * engine._exact_lineup_score(replacement, f'GW{gw}_predicted_points')
                                    for weight, gw in zip(engine.HORIZON_WEIGHTS, (1, 2)))
            expected_weighted -= sum(weight * engine._exact_lineup_score(squad, f'GW{gw}_predicted_points')
                                     for weight, gw in zip(engine.HORIZON_WEIGHTS, (1, 2)))
            self.assertEqual(row.weighted_gain, expected_weighted)
            for gw in (1, 2):
                column = f'GW{gw}_predicted_points'
                starters, captain = engine.best_lineup(replacement, column)
                expected = replacement.loc[starters, column].sum() + replacement.at[captain, column] - engine._exact_lineup_score(squad, column)
                self.assertAlmostEqual(row.weekly_gains[str(gw)], expected)

    def test_scores_handle_bench_formation_and_captain_changes(self):
        squad = legal_squad().assign(status='a', now_cost=5., excluded=False)
        squad['web_name'] = squad.player_code.astype(str)
        squad['GW1_predicted_points'] = squad.predicted_points.astype(float)
        for position, points in [('Goalkeeper', .5), ('Forward', 12.), ('Forward', 30.)]:
            incoming = squad.loc[squad.position.eq(position)].iloc[[-1]].copy()
            incoming['player_code'], incoming['team_code'], incoming['GW1_predicted_points'] = 99, 99, points
            pool = pd.concat([squad, incoming], ignore_index=True)
            options = engine._transfer_options(squad, 0, pool, [1], include_weekly_gains=True)
            for row in options.itertuples():
                replacement = squad.copy()
                replacement.loc[replacement.player_code.eq(row.out_player_code), 'GW1_predicted_points'] = points
                starters, captain = engine.best_lineup(replacement, 'GW1_predicted_points')
                expected = replacement.loc[starters, 'GW1_predicted_points'].sum() + replacement.at[captain, 'GW1_predicted_points'] - engine._exact_lineup_score(squad, 'GW1_predicted_points')
                self.assertAlmostEqual(row.next_gw_gain, expected)
                self.assertAlmostEqual(row.weighted_gain, expected)
            if position == 'Goalkeeper':
                self.assertEqual(options.iloc[0].next_gw_gain, 0)

    def test_holds_are_independent_and_ties_use_bank_then_ids(self):
        rows = pd.DataFrame([
            dict(next_gw_gain=0, weighted_gain=5, bank_after=2, out_player_code=3, in_player_code=9),
            dict(next_gw_gain=-1, weighted_gain=10, bank_after=3, out_player_code=2, in_player_code=8),
        ])
        self.assertTrue(engine._next_gameweek_result(rows, 9)['hold'])
        self.assertGreater(rows.weighted_gain.max(), 0)
        rows['next_gw_gain'], rows['weighted_gain'] = 2, -1
        self.assertFalse(engine._next_gameweek_result(rows, 9)['hold'])
        self.assertLess(rows.weighted_gain.max(), 0)
        self.assertEqual(engine._next_gameweek_result(rows, 9)['transfers'][0]['out_player_code'], 2)
        rows['bank_after'] = 1
        self.assertEqual(engine._next_gameweek_result(rows.iloc[::-1], 9)['transfers'][0]['out_player_code'], 2)
        self.assertTrue(engine._next_gameweek_result(rows.head(0), 9)['hold'])

    def test_default_transfer_contract_and_private_report_remain_legacy(self):
        frame, squad, snapshot = fixture()
        incoming = frame.iloc[-1].to_dict()
        incoming.update(player_code=99, player_id=99, team_code=99, web_name='Immediate', GW9_predicted_points=30)
        snapshot['players'].append(incoming)
        result = analyse(snapshot, squad)
        json.dumps(result, allow_nan=False)
        self.assertNotIn('next_gameweek', result)
        columns = ['out_player_code', 'out', 'in_player_code', 'in', 'selling_price',
                   'buy_price', 'bank_after', 'weighted_gain']
        self.assertEqual(list(result['transfers'][0]), columns)
        user, bank, _ = engine.resolve_squad(squad, pd.DataFrame(snapshot['players']))
        default = engine._transfer_options(user, bank, pd.DataFrame(snapshot['players']).assign(excluded=False), [9])
        enriched = engine._transfer_options(user, bank, pd.DataFrame(snapshot['players']).assign(excluded=False), [9], include_weekly_gains=True)
        pd.testing.assert_frame_equal(default, enriched[columns])
        self.assertEqual(list(engine._transfer_options(user, bank, frame.assign(excluded=False), [9]).columns), columns)
        with patch.object(engine, '_data_sha', return_value='test'):
            _, markdown = private_report(snapshot, result)
        normalized = '\n'.join(line for line in markdown.splitlines() if not line.startswith('Last generated:'))
        self.assertEqual(hashlib.sha256(normalized.encode()).hexdigest(), 'fdcc1bd4923d894d793281a5174033b5fffe0e8b09d9b5cd2ec86a4f4a324ff1')
        self.assertIn('## One-transfer recommendation', markdown)
        self.assertNotIn('Next-gameweek transfer', markdown)

    def test_cli_opts_into_both_report_objectives_without_writing_outputs(self):
        frame, draft, snapshot = fixture()
        weeks = list(range(9, 14))
        for gw in weeks:
            frame[f'GW{gw}_predicted_points'] = frame.GW9_predicted_points
            frame[f'GW{gw}_availability'] = 1.
        incoming = frame.iloc[-1].copy()
        incoming['player_code'], incoming['player_id'], incoming['team_code'] = 99, 99, 99
        incoming['web_name'] = 'Immediate'
        incoming['GW9_predicted_points'] = 30.
        frame = pd.concat([frame, incoming.to_frame().T], ignore_index=True).infer_objects()
        user, bank, excluded = engine.resolve_squad(draft, frame)
        with ExitStack() as stack:
            for name, value in {
                '_latest_season': engine.TRAIN_SEASON, '_season_path': Path('/unused'),
                '_before_gameweek_deadline': True, '_load_training_data': pd.DataFrame(),
                '_evaluate_and_fit': (None, {}, {}), '_forecast': frame,
                '_incomplete_source_gameweeks': [], '_live_performance': pd.DataFrame(),
                '_resolve_user_squad': (user, bank, excluded), '_select_initial_squad': list(range(15)),
                '_data_sha': 'test', '_model_sha': 'test',
            }.items():
                stack.enter_context(patch.object(engine, name, return_value=value))
            snapshot_writer = stack.enter_context(patch('scripts.fpml_data.write_snapshot'))
            writer = stack.enter_context(patch.object(engine, '_write_outputs'))
            transfer_options = stack.enter_context(patch.object(engine, '_transfer_options', wraps=engine._transfer_options))
            engine.run(gameweek=9, squad_path=Path('/unused'))
            self.assertTrue(transfer_options.call_args.kwargs['include_weekly_gains'])
            snapshot_writer.assert_called_once()
            markdown = writer.call_args.args[1]
        self.assertLess(markdown.index('### GW9 immediate'), markdown.index('### 5-GW weighted alternative'))
        self.assertEqual(markdown.count('## Your current squad'), 1)
        self.assertIn('Weekly XI+captain gains', markdown)
        self.assertIn('GW9 gain | Weighted gain', markdown)
        self.assertIn('availability 100%', markdown)
        self.assertIn('Bank after', markdown)
        self.assertIn('before transfer costs', markdown)
        self.assertNotIn('Recalculate', markdown)

    def test_returner_has_no_immediate_gain(self):
        frame, squad, snapshot = fixture()
        frame['GW10_predicted_points'] = frame.GW9_predicted_points
        frame['GW10_availability'] = 1.
        incoming = frame.iloc[-1].copy()
        incoming['player_code'], incoming['player_id'], incoming['team_code'] = 99, 99, 99
        incoming['web_name'], incoming['status'] = 'Returning', 's'
        incoming['GW9_predicted_points'], incoming['GW9_availability'] = 0., 0.
        incoming['GW10_predicted_points'] = 100.
        frame = pd.concat([frame, incoming.to_frame().T], ignore_index=True).infer_objects()
        user, bank, _ = engine.resolve_squad(squad, frame)
        options = engine._transfer_options(user, bank, frame.assign(excluded=False), [9, 10], include_weekly_gains=True)
        self.assertGreater(options.iloc[0].weighted_gain, 0)
        self.assertTrue(engine._next_gameweek_result(options, 9)['hold'])
        self.assertTrue(all(options.next_gw_gain <= 0))

    def test_empty_cli_report_holds_for_both_objectives(self):
        frame, squad, snapshot = fixture()
        analysis = analyse(snapshot, squad)
        report_forecast, _ = private_report(snapshot, analysis)
        user, bank, _ = engine.resolve_squad(squad, frame)
        options = engine._transfer_options(user, bank, frame.assign(excluded=False), [9], include_weekly_gains=True)
        self.assertTrue(options.empty)
        result = engine._next_gameweek_result(options, 9)
        markdown = engine._render_markdown(report_forecast, {}, 'test', [9], set(range(1, 16)),
                                           options, next_gameweek=result)
        self.assertEqual(markdown.count('**HOLD**'), 2)
        self.assertEqual(markdown.count('## Your current squad'), 1)
        self.assertIn('### GW9 immediate', markdown)
        self.assertIn('### 1-GW weighted alternative', markdown)
