# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-17 04:53 UTC

Data commit: `174d22b32badeac7c6d329fdc1d20e0276919b9a`

## Data freshness

All scheduled Premier League fixtures before GW7 are complete.

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
| 6 | 1.120 | 2.092 | 0.724 | 4.70 | 1.85 | 55 | 58 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW7 player forecasts

| Player | Club | Pos | GW7 | GW8 | GW9 | GW10 | GW11 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | 8.46 | 5.99 | 7.39 | 6.95 | 7.71 | 29.25 | 1.86 | high | 5-GW avg pts 8.60; mins 88; xGI 0.92; current GWs 6; fixture Elo diff +163 |
| Semenyo | MCI | Midfielder | 7.60 | 5.77 | 6.06 | 6.28 | 6.21 | 25.76 | 3.10 | high | 5-GW avg pts 6.80; mins 90; xGI 0.35; current GWs 6; fixture Elo diff +163 |
| Cherki | MCI | Midfielder | 7.04 | 4.98 | 5.84 | 5.30 | 5.78 | 23.37 | 2.96 | high | 5-GW avg pts 7.20; mins 73; xGI 0.50; current GWs 6; fixture Elo diff +163 |
| Silva | BOU | Defender | 5.83 | 4.50 | 5.16 | 5.81 | 5.06 | 21.11 | 4.22 | high | 5-GW avg pts 2.20; mins 90; xGI 0.32; current GWs 6; fixture Elo diff +90 |
| Guéhi | MCI | Defender | 5.71 | 4.11 | 4.68 | 4.90 | 4.96 | 19.56 | 3.26 | high | 5-GW avg pts 5.20; mins 90; xGI 0.03; current GWs 6; fixture Elo diff +163 |
| Iwobi | FUL | Midfielder | 5.65 | 5.21 | 3.28 | 3.97 | 3.34 | 17.75 | 3.29 | high | 5-GW avg pts 3.20; mins 81; xGI 0.35; current GWs 6; fixture Elo diff +28 |
| Rúben | MCI | Defender | 5.41 | 3.73 | 4.36 | 4.62 | 4.74 | 18.33 | 3.33 | high | 5-GW avg pts 4.20; mins 90; xGI 0.18; current GWs 6; fixture Elo diff +163 |
| Donnarumma | MCI | Goalkeeper | 5.22 | 3.46 | 4.08 | 4.25 | 4.36 | 17.18 | 3.12 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 6; fixture Elo diff +163 |
| Gabriel | ARS | Defender | 5.12 | 5.00 | 4.60 | 5.62 | 4.78 | 20.11 | 2.55 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +283 |
| B.Fernandes | MUN | Midfielder | 4.92 | 5.15 | 4.79 | 4.99 | 4.81 | 19.76 | 1.67 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +49 |
| Palmer | CHE | Midfielder | 4.86 | 5.12 | 4.56 | 4.87 | 5.25 | 19.67 | 2.03 | high | 5-GW avg pts 4.60; mins 89; xGI 0.34; current GWs 6; fixture Elo diff +25 |
| Hill | BOU | Defender | 4.72 | 3.82 | 4.35 | 5.19 | 4.33 | 17.88 | 3.25 | high | 5-GW avg pts 2.60; mins 90; xGI 0.16; current GWs 6; fixture Elo diff +90 |
| Cunha | MUN | Midfielder | 4.70 | 4.62 | 4.42 | 4.45 | 4.30 | 18.10 | 2.29 | high | 5-GW avg pts 6.80; mins 84; xGI 0.26; current GWs 6; fixture Elo diff +49 |
| Groß | BHA | Midfielder | 4.69 | 3.89 | 3.85 | 4.55 | 5.81 | 17.93 | 2.94 | high | 5-GW avg pts 10.20; mins 90; xGI 0.56; current GWs 6; fixture Elo diff +31 |
| Van Hecke | TOT | Defender | 4.67 | 3.26 | 3.89 | 3.68 | 4.33 | 15.89 | 3.24 | high | 5-GW avg pts 5.20; mins 90; xGI 0.22; current GWs 6; fixture Elo diff +31 |
| Anderson | MCI | Midfielder | 4.62 | 3.69 | 4.13 | 4.29 | 4.41 | 16.90 | 2.68 | high | 5-GW avg pts 3.80; mins 88; xGI 0.14; current GWs 6; fixture Elo diff +163 |
| Rice | ARS | Midfielder | 4.57 | 4.66 | 4.20 | 4.86 | 4.26 | 18.08 | 2.48 | high | 5-GW avg pts 4.80; mins 87; xGI 0.15; current GWs 6; fixture Elo diff +283 |
| Mbeumo | MUN | Midfielder | 4.46 | 4.95 | 4.43 | 4.79 | 4.65 | 18.61 | 2.39 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +49 |
| Thiago | BRE | Forward | 4.44 | 5.17 | 5.23 | 4.77 | 4.97 | 19.60 | 2.51 | high | 5-GW avg pts 2.80; mins 90; xGI 0.48; current GWs 6; fixture Elo diff +54 |
| Matheus N. | MCI | Defender | 4.40 | 3.54 | 4.00 | 4.24 | 4.32 | 16.34 | 2.77 | high | 5-GW avg pts 3.20; mins 54; xGI 0.01; current GWs 6; fixture Elo diff +163 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£98.9m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.2m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 21.11 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gabriel | ARS | Defender | £7.9m | 20.11 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Hill | BOU | Defender | £5.5m | 17.88 | GW7, GW9, GW10, GW11 | — | — |
| Richards | CRY | Defender | £4.9m | 16.80 | GW7, GW8, GW9, GW11 | — | — |
| Muharemović | LEE | Defender | £5.0m | 15.58 | GW8, GW10 | — | — |
| Haaland | MCI | Forward | £15.7m | 29.25 | GW7, GW8, GW9, GW10, GW11 | GW7, GW8, GW9, GW10, GW11 | — |
| Thiago | BRE | Forward | £7.8m | 19.60 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Kusi-Asare | FUL | Forward | £4.4m | 0.48 | Bench | — | — |
| Raya | ARS | Goalkeeper | £6.1m | 15.67 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Steele | BHA | Goalkeeper | £4.0m | 0.37 | Bench | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 25.76 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW8, GW9, GW10, GW11 |
| Cherki | MCI | Midfielder | £7.9m | 23.37 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Groß | BHA | Midfielder | £6.1m | 17.93 | GW7, GW9, GW10, GW11 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 17.75 | GW7, GW8, GW10 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 15.95 | GW8, GW9, GW11 | — | — |

