import copy
from concurrent.futures import ThreadPoolExecutor
import threading
import json
import os
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

import pandas as pd
from scripts import fpl_predictions as engine
from scripts.fpml_data import analyse, write_snapshot, validate_snapshot


def fixture():
    positions = ["Goalkeeper"]*2 + ["Defender"]*5 + ["Midfielder"]*5 + ["Forward"]*3
    frame = pd.DataFrame(dict(player_code=range(1,16), player_id=range(1,16), position=positions,
                              team_code=[i%5 for i in range(15)], team="Team", web_name=[f"Player {i}" for i in range(15)],
                              status="a", team_short_name="TM", recent_gameweek_points="No completed GW history", recent_points_count=0, recent_points_total=None, recent_points_average=None, recent_points_breakdown="", now_cost=5.2, GW9_predicted_points=range(1,16), GW9_availability=1,
                              weighted_score=range(1,16), predicted_value=1, baseline=1,
                              baseline_rolling_points=1, baseline_ep_next=1, confidence_score=1, confidence="high", drivers="form"))
    squad = dict(bank=2.0, players=[dict(player_code=i,purchase_price=5.0) for i in range(1,16)], excluded_player_codes=[])
    snapshot = dict(id="test",schema_version=1,season="test",generated_at="2026-10-28T00:00:00Z",deadline=None,weights=[1.0],methodology="test",limits=[],evaluation={},evaluation_context={},freshness=[],performance=[],gameweeks=[9],players=json.loads(frame.to_json(orient="records")))
    return frame,squad,snapshot


class DataTests(unittest.TestCase):
    def test_shared_analysis_money_and_lineup_parity(self):
        frame,squad,snapshot=fixture()
        result=analyse(snapshot,squad)
        self.assertAlmostEqual(result["budget"]["selling_value"],76.5)
        self.assertAlmostEqual(result["budget"]["available"],78.5)
        self.assertAlmostEqual(result["current"]["weighted_points"],engine._exact_lineup_score(frame,"GW9_predicted_points")*engine.HORIZON_WEIGHTS[0])
        self.assertTrue(result["hold"])
        self.assertEqual(squad["players"][0]["purchase_price"],5.0)

    def test_owned_exclusion_preserves_sale_value_but_removes_points(self):
        frame,squad,snapshot=fixture()
        extra=frame.iloc[0].to_dict()
        extra.update(player_code=16,player_id=16,team_code=5)
        snapshot['players'].append(extra)
        squad['excluded_player_codes']=[1]
        result=analyse(snapshot,squad)
        self.assertAlmostEqual(result['budget']['selling_value'],76.5)
        self.assertIn(1,result['current']['players'])
        self.assertNotIn(1,result['current']['lineups']['9']['starters'])
        self.assertNotIn(1,result['optimal']['players'])
        self.assertEqual(snapshot['players'][0]['GW9_predicted_points'],1)

    def test_snapshot_never_contains_private_fields(self):
        frame,_,_=fixture()
        frame=frame.assign(purchase_price=5, selling_price=5, excluded=True,current_squad=True,recommended_squad=True,current_GW9_lineup=True)
        with tempfile.TemporaryDirectory() as directory:
            result=write_snapshot(frame,"test",[9],{}, {}, [],pd.DataFrame(),Path(directory))
            player=result["players"][0]
            self.assertNotIn("excluded",player)
            self.assertNotIn("purchase_price",player)
            self.assertNotIn("current_GW9_lineup",player)

    def test_optional_player_fields_match_frontend_types(self):
        _, _, snapshot = fixture()
        for key, value in [('first_name', None), ('second_name', None), ('news', 3),
                           ('recent_gameweek_points', 3), ('recent_points_breakdown', []),
                           ('recent_points_total', '4'), ('recent_points_average', float('inf')),
                           ('recent_points_count', '5'), ('data_coverage', 'full')]:
            with self.subTest(key=key):
                malformed = copy.deepcopy(snapshot)
                malformed['players'][0][key] = value
                with self.assertRaises(ValueError):
                    validate_snapshot(malformed)
        for key in ('news', 'recent_gameweek_points', 'recent_points_breakdown',
                    'recent_points_total', 'recent_points_average', 'recent_points_count', 'data_coverage'):
            snapshot['players'][0][key] = None
        self.assertIs(validate_snapshot(snapshot), snapshot)

    def test_exclusions_are_request_local(self):
        _,squad,snapshot=fixture()
        before=copy.deepcopy(snapshot)
        squad["excluded_player_codes"]=[1]
        with self.assertRaises(ValueError):
            analyse(snapshot,squad)  # Only 14 selectable candidates remain.
        self.assertEqual(snapshot,before)


try:
    from fastapi.testclient import TestClient
    from scripts.fpml_api import create_app, Store
except ImportError:
    TestClient=None


