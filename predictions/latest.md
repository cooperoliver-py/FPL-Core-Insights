# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-13 21:27 UTC

Data commit: `d5a6022f49c8568babf7bb69a659cd17cc227cb7`

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
| Haaland | MCI | Forward | 8.42 | 5.97 | 7.45 | 6.98 | 7.77 | 29.31 | 1.88 | high | 5-GW avg pts 8.60; mins 88; xGI 0.92; current GWs 6; fixture Elo diff +163 |
| Semenyo | MCI | Midfielder | 7.68 | 5.60 | 6.13 | 6.19 | 6.28 | 25.72 | 3.10 | high | 5-GW avg pts 6.80; mins 90; xGI 0.35; current GWs 6; fixture Elo diff +163 |
| Cherki | MCI | Midfielder | 6.84 | 4.94 | 5.73 | 5.19 | 5.67 | 22.90 | 2.94 | high | 5-GW avg pts 7.20; mins 73; xGI 0.50; current GWs 6; fixture Elo diff +163 |
| Guéhi | MCI | Defender | 5.65 | 3.85 | 4.61 | 4.71 | 4.85 | 19.00 | 3.17 | high | 5-GW avg pts 5.20; mins 90; xGI 0.03; current GWs 6; fixture Elo diff +163 |
| Iwobi | FUL | Midfielder | 5.64 | 5.19 | 3.27 | 3.96 | 3.33 | 17.69 | 3.28 | high | 5-GW avg pts 3.20; mins 81; xGI 0.35; current GWs 6; fixture Elo diff +28 |
| Rúben | MCI | Defender | 5.42 | 3.88 | 4.35 | 4.77 | 4.74 | 18.57 | 3.38 | high | 5-GW avg pts 4.20; mins 90; xGI 0.18; current GWs 6; fixture Elo diff +163 |
| Silva | BOU | Defender | 5.29 | 3.87 | 4.68 | 5.31 | 4.67 | 19.05 | 3.81 | high | 5-GW avg pts 2.20; mins 90; xGI 0.32; current GWs 6; fixture Elo diff +90 |
| Donnarumma | MCI | Goalkeeper | 5.06 | 3.28 | 3.89 | 4.09 | 4.17 | 16.48 | 3.00 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 6; fixture Elo diff +163 |
| B.Fernandes | MUN | Midfielder | 5.00 | 5.16 | 4.80 | 5.00 | 4.82 | 19.87 | 1.67 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +49 |
| Gabriel | ARS | Defender | 4.90 | 4.97 | 4.37 | 5.63 | 4.56 | 19.55 | 2.47 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +283 |
| Palmer | CHE | Midfielder | 4.86 | 5.12 | 4.57 | 4.88 | 5.25 | 19.69 | 2.03 | high | 5-GW avg pts 4.60; mins 89; xGI 0.34; current GWs 6; fixture Elo diff +25 |
| Cunha | MUN | Midfielder | 4.70 | 4.62 | 4.42 | 4.45 | 4.30 | 18.09 | 2.29 | high | 5-GW avg pts 6.80; mins 84; xGI 0.26; current GWs 6; fixture Elo diff +49 |
| Van Hecke | TOT | Defender | 4.66 | 3.25 | 3.88 | 3.67 | 4.32 | 15.84 | 3.23 | high | 5-GW avg pts 5.20; mins 90; xGI 0.22; current GWs 6; fixture Elo diff +31 |
| Anderson | MCI | Midfielder | 4.64 | 3.63 | 4.14 | 4.29 | 4.39 | 16.85 | 2.68 | high | 5-GW avg pts 3.80; mins 88; xGI 0.14; current GWs 6; fixture Elo diff +163 |
| Gibbs-White | NFO | Midfielder | 4.56 | 6.59 | 5.69 | 4.79 | 5.25 | 21.54 | 2.69 | high | 5-GW avg pts 5.60; mins 90; xGI 0.67; current GWs 6; fixture Elo diff -55 |
| Thiago | BRE | Forward | 4.52 | 5.24 | 5.30 | 4.84 | 5.04 | 19.89 | 2.55 | high | 5-GW avg pts 2.80; mins 90; xGI 0.48; current GWs 6; fixture Elo diff +54 |
| Rice | ARS | Midfielder | 4.49 | 4.68 | 4.08 | 4.88 | 4.19 | 17.90 | 2.45 | high | 5-GW avg pts 4.80; mins 87; xGI 0.15; current GWs 6; fixture Elo diff +283 |
| Mbeumo | MUN | Midfielder | 4.48 | 4.97 | 4.36 | 4.81 | 4.58 | 18.56 | 2.35 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +49 |
| Dewsbury-Hall | EVE | Midfielder | 4.37 | 3.40 | 4.40 | 5.88 | 4.40 | 17.72 | 2.68 | high | 5-GW avg pts 4.40; mins 90; xGI 0.40; current GWs 6; fixture Elo diff -43 |
| Matheus N. | MCI | Defender | 4.36 | 3.53 | 3.91 | 4.22 | 4.23 | 16.15 | 2.74 | high | 5-GW avg pts 3.20; mins 54; xGI 0.01; current GWs 6; fixture Elo diff +163 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.6m**. Current squad selling value: **£98.6m**. Total available funds: **£99.2m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.55 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Silva | BOU | Defender | £5.0m | 19.05 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Botman | NEW | Defender | £5.0m | 16.00 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Van Hecke | TOT | Defender | £4.9m | 15.84 | GW7, GW9, GW10, GW11 | — | — |
| van Ewijk | COV | Defender | £3.9m | 9.69 | Bench | — | — |
| Haaland | MCI | Forward | £15.6m | 29.31 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW10, GW11 | GW8 |
| Thiago | BRE | Forward | £7.8m | 19.89 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Danns | LIV | Forward | £4.5m | 0.27 | Bench | — | — |
| Raya | ARS | Goalkeeper | £6.1m | 15.01 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Balcombe | BRE | Goalkeeper | £4.0m | 0.28 | Bench | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 25.72 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9, GW10, GW11 |
| Cherki | MCI | Midfielder | £7.8m | 22.90 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.54 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Iwobi | FUL | Midfielder | £5.4m | 17.69 | GW7, GW8, GW10 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 15.95 | GW8, GW9, GW11 | — | — |

