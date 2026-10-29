# FPML implementation plan

Finalised 28 October 2026 using Frontend Design, Web Design Guidelines, Vercel React Best Practices, Emil Kowalski's web design skills, and Impeccable.
This document replaces the earlier chat plan. [PRODUCT.md](PRODUCT.md) records confirmed product requirements and open decisions.
The local implementation now follows this plan. See [verification and remaining external checks](docs/FPML_VERIFICATION.md).

Build a private, single-owner app called FPML for desktop and mobile. Keep the current team and next decision first, with a premium dark interface, white emphasis, and selective green highlights.
Use FigCraft for screen modelling before frontend implementation. Use React, TypeScript, Vite, and FastAPI as the implementation defaults.
Use Render Free and Supabase Free as the initial hosting recommendation. The owner has discussed free hosting but has not selected or provisioned a provider.
Provider setup, secrets, and the owner login are deployment inputs. No paid service or custom domain is purchased under this plan.

## 1. Structure and report coverage

Open directly to **Team**. Use **Team**, **Players**, and **Model** as ordinary routes with labelled navigation.
Use `/team`, `/players`, and `/model`, with `/` opening Team.
Keep the selected Gameweek, player, filters, and sorting in the URL. Preserve each route's scroll position when returning from details.
The Team Gameweek control changes the displayed lineup and points. Transfer advice always covers the full available forecast horizon and says so.
Keep the forecast timestamp accessible from every route, with freshness warnings visible when relevant. Display deadlines and timestamps in the viewer's local timezone, including its timezone label.

| Destination | Default view | Detail available on demand |
| --- | --- | --- |
| Team | Current XI, captain, vice-captain, bench, bank, selling value, and suggested transfer or Hold | Purchase and sale values, available funds, top ten legal transfers, affordable optimal squad, and weekly lineup comparisons |
| Players | Searchable forecasts sorted by selected-GW points, with a Recent form view | Up to five forecasts, weighted score, value, availability, recent recorded points, totals, averages, recorded-GW counts, history coverage, and descriptive inputs |
| Model | Completed-GW model XI + captain results versus the FPL average | Full live metrics, historical walk-forward evaluation, baseline comparisons, appearances-only results, sample sizes, freshness, deferred clubs, model provenance, assumptions, and limits |

The Players filters cover position, club, maximum price, and owned players. Forecasts omit personally excluded players by default, with an explicit inclusion control.
Recent form preserves the report's inclusion of injured and excluded players. Paginate the player list, with 25 players per page.
Keep original Markdown and CSV downloads in a small menu. Generate private exports from private analysis rather than linking a public squad report.

Label transfer improvement **Weighted 5-GW XI + captain gain**, adapting the horizon near season end.
Label the model's existing confidence measure **History coverage**. It is not calibrated prediction certainty.
Raw drivers are descriptive inputs, not causal explanations. Explain weighted score and value beside their labels when requested.
Show missing results as an em dash and recorded zero results as 0. Never truncate comparable numbers or monetary values.

The optimal squad is a comparison, not the next transfer. Show that it may require multiple transfers.
The Model chart uses frozen forecasts and clearly identifies scoring before autosubs and possible differences in model versions.
Keep all underlying report metrics accessible in tables. Do not replace evaluation detail with a single accuracy percentage.

Use this report-to-screen mapping as the completeness checklist:

| Existing report section | FPML location |
| --- | --- |
| Data freshness | Shared status and Model detail |
| Historical walk-forward evaluation | Model, historical results and baseline comparison |
| Live-season performance | Model, chart and full metric table |
| Top 20 over the last five Gameweeks | Players, Recent form |
| Upcoming player forecasts | Players, Forecasts and player details |
| Your budget | Team, budget summary and price details |
| ML-optimal squad within your budget | Team, optimal comparison |
| Your current squad | Team, current lineup and full 15-player squad |
| One-transfer recommendation | Team, next move and top ten alternatives |
| Limits | Model, assumptions and limits |

## 2. Team review, editing, and recovery

