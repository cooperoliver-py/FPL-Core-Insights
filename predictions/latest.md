# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-15 20:00 UTC

Data commit: `d5e4db357272f7f89e8ccf5c0ce3e6773b35581d`

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
| Haaland | MCI | Forward | 8.42 | 6.00 | 7.37 | 6.95 | 7.67 | 29.18 | 1.87 | high | 5-GW avg pts 8.60; mins 88; xGI 0.92; current GWs 6; fixture Elo diff +163 |
| Semenyo | MCI | Midfielder | 7.64 | 5.89 | 6.15 | 6.40 | 6.31 | 26.12 | 3.15 | high | 5-GW avg pts 6.80; mins 90; xGI 0.35; current GWs 6; fixture Elo diff +163 |
| Cherki | MCI | Midfielder | 7.03 | 4.98 | 5.83 | 5.30 | 5.77 | 23.35 | 2.96 | high | 5-GW avg pts 7.20; mins 73; xGI 0.50; current GWs 6; fixture Elo diff +163 |
| Guéhi | MCI | Defender | 5.75 | 4.23 | 4.78 | 5.02 | 5.05 | 19.92 | 3.32 | high | 5-GW avg pts 5.20; mins 90; xGI 0.03; current GWs 6; fixture Elo diff +163 |
| Iwobi | FUL | Midfielder | 5.65 | 5.21 | 3.28 | 3.97 | 3.34 | 17.75 | 3.29 | high | 5-GW avg pts 3.20; mins 81; xGI 0.35; current GWs 6; fixture Elo diff +28 |
| Rúben | MCI | Defender | 5.41 | 3.98 | 4.44 | 4.86 | 4.80 | 18.83 | 3.42 | high | 5-GW avg pts 4.20; mins 90; xGI 0.18; current GWs 6; fixture Elo diff +163 |
| Silva | BOU | Defender | 5.30 | 3.89 | 4.70 | 5.33 | 4.69 | 19.10 | 3.82 | high | 5-GW avg pts 2.20; mins 90; xGI 0.32; current GWs 6; fixture Elo diff +90 |
| Donnarumma | MCI | Goalkeeper | 5.25 | 3.58 | 4.18 | 4.37 | 4.46 | 17.55 | 3.19 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 6; fixture Elo diff +163 |
| Gabriel | ARS | Defender | 5.24 | 5.10 | 4.83 | 5.62 | 4.90 | 20.56 | 2.60 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +283 |
| B.Fernandes | MUN | Midfielder | 4.94 | 5.16 | 4.81 | 5.12 | 4.94 | 19.97 | 1.68 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +49 |
| Palmer | CHE | Midfielder | 4.86 | 5.12 | 4.56 | 4.87 | 5.25 | 19.67 | 2.03 | high | 5-GW avg pts 4.60; mins 89; xGI 0.34; current GWs 6; fixture Elo diff +25 |
| Cunha | MUN | Midfielder | 4.72 | 4.62 | 4.44 | 4.57 | 4.44 | 18.29 | 2.32 | high | 5-GW avg pts 6.80; mins 84; xGI 0.26; current GWs 6; fixture Elo diff +49 |
| Van Hecke | TOT | Defender | 4.67 | 3.26 | 3.89 | 3.68 | 4.33 | 15.89 | 3.24 | high | 5-GW avg pts 5.20; mins 90; xGI 0.22; current GWs 6; fixture Elo diff +31 |
| Anderson | MCI | Midfielder | 4.66 | 3.76 | 4.17 | 4.35 | 4.45 | 17.10 | 2.71 | high | 5-GW avg pts 3.80; mins 88; xGI 0.14; current GWs 6; fixture Elo diff +163 |
| Rice | ARS | Midfielder | 4.58 | 4.66 | 4.24 | 4.86 | 4.28 | 18.14 | 2.48 | high | 5-GW avg pts 4.80; mins 87; xGI 0.15; current GWs 6; fixture Elo diff +283 |
| Thiago | BRE | Forward | 4.44 | 5.17 | 5.23 | 4.77 | 4.97 | 19.60 | 2.51 | high | 5-GW avg pts 2.80; mins 90; xGI 0.48; current GWs 6; fixture Elo diff +54 |
| Mbeumo | MUN | Midfielder | 4.43 | 4.90 | 4.40 | 4.86 | 4.74 | 18.61 | 2.36 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +49 |
| Matheus N. | MCI | Defender | 4.41 | 3.59 | 4.01 | 4.28 | 4.33 | 16.44 | 2.79 | high | 5-GW avg pts 3.20; mins 54; xGI 0.01; current GWs 6; fixture Elo diff +163 |
| Gibbs-White | NFO | Midfielder | 4.39 | 6.64 | 5.74 | 4.63 | 5.30 | 21.39 | 2.67 | high | 5-GW avg pts 5.60; mins 90; xGI 0.67; current GWs 6; fixture Elo diff -55 |
| Hill | BOU | Defender | 4.34 | 3.43 | 3.99 | 4.84 | 3.97 | 16.39 | 2.98 | high | 5-GW avg pts 2.60; mins 90; xGI 0.16; current GWs 6; fixture Elo diff +90 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£99.0m**. Total available funds: **£99.2m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.56 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Silva | BOU | Defender | £5.0m | 19.10 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Van Hecke | TOT | Defender | £4.9m | 15.89 | GW7, GW9, GW10, GW11 | — | — |
| Muharemović | LEE | Defender | £5.0m | 15.58 | GW8, GW10, GW11 | — | — |
| Diop | IPS | Defender | £4.0m | 12.42 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 29.18 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW10, GW11 | GW8 |
| Thiago | BRE | Forward | £7.8m | 19.60 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Kusi-Asare | FUL | Forward | £4.4m | 0.48 | Bench | — | — |
| Raya | ARS | Goalkeeper | £6.1m | 16.06 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Matthews | CRY | Goalkeeper | £4.0m | 0.39 | Bench | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 26.12 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9, GW10, GW11 |
| Cherki | MCI | Midfielder | £7.9m | 23.35 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.39 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Iwobi | FUL | Midfielder | £5.4m | 17.75 | GW7, GW8, GW10 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 15.95 | GW7, GW8, GW9, GW11 | — | — |

