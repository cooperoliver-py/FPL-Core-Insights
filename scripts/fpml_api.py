"""Single-owner API. Local access must be explicitly enabled on loopback."""
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager
from datetime import UTC, datetime
import json
import os
from pathlib import Path
import sqlite3
import threading
import uuid

import httpx
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from scripts.fpml_data import analyse, load_snapshot, private_report, validate_snapshot
from scripts import fpl_predictions as engine

ROOT = Path(__file__).resolve().parents[1]


def now():
    return datetime.now(UTC).isoformat()


class Player(BaseModel):
    model_config = ConfigDict(extra="forbid")
    player_code: StrictInt
    purchase_price: float = Field(ge=0, allow_inf_nan=False)


class Squad(BaseModel):
    model_config = ConfigDict(extra="forbid")
    bank: float = Field(ge=0, allow_inf_nan=False)
    players: list[Player] = Field(min_length=15, max_length=15)
    excluded_player_codes: list[StrictInt] = Field(default_factory=list)


class PreviewInput(BaseModel):
    snapshot_id: str
    revision: int = Field(ge=0)
    draft: Squad


class SaveInput(BaseModel):
    preview_id: str
    revision: int = Field(ge=0)


class Store:
    def __init__(self):
        self.remote = bool(os.getenv("SUPABASE_URL")) and os.getenv("FPML_LOCAL") != "1"
        self.lock = threading.Lock()
        self.owner = os.getenv("FPML_OWNER_ID", "local")
        if not self.remote:
            path = Path(os.getenv("FPML_DB", str(ROOT / ".fpml/state.db")))
            path.parent.mkdir(parents=True, exist_ok=True)
            self.db = sqlite3.connect(path, check_same_thread=False)
            self.db.execute("CREATE TABLE IF NOT EXISTS state (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
            self.db.commit()

    def request(self, method, path, **kwargs):
        key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
        result = httpx.request(method, os.environ["SUPABASE_URL"].rstrip("/") + "/rest/v1/" + path,
                               headers={"apikey": key, "Authorization": f"Bearer {key}", "Prefer": "resolution=merge-duplicates"}, timeout=20, **kwargs)
        result.raise_for_status()
        return result.json() if result.content else None

    def get(self, key):
        if self.remote:
            rows = self.request("GET", "fpml_state", params={"owner_id": f"eq.{self.owner}", "key": f"eq.{key}", "select": "value"})
            return rows[0]["value"] if rows else None
        with self.lock:
            row = self.db.execute("SELECT value FROM state WHERE key=?", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def put(self, key, value):
        if self.remote:
            self.request("POST", "fpml_state", json=dict(owner_id=self.owner, key=key, value=value))
        else:
            with self.lock, self.db:
                self.db.execute("INSERT OR REPLACE INTO state VALUES (?,?)", (key, json.dumps(value, allow_nan=False)))

    def save(self, revision, value):
        if self.remote:
            return self.request("POST", "rpc/fpml_save_team", json={"owner": self.owner, "expected_revision": revision, "payload": value})
        with self.lock:
            self.db.execute("BEGIN IMMEDIATE")
            try:
                row = self.db.execute("SELECT value FROM state WHERE key='team'").fetchone()
                existing = json.loads(row[0]) if row else None
                if (existing["team"]["revision"] if existing else 0) != revision:
                    self.db.rollback()
                    return False
                self.db.execute("INSERT OR REPLACE INTO state VALUES ('team',?)", (json.dumps(value),))
                self.db.commit()
            except Exception:
                self.db.rollback()
                raise
        return True

    def interrupt_jobs(self):
        if self.remote:
            rows = self.request("GET", "fpml_state", params={"owner_id": f"eq.{self.owner}", "key": "like.preview:*", "select": "key,value"})
        else:
            with self.lock:
                rows = [dict(key=k, value=json.loads(v)) for k, v in self.db.execute("SELECT key,value FROM state WHERE key LIKE 'preview:%'")]
        for row in rows:
            if row["value"]["status"] in ("queued", "running"):
                self.put(row["key"], {**row["value"], "status": "interrupted", "error": "Server restarted. Calculate again."})


def create_app(snapshot_path=None, store=None, analyser=analyse):
    storage = store
    executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="fpml")
    capacity = threading.BoundedSemaphore(2)
    path = Path(snapshot_path or os.getenv("FPML_SNAPSHOT", str(ROOT / "predictions/latest.json")))
    cached = None
    refresh_lock = threading.Lock()
    last_refresh = 0.0

    def snapshot():
        nonlocal cached, last_refresh
        import time
        with refresh_lock:
            remote = os.getenv("FPML_SNAPSHOT_URL")
            if remote and time.monotonic() - last_refresh > 300:
                last_refresh = time.monotonic()
                try:
                    response = httpx.get(remote, timeout=15)
                    response.raise_for_status()
                    cached = validate_snapshot(response.json())
                except (httpx.HTTPError, ValueError):
                    pass  # Keep the last valid forecast during a network failure.
            if not remote or cached is None:
                try:
                    cached = load_snapshot(path)
                except (OSError, ValueError):
                    if cached is None:
                        raise HTTPException(503, "No complete forecast available. Generate predictions first.")
            return cached

    @asynccontextmanager
    async def lifespan(app):
        nonlocal storage
        storage = storage or Store()
        storage.interrupt_jobs()
        initial = os.getenv("FPML_INITIAL_SQUAD")
        if initial and storage.get("team") is None:
            payload = json.loads(Path(initial).read_text())
            draft = Squad.model_validate({key: value for key, value in payload.items() if not key.startswith("_comment")}).model_dump()
            result = analyser(snapshot(), draft)
            storage.save(0, dict(team=dict(revision=1, saved_at=now(), squad=draft), analysis=result))
        yield
        executor.shutdown(wait=False, cancel_futures=True)

    app = FastAPI(title="FPML", lifespan=lifespan)
    origins = [x.strip() for x in os.getenv("FPML_FRONTEND_ORIGIN", "http://localhost:5173,http://127.0.0.1:5173").split(",") if x.strip()]
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["GET", "POST", "PUT"], allow_headers=["Authorization", "Content-Type"])

    def owner(request: Request):
        if request.headers.get("origin") and request.headers["origin"] not in origins:
            raise HTTPException(403, "Origin is not permitted")
        if os.getenv("FPML_LOCAL") == "1" and request.client and request.client.host in ("127.0.0.1", "::1"):
            return "local"
        auth = request.headers.get("authorization", "")
        url, key, allowed = (os.getenv(n) for n in ("SUPABASE_URL", "SUPABASE_ANON_KEY", "FPML_OWNER_ID"))
        if not auth.startswith("Bearer ") or not all((url, key, allowed)):
            raise HTTPException(401, "Sign in required")
        try:
            response = httpx.get(url.rstrip("/") + "/auth/v1/user", headers={"apikey": key, "Authorization": auth}, timeout=10)
            response.raise_for_status()
            user = response.json()
        except (httpx.HTTPError, ValueError):
            raise HTTPException(401, "Session expired. Sign in again.")
        if user.get("id") != allowed:
            raise HTTPException(403, "This account does not own FPML")
        return allowed

    def check(revision, snapshot_id, current_id):
        state = storage.get("team")
        if revision != (state["team"]["revision"] if state else 0):
            raise HTTPException(409, "Team changed on another device. Reload before saving.")
        if snapshot_id != current_id:
            raise HTTPException(409, "Forecast changed. Calculate again.")

    @app.get("/api/workspace", dependencies=[Depends(owner)])
    def workspace():
        current = snapshot()
        state = storage.get("team") or {}
        analysis = state.get("analysis")
        return dict(snapshot=current, team=state.get("team"), analysis=analysis,
                    auth=dict(mode="local" if os.getenv("FPML_LOCAL") == "1" else "supabase"))

    @app.post("/api/previews", dependencies=[Depends(owner)])
    def preview(payload: PreviewInput):
        current = snapshot()
        check(payload.revision, payload.snapshot_id, current["id"])
        draft = payload.draft.model_dump()
        try:
            import pandas as pd
            catalog = pd.DataFrame(current["players"])
            _, _, excluded = engine.resolve_squad(draft, catalog)
            unknown = excluded - set(catalog.player_code)
            if unknown:
                raise ValueError(f"Unknown excluded player codes: {sorted(unknown)}")
        except (ValueError, TypeError, KeyError) as exc:
            raise HTTPException(422, str(exc))
        if not capacity.acquire(blocking=False):
            raise HTTPException(429, "Analysis is busy. Try again shortly.")
        job = dict(id=str(uuid.uuid4()), status="queued", revision=payload.revision, snapshot_id=current["id"])
        try:
            storage.put("preview:" + job["id"], job)
        except Exception:
            capacity.release()
            raise
        def calculate():
            try:
                storage.put("preview:" + job["id"], {**job, "status": "running"})
                result = analyser(current, draft)
                storage.put("preview:" + job["id"], {**job, "status": "completed", "analysis": result})
            except Exception:
                storage.put("preview:" + job["id"], {**job, "status": "failed", "error": "Analysis failed. Check your squad and try again."})
            finally:
                capacity.release()
        executor.submit(calculate)
        return job

    @app.get("/api/previews/{preview_id}", dependencies=[Depends(owner)])
    def get_preview(preview_id: str):
        job = storage.get("preview:" + preview_id)
        if not job:
            raise HTTPException(404, "Preview not found")
        return job

    @app.put("/api/team", dependencies=[Depends(owner)])
    def save(payload: SaveInput):
        job = get_preview(payload.preview_id)
        if job["status"] != "completed":
            raise HTTPException(409, "Calculate a successful preview before saving")
        if job["revision"] != payload.revision:
            raise HTTPException(409, "Preview belongs to another team revision")
        if job["analysis"]["snapshot_id"] != job["snapshot_id"]:
            raise HTTPException(409, "Preview forecast is inconsistent. Calculate again.")
        current = snapshot()
        check(payload.revision, job["snapshot_id"], current["id"])
        value = dict(team=dict(revision=payload.revision+1, saved_at=now(), squad=job["analysis"]["team"]), analysis=job["analysis"])
        if not storage.save(payload.revision, value):
            raise HTTPException(409, "Team changed on another device")
        return value

    @app.get("/api/export", dependencies=[Depends(owner)])
    def export(format: str = "json"):
        state = storage.get("team")
        if not state:
            raise HTTPException(404, "Save your team first")
        if format == "json":
            body, media = json.dumps(state["team"]["squad"], indent=2), "application/json"
        elif format in ("md", "csv"):
            current = snapshot()
            if state["analysis"]["snapshot_id"] != current["id"]:
                raise HTTPException(409, "Forecast changed. Calculate and save before exporting analysis.")
            forecast, markdown = private_report(current, state["analysis"])
            body = markdown if format == "md" else forecast.to_csv(index=False, lineterminator="\n")
            media = "text/markdown" if format == "md" else "text/csv"
        else:
            raise HTTPException(422, "Choose json, csv or md")
        return Response(body, media_type=media, headers={"Content-Disposition": f'attachment; filename="fpml.{format}"', "Cache-Control": "no-store"})

    @app.middleware("http")
    async def private_headers(request, call_next):
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    return app


app = create_app()
