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