Squad cost: £99.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.11 | GW7, GW8, GW9, GW10, GW11 | — | GW10 |
| Egan | HUL | Defender | £4.1m | 13.69 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 12.99 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Branthwaite | EVE | Defender | £5.5m | 8.15 | Bench | — | — |
| Furlong | IPS | Defender | £3.9m | 0.74 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.60 | GW7, GW8, GW9, GW10, GW11 | — | GW8 |
| Havertz | ARS | Forward | £7.5m | 16.41 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.31 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.83 | GW7, GW8, GW10 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.37 | GW9, GW11 | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 25.76 | GW7, GW8, GW9, GW10, GW11 | GW7, GW8, GW9, GW10, GW11 | — |
| Cherki | MCI | Midfielder | £7.9m | 23.37 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9, GW11 |
| B.Fernandes | MUN | Midfielder | £11.8m | 19.76 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Rogers | CHE | Midfielder | £7.9m | 17.61 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 11.97 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £99.1m.

## One-transfer recommendation

**Branthwaite → Silva** (projected weighted XI+captain gain 10.58).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Branthwaite | Silva | £5.5m | £5.0m | £0.7m | 10.58 |
| Branthwaite | Rúben | £5.5m | £5.5m | £0.2m | 7.79 |
| Branthwaite | Hill | £5.5m | £5.5m | £0.2m | 7.34 |
| Gibbs-White | Mbeumo | £8.0m | £7.8m | £0.4m | 6.64 |
| Branthwaite | Richards | £5.5m | £4.9m | £0.8m | 6.27 |
| Gibbs-White | Cunha | £8.0m | £7.9m | £0.3m | 6.13 |
| Gibbs-White | Rice | £8.0m | £7.3m | £0.9m | 6.12 |
| Gibbs-White | Groß | £8.0m | £6.1m | £2.1m | 5.96 |
| Gibbs-White | Iwobi | £8.0m | £5.4m | £2.8m | 5.78 |
| Branthwaite | Van Hecke | £5.5m | £4.9m | £0.8m | 5.46 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
