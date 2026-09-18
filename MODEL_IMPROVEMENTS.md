# Prediction model refinement — 18 September 2026

The predictor now uses observed workload from other competitions, richer PL form and set-piece features, completed current-season training examples, and date-aware availability. It averages a core gradient-boosting model with the expanded model to reduce reliance on the extra features. No dependencies were added.

**The accuracy result is mixed.** The blend slightly improves overall MAE/RMSE against a core model using the same restricted Elo information, but it does not beat the original v1 on late-season overall error or top-20 selection. The original used fixture-time Elo, which can include information after the gameweek deadline; the revised pipeline only reads ratings attached to earlier completed matches or the prior season. That difference is exposed rather than hidden. There is not yet evidence to call this an unqualified accuracy improvement.

## What changed

- Training and live form now share one shifted feature builder. Histories cross seasons by `player_code`; reused season-local IDs cannot mix different players. Summer price, health and set-piece snapshots reset. Completed and officially checked current-season gameweeks enter fitting; partial completed clubs may inform form but not final training labels.
- Added 10-gameweek per-90 xG, xA, saves and defensive-contribution rates, requiring 180 observed minutes; recent appearance/60-minute frequencies; minutes when playing; and known penalty/free-kick/corner responsibilities. These are predictive features, not calibrated start probabilities.
- Added canonical all-competition/non-PL minutes over 7/14 days, preseason workload and time since the last recorded appearance. Future/unfinished matches are excluded, repeated gameweek projections are not counted twice, and conflicting optional cup records are omitted. A missing match row means unobserved workload, not proven rest.
- Elo is taken from before the information cutoff. It incorporates newer available ratings in the current season rather than always using last season's final values, but remains a lagged rating rather than a newly calculated live rating.
- Known suspension expiry restores future eligibility. Injury returns use an empirical historical appearance rate only when sufficient earlier examples exist; the next round's explicit chance stays authoritative. Unknown/stale dates and permanent departures remain conservative. Future eligibility is not a promise to start.
- Historical zero rows for players absent from that week's roster are excluded from training. Unmapped rows with minutes or points still fail validation.
- Reports distinguish history coverage from prediction certainty. CSVs record per-week availability, observed workload, model version, source hash and creation time. Live scores retain the version of the archived forecast rather than attributing older predictions to the new model.

## Reproducible retrospective comparison

Development uses expanding folds for GWs 16–30 of 2025/26; the later comparison uses GWs 31–38. Every model is fitted only on earlier gameweeks. Current-season labels never enter these historical folds. `legacy_v1` preserves the original feature set, fixture Elo, hyperparameters and row order; `deadline_core` uses the restricted Elo information and current stable-identity ordering without the extra features; `refined` is the equal-weight blend.

| Period | Model | MAE ↓ | RMSE ↓ | Top-20 actual points ↑ | Top-ranked captain actual points ↑ |
|---|---|---:|---:|---:|---:|
| Development | Original v1 | 0.9177 | 1.8713 | 4.3833 | 5.5333 |
| Development | Deadline core | 0.9152 | 1.8686 | 4.5133 | 5.7333 |
| Development | Refined blend | 0.9111 | 1.8626 | 4.3767 | 5.8000 |
| Later comparison | Original v1 | 0.8449 | 1.8287 | 5.1438 | 5.5000 |
| Later comparison | Deadline core | 0.8542 | 1.8475 | 5.0000 | 4.2500 |
| Later comparison | Refined blend | 0.8497 | 1.8465 | 4.8188 | 6.2500 |

Top-player metrics average each gameweek equally; errors weight player-gameweek rows equally. Captain figures are the actual points of the top predicted selectable player, before doubling, not the score of a legal squad's captain. The later comparison has only eight gameweeks. It was inspected during refinement and should be treated as a retrospective diagnostic, not an untouched final test. No statistical significance or guaranteed future gain is claimed.

The new `scripts/evaluate_predictions.py` also reports appeared-only, position, double-gameweek and low-history metrics, with per-week results and source/version metadata:

```bash
OMP_NUM_THREADS=1 .venv/bin/python scripts/evaluate_predictions.py --split development --output-dir predictions/evaluation/development
OMP_NUM_THREADS=1 .venv/bin/python scripts/evaluate_predictions.py --split holdout --output-dir predictions/evaluation/holdout
```

Committed outputs are under `predictions/evaluation/`. The name `holdout` denotes the later time block; it does not imply that this block has never been inspected.

## Experiments not retained

Development checks did not support adding every available feature. Competition-specific xGI rates and rolling team xG context did not improve the selected workload/form combination. A separate appearance classifier plus conditional-points model and fixed 100/200-iteration models also failed to improve development error. These experimental implementations were not added to production.

Per-fixture targets and individual-fixture summation reduced double-gameweek error in an exploratory comparison, but weakened top-player selection and introduced additional target-allocation assumptions. The production model retains gameweek targets and aggregated fixture context; double-gameweek calibration remains a limitation.

## Evidence still needed

Historical match exports have no publication timestamps, so backtests assume finished match detail was available three hours after kickoff and cannot reproduce later source corrections. Historical cup/European detail ends during February 2026. Friendlies inform observed workload, not a claim that a friendly goal equals a league goal.

The retrospective comparison does not independently establish the benefit of current-season refitting, five-week injury recovery, summer cold starts, or prediction intervals. Future form/workload and prices stay fixed at the forecast origin. Bench autosubstitution and transfer-option value remain outside the optimiser's objective. Existing archived forecasts must remain frozen; use the next completed live gameweeks to evaluate this version prospectively, including captain and top-player performance rather than relying only on aggregate error.

Validation includes the full unittest suite, an end-to-end forecast run, and regression checks for cross-season identity collisions, duplicate history, shifted features, future match/Elo exclusion, historical roster membership, and injury/suspension boundaries.
