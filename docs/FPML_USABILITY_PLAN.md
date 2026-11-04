# FPML usability review and improvement plan

Reviewed 4 November 2026 in Safari at https://fpml.onrender.com. This was an approximately ten-minute live walkthrough, beginning at 11:30 UTC. It covered the saved team, recalculation, a hypothetical transfer, player search and recent form, player details, model results, draft recovery, validation, report download, and browser-zoom reflow.

The app's dark visual identity and compact navigation work well. The main friction is knowing which information belongs to the saved team, which belongs to a hypothetical preview, and what needs recalculating. Improve that weekly workflow before adding features or redesigning the app.

No actual team save, FPL transfer, preference save, deployment, or code change was performed. Two temporary preview calculations were requested. The test draft was discarded. The saved-team footer remained dated 3 November, 15:19 GMT, and the original saved players and bank were restored. Server-side preview records may remain. Browser zoom was restored.

## What worked

- Saved players, prices and bank survived a new forecast and a page reload.
- Calculations completed while navigating to other pages, with an explicit completion notice.
- Transfers updated the preview bank and players without changing the saved squad.
- Recent-form filters and page state survived navigation between Team and Players.
- Native validation rejected a negative bank and focused the input. An incomplete squad was blocked before calculation.
- The narrow player-detail sheet focused its close control and dismissed with Escape.
- Discard clearly stated that the saved team would remain unchanged and restored it correctly.
- Model results have a chart, exact tables, methodology and useful metric explanations.

## Priority findings

| ID | Priority | Observed pain point | Improvement |
| --- | --- | --- | --- |
| U1 | High | The first workspace load failed with “Load failed” and “Workspace unavailable.” Retrying recovered it. A later generic load error also appeared while the saved view remained usable. | Add bounded automatic retry, clear connection states and a useful recovery action. Keep available information visible. |
| U2 | High | A new forecast requires opening the full 15-player editor and pressing Calculate preview. Recalculating an unchanged squad then offers Save as current team with “Save only after updating your actual FPL team.” Merely opening and closing the editor creates an Unsaved preview state. | Separate recalculating forecasts from editing/saving the actual squad. |
| U3 | High | A hypothetical incoming player appeared in Owned only and was labelled Owned in player details before saving. Team still showed the outgoing player in the saved squad. | Use explicit saved-team and preview terminology across pages and show a compact change summary. |
| U4 | High, confirm input cause first | During a pending calculation, native rapid typing of Erling produced Elg, and Salah produced aah. Pasting worked. A later Rogers typing check without a pending calculation succeeded. | Reproduce with normal human typing and an input regression test. Keep immediate input state stable while synchronising URL filters. |
| U5 | Medium | Reload recovered the draft but lost its completed analysis, requiring another calculation. Starting a second calculation also replaced the useful previous result with the saved-squad fallback. | Resume valid preview jobs/results after reload and retain the last calculated result with a clear pending/stale label. |
| U6 | Medium | Full report download failed with “Download failed. Check the connection and try again.” The UI did not reveal whether the problem was connectivity or outdated analysis. | Preserve useful server error details and distinguish saved-squad downloads from analysis/preview exports. |
| U7 | Medium | Forecast strips show Gameweek numbers and points without opponent or home/away information. Transfer alternatives are difficult to compare beyond price and weighted gain. | Add compact fixture context and before/after transfer comparison. |
| U8 | Medium | In the narrow, short viewport reached through zoom, the persistent preview bar plus bottom navigation occupied substantial space on Players and Model. Active filters were hidden behind “Filter players” with no count. | Compact the global preview indicator away from Team and make active filters visible. |

“High” means likely to interrupt the main weekly workflow or mislead a decision. “Medium” means extra work, unclear recovery or missing decision context. No loss of saved squad data was observed.

## Phase 1: make state and recovery trustworthy

### U1. Explain loading and recover without repeated clicks

The live failure is confirmed. A sleeping host is a plausible cause, but this session did not establish the server-side cause.

