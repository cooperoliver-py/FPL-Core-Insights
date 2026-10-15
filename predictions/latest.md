# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-15 05:02 UTC

Data commit: `978d9399918099eea2cb2843162bbdc2a0d07d78`

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
| Haaland | MCI | Forward | 8.42 | 5.95 | 7.45 | 6.97 | 7.77 | 29.28 | 1.88 | high | 5-GW avg pts 8.60; mins 88; xGI 0.92; current GWs 6; fixture Elo diff +163 |
| Semenyo | MCI | Midfielder | 7.68 | 5.38 | 6.03 | 6.08 | 6.18 | 25.31 | 3.05 | high | 5-GW avg pts 6.80; mins 90; xGI 0.35; current GWs 6; fixture Elo diff +163 |
| Cherki | MCI | Midfielder | 7.07 | 4.99 | 5.90 | 5.36 | 5.84 | 23.54 | 2.98 | high | 5-GW avg pts 7.20; mins 73; xGI 0.50; current GWs 6; fixture Elo diff +163 |
| Iwobi | FUL | Midfielder | 5.65 | 5.21 | 3.28 | 3.97 | 3.34 | 17.75 | 3.29 | high | 5-GW avg pts 3.20; mins 81; xGI 0.35; current GWs 6; fixture Elo diff +28 |
| Guéhi | MCI | Defender | 5.65 | 3.71 | 4.51 | 4.60 | 4.75 | 18.66 | 3.11 | high | 5-GW avg pts 5.20; mins 90; xGI 0.03; current GWs 6; fixture Elo diff +163 |
| Rúben | MCI | Defender | 5.42 | 3.61 | 4.25 | 4.52 | 4.64 | 18.01 | 3.27 | high | 5-GW avg pts 4.20; mins 90; xGI 0.18; current GWs 6; fixture Elo diff +163 |
| Silva | BOU | Defender | 5.30 | 3.89 | 4.70 | 5.33 | 4.69 | 19.10 | 3.82 | high | 5-GW avg pts 2.20; mins 90; xGI 0.32; current GWs 6; fixture Elo diff +90 |
| Gabriel | ARS | Defender | 5.26 | 5.09 | 4.91 | 5.61 | 4.98 | 20.68 | 2.62 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +283 |
| Donnarumma | MCI | Goalkeeper | 5.06 | 3.14 | 3.79 | 3.97 | 4.07 | 16.14 | 2.93 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 6; fixture Elo diff +163 |
| B.Fernandes | MUN | Midfielder | 5.03 | 5.24 | 4.90 | 5.20 | 5.03 | 20.32 | 1.71 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +49 |
| Palmer | CHE | Midfielder | 4.86 | 5.12 | 4.56 | 4.87 | 5.25 | 19.67 | 2.03 | high | 5-GW avg pts 4.60; mins 89; xGI 0.34; current GWs 6; fixture Elo diff +25 |
| Cunha | MUN | Midfielder | 4.72 | 4.61 | 4.44 | 4.56 | 4.44 | 18.28 | 2.31 | high | 5-GW avg pts 6.80; mins 84; xGI 0.26; current GWs 6; fixture Elo diff +49 |
| Van Hecke | TOT | Defender | 4.67 | 3.26 | 3.89 | 3.68 | 4.33 | 15.89 | 3.24 | high | 5-GW avg pts 5.20; mins 90; xGI 0.22; current GWs 6; fixture Elo diff +31 |
| Anderson | MCI | Midfielder | 4.64 | 3.59 | 4.14 | 4.27 | 4.39 | 16.80 | 2.67 | high | 5-GW avg pts 3.80; mins 88; xGI 0.14; current GWs 6; fixture Elo diff +163 |
| Rice | ARS | Midfielder | 4.58 | 4.65 | 4.24 | 4.85 | 4.28 | 18.12 | 2.48 | high | 5-GW avg pts 4.80; mins 87; xGI 0.15; current GWs 6; fixture Elo diff +283 |
| Mbeumo | MUN | Midfielder | 4.52 | 4.99 | 4.50 | 4.94 | 4.83 | 18.96 | 2.40 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +49 |
| Thiago | BRE | Forward | 4.46 | 5.19 | 5.25 | 4.79 | 4.99 | 19.68 | 2.52 | high | 5-GW avg pts 2.80; mins 90; xGI 0.48; current GWs 6; fixture Elo diff +54 |
| Gibbs-White | NFO | Midfielder | 4.39 | 6.64 | 5.74 | 4.63 | 5.30 | 21.39 | 2.67 | high | 5-GW avg pts 5.60; mins 90; xGI 0.67; current GWs 6; fixture Elo diff -55 |
| Matheus N. | MCI | Defender | 4.36 | 3.38 | 3.81 | 4.11 | 4.13 | 15.80 | 2.68 | high | 5-GW avg pts 3.20; mins 54; xGI 0.01; current GWs 6; fixture Elo diff +163 |
| Rogers | CHE | Midfielder | 4.34 | 4.57 | 4.18 | 4.33 | 4.70 | 17.65 | 2.23 | high | 5-GW avg pts 6.00; mins 88; xGI 0.43; current GWs 6; fixture Elo diff +25 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.6m**. Current squad selling value: **£98.6m**. Total available funds: **£99.2m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.68 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Silva | BOU | Defender | £5.0m | 19.10 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Van Hecke | TOT | Defender | £4.9m | 15.89 | GW7, GW9, GW10, GW11 | — | — |
| Muharemović | LEE | Defender | £5.0m | 15.58 | GW8, GW10, GW11 | — | — |
| Diop | IPS | Defender | £4.0m | 12.42 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 29.28 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW10, GW11 | GW8 |
| Thiago | BRE | Forward | £7.8m | 19.68 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Kusi-Asare | FUL | Forward | £4.4m | 0.48 | Bench | — | — |
| Raya | ARS | Goalkeeper | £6.1m | 16.25 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Austin | TOT | Goalkeeper | £4.0m | 0.30 | Bench | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 25.31 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9, GW10, GW11 |
| Cherki | MCI | Midfielder | £7.9m | 23.54 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.39 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Iwobi | FUL | Midfielder | £5.4m | 17.75 | GW7, GW8, GW10 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 15.95 | GW7, GW8, GW9, GW11 | — | — |

