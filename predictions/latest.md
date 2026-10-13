# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-13 16:18 UTC

Data commit: `e93925694053b2256c802e18b3972ece69ef9188`

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

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW7 player forecasts

| Player | Club | Pos | GW7 | GW8 | GW9 | GW10 | GW11 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | 7.80 | 5.73 | 6.68 | 6.43 | 6.93 | 26.95 | 1.73 | high | 5-GW avg pts 8.60; mins 88; xGI 0.92; current GWs 6; fixture Elo diff +163 |
| Semenyo | MCI | Midfielder | 7.51 | 4.47 | 5.31 | 4.77 | 5.56 | 22.45 | 2.70 | high | 5-GW avg pts 6.80; mins 90; xGI 0.35; current GWs 6; fixture Elo diff +163 |
| Cherki | MCI | Midfielder | 6.92 | 3.93 | 4.77 | 3.97 | 4.73 | 19.89 | 2.55 | high | 5-GW avg pts 7.20; mins 73; xGI 0.50; current GWs 6; fixture Elo diff +163 |
| Silva | BOU | Defender | 5.41 | 4.25 | 5.11 | 5.21 | 5.07 | 20.01 | 4.00 | high | 5-GW avg pts 2.20; mins 90; xGI 0.32; current GWs 6; fixture Elo diff +90 |
| Guéhi | MCI | Defender | 5.33 | 3.64 | 4.09 | 4.39 | 4.57 | 17.69 | 2.95 | high | 5-GW avg pts 5.20; mins 90; xGI 0.03; current GWs 6; fixture Elo diff +163 |
| Iwobi | FUL | Midfielder | 5.31 | 4.86 | 3.56 | 4.07 | 3.49 | 17.48 | 3.24 | high | 5-GW avg pts 3.20; mins 81; xGI 0.35; current GWs 6; fixture Elo diff +28 |
| B.Fernandes | MUN | Midfielder | 5.29 | 5.56 | 5.06 | 5.24 | 4.84 | 20.92 | 1.76 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +49 |
| Palmer | CHE | Midfielder | 4.91 | 5.16 | 4.61 | 4.78 | 5.20 | 19.71 | 2.03 | high | 5-GW avg pts 4.60; mins 89; xGI 0.34; current GWs 6; fixture Elo diff +25 |
| Donnarumma | MCI | Goalkeeper | 4.73 | 3.22 | 3.72 | 3.94 | 3.98 | 15.74 | 2.86 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 6; fixture Elo diff +163 |
| Gonzalo | FUL | Forward | 4.70 | 4.54 | 3.19 | 3.93 | 2.97 | 15.87 | 2.60 | high | 5-GW avg pts 2.00; mins 84; xGI 0.57; current GWs 6; fixture Elo diff +28 |
| Thiago | BRE | Forward | 4.69 | 5.34 | 5.11 | 4.47 | 5.00 | 19.72 | 2.53 | high | 5-GW avg pts 2.80; mins 90; xGI 0.48; current GWs 6; fixture Elo diff +54 |
| Rúben | MCI | Defender | 4.68 | 3.35 | 3.95 | 4.32 | 4.37 | 16.50 | 3.00 | high | 5-GW avg pts 4.20; mins 90; xGI 0.18; current GWs 6; fixture Elo diff +163 |
| Van Hecke | TOT | Defender | 4.55 | 3.36 | 3.86 | 3.87 | 4.61 | 16.14 | 3.29 | high | 5-GW avg pts 5.20; mins 90; xGI 0.22; current GWs 6; fixture Elo diff +31 |
| Sávio | TOT | Midfielder | 4.50 | 3.51 | 3.95 | 3.95 | 4.63 | 16.36 | 2.52 | high | 5-GW avg pts 2.00; mins 66; xGI 0.30; current GWs 6; fixture Elo diff +31 |
| Gabriel | ARS | Defender | 4.48 | 5.21 | 4.25 | 6.27 | 4.32 | 19.55 | 2.47 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +283 |
| Saka | ARS | Midfielder | 4.41 | 4.83 | 4.17 | 6.27 | 4.38 | 19.11 | 1.99 | high | 5-GW avg pts 5.00; mins 88; xGI 0.79; current GWs 6; fixture Elo diff +283 |
| Anderson | MCI | Midfielder | 4.40 | 3.43 | 3.82 | 4.05 | 4.15 | 15.87 | 2.52 | high | 5-GW avg pts 3.80; mins 88; xGI 0.14; current GWs 6; fixture Elo diff +163 |
| Havertz | ARS | Forward | 4.38 | 4.86 | 4.29 | 5.05 | 4.31 | 18.31 | 2.44 | high | 5-GW avg pts 3.00; mins 82; xGI 0.38; current GWs 6; fixture Elo diff +283 |
| Mbeumo | MUN | Midfielder | 4.36 | 4.83 | 4.36 | 4.71 | 4.38 | 18.13 | 2.29 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +49 |
| Dewsbury-Hall | EVE | Midfielder | 4.35 | 3.04 | 4.16 | 5.17 | 4.16 | 16.53 | 2.50 | high | 5-GW avg pts 4.40; mins 90; xGI 0.40; current GWs 6; fixture Elo diff -43 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.6m**. Current squad selling value: **£98.6m**. Total available funds: **£99.2m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 20.01 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gabriel | ARS | Defender | £7.9m | 19.55 | GW7, GW8, GW9, GW10, GW11 | — | GW10 |
| Van Hecke | TOT | Defender | £4.9m | 16.14 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Diop | IPS | Defender | £4.0m | 13.16 | GW9 | — | — |
| Davis | IPS | Defender | £4.0m | 12.56 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 26.95 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW10, GW11 | GW8 |
| Thiago | BRE | Forward | £7.8m | 19.72 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Salia | NEW | Forward | £4.5m | 0.33 | Bench | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 14.16 | GW9, GW10, GW11 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.86 | GW7, GW8 | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 22.45 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9 |
| Cherki | MCI | Midfielder | £7.8m | 19.89 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 18.91 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Iwobi | FUL | Midfielder | £5.4m | 17.48 | GW7, GW8, GW10, GW11 | — | — |
| Groß | BHA | Midfielder | £6.0m | 16.52 | GW7, GW8, GW10, GW11 | — | GW11 |

