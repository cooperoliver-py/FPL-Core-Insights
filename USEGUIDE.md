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