Squad cost: £99.2m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.55 | GW7, GW8, GW9, GW10, GW11 | GW10 | — |
| Branthwaite | EVE | Defender | £5.5m | 15.00 | GW7, GW9, GW10, GW11 | — | — |
| Egan | HUL | Defender | £4.1m | 13.77 | GW8, GW9, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 12.99 | GW7, GW8, GW10 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.74 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.89 | GW7, GW8, GW9, GW10, GW11 | — | GW8 |
| Havertz | ARS | Forward | £7.5m | 16.37 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.31 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.82 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.75 | GW9, GW10, GW11 | — | — |
| Cherki | MCI | Midfielder | £7.8m | 22.90 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW11 | GW10 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.54 | GW7, GW8, GW9, GW10, GW11 | GW8 | GW9, GW11 |
| B.Fernandes | MUN | Midfielder | £11.9m | 19.87 | GW7, GW8, GW9, GW10, GW11 | — | GW7 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.56 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Rogers | CHE | Midfielder | £7.9m | 17.40 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £98.7m.

## One-transfer recommendation

**Rogers → Semenyo** (projected weighted XI+captain gain 10.24).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Rogers | Semenyo | £7.8m | £8.3m | £0.1m | 10.24 |
| Mbeumo | Semenyo | £7.9m | £8.3m | £0.2m | 9.08 |
| B.Fernandes | Semenyo | £11.9m | £8.3m | £4.2m | 7.76 |
| Gibbs-White | Semenyo | £8.0m | £8.3m | £0.3m | 5.20 |
| Cherki | Semenyo | £7.8m | £8.3m | £0.1m | 4.73 |
| Bassey | Silva | £4.5m | £5.0m | £0.1m | 4.44 |
| Horníček | Donnarumma | £5.0m | £5.5m | £0.1m | 4.20 |
| Branthwaite | Silva | £5.5m | £5.0m | £1.1m | 3.69 |
| Branthwaite | Guéhi | £5.5m | £6.0m | £0.1m | 3.64 |
| Branthwaite | Rúben | £5.5m | £5.5m | £0.6m | 3.21 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
