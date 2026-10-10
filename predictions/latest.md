# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-10 14:38 UTC

Data commit: `f0556f6857eb6ba9d26f151b737a1db4362dc085`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW6: 1/10 fixtures finished. Completed clubs contribute current-season form; AVL, BHA, BOU, BRE, CHE, COV, CRY, EVE, FUL, HUL, IPS, LIV, MCI, MUN, NEW, NFO, SUN, TOT are deferred.

Incomplete Gameweeks are not scored in live performance reporting until the official data is finished and checked.

The model learns from 2025/26 and completed, checked current-season Gameweeks. An equal-weight blend balances the original features with recent participation, longer-window per-90 rates, set-piece roles and observed workload across league, cup, European and friendly matches. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; prices remain fixed. Dated suspensions expire and later injury-return forecasts use a conservative historical recovery rate.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.852 | 1.847 | 0.753 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.020 and Spearman is 0.370.

The predicted top 20 averaged 4.87 actual points versus 1.69 for the selectable pool.

## Live-season performance

| GW | MAE | RMSE | Spearman | Top 20 | Pool | XI + captain | FPL avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.528 | 2.580 | 0.553 | 3.40 | 1.88 | 39 | 50 |
| 2 | 1.211 | 2.131 | 0.697 | 6.60 | 1.74 | 112 | 81 |
| 3 | 1.211 | 2.030 | 0.750 | 4.25 | 1.83 | 44 | 51 |
| 4 | 1.278 | 2.257 | 0.711 | 5.40 | 1.91 | 72 | 69 |
| 5 | 1.240 | 2.245 | 0.746 | 5.15 | 2.02 | 47 | 48 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW7 player forecasts

| Player | Club | Pos | GW7 | GW8 | GW9 | GW10 | GW11 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | 7.51 | 5.16 | 5.93 | 5.71 | 6.18 | 24.60 | 1.58 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +163 |
| Cherki | MCI | Midfielder | 5.49 | 4.09 | 4.23 | 4.11 | 4.23 | 17.97 | 2.30 | high | 5-GW avg pts 6.80; mins 60; xGI 0.45; current GWs 5; fixture Elo diff +163 |
| Silva | BOU | Defender | 5.39 | 3.99 | 4.95 | 5.05 | 4.56 | 19.22 | 3.84 | high | 5-GW avg pts 2.60; mins 90; xGI 0.23; current GWs 5; fixture Elo diff +90 |
| B.Fernandes | MUN | Midfielder | 5.26 | 5.25 | 5.04 | 5.07 | 4.88 | 20.49 | 1.72 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +49 |
| Anderson | MCI | Midfielder | 4.73 | 3.58 | 3.88 | 4.11 | 4.14 | 16.41 | 2.60 | high | 5-GW avg pts 3.00; mins 83; xGI 0.16; current GWs 5; fixture Elo diff +163 |
| Thiago | BRE | Forward | 4.56 | 5.29 | 5.00 | 4.53 | 4.89 | 19.43 | 2.49 | high | 5-GW avg pts 2.00; mins 88; xGI 0.66; current GWs 5; fixture Elo diff +54 |
| Iwobi | FUL | Midfielder | 4.50 | 4.00 | 2.83 | 3.06 | 2.98 | 14.30 | 2.65 | high | 5-GW avg pts 2.80; mins 82; xGI 0.32; current GWs 5; fixture Elo diff +28 |
| Guéhi | MCI | Defender | 4.45 | 3.31 | 3.73 | 3.89 | 4.04 | 15.56 | 2.59 | high | 5-GW avg pts 6.00; mins 90; xGI 0.27; current GWs 5; fixture Elo diff +163 |
| Gibbs-White | NFO | Midfielder | 4.40 | 6.16 | 4.81 | 4.53 | 4.72 | 19.79 | 2.47 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -55 |
| Van Hecke | TOT | Defender | 4.39 | 3.40 | 3.82 | 3.88 | 4.39 | 15.86 | 3.24 | high | 5-GW avg pts 4.80; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +31 |
| Semenyo | MCI | Midfielder | 4.38 | 2.34 | 2.78 | 2.44 | 2.87 | 12.14 | 1.45 | high | 5-GW avg pts 6.60; mins 90; xGI 0.30; current GWs 5; fixture Elo diff +163 |
| Rúben | MCI | Defender | 4.36 | 3.09 | 3.54 | 3.96 | 3.98 | 15.14 | 2.75 | high | 5-GW avg pts 3.40; mins 90; xGI 0.21; current GWs 5; fixture Elo diff +163 |
| Groß | BHA | Midfielder | 4.30 | 3.52 | 3.38 | 4.22 | 5.43 | 16.37 | 2.78 | high | 5-GW avg pts 9.40; mins 90; xGI 0.53; current GWs 5; fixture Elo diff +31 |
| Mbeumo | MUN | Midfielder | 4.23 | 4.53 | 4.24 | 4.44 | 4.26 | 17.36 | 2.20 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +49 |
| Gonzalo | FUL | Forward | 4.22 | 4.04 | 2.80 | 3.40 | 2.70 | 14.10 | 2.31 | high | 5-GW avg pts 2.80; mins 85; xGI 0.58; current GWs 5; fixture Elo diff +28 |
| Truffert | BOU | Defender | 4.21 | 3.53 | 3.95 | 4.20 | 3.88 | 15.82 | 2.93 | high | 5-GW avg pts 2.00; mins 90; xGI 0.08; current GWs 5; fixture Elo diff +90 |
| King | FUL | Midfielder | 4.20 | 3.74 | 2.62 | 3.09 | 2.45 | 13.29 | 2.37 | high | 5-GW avg pts 4.80; mins 85; xGI 0.40; current GWs 5; fixture Elo diff +28 |
| Palmer | CHE | Midfielder | 4.19 | 4.40 | 4.11 | 4.25 | 4.40 | 17.06 | 1.76 | high | 5-GW avg pts 5.60; mins 88; xGI 0.42; current GWs 5; fixture Elo diff +25 |
| Hill | BOU | Defender | 4.16 | 3.55 | 3.83 | 4.20 | 3.94 | 15.73 | 2.86 | high | 5-GW avg pts 2.40; mins 90; xGI 0.16; current GWs 5; fixture Elo diff +90 |
| Rogers | CHE | Midfielder | 4.09 | 4.20 | 3.97 | 4.09 | 4.20 | 16.43 | 2.11 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +25 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.6m**. Current squad selling value: **£98.7m**. Total available funds: **£99.3m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 19.22 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Van Hecke | TOT | Defender | £4.9m | 15.86 | GW7, GW9, GW10, GW11 | — | — |
| Truffert | BOU | Defender | £5.4m | 15.82 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mukiele | SUN | Defender | £5.4m | 14.54 | GW8, GW9, GW10 | — | — |
| Davis | IPS | Defender | £4.0m | 12.93 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 24.60 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW10, GW11 | — |
| Thiago | BRE | Forward | £7.8m | 19.43 | GW7, GW8, GW9, GW10, GW11 | — | GW8, GW9 |
| Gonzalo | FUL | Forward | £6.1m | 14.10 | GW7, GW8 | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 13.83 | GW7, GW9, GW10, GW11 | — | GW10 |
| Kelleher | BRE | Goalkeeper | £5.0m | 12.94 | GW8 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 19.79 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Cherki | MCI | Midfielder | £7.8m | 17.97 | GW7, GW8, GW9, GW10, GW11 | — | GW7 |
| Mbeumo | MUN | Midfielder | £7.9m | 17.36 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Groß | BHA | Midfielder | £5.9m | 16.37 | GW7, GW10, GW11 | — | GW11 |
| Janelt | BRE | Midfielder | £5.0m | 15.15 | GW8, GW11 | — | — |

