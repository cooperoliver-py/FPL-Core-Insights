# FPL Prediction Model — Simple Use Guide

## First-time setup

Run these commands from the repository folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the model locally

```bash
source .venv/bin/activate
python scripts/fpl_predictions.py
```

The model automatically reads the root-level `squad.json`. Open
`predictions/latest.md` when it finishes.

The report starts with data freshness. If an earlier Gameweek is still in
progress, it shows the completed-fixture count and the clubs whose form is
deferred. Finished clubs can contribute recent form, but live performance is
not scored until the Gameweek is officially finished and data-checked.

The final pre-deadline forecast is saved under
`predictions/archive/{season}/GWxx.csv`. Completed archived forecasts are
summarised in `predictions/performance.csv` and in the live-performance section
of `predictions/latest.md`.

Generate the highest-scoring completed weekly squads with:

```bash
python scripts/team_of_the_week.py
```

This writes `TeamOfTheWeek/GWx/team.md` and `team.csv` only after the official
Gameweek is both finished and data-checked.

## Exclude players from recommendations

Add stable `player_code` values to `excluded_player_codes` in `squad.json`:

```json
"excluded_player_codes": [178301, 448047]
```

Excluded players remain visible in the CSV with zero forecasts and can still be
recommended as a transfer-out when already owned. They cannot start, captain,
appear in top picks, enter the ML-optimal squad, or be suggested as a
transfer-in. Their valid historical performances remain part of model training.
This setting never modifies `data/` and survives upstream updates.

## Update data from the original repository

The GitHub Actions workflow does this automatically. To update immediately on
your computer, first check that you have no local edits inside `data/`:

```bash
git status --short -- data
```

If that command prints nothing, check whether the original repository is
already configured as `upstream`:

```bash
git remote -v
```

If `upstream` is missing, add it once:

```bash
git remote add upstream https://github.com/olbauday/FPL-Core-Insights.git
```

Then fetch the original repository, copy only its latest data, and rerun the
model:

```bash
git fetch upstream main
git restore --source=upstream/main --worktree -- data
source .venv/bin/activate
python scripts/fpl_predictions.py
python scripts/team_of_the_week.py
```

This replaces your local `data/` files with the upstream versions without
merging the rest of the original repository. Avoid `git pull upstream main`,
which would merge the entire upstream repository.

To save the refreshed data and report to your fork:

```bash
git add -- data predictions TeamOfTheWeek
git commit -m "Update upstream FPL data and predictions"
git push origin main
```

## Run it through GitHub Actions

1. Open the repository's **Actions** tab.
2. Select **FPL Predictions**.
3. Select **Run workflow**, choose `main`, then select **Run workflow** again.
4. Wait for the green tick.

Get the new report on your computer with:

```bash
git pull --ff-only origin main
```

## After making an FPL transfer

Set `"bank": 0.2` in `squad.json` for £0.2m of cash. Update this to the bank
balance shown in FPL, and keep each player's original `purchase_price` accurate.
Price changes affect selling values; they do not directly add cash to your bank.
Transfer recommendations spend at most your bank plus the outgoing player's
selling value. The full-squad comparison also uses your actual funds, preserving
the value of players you keep, rather than assuming a new £100m budget.

Update the player, purchase price, and bank in `squad.json`, then run:

```bash
git add -- squad.json
git commit -m "Update current FPL squad"
git push origin main
```

The scheduled workflow will use the updated squad automatically.

## Optional: run the tests

```bash
source .venv/bin/activate
python -m unittest discover -s tests
```

## Compare model accuracy

```bash
OMP_NUM_THREADS=1 python scripts/evaluate_predictions.py --split development --output-dir predictions/evaluation/development
OMP_NUM_THREADS=1 python scripts/evaluate_predictions.py --split holdout --output-dir predictions/evaluation/holdout
```

See `metrics.csv`, `by_gameweek.csv` and `metadata.json` in each output folder.
`by_horizon.csv` and `horizon_by_gameweek.csv` evaluate one-to-five-week forecasts
with player information frozen at the origin and the production availability logic.
`refined_no_soft_scaling` tests removing the extra fractional availability multiplier
while preserving hard unavailability and blank-gameweek rules.
The comparisons are retrospective; `predictions/performance.csv` continues to
score the original frozen forecasts and records the model version used.

The report's **history coverage** label is not prediction certainty. In the CSV,
`GWx_availability` shows the chance factor applied to each forecast week. Known
suspensions can expire; a stated injury return remains an uncertain estimate.
In double Gameweeks this factor averages availability across individual fixtures.
Players returning within the horizon can be selected; departures and explicit
exclusions remain ineligible. Missing workload is blank in CSV exports and encoded
as -1 inside the model, alongside observed-record counts, rather than zero minutes.

Live runs reject past-deadline Gameweeks, including those in the current season.
The known copied metadata in 2025/26 GW1 is masked before building historical
features; the underlying match results and original source files are retained.
