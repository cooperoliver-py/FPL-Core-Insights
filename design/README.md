# FPML editable design

`FPML.figcraft` is a native FigCraft archive, created through the installed FigCraft 0.11.2 engine. The PNGs are native document exports, not browser screenshots or a renamed SVG. Source creation is repeatable with Python's standard library.

## Contents

- Components: native auto-layout components for player rows, primary action, navigation, forecast strip and price field; an action instance with a persisted text override.
- Composition study: squad-first desktop and decision-first mobile, using the same saved team. The chosen combination preserves squad context on desktop and puts the decision before the long list on mobile.
- Desktop and Mobile: Team, Players and Model at 1440px and 390px. Team contains all 15 actual squad players, current XI first. Model uses real completed-Gameweek performance values.
- Layout checks: Team at 320px and 768px.
- Flow and states: player details, transfer preview, calculated preview, saved team, loading, Hold, invalid squad, stale analysis and save error. Native on-click links connect Team → details → preview → calculation result → saved team → Team. These are simulated states, not calls to the optimizer or a save API.
- Six named colour variables preserve the agreed palette. IBM Plex Sans is bundled under its OFL license. No football imagery or motion is required for the information-heavy rows.

## Rebuild

From the repository root, launch the installed app with a dedicated local control port:

```sh
/Applications/FigCraft.app/Contents/MacOS/FigCraft --control 7979
```

In another terminal:

```sh
python3 design/build_fpml_design.py
```

The script writes only this directory, reads `predictions/latest.csv`, `predictions/performance.csv` and `squad.json`, and uses the engine's native node/component/prototype commands. It loads the bundled font into the app session without system installation. This reference is pinned to the GW9–13 dataset used during implementation; update the Gameweek bindings before regenerating from a future forecast horizon.

## Verified

The final run generated a seven-page, 781-layer archive, saved it, reloaded it from disk with `file.revert`, then parsed its bytes as a fresh document with `file.open`. The fresh import reported **no repairs**. Ten native prototype interactions survived the reload. A component instance's `Save as current team` override survived the round trip. `text.missingFonts` reported no missing families after loading the bundled font. See `verification.json` for the engine results.

Native `ui.render` generated the six Team/Players/Model references plus the two composition references and two additional responsive checks. Team desktop and mobile/320px exports were visually inspected for hierarchy, legibility and clipping. All screen references are intentionally full-content frames; bottom navigation appears at their bottom rather than pretending that a static PNG demonstrates sticky viewport behaviour.

## Limits and handoff

The controlled app reports its window as hidden in this execution environment. `open -a FigCraft` and `window.focus` did not change this; `ui.screenshot` returned `window 0 is minimised or hidden`. Document rendering and editing work, but the native presenter's click playback could not be observed. The persisted flow links are structurally verified; interactive playback must be checked once the window is visible.

Model and Players frames establish the shared hierarchy rather than duplicating every expanded report table. The React implementation is the functional accessibility and responsiveness artifact. The design's transfer screens deliberately label simulated calculations and do not invent a live optimizer result. The final implementation can expose actual recommendations from Python. Font loading is session-local: on a different machine open/load `IBMPlexSans.ttf` before reviewing typography.

The design uses the local personal squad. Keep it private if publishing the source repository or design exports is undesirable. No credentials are included.
