# Prediction model v3 — 18 September 2026

The predictor uses observed workload from other competitions, richer PL form and set-piece features, completed current-season training examples, and date-aware availability. Version `v3-snapshot-availability` fixes historical metadata contamination, availability/selection inconsistencies, and missing-workload handling. It retains the equal-weight core/expanded gradient-boosting blend. No dependencies were added.

**Accuracy remains mixed.** On sanitized inputs, the blend improves development MAE/RMSE over the deadline core. In the later period it slightly improves MAE and top-20 selection but slightly worsens RMSE. It does not beat the legacy-context comparison on later overall error. The legacy comparison uses fixture-time Elo, which can include information after the deadline. These results do not establish a universal performance improvement.

## What changed

- The 2025/26 GW1 prices, status, news, availability and set-piece fields exactly matched GW15 for all 759 stat rows. The shared feature builder now masks that snapshot's metadata, including `ep_next`, before shifting it into GW2. Match outcomes remain usable, and original source files are retained. This is an explicit quarantine of an audited defect, not a claim that every source snapshot has been independently verified. Remove the quarantine only after trustworthy GW1 metadata is restored and audited.
- Availability is calculated for every fixture and averaged across a gameweek. A suspension covering only the first match of a double gameweek no longer zeroes the whole week. Expired suspensions remain eligible even when the source status has not refreshed; stale injury dates remain conservative. Equal fixture weights approximate availability for the existing gameweek-total model.
- Squad and transfer selection use availability across the forecast horizon, so a currently injured or suspended player can be selected if expected to return. Permanent departures, unavailable registrations and user exclusions remain ineligible.
- Live runs reject past-deadline targets, including completed gameweeks in the latest season, because the current catalog cannot support a historical replay.
- Training and live form now share one shifted feature builder. Histories cross seasons by `player_code`; reused season-local IDs cannot mix different players. Summer price, health and set-piece snapshots reset. Completed and officially checked current-season gameweeks enter fitting; partial completed clubs may inform form but not final training labels.
- Added 10-gameweek per-90 xG, xA, saves and defensive-contribution rates, requiring 180 observed minutes; recent appearance/60-minute frequencies; minutes when playing; and known penalty/free-kick/corner responsibilities. These are predictive features, not calibrated start probabilities.
- Canonical all-competition/non-PL minutes over 7/14 days, preseason workload and time since the last recorded appearance remain available. Missing workload is now blank in exported features, with separate record-count features. The model encodes unknown workload as -1, distinct from recorded zero minutes; this also supports historical folds with no friendly records at all. Future/unfinished matches and conflicting optional cup records are excluded.
- Elo is taken from before the information cutoff. It incorporates newer available ratings in the current season rather than always using last season's final values, but remains a lagged rating rather than a newly calculated live rating.
- Known suspension expiry restores future eligibility. Injury returns use an empirical historical appearance rate only when sufficient earlier examples exist; the next round's explicit chance stays authoritative. Unknown/stale dates and permanent departures remain conservative. Future eligibility is not a promise to start.
- Historical zero rows for players absent from that week's roster are excluded from training. Unmapped rows with minutes or points still fail validation.
- Reports distinguish history coverage from prediction certainty. CSVs record per-week availability, observed workload, model version, source hash and creation time. Live scores retain the version of the archived forecast rather than attributing older predictions to the new model.

## Reproducible retrospective comparison

Development uses expanding folds for GWs 16–30 of 2025/26; the later comparison uses GWs 31–38. Every model is fitted only on earlier gameweeks. Current-season labels never enter these historical folds. `legacy_context` uses the original feature set, fixture-time Elo, hyperparameters and row order on the sanitized inputs; it is no longer an exact replay of v1. `deadline_core` uses restricted Elo and stable-identity ordering; `refined` is the blend. Historical fitting and scoring now use the same per-fixture availability calculation as live forecasts.