Squad cost: £99.3m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Branthwaite | EVE | Defender | £5.5m | 14.99 | GW7, GW9, GW10, GW11 | — | GW10 |
| Egan | HUL | Defender | £4.1m | 12.55 | GW7, GW8, GW9, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 12.42 | GW7, GW8, GW10 | — | — |
| Gabriel | ARS | Defender | £8.0m | 12.09 | GW8, GW9, GW10, GW11 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.62 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.43 | GW7, GW8, GW9, GW10, GW11 | GW11 | GW8, GW9 |
| Havertz | ARS | Forward | £7.6m | 13.66 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.87 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.11 | GW9, GW10, GW11 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 20.49 | GW7, GW8, GW9, GW10, GW11 | GW9, GW10 | GW7, GW11 |
| Gibbs-White | NFO | Midfielder | £8.0m | 19.79 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Cherki | MCI | Midfielder | £7.8m | 17.97 | GW7, GW8, GW9, GW10, GW11 | GW7 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 17.36 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Rogers | CHE | Midfielder | £7.8m | 16.43 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £98.8m.

## One-transfer recommendation

**Gabriel → Silva** (projected weighted XI+captain gain 7.00).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Gabriel | Silva | £8.0m | £5.0m | £3.6m | 7.00 |
| Bassey | Silva | £4.5m | £5.0m | £0.1m | 6.24 |
| Branthwaite | Silva | £5.5m | £5.0m | £1.1m | 4.00 |
| Gabriel | Van Hecke | £8.0m | £4.9m | £3.7m | 3.64 |
| Gabriel | Truffert | £8.0m | £5.4m | £3.2m | 3.60 |
| Gabriel | Hill | £8.0m | £5.5m | £3.1m | 3.51 |
| Gabriel | Guéhi | £8.0m | £6.0m | £2.6m | 3.34 |
| Gabriel | Rúben | £8.0m | £5.5m | £3.1m | 2.92 |
| Bassey | Van Hecke | £4.5m | £4.9m | £0.2m | 2.88 |
| Gabriel | Richards | £8.0m | £4.9m | £3.7m | 2.45 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
