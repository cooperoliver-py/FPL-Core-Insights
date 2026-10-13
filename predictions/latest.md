# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-13 07:00 UTC

Data commit: `097b3bde188162cb6001240d01b8c6b0d3d54b27`

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
| Haaland | MCI | Forward | 7.67 | 5.78 | 6.54 | 6.49 | 6.80 | 26.73 | 1.71 | high | 5-GW avg pts 8.60; mins 88; xGI 0.92; current GWs 6; fixture Elo diff +163 |
| Semenyo | MCI | Midfielder | 7.33 | 4.42 | 5.16 | 4.69 | 5.38 | 21.94 | 2.64 | high | 5-GW avg pts 6.80; mins 90; xGI 0.35; current GWs 6; fixture Elo diff +163 |
| Cherki | MCI | Midfielder | 6.67 | 4.10 | 4.82 | 4.15 | 4.78 | 19.99 | 2.56 | high | 5-GW avg pts 7.20; mins 73; xGI 0.50; current GWs 6; fixture Elo diff +163 |
| Silva | BOU | Defender | 5.32 | 4.19 | 4.97 | 5.12 | 4.98 | 19.64 | 3.93 | high | 5-GW avg pts 2.20; mins 90; xGI 0.32; current GWs 6; fixture Elo diff +90 |
| Iwobi | FUL | Midfielder | 5.25 | 4.78 | 3.50 | 4.02 | 3.42 | 17.22 | 3.19 | high | 5-GW avg pts 3.20; mins 81; xGI 0.35; current GWs 6; fixture Elo diff +28 |
| B.Fernandes | MUN | Midfielder | 5.19 | 5.51 | 5.02 | 5.20 | 4.80 | 20.68 | 1.74 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +49 |
| Guéhi | MCI | Defender | 5.12 | 3.51 | 3.94 | 4.33 | 4.35 | 17.07 | 2.85 | high | 5-GW avg pts 5.20; mins 90; xGI 0.03; current GWs 6; fixture Elo diff +163 |
| Palmer | CHE | Midfielder | 5.00 | 5.26 | 4.68 | 4.88 | 5.29 | 20.07 | 2.07 | high | 5-GW avg pts 4.60; mins 89; xGI 0.34; current GWs 6; fixture Elo diff +25 |
| Mbeumo | MUN | Midfielder | 4.79 | 4.99 | 4.63 | 4.81 | 4.64 | 19.13 | 2.42 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +49 |
| Thiago | BRE | Forward | 4.77 | 5.63 | 5.22 | 4.68 | 5.17 | 20.39 | 2.61 | high | 5-GW avg pts 2.80; mins 90; xGI 0.48; current GWs 6; fixture Elo diff +54 |
| Donnarumma | MCI | Goalkeeper | 4.67 | 3.22 | 3.64 | 3.94 | 3.93 | 15.59 | 2.84 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 6; fixture Elo diff +163 |
| Anderson | MCI | Midfielder | 4.59 | 3.32 | 3.73 | 4.06 | 4.01 | 15.82 | 2.51 | high | 5-GW avg pts 3.80; mins 88; xGI 0.14; current GWs 6; fixture Elo diff +163 |
| Saka | ARS | Midfielder | 4.58 | 4.94 | 4.43 | 6.47 | 4.55 | 19.83 | 2.07 | high | 5-GW avg pts 5.00; mins 88; xGI 0.79; current GWs 6; fixture Elo diff +283 |
| Gabriel | ARS | Defender | 4.49 | 5.23 | 4.25 | 6.30 | 4.32 | 19.60 | 2.48 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +283 |
| Rúben | MCI | Defender | 4.46 | 3.30 | 3.82 | 4.26 | 4.24 | 16.02 | 2.91 | high | 5-GW avg pts 4.20; mins 90; xGI 0.18; current GWs 6; fixture Elo diff +163 |
| Dewsbury-Hall | EVE | Midfielder | 4.45 | 3.17 | 4.21 | 5.02 | 4.21 | 16.71 | 2.53 | high | 5-GW avg pts 4.40; mins 90; xGI 0.40; current GWs 6; fixture Elo diff -43 |
| Van Hecke | TOT | Defender | 4.42 | 3.34 | 3.91 | 3.85 | 4.48 | 15.94 | 3.25 | high | 5-GW avg pts 5.20; mins 90; xGI 0.22; current GWs 6; fixture Elo diff +31 |
| Havertz | ARS | Forward | 4.39 | 5.01 | 4.30 | 5.09 | 4.33 | 18.49 | 2.47 | high | 5-GW avg pts 3.00; mins 82; xGI 0.38; current GWs 6; fixture Elo diff +283 |
| Cunha | MUN | Midfielder | 4.33 | 4.71 | 4.21 | 4.48 | 4.13 | 17.55 | 2.22 | high | 5-GW avg pts 6.80; mins 84; xGI 0.26; current GWs 6; fixture Elo diff +49 |
| Groß | BHA | Midfielder | 4.30 | 3.49 | 3.42 | 4.26 | 5.62 | 16.53 | 2.76 | high | 5-GW avg pts 10.20; mins 90; xGI 0.56; current GWs 6; fixture Elo diff +31 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.6m**. Current squad selling value: **£98.6m**. Total available funds: **£99.2m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 19.64 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gabriel | ARS | Defender | £7.9m | 19.60 | GW7, GW8, GW9, GW10, GW11 | — | GW10 |
| Van Hecke | TOT | Defender | £4.9m | 15.94 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Diop | IPS | Defender | £4.0m | 12.72 | GW9 | — | — |
| Davis | IPS | Defender | £4.0m | 12.55 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 26.73 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW10, GW11 | GW8 |
| Thiago | BRE | Forward | £7.8m | 20.39 | GW7, GW8, GW9, GW10, GW11 | — | GW9 |
| Danns | LIV | Forward | £4.5m | 0.33 | Bench | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 14.18 | GW9, GW10, GW11 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.87 | GW7, GW8 | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 21.94 | GW7, GW8, GW9, GW10, GW11 | — | GW7 |
| Cherki | MCI | Midfielder | £7.8m | 19.99 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 19.14 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Iwobi | FUL | Midfielder | £5.4m | 17.22 | GW7, GW8, GW10, GW11 | — | — |
| Groß | BHA | Midfielder | £6.0m | 16.53 | GW7, GW8, GW10, GW11 | — | GW11 |