On desktop, show a position-grouped squad table beside the next move. Open player details in that second column while retaining the team.
Show transfer alternatives and optimal comparisons inline through expandable sections. Use overlays only when the available space requires them.
On mobile, place a compact team summary and the next move before the full squad. Use one full-height detail or edit sheet at a time.

The edit flow is explicit:

1. **Edit team** creates a draft from the saved squad. Let the owner change players, purchase prices, bank, and exclusions.
2. **Preview transfer** fills the incoming player, current purchase price, and calculated bank after. Retained players keep their purchase prices.
3. **Calculate preview** validates all 15 players and calculates squad advice without training the model or saving the current team.
4. Show changed players, bank, and projected differences together. Keep the saved team available for comparison.
5. **Save as current team** records the successfully analysed draft. State beside this action that it records the owner's actual FPL team.

After further edits, mark the previous result **Needs recalculation** and prevent saving it as a current analysis.
Keep a visible draft indicator. Show Calculate before analysis succeeds and Save after it succeeds, avoiding two competing primary actions.
**Discard preview** restores the saved team. Confirm discard when changes would be lost.
Keep drafts through route changes and recover them from session storage after a reload. Do not place squad data in URL parameters.

Field errors identify the exact issue and focus the first error on submission. Incomplete drafts remain editable, but analysis and saving require a legal squad.
Prevent duplicate submissions. A failed save retains the draft and identifies whether retry or recalculation is needed.
Use revision checks so a stale mobile session cannot overwrite a newer desktop save. Preserve the conflicting draft for review.
A new forecast or price snapshot requires recalculation before saving. Keep the prior preview labelled with its original snapshot until then.

Use static skeletons for the first load. During recalculation, retain existing results with a visible Calculating state rather than blanking the screen.
Show success next to the affected control. Reserve toasts for optional notices, never the only evidence that a team saved.
Show stale data, unavailable forecasts, no search matches, no positive transfer, and no completed results as distinct states with an appropriate next action.

## 3. FigCraft, visual and interaction rules

Use the installed FigCraft app as the editable visual reference. Its installed version was verified as 0.11.2; automation and file reliability remain untested.
Begin with a small file: a player row, a button, and desktop/mobile Team frames. Verify save, reopen, component overrides, font rendering, and PNG export before expanding the file.
Try its command or control interface for repeatable creation and export. If automation is unreliable, use the native app controls. Neither route changes the product scope.

Create the planned source file `design/FPML.figcraft` with components, desktop screens, mobile screens, and interaction states on separate pages.
Define colour, spacing, typography, and component states once. Use auto layout and reusable components for player rows, navigation, forecast strips, fields, and actions.
Model two Team compositions within the agreed dark style. Compare a squad-first composition with a decision-first composition using the same real data.
Use the squad-first two-column arrangement on desktop and decision-first single-column arrangement on mobile as the default, unless the comparison exposes a task or readability failure.

Connect the primary prototype flow: Team, player details, transfer preview, calculation result, and Save as current team.
Include loading, Hold, invalid squad, stale analysis, save error, and successful save states. Mark forecasts and simulated prototype behaviour clearly.
Extend the selected component system to Players and Model. Export reference images at 390px mobile and 1440px desktop widths, with 320px and 768px layout checks.
Save local source and exported images in the repository. Online sharing is unnecessary for this personal project.
Use FigCraft output to review layout, hierarchy, and flow. Implement semantic responsive React components rather than treating generated export code as finished application code.
Maintain the source design and implementation tokens together. Verify actual motion, forms, charts, and accessibility in the browser.

FPML is an operational app. Use familiar tables, tabs, buttons, inputs, and disclosures.
Its identity comes from consistent numeric alignment and a compact five-Gameweek forecast strip repeated in player details and comparisons.
The strip always has labels and values. Its cells communicate actual forecasts rather than decorative activity.

| Token | Proposed value |
| --- | --- |
| Background | `#101417` |
| Editors and secondary panels | `#181E22` |
| Dividers | `#2D363D` |
| Primary text | `#F4F7F5` |
| Secondary text | `#A6B2B9` |
| Positive projected gain | `#77C99B` |
| Typeface | Self-hosted IBM Plex Sans, one family, with tabular numerals |

