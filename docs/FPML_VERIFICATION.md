# FPML implementation checks

Verified locally on 28 October 2026.

- Python suite: 61 tests pass. Coverage includes forecast validation, engine parity, private access, preview/save conflicts, snapshot races and SQLite concurrent saves.
- Frontend: 9 tests pass, including transfer accounting, filter navigation, draft preservation, save conflicts and refresh/save ordering.
- TypeScript and Vite production build pass. Development fixture data is loaded only in development.
- Impeccable detector reports no findings for `frontend/src`.
- Safari exercised Team, Players, Model, player search/details, a real optimizer transfer preview, calculation and discard. The hypothetical transfer was not saved. Browser Back closes the editor. Normal browser zoom was restored after enlarged responsive checks.
- Native FigCraft save/reopen/export and persisted links pass. See `design/verification.json` and `design/README.md` for evidence and limits.

The API and frontend run locally at ports 8000 and 5173. Local state lives in ignored `.fpml/state.db`; generated public forecasts contain no private squad fields. Existing CLI reports and the native design still contain the repository's squad.

## Remaining external checks

Render and Supabase have not been provisioned. Their configuration and schema are prepared, but live hosted authentication, multi-device persistence, restart/recovery, backup restoration, optimizer memory and latency require the configured services. Free-tier sleep or quota behaviour is not measured.

A physical phone and the native FigCraft presenter were not tested. Safari zoom checks cover responsive reflow, not hardware touch or mobile Safari behaviour. No deployment, commit or push was performed.
