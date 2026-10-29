# FPML

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

The existing engine uses Python, pandas, scikit-learn, and SciPy. The local frontend uses React, TypeScript and Vite; FastAPI connects it to the existing engine.
Implementation follows [the final plan](FPML_PLAN.md).
These are technical recommendations. The user has not explicitly selected or provisioned a hosting provider.

## Users

The owner uses FPML as a personal tool on desktop and mobile. Public signup and multiple users are outside the first version.

## Product purpose

Help the owner manage their current FPL squad, inspect forecasts, choose a starting XI and captains, evaluate transfers, and inspect model performance.
Success means completing the weekly team review without editing JSON or reading the generated Markdown report.

## Operating context

The existing program generates player forecasts, squad recommendations, and performance reports on a schedule.
The owner wants private hosted access with the same saved squad on both devices.
The owner has proposed the installed FigCraft app as an alternative to Figma for modelling the interface. The editable FigCraft archive and native exports are in `design/`.
The owner prefers previewing edits before explicitly saving them as the recorded current team.
Saving records changes already made in FPL. FPML never submits transfers to FPL.

## Capabilities and constraints

- Include every substantive capability in `predictions/latest.md`.
- Support editing the squad, purchase prices, bank, and player exclusions.
- Preserve existing squad legality, selling-price, budget, lineup, and transfer calculations.
- Keep one actual current squad. Temporary previews do not create separate saved future teams.
- Keep personal saved state outside public generated artifacts.
- Keep the model's existing limits, including no chips, transfer hits, or predicted price changes.
- Hosting remains undecided. The owner initially accepted a modest paid cost and then asked about free services. Render Free with Supabase Free is the latest recommendation, not a confirmed choice.

## Brand commitments

The app is called FPML. The owner wants a premium, minimalist dark interface with white emphasis and selective green highlights.
Avoid football-themed decoration, generic dashboard styling, and unnecessary explanatory text.

## Evidence on hand

`predictions/latest.md` defines report coverage. `predictions/latest.csv` contains player forecasts and squad-selection flags.
`predictions/performance.csv` contains scored archived predictions. `scripts/fpl_predictions.py` owns forecast generation and optimization.
`squad.example.json` documents saved-team input. The repository currently tracks `squad.json` and reports with squad details.
The implemented UI is in `frontend/`; public forecast exchange uses `predictions/latest.json`.
FigCraft 0.11.2 save, reopen, native export and persisted prototype links were verified. Native presenter playback remains unverified.
Hosted preview performance and physical phone interaction remain unmeasured.

## Product principles

- Put the current team and next decision first.
- Preserve precise meanings for predicted points, weighted gain, selling value, and history coverage.
- Keep detailed evidence available without requiring it for routine tasks.
- Preserve drafts and the last useful result when a calculation or connection fails.

## Accessibility and inclusion

Desktop and mobile must support the same core tasks. Labels must be understandable without relying on colour, hover, or football knowledge beyond the task itself.
Keyboard access, visible focus, zoom, reduced motion, readable contrast, and touch targets are requirements of the implementation.