Use white for primary actions and selection. Reserve green for positive gains and success, so an enabled Save button cannot imply a good prediction.
Warnings and errors use text and distinct semantic colours, with verified contrast.
Use a fixed rem type scale, approximately 14px secondary text, 16px controls and body, 20px section headings, and 28px page headings at default root size.
Use spacing and restrained dividers for hierarchy. Avoid a wall of identical cards, decorative glows, gradients, football imagery, and animated counters.

Keep page navigation, sorting, filtering, and Gameweek changes immediate. Never stagger the entry of player rows or animate chart lines on every visit.
Animate occasional sheets through transform and opacity for 200ms on entry and 150ms on exit, using an ease-out curve.
Pointer press feedback may take 100ms and shrink a primary button to 0.98 scale. Keyboard activation stays immediate.
Use interruptible CSS transitions. Reduced motion removes movement while preserving clear state changes. No animation library is needed for these effects.

Use sentence-case labels and one term per action. Keep explanations next to the relevant metric in a keyboard- and tap-accessible disclosure.
Do not rely on hover tooltips to convey essential information.

## 4. Responsive behaviour and implementation

Use a single column below 768px and labelled bottom navigation. Use two Team columns from 1024px and horizontal navigation on wider screens.
At intermediate widths, stack the work areas rather than shrinking tables and type. Keep core tasks usable at 320px and 200% zoom.
Full statistical tables may scroll inside labelled containers. Player names can wrap; full names remain available in details. Prices and scores stay visible.
Target WCAG 2.2 AA and 44px touch targets. Provide a skip link, semantic table headers, visible focus, labelled controls, and announced calculation and validation results.

Mobile requirements include dynamic viewport height, safe-area padding, 16px inputs, decimal keyboards for prices, visible press feedback, and capability-gated hover.
The software keyboard must leave the edited field and relevant action reachable. Avoid autofocus that unexpectedly opens it.
Browser Back closes the current detail state before leaving its parent route. Sheets restore focus and scroll to their opener when closed.
Contain scrolling within sheets without suppressing normal page scrolling or pinch zoom. Do not add swipe-only gestures.

Use React, TypeScript, Vite, and CSS variables. Use native controls where adequate and accessible component behaviour for dialogs and popovers.
Apply the installed React guidance: parallel independent requests, local filtering, no redundant derived state, and lazy loading of Model charts.
Retain the existing Python engine behind FastAPI. Separate exclusion-free scheduled forecasts from private squad analysis.
Export versioned JSON from existing in-memory report data, including recent history, evaluation, and freshness. Do not parse Markdown.
Reuse Python validation, selling prices, budget calculations, optimization, and transfer ranking. Preserve CLI behaviour and existing report outputs.
Apply personal exclusions to a request-local analysis copy using the existing engine's behaviour. Never overwrite the shared baseline or lose an owned player's purchase and sale information.

Keep the HTTP interface small:

| Endpoint | Contract |
| --- | --- |
| `GET /api/workspace` | Read the latest complete forecast, saved team revision, and available analysis for the authenticated owner |
| `POST /api/previews` | Submit the complete draft, forecast ID, and saved-team revision; return a preview ID and calculation status |
| `GET /api/previews/{id}` | Read the owner's queued, running, completed, interrupted, or failed calculation |
| `PUT /api/team` | Save an exact completed preview against its expected team revision; reject stale team or forecast state with a conflict |

The saved team retains the existing input shape: `players` with stable `player_code` and `purchase_price`, `bank`, and `excluded_player_codes`.
Add revision and snapshot metadata around that shape. Continue JSON import and export for backup and initial setup.
Validate API input on the server and expose schemas through FastAPI. Parse external data once before using typed frontend state.
Use one bounded analysis worker. A result belongs to its exact draft and forecast snapshot; late results must never replace a newer preview.
Private exports, drafts, squad data, and personal exclusions stay outside shared snapshots and public artifacts.

