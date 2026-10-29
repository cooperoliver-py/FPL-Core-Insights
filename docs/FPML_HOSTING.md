# Run FPML

FPML needs **two servers running at the same time**. The API performs calculations and stores your team. The frontend serves the website.

## Set up once

Open a terminal in the repository root (`FPL-Core-Insights`). You need Python, Node.js and npm installed.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-web.txt
npm --prefix frontend ci
```

Skip these installation steps on later runs unless dependencies change. Local mode does not require Render, Supabase or a frontend `.env` file.

## Start the API in terminal 1

From the repository root, run:

```sh
FPML_LOCAL=1 FPML_INITIAL_SQUAD=squad.json .venv/bin/uvicorn scripts.fpml_api:app --host 127.0.0.1 --port 8000
```

Wait for `Application startup complete`. Leave this terminal running.

The API listens at `http://127.0.0.1:8000`. Its root page returns **404 Not Found** because the API does not serve the website. To check the API, open `http://127.0.0.1:8000/api/workspace`; it returns JSON.

## Start the frontend in terminal 2

Open a second terminal in the same repository root, then run:

```sh
npm --prefix frontend run dev
```

Wait for Vite to display its local URL. Leave this terminal running too.

Open **http://127.0.0.1:5173/team** in Safari. This is the website address. The frontend forwards `/api` requests to the API on port 8000.

If Vite reports that port 5173 is occupied, stop the existing frontend before retrying. Use port 5173 for the configured local setup.

## Stop or restart FPML

Press **Ctrl+C** in terminal 1 and terminal 2 to stop both servers. Closing the browser tab does not stop them.

To restart, repeat the two start commands above. You do not need to reinstall dependencies or regenerate forecasts each time.

## Update local forecasts

The repository includes `predictions/latest.json`, so forecast generation is not required to start FPML.

To download forecasts produced by the scheduled GitHub workflow, run `git pull` from the repository root. Alternatively, generate forecasts locally:

```sh
.venv/bin/python -m scripts.fpl_predictions
```

Generation writes the public JSON snapshot and the existing Markdown and CSV reports. After updating, press **Refresh forecasts** in FPML or reload the page. Starting the local servers does not automatically download forecasts from GitHub.

## Keep your saved team

The API imports `squad.json` only when no saved team exists. Later saves live in `.fpml/state.db`, outside public report files. Restarting the servers preserves this database.

Stop the API before copying the database for backup. Restore to an empty stopped local instance and verify `/api/workspace` before replacing the active copy.

Local mode accepts loopback connections only. Do not expose it through a tunnel or reverse proxy.

## Free hosted setup

`render.yaml` prepares a static frontend and one free Python service. No deployment is performed by this repository change.
Create a Supabase project, apply `supabase/schema.sql`, disable public signup, then create the owner's user in the authentication console.
Set the following server environment variables through Render's secret settings:

| Variable | Value |
| --- | --- |
| `SUPABASE_URL` | Supabase project URL |
| `SUPABASE_ANON_KEY` | Supabase public key used to validate user sessions |
| `SUPABASE_SERVICE_ROLE_KEY` | Server-only service key; never prefix with VITE or place in frontend code |
| `FPML_OWNER_ID` | Allowed auth user UUID |
| `FPML_FRONTEND_ORIGIN` | Exact HTTPS frontend origin |
| `FPML_SNAPSHOT_URL` | Public raw URL of the exclusion-free `predictions/latest.json` |

Never set `FPML_LOCAL` on hosted services. Run one API instance with one Uvicorn worker; startup marks interrupted jobs for retry. The bounded analysis worker accepts at most two running/queued jobs. All durable state uses Supabase, including preview results. Owner access is checked server-side against Supabase Auth on every request. Database tables and save RPC are inaccessible to anonymous and authenticated browser roles; only the server service role can write them.

Configure the frontend's Supabase URL/public key and API URL as described in `frontend/.env.example`. The owner UUID belongs only in the API configuration. The owner signs in with the account created above. Bearer sessions avoid cookie-based CSRF; the API additionally restricts browser origins. Supabase handles password login throttling. Session expiry requires sign-in again.

The API refreshes a configured public snapshot at most every five minutes and keeps the last valid snapshot on failure. The scheduled prediction workflow must commit `predictions/latest.json` alongside existing outputs. Never publish the SQLite database, squad exports, service key, or Supabase state dumps. Current CLI CSV/Markdown outputs already include the repository's squad; retain or remove that public reporting separately according to the repository owner's policy.

## Validation before relying on hosting

Verify private access with no token and a non-owner account. Save on desktop, reload on mobile, and confirm a stale tab receives a conflict. Restart the API and confirm saved squads persist and interrupted previews can be retried. Verify database backup and restore on a separate project using Supabase's documented database export tools before calling recovery tested.

Measure preview latency and peak memory using a real squad on the selected host. No hosted benchmark, physical-device test, remote backup restore or deployment is claimed here. Free services may sleep or pause, and quotas may change. A paid upgrade requires the owner's decision.