| Period | Model | MAE ↓ | RMSE ↓ | Top-20 actual points ↑ | Top-ranked captain actual points ↑ |
|---|---|---:|---:|---:|---:|
| Development | Legacy context | 0.9197 | 1.8733 | 4.3467 | 5.4667 |
| Development | Deadline core | 0.9144 | 1.8663 | 4.5833 | 6.1333 |
| Development | Refined blend | 0.9112 | 1.8631 | 4.5467 | 6.8000 |
| Later comparison | Legacy context | 0.8462 | 1.8284 | 4.9313 | 6.5000 |
| Later comparison | Deadline core | 0.8536 | 1.8465 | 4.7625 | 3.7500 |
| Later comparison | Refined blend | 0.8521 | 1.8483 | 4.7813 | 6.6250 |

Top-player metrics average each gameweek equally; errors weight player-gameweek rows equally. Captain figures are the actual points of the top predicted selectable player, before doubling, not the score of a legal squad's captain. The later comparison has only eight gameweeks. It was inspected during refinement and should be treated as a retrospective diagnostic, not an untouched final test. No statistical significance or guaranteed future gain is claimed.

`scripts/evaluate_predictions.py` reports appeared-only, position, double-gameweek and low-history metrics, with per-week results and source/version metadata. It also freezes origin player features and workload while evolving fixture context and dated availability across horizons one to five. Future outcomes only enter scoring; they cannot update origin features or the recovery prior. `by_horizon.csv` and `horizon_by_gameweek.csv` contain those results:

```bash
OMP_NUM_THREADS=1 .venv/bin/python scripts/evaluate_predictions.py --split development --output-dir predictions/evaluation/development
OMP_NUM_THREADS=1 .venv/bin/python scripts/evaluate_predictions.py --split holdout --output-dir predictions/evaluation/holdout
```

Committed outputs are under `predictions/evaluation/`. The name `holdout` denotes the later time block; it does not imply that this block has never been inspected.

The availability-scaling ablation retains hard zero-availability and blank-gameweek rules but removes the fractional multiplier after regression. It worsened one-week development MAE from 0.9112 to 0.9167 and RMSE from 1.8631 to 1.8641; later MAE also worsened, from 0.8521 to 0.8578. At longer horizons it improved RMSE but worsened MAE. Production therefore retains the multiplier; this is an empirical decision, not a claim that its probability interpretation is calibrated.

Development MAE increases from 0.9112 at horizon one to 1.0791 at horizon five. Later-period values are 0.8521 and 1.0406, respectively, with fewer origins near season end. Overlapping horizons are not independent samples. Final exported fixture schedules are used because historical schedule snapshots are unavailable, and only observed target labels are scored.

## Experiments not retained

Earlier development checks did not support adding every available feature. Competition-specific xGI rates and rolling team xG context did not improve the selected workload/form combination. A separate appearance classifier plus conditional-points model and fixed 100/200-iteration models also failed to improve development error. These experimental implementations were not added to production.

Per-fixture targets and individual-fixture summation reduced double-gameweek error in an exploratory comparison, but weakened top-player selection and introduced additional target-allocation assumptions. The production model retains gameweek targets and aggregated fixture context; double-gameweek calibration remains a limitation.

## Evidence still needed

Historical match exports have no publication timestamps, so backtests assume finished match detail was available three hours after kickoff and cannot reproduce later source corrections. Historical cup/European detail ends during February 2026. Friendlies inform observed workload, not a claim that a friendly goal equals a league goal.

The retrospective comparison now exercises five-week availability, but does not independently establish the benefit of current-season refitting, summer cold starts, or prediction intervals. Future form/workload and prices stay fixed at the forecast origin. These evaluations measure player predictions, not historical squad/transfer optimization. Bench autosubstitution and transfer-option value remain outside the optimiser's objective. Completed archived forecasts remain frozen; use future completed live gameweeks to evaluate this version prospectively.

Validation includes 44 passing tests, an end-to-end forecast run, and regression checks for snapshot quarantine, cross-season identity collisions, shifted features, future match/Elo exclusion, frozen-origin horizon evaluation, returning-player selection, missing workload, past-deadline rejection and injury/suspension boundaries.