Squad cost: £99.2m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.60 | GW7, GW8, GW9, GW10, GW11 | GW10 | — |
| Branthwaite | EVE | Defender | £5.5m | 14.13 | GW7, GW9, GW10, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.27 | GW7, GW8, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 11.69 | GW8, GW9, GW11 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.72 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 20.39 | GW7, GW8, GW9, GW10, GW11 | GW9, GW11 | GW8 |
| Havertz | ARS | Forward | £7.5m | 18.49 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.87 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.71 | GW9, GW10, GW11 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 20.68 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9, GW10, GW11 |
| Cherki | MCI | Midfielder | £7.8m | 19.99 | GW7, GW8, GW9, GW10, GW11 | GW7 | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 19.14 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 19.13 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Rogers | CHE | Midfielder | £7.9m | 16.78 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £98.7m.

## One-transfer recommendation

**Rogers → Semenyo** (projected weighted XI+captain gain 5.94).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Rogers | Semenyo | £7.8m | £8.3m | £0.1m | 5.94 |
| Bassey | Silva | £4.5m | £5.0m | £0.1m | 5.53 |
| Branthwaite | Silva | £5.5m | £5.0m | £1.1m | 5.30 |
| Mbeumo | Semenyo | £7.9m | £8.3m | £0.2m | 3.60 |
| Gibbs-White | Semenyo | £8.0m | £8.3m | £0.3m | 2.95 |
| Horníček | Donnarumma | £5.0m | £5.5m | £0.1m | 2.88 |
| Branthwaite | Guéhi | £5.5m | £6.0m | £0.1m | 2.74 |
| Cherki | Semenyo | £7.8m | £8.3m | £0.1m | 2.74 |
| Horníček | Pickford | £5.0m | £5.5m | £0.1m | 2.27 |
| B.Fernandes | Semenyo | £11.9m | £8.3m | £4.2m | 2.04 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