Squad cost: £99.3m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.68 | GW7, GW8, GW9, GW10, GW11 | GW10 | GW7 |
| Branthwaite | EVE | Defender | £5.5m | 14.29 | GW7, GW9, GW10, GW11 | — | — |
| Egan | HUL | Defender | £4.1m | 13.69 | GW8, GW9, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 12.99 | GW7, GW8, GW10 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.74 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.68 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Havertz | ARS | Forward | £7.5m | 16.76 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.31 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.83 | GW7, GW8, GW10 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.41 | GW9, GW11 | — | — |
| Cherki | MCI | Midfielder | £7.9m | 23.54 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW11 | GW10 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.39 | GW7, GW8, GW9, GW10, GW11 | GW8 | GW9, GW11 |
| B.Fernandes | MUN | Midfielder | £11.9m | 20.32 | GW7, GW8, GW9, GW10, GW11 | — | GW8 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.96 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Rogers | CHE | Midfielder | £7.9m | 17.65 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £98.8m.

## One-transfer recommendation

**Rogers → Semenyo** (projected weighted XI+captain gain 8.90).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Rogers | Semenyo | £7.8m | £8.3m | £0.1m | 8.90 |
| Mbeumo | Semenyo | £7.9m | £8.3m | £0.2m | 7.58 |
| B.Fernandes | Semenyo | £11.9m | £8.3m | £4.2m | 6.22 |
| Bassey | Silva | £4.5m | £5.0m | £0.1m | 4.61 |
| Branthwaite | Silva | £5.5m | £5.0m | £1.1m | 4.19 |
| Horníček | Donnarumma | £5.0m | £5.5m | £0.1m | 4.15 |
| Gibbs-White | Semenyo | £8.0m | £8.3m | £0.3m | 4.02 |
| Branthwaite | Guéhi | £5.5m | £6.0m | £0.1m | 3.75 |
| Branthwaite | Rúben | £5.5m | £5.5m | £0.6m | 3.11 |
| Cherki | Semenyo | £7.8m | £8.3m | £0.1m | 3.00 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