- Distinguish connecting, retrying, offline/network failure, expired login, and unavailable analysis service.
- Retry temporary read failures with a bounded delay and a visible stop/retry option. Do not invent a percentage or claim that the host is waking unless that is known.
- Clear obsolete errors when a retry begins. Avoid showing a success banner and instructions to calculate alongside a calculation already in progress.
- Preserve loaded team/player information during a failed refresh. Keep last-updated and stale status visible.

Acceptance: a delayed or temporarily failing workspace request recovers without losing the saved view or draft. Permanent failure gives one useful explanation and action. Expired authentication asks for sign-in rather than a generic connection retry.

### U2–U3. Separate the actual squad, a preview, and its forecast analysis

Treat the saved squad and its calculated analysis as separate data. Preserve the existing revision and forecast consistency checks.

- Provide Recalculate team directly on Team without opening the price editor.
- Recalculating unchanged holdings must not imply an actual FPL transfer or require the user to save the same squad again. Cache or associate analysis with its team revision and forecast ID without changing holdings.
- Entering and leaving the editor without edits must not be labelled an unsaved team change.
- Use Owned for the saved squad. Label a hypothetical incoming player In preview and the outgoing player Leaving preview. If filtering the preview, name the filter Preview squad rather than Owned only.
- Show a short change summary before Save as current team. State the player changes, bank change and changed preferences. Keep explicit save for actual squad/preference edits.

Acceptance: previewing an A-to-B transfer leaves A owned and labels B as hypothetical until save. Discard restores every label/filter. Recalculating unchanged holdings leaves the saved revision and saved timestamp unchanged. A new forecast remains usable without importing JSON or opening the squad editor.

### U4. Stabilise player-search input

Observed character loss was intermittent and occurred through native automation. Confirm its cause before choosing an implementation fix. The current source derives search text directly from URL parameters and navigates on each change, which is a candidate mechanism rather than proof.

- Test rapid typing, paste, backspace and selection replacement while calculation polling is updating the page.
- Keep the input immediately responsive. Synchronise shareable URL state without replacing newer keystrokes with an older navigation result.
- Preserve filter/history behaviour when navigating away and returning.

Acceptance: the displayed query exactly matches entered text during pending calculations, normal browsing and browser Back/Forward. Search results and URL eventually agree. Include a behavioural regression test if reproduced.

## Phase 2: reduce repeated work

### U5. Preserve previews and shorten the transfer journey

- Keep the last completed result visible while the next calculation runs, labelled as the previous result.
- Recover a preview ID and completed result after reload when owner, squad revision and forecast still match. Otherwise explain why recalculation is required.
- Change Preview transfer into a focused review of the outgoing/incoming players, prices and bank. Keep the full editor available for adjustments, rather than opening all 15 holdings by default.
- Make desktop player-detail Escape behaviour match the narrow sheet. Restore focus to the opening row.

Acceptance: a valid completed preview can be resumed after refresh without recomputation. A stale or interrupted job has an explicit recovery path. One transfer can be reviewed without scrolling through unrelated purchase-price fields. No stale result becomes eligible for save.

### U6. Make export failures actionable

- Keep Squad JSON clearly identified as the saved squad, independent of a hypothetical preview.
- Identify whether CSV/report refers to the saved team or the displayed preview.
- For outdated analysis, offer recalculation rather than a misleading network error. For authentication/network errors, offer the appropriate recovery.
- Do not require recording a hypothetical transfer as the current team merely to export its analysis.

Acceptance: expired login, network failure and stale analysis produce distinct messages. Download controls accurately identify their data. A preview report, if supported, can be exported without changing the saved squad.

The session confirmed the generic failure message, not its HTTP status. Existing source rejects stale saved analysis for CSV/report exports, so that is an important case to reproduce when implementing.

## Phase 3: make comparisons easier

### U7. Add compact decision context

- Show opponent and home/away alongside each Gameweek forecast, including multiple fixtures or blanks where applicable. Extend the public snapshot with validated fixture data if it is not already available.
- Add club and position to alternative transfer rows, and make their players inspectable.
- Compare outgoing and incoming forecasts together. Keep the existing explanation that weighted XI/captain gain differs from raw player points.
- Put the next deadline near the Gameweek controls. In this session it was discoverable under Model provenance, but absent from the main team decision area.