Squad cost: £99.3m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.56 | GW7, GW8, GW9, GW10, GW11 | — | GW10 |
| Branthwaite | EVE | Defender | £5.5m | 14.29 | GW7, GW9, GW10, GW11 | — | — |
| Egan | HUL | Defender | £4.1m | 13.69 | GW8, GW9, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 12.99 | GW7, GW8, GW10 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.74 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.60 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Havertz | ARS | Forward | £7.5m | 16.77 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.31 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.83 | GW7, GW8, GW10 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.36 | GW9, GW11 | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 26.12 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW10, GW11 | GW8 |
| Cherki | MCI | Midfielder | £7.9m | 23.35 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9, GW11 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.39 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 19.97 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Rogers | CHE | Midfielder | £7.9m | 17.61 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Branthwaite → Silva** (projected weighted XI+captain gain 4.19).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Branthwaite | Silva | £5.5m | £5.0m | £0.7m | 4.19 |
| Branthwaite | Rúben | £5.5m | £5.5m | £0.2m | 3.93 |
| Branthwaite | Hill | £5.5m | £5.5m | £0.2m | 1.49 |
| Horníček | Suzuki | £5.0m | £5.0m | £0.2m | 1.11 |
| Branthwaite | Van Hecke | £5.5m | £4.9m | £0.8m | 1.09 |
| Horníček | Kinsky | £5.0m | £4.5m | £0.7m | 1.06 |
| Horníček | Lammens | £5.0m | £4.9m | £0.3m | 1.03 |
| Rogers | Mbeumo | £7.8m | £7.9m | £0.1m | 1.00 |
| Horníček | Petrović | £5.0m | £4.5m | £0.7m | 0.95 |
| Branthwaite | Muharemović | £5.5m | £5.0m | £0.7m | 0.80 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