For the recommended free setup, use a Render static site for React, a Render Free Python API, and Supabase Free for durable private state and owner authentication.
Serving the static UI separately lets FPML show that the API is waking instead of waiting on the host's loading page.
Show Connecting to analysis while awaiting the API. Do not report a cold start as a fact when the cause is unknown, and do not invent percentage progress.
Persist saved squads and preview-job status externally. A sleeping or restarted API must recover pending work or mark it interrupted so it can be retried.
Restrict access to the owner's identity, validate authentication on the API, and enforce database access policies. Keep service credentials on the server.
Disable public signup. Reject unauthenticated and non-owner access to saved squads, preview results, and private downloads. Restrict cross-origin requests to the frontend origin.
Keep model training on the existing three-daily GitHub Actions schedule. Publish only complete, exclusion-free shared snapshots, and retain the last valid snapshot when refresh fails.
Use the providers' supplied addresses initially. The target recurring hosting cost is zero within free allowances; inactivity pauses and quotas are accepted limitations of this recommendation.
If measured optimizer memory or latency makes the free API impractical, report the result before selecting a paid upgrade. Paid hosting remains an explicit owner decision.

## 5. Delivery and acceptance

Implement in these units, each ending in a reviewable result:

1. Extract reusable squad analysis and export structured report data. Check parity against the existing Python results before building screens.
2. Complete the FigCraft reliability check, shared components, responsive screen models, and clickable team-edit flow. Review its exported desktop and mobile references before frontend implementation.
3. Build the actual Team review and preview flow with real data. Compare the browser UI with the FigCraft references before extending the pattern to Players and Model.
4. Add owner authentication, durable saves, private exports, and hosted recovery. Import the existing squad once without synchronising future edits back to Git.
5. Run visual, accessibility, state, and data-parity checks. Review the resulting UI with Impeccable, Frontend Design, Web Design Guidelines, and the relevant Emil skills. Record implemented tokens and components in `DESIGN.md` with Impeccable's token record.

Acceptance requires:

- Every substantive `latest.md` section has a destination in FPML, including report limits and provenance.
- Squad selection, prices, affordability, XI, captains, transfer ranking, and Hold match the Python engine.
- Previewing leaves saved state unchanged. Saving requires the exact valid draft and protects against conflicting device saves.
- Loading, errors, session expiry, interrupted calculations, offline connections, and stale forecasts preserve useful context and drafts.
- No forecast exists beyond its actual available horizon. End-of-season and missing-result states remain usable.
- Keyboard access, focus restoration, screen-reader announcements, contrast, reduced motion, and 200% zoom work across core tasks.
- Realistic difficult data works at 320px, typical mobile width, tablet width, and desktop width: long names with diacritics, duplicate display names, zero prices where allowed, missing history, long injury news, empty filters, and a full player catalog.
- Identity uses stable player codes. Equal display names cannot select or replace the wrong player.
- Mobile Safari and Android Chrome tests include the keyboard open, Back navigation, landscape orientation, and device safe areas.
- A deployment or API restart preserves saved squads. Verify database backup and restore rather than relying on the API filesystem.
- The FigCraft file reopens and exports correctly, and the browser matches the reviewed composition at desktop and mobile sizes.
- Unauthenticated and non-owner users cannot access private data. Secrets and private payloads never appear in public exports or application logs.
- Measure preview latency and peak memory on the proposed host using a real legal squad. Report both before calling the deployment suitable for weekly use.

Use a development-only fixture switch for normal, difficult, empty, and large datasets. It never ships as a product feature.
Emulation can verify layout; physical-device checks are still required before claiming touch and keyboard behaviour are verified.

Defer public accounts, FPL account integration, saved future squads, chips, notifications, drag-and-drop, and decorative motion.
The UI and native FigCraft design are implemented and locally verified. Hosted wake-up delays, optimizer resource use and physical-device behaviour remain unmeasured.
The repository already contains squad details in Git history; protecting the hosted app does not remove those historical copies.