Acceptance: the owner can explain which fixtures support a transfer without switching to another website. Double/blank Gameweeks remain accurate. Missing fixture data is shown as unknown rather than inferred.

### U8. Keep controls useful on smaller screens

- Use a compact preview indicator on Players and Model, with a route back to review. Keep the full save action on the deliberate team-review step.
- Show active-filter count or concise chips outside the collapsed filter section, plus Clear filters when filters are active.
- Verify player rows and the last results remain reachable above fixed controls. Preserve zoom and visible keyboard focus.

Acceptance: desktop zoom/reflow and real portrait/landscape phone checks allow access to search, results, details and navigation without controls obscuring them. Active filtering is apparent without opening a disclosure.

## Phase 4: targeted polish

- Replace “Too small: expected array to have exactly 15 items” with “Add 1 player to complete your 15-player squad.” Include position-count or budget guidance when relevant.
- Use “1 player” for a single result.
- Make the 55-player exclusion list searchable and identifiable by club/position. Two entries were named Phillips with no distinguishing context. Accessible button names should identify the player, such as Include [name].
- Add a concise Model summary of the displayed live-season results, with the pre-autosub/model-version caveats nearby. Keep the detailed metrics in disclosures. Use consistent plain labels for MAE/mean absolute error and explain whether higher or lower is better.
- For lazy-loaded page navigation, show clear pending feedback rather than leaving Team selected/content visible while the URL already says Model. This occurred briefly and needs a controlled repeat before treating it as a persistent defect.

## Delivery and verification

Implement the phases in order. Keep the existing visual system, small text footprint, owner authentication, explicit actual-team saving and revision protection. No new framework or broad visual redesign is justified by this walkthrough.

For each phase, reproduce the observed trigger first, add the smallest meaningful behavioural check, and use the live workflow again after deployment. Keep the changed squad and discard paths covered. Do not test successful production saves using hypothetical transfers.

Deferred from this review: login/logout and password recovery, JSON file-picker import, successful file export, real save and cross-device persistence, physical-phone touch behaviour, VoiceOver, offline simulation and host performance benchmarking. Zoom checks are not a substitute for a physical phone. This is a usability plan, not a new security or model-accuracy audit.

## Implementation status, 4 November 2026

The local implementation now covers U1 through U8 and the targeted copy, exclusion-list, and Model-summary changes. The existing design system remains in place.

- Workspace reads retry temporary failures twice. Connecting can be stopped. Errors retain authentication, offline, and server detail where available.
- Recalculate team runs directly against saved holdings. Its derived analysis is stored separately by team revision and forecast ID. It does not change the saved squad, revision, or timestamp.
- Owned refers to saved holdings. Hypothetical incoming and outgoing players have separate labels. Team shows a change summary before explicit saving.
- Search has immediate local input state and synchronises URL filters. Completed and pending calculations can resume from session storage when owner, revision, and forecast match. Previous results remain available during another calculation.
- Transfers have a focused price/bank review, with the full editor available for adjustments. Desktop Escape closes details and restores focus.
- Saved squad JSON remains independent of previews. Displayed analysis can be exported without saving a hypothetical team. Outdated analysis retains the server's recalculation guidance.
- New scheduled snapshots include validated opponent/home-away fixtures. Existing snapshots show fixture data as unknown until the next generation. Multiple fixtures and blank Gameweeks have distinct representations.
- Players and Model use a compact preview action. Active filter counts, Clear filters, searchable exclusions, identifiable Include actions, singular result labels, and a derived live-season Model summary are present.

Verification passed with 65 Python tests, 24 frontend tests, TypeScript compilation, and the production frontend build. A running local API check used an isolated temporary database and confirmed completed recalculation, an unchanged saved-team record, and a successful report export. An independent code review checked saved-team protection, preview exports, recovery, and search.

Safari rendering verification was blocked because the Mac was locked. Physical-phone, VoiceOver, and post-deployment checks remain open. The previously observed lazy-route transition was not reproduced in a browser during this implementation, so no additional navigation mechanism was introduced. The existing Suspense loading fallback remains.

These changes have not been committed, pushed, or deployed. Production saved-team data was not modified. Temporary local test servers were stopped after verification.