@unittest.skipIf(TestClient is None,"Install requirements-web.txt to run API checks")
class APITests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        _,self.squad,self.snapshot=fixture()
        self.path=Path(self.temp.name)/"snapshot.json"
        self.path.write_text(json.dumps(self.snapshot))
        self.env=patch.dict(os.environ,{"FPML_LOCAL":"1","FPML_DB":str(Path(self.temp.name)/"state.db")})
        self.env.start()
        self.store=Store()
        self.client=TestClient(create_app(self.path,self.store),client=("127.0.0.1",1234))
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None,None,None)
        self.env.stop()
        self.temp.cleanup()

    def test_preview_does_not_save_and_save_checks_revision(self):
        response=self.client.post('/api/previews',json=dict(snapshot_id="test",revision=0,draft=self.squad))
        self.assertEqual(response.status_code,200,response.text)
        job=response.json()
        for _ in range(100):
            job=self.client.get('/api/previews/'+job['id']).json()
            if job['status'] in ('completed','failed'): break
            time.sleep(.02)
        self.assertEqual(job['status'],'completed',job)
        self.assertIsNone(self.client.get('/api/workspace').json()['team'])
        saved=self.client.put('/api/team',json=dict(preview_id=job['id'],revision=0))
        self.assertEqual(saved.status_code,200,saved.text)
        self.assertEqual(self.client.put('/api/team',json=dict(preview_id=job['id'],revision=0)).status_code,409)
        self.assertEqual(self.client.get('/api/export').json(),self.squad)
        markdown = self.client.get('/api/export?format=md')
        self.assertEqual(markdown.status_code,200,markdown.text)
        self.assertIn('# FPL predictions',markdown.text)
        self.assertIn('## Your current squad',markdown.text)
        exported = self.client.get('/api/export?format=csv')
        self.assertIn('player_code',exported.text.splitlines()[0])
        self.assertIn('GW9_predicted_points',exported.text.splitlines()[0])

    def test_auth_fails_closed_and_nonowner_denied(self):
        with patch.dict(os.environ,{"FPML_LOCAL":"0"}):
            self.assertEqual(self.client.get('/api/workspace').status_code,401)
            with patch.dict(os.environ,{"SUPABASE_URL":"https://example.invalid","SUPABASE_ANON_KEY":"key","FPML_OWNER_ID":"owner"}):
                with patch('scripts.fpml_api.httpx.get') as get:
                    get.return_value.json.return_value={"id":"other"}
                    self.assertEqual(self.client.get('/api/workspace',headers={"Authorization":"Bearer token"}).status_code,403)

    def test_restart_marks_pending_jobs_interrupted_and_preserves_team(self):
        self.store.put('preview:old',dict(id='old',status='running'))
        saved=dict(team=dict(revision=3,saved_at='then',squad=self.squad),analysis=None)
        self.store.put('team',saved)
        self.store.interrupt_jobs()
        self.assertEqual(self.store.get('preview:old')['status'],'interrupted')
        self.assertEqual(self.store.get('team'),saved)

    def test_failed_preview_retains_saved_state(self):
        def fail(snapshot,draft):
            raise RuntimeError('private server detail')
        with TestClient(create_app(self.path,self.store,analyser=fail),client=('127.0.0.1',1234)) as client:
            response=client.post('/api/previews',json=dict(snapshot_id='test',revision=0,draft=self.squad))
            job=response.json()
            for _ in range(100):
                job=client.get('/api/previews/'+job['id']).json()
                if job['status']=='failed': break
                time.sleep(.01)
            self.assertEqual(job['status'],'failed')
            self.assertNotIn('private server detail',job['error'])
            self.assertIsNone(client.get('/api/workspace').json()['team'])
            self.assertEqual(client.put('/api/team',json=dict(preview_id=job['id'],revision=0)).status_code,409)

    def test_snapshot_update_between_reads_cannot_accept_mismatched_preview(self):
        newer = {**self.snapshot, 'id': 'new'}
        with patch('scripts.fpml_api.load_snapshot', side_effect=[self.snapshot, newer]) as read:
            response = self.client.post('/api/previews', json=dict(snapshot_id='new', revision=0, draft=self.squad))
        self.assertEqual(response.status_code, 409, response.text)
        self.assertEqual(read.call_count, 1)
        self.assertIsNone(self.store.get('team'))

    def test_save_rejects_preview_with_mismatched_analysis_snapshot(self):
        analysis = analyse(self.snapshot, self.squad)
        analysis['snapshot_id'] = 'older'
        self.store.put('preview:mismatched', dict(id='mismatched', status='completed', revision=0,
                                               snapshot_id='test', analysis=analysis))
        response = self.client.put('/api/team', json=dict(preview_id='mismatched', revision=0))
        self.assertEqual(response.status_code, 409, response.text)
        self.assertIsNone(self.store.get('team'))

    def test_malformed_remote_retains_complete_local_snapshot(self):
        self.assertEqual(self.client.get('/api/workspace').json()['snapshot']['id'], 'test')
        malformed = copy.deepcopy(self.snapshot)
        malformed['players'][0]['first_name'] = None
        with patch.dict(os.environ, {'FPML_SNAPSHOT_URL': 'https://example.invalid/latest.json'}):
            with patch('scripts.fpml_api.httpx.get') as get:
                get.return_value.json.return_value = malformed
                response = self.client.get('/api/workspace')
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()['snapshot'], self.snapshot)

    def test_two_connections_allow_only_one_revision_save(self):
        second = Store()
        barrier = threading.Barrier(2)
        def save(store, label):
            barrier.wait()
            return store.save(0, dict(team=dict(revision=1, saved_at=label, squad=self.squad), analysis=None))
        with ThreadPoolExecutor(max_workers=2) as pool:
            first = pool.submit(save, self.store, 'first')
            other = pool.submit(save, second, 'second')
            results = [first.result(), other.result()]
        self.assertEqual(sorted(results), [False, True])
        self.assertEqual(self.store.get('team')['team']['revision'], 1)
        second.db.close()

    def test_invalid_squad_and_stale_snapshot(self):
        self.assertEqual(self.client.post('/api/previews',json=dict(snapshot_id="old",revision=0,draft=self.squad)).status_code,409)
        self.squad['players'][1]=self.squad['players'][0]
        self.assertEqual(self.client.post('/api/previews',json=dict(snapshot_id="test",revision=0,draft=self.squad)).status_code,422)