Squad cost: £99.2m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.55 | GW7, GW8, GW9, GW10, GW11 | GW10 | — |
| Branthwaite | EVE | Defender | £5.5m | 15.14 | GW7, GW9, GW10, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.31 | GW7, GW8, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 12.05 | GW8, GW9, GW11 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.72 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.72 | GW7, GW8, GW9, GW10, GW11 | GW9, GW11 | — |
| Havertz | ARS | Forward | £7.5m | 18.31 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.86 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.72 | GW9, GW10, GW11 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 20.92 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW8, GW9, GW10, GW11 |
| Cherki | MCI | Midfielder | £7.8m | 19.89 | GW7, GW8, GW9, GW10, GW11 | GW7 | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 18.91 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 18.13 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Rogers | CHE | Midfielder | £7.9m | 16.10 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £98.7m.

## One-transfer recommendation

**Rogers → Semenyo** (projected weighted XI+captain gain 7.43).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Rogers | Semenyo | £7.8m | £8.3m | £0.1m | 7.43 |
| Bassey | Silva | £4.5m | £5.0m | £0.1m | 5.70 |
| Mbeumo | Semenyo | £7.9m | £8.3m | £0.2m | 5.40 |
| Branthwaite | Silva | £5.5m | £5.0m | £1.1m | 4.70 |
| Gibbs-White | Semenyo | £8.0m | £8.3m | £0.3m | 3.98 |
| Cherki | Semenyo | £7.8m | £8.3m | £0.1m | 3.65 |
| Horníček | Donnarumma | £5.0m | £5.5m | £0.1m | 3.02 |
| B.Fernandes | Semenyo | £11.9m | £8.3m | £4.2m | 2.61 |
| Branthwaite | Guéhi | £5.5m | £6.0m | £0.1m | 2.34 |
| Horníček | Pickford | £5.0m | £5.5m | £0.1m | 2.24 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
