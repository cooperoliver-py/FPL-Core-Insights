# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-24 05:13 UTC

Data commit: `392f79ad85fcbe5c47b8f1e33d6c3dc787dcfd53`

## Data freshness

All scheduled Premier League fixtures before GW6 are complete.

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

## Top GW6 player forecasts

| Player | Club | Pos | GW6 | GW7 | GW8 | GW9 | GW10 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 6.04 | 5.51 | 5.53 | 5.04 | 5.26 | 22.10 | 1.86 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +76 |
| Gabriel | ARS | Defender | 5.56 | 4.88 | 5.56 | 4.48 | 6.83 | 21.63 | 2.70 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Gibbs-White | NFO | Midfielder | 5.49 | 4.46 | 6.66 | 5.16 | 4.82 | 21.34 | 2.67 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| Haaland | MCI | Forward | 5.26 | 7.91 | 5.31 | 6.17 | 6.01 | 24.56 | 1.57 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +144 |
| Cunha | MUN | Midfielder | 4.98 | 4.31 | 4.96 | 4.21 | 4.73 | 18.61 | 2.36 | high | 5-GW avg pts 5.20; mins 81; xGI 0.29; current GWs 5; fixture Elo diff +76 |
| Dewsbury-Hall | EVE | Midfielder | 4.88 | 4.03 | 3.04 | 3.90 | 4.98 | 16.65 | 2.52 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Havertz | ARS | Forward | 4.76 | 4.22 | 4.71 | 4.11 | 6.15 | 18.90 | 2.49 | high | 5-GW avg pts 3.80; mins 87; xGI 0.41; current GWs 5; fixture Elo diff +291 |
| Mykolenko | EVE | Defender | 4.75 | 3.38 | 2.46 | 3.30 | 5.06 | 15.10 | 3.28 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Pickford | EVE | Goalkeeper | 4.74 | 3.28 | 2.48 | 3.20 | 5.19 | 15.03 | 2.73 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 5; fixture Elo diff +18 |
| Mbeumo | MUN | Midfielder | 4.64 | 4.35 | 4.74 | 4.35 | 4.57 | 18.13 | 2.30 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +76 |
| Rogers | CHE | Midfielder | 4.59 | 4.28 | 4.56 | 4.32 | 4.28 | 17.69 | 2.30 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Saka | ARS | Midfielder | 4.54 | 4.27 | 4.54 | 4.14 | 6.14 | 18.59 | 1.96 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Tarkowski | EVE | Defender | 4.48 | 3.68 | 2.50 | 3.48 | 4.83 | 15.13 | 2.48 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Branthwaite | EVE | Defender | 4.43 | 3.83 | 2.64 | 3.67 | 4.62 | 15.33 | 2.79 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Barry | EVE | Forward | 4.42 | 4.06 | 2.38 | 3.79 | 4.50 | 15.33 | 2.74 | high | 5-GW avg pts 4.00; mins 83; xGI 0.73; current GWs 5; fixture Elo diff +18 |
| Murillo | NFO | Defender | 4.36 | 2.99 | 4.35 | 3.68 | 3.15 | 15.00 | 2.73 | high | 5-GW avg pts 4.60; mins 90; xGI 0.16; current GWs 5; fixture Elo diff -41 |
| Thiago | BRE | Forward | 4.33 | 4.80 | 5.44 | 5.24 | 4.65 | 19.46 | 2.49 | high | 5-GW avg pts 2.00; mins 88; xGI 0.66; current GWs 5; fixture Elo diff +31 |
| Barnes | NEW | Midfielder | 4.31 | 3.52 | 4.10 | 4.08 | 4.24 | 16.16 | 2.65 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Iwobi | FUL | Midfielder | 4.30 | 4.69 | 4.16 | 2.97 | 3.23 | 15.87 | 2.94 | high | 5-GW avg pts 2.80; mins 82; xGI 0.32; current GWs 5; fixture Elo diff +95 |
| Garner | EVE | Midfielder | 4.30 | 4.07 | 2.95 | 3.92 | 4.26 | 15.62 | 2.60 | high | 5-GW avg pts 2.20; mins 66; xGI 0.07; current GWs 5; fixture Elo diff +18 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.0m**. Current squad selling value: **£99.3m**. Total available funds: **£99.3m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.3m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.63 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW6, GW8 |
| Silva | BOU | Defender | £5.0m | 17.48 | GW7, GW8, GW9, GW10 | — | — |
| Truffert | BOU | Defender | £5.4m | 16.89 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Mykolenko | EVE | Defender | £4.6m | 15.10 | GW6, GW10 | — | — |
| Giles | HUL | Defender | £4.0m | 12.25 | GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 19.46 | GW6, GW7, GW8, GW9, GW10 | GW9 | — |
| Havertz | ARS | Forward | £7.6m | 18.90 | GW6, GW7, GW8, GW9, GW10 | — | GW10 |
| Salia | NEW | Forward | £4.5m | 0.45 | Bench | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 15.03 | GW6, GW7, GW9, GW10 | — | — |
| Kelleher | BRE | Goalkeeper | £5.0m | 13.05 | GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 22.10 | GW6, GW7, GW8, GW9, GW10 | GW6 | GW7 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.34 | GW6, GW7, GW8, GW9, GW10 | GW8 | GW9 |
| Semenyo | MCI | Midfielder | £8.4m | 20.74 | GW6, GW7, GW8, GW9, GW10 | GW7 | — |
| Cunha | MUN | Midfielder | £7.9m | 18.61 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 15.87 | GW6, GW7, GW8 | — | — |

Squad cost: £99.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.63 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW6, GW8 |
| Branthwaite | EVE | Defender | £5.5m | 15.33 | GW6, GW7, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.95 | GW6, GW7, GW8, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 11.98 | GW8, GW9 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.99 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.46 | GW6, GW7, GW8, GW9, GW10 | GW9 | — |
| Havertz | ARS | Forward | £7.6m | 18.90 | GW6, GW7, GW8, GW9, GW10 | — | GW10 |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.29 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.13 | GW6, GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 22.10 | GW6, GW7, GW8, GW9, GW10 | GW6 | GW7 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.34 | GW6, GW7, GW8, GW9, GW10 | GW8 | GW9 |
| Semenyo | MCI | Midfielder | £8.4m | 20.74 | GW6, GW7, GW8, GW9, GW10 | GW7 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 18.13 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Rogers | CHE | Midfielder | £7.7m | 17.69 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.3m.

## One-transfer recommendation

**Branthwaite → Silva** (projected weighted XI+captain gain 1.91).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Branthwaite | Silva | £5.5m | £5.0m | £0.5m | 1.91 |
| Branthwaite | Truffert | £5.5m | £5.4m | £0.1m | 1.32 |
| Egan | Davis | £4.1m | £4.0m | £0.1m | 0.84 |
| Egan | Thomas | £4.1m | £4.0m | £0.1m | 0.70 |
| Egan | Giles | £4.1m | £4.0m | £0.1m | 0.53 |
| Mbeumo | Cunha | £7.9m | £7.9m | £0.0m | 0.47 |
| Egan | Diop | £4.1m | £4.0m | £0.1m | 0.26 |
| Egan | Dasilva | £4.1m | £4.0m | £0.1m | 0.21 |
| Horníček | Tzolakis | £5.0m | £4.6m | £0.4m | 0.21 |
| Horníček | Petrović | £5.0m | £4.5m | £0.5m | 0.12 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
