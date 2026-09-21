# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-21 20:31 UTC

Data commit: `75e74565b50bc481a38393b73ced31eee798c4f1`

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
| B.Fernandes | MUN | Midfielder | 6.07 | 5.54 | 5.56 | 5.07 | 5.30 | 22.23 | 1.85 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +76 |
| Gabriel | ARS | Defender | 5.72 | 5.16 | 5.72 | 4.72 | 6.83 | 22.34 | 2.79 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Haaland | MCI | Forward | 5.61 | 7.73 | 5.66 | 6.32 | 6.36 | 25.33 | 1.62 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +144 |
| Gibbs-White | NFO | Midfielder | 5.44 | 4.41 | 6.61 | 5.11 | 4.77 | 21.14 | 2.64 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| Cunha | MUN | Midfielder | 4.98 | 4.31 | 4.96 | 4.21 | 4.73 | 18.61 | 2.36 | high | 5-GW avg pts 5.20; mins 81; xGI 0.29; current GWs 5; fixture Elo diff +76 |
| Mbeumo | MUN | Midfielder | 4.95 | 4.66 | 5.05 | 4.66 | 4.88 | 19.38 | 2.45 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +76 |
| Dewsbury-Hall | EVE | Midfielder | 4.91 | 4.24 | 3.44 | 4.11 | 5.01 | 17.37 | 2.63 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Havertz | ARS | Forward | 4.76 | 4.22 | 4.71 | 4.11 | 6.15 | 18.89 | 2.49 | high | 5-GW avg pts 3.80; mins 87; xGI 0.41; current GWs 5; fixture Elo diff +291 |
| Pickford | EVE | Goalkeeper | 4.76 | 3.47 | 2.86 | 3.39 | 5.22 | 15.67 | 2.85 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 5; fixture Elo diff +18 |
| Mykolenko | EVE | Defender | 4.69 | 3.43 | 2.69 | 3.35 | 5.02 | 15.28 | 3.32 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Rogers | CHE | Midfielder | 4.59 | 4.28 | 4.56 | 4.32 | 4.28 | 17.69 | 2.30 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Saka | ARS | Midfielder | 4.47 | 4.20 | 4.47 | 4.08 | 6.07 | 18.32 | 1.93 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Tarkowski | EVE | Defender | 4.46 | 3.80 | 2.62 | 3.59 | 4.80 | 15.36 | 2.52 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Groß | BHA | Midfielder | 4.45 | 4.75 | 3.94 | 3.87 | 4.65 | 17.38 | 3.00 | high | 5-GW avg pts 9.40; mins 90; xGI 0.53; current GWs 5; fixture Elo diff -10 |
| Branthwaite | EVE | Defender | 4.45 | 3.94 | 2.75 | 3.78 | 4.64 | 15.63 | 2.84 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Barnes | NEW | Midfielder | 4.43 | 3.76 | 4.33 | 4.30 | 4.47 | 16.98 | 2.78 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Thiago | BRE | Forward | 4.42 | 4.88 | 5.53 | 5.32 | 4.73 | 19.80 | 2.54 | high | 5-GW avg pts 2.00; mins 88; xGI 0.66; current GWs 5; fixture Elo diff +31 |
| Semenyo | MCI | Midfielder | 4.40 | 7.46 | 4.45 | 5.22 | 4.77 | 21.19 | 2.52 | high | 5-GW avg pts 6.60; mins 90; xGI 0.30; current GWs 5; fixture Elo diff +144 |
| Barry | EVE | Forward | 4.40 | 4.04 | 2.47 | 3.78 | 4.49 | 15.35 | 2.74 | high | 5-GW avg pts 4.00; mins 83; xGI 0.73; current GWs 5; fixture Elo diff +18 |
| Murillo | NFO | Defender | 4.38 | 3.10 | 4.31 | 3.79 | 3.26 | 15.23 | 2.77 | high | 5-GW avg pts 4.60; mins 90; xGI 0.16; current GWs 5; fixture Elo diff -41 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.0m**. Current squad selling value: **£99.4m**. Total available funds: **£99.4m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.2m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 22.34 | GW6, GW7, GW8, GW9, GW10 | GW6, GW10 | GW8 |
| Silva | BOU | Defender | £5.0m | 17.73 | GW7, GW8, GW9, GW10 | — | — |
| Truffert | BOU | Defender | £5.5m | 17.67 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Mykolenko | EVE | Defender | £4.6m | 15.28 | GW6, GW10 | — | — |
| Giles | HUL | Defender | £4.0m | 12.30 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 25.33 | GW6, GW7, GW8, GW9, GW10 | GW7, GW9 | GW6, GW10 |
| Thiago | BRE | Forward | £7.8m | 19.80 | GW6, GW7, GW8, GW9, GW10 | — | GW9 |
| Barry | EVE | Forward | £5.6m | 15.35 | GW6, GW7, GW10 | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 15.67 | GW6, GW9, GW10 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.55 | GW7, GW8 | — | — |
| Semenyo | MCI | Midfielder | £8.4m | 21.19 | GW6, GW7, GW8, GW9, GW10 | — | GW7 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.14 | GW6, GW7, GW8, GW9, GW10 | GW8 | — |
| Groß | BHA | Midfielder | £5.8m | 17.38 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Xhaka | SUN | Midfielder | £5.5m | 16.10 | GW8, GW9 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 15.74 | GW6, GW7, GW8 | — | — |

Squad cost: £99.2m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 22.34 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW6, GW8 |
| Branthwaite | EVE | Defender | £5.5m | 15.63 | GW6, GW7, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.26 | GW6, GW7, GW8, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 12.00 | GW8, GW9 | — | — |
| Furlong | IPS | Defender | £3.9m | 1.03 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.80 | GW6, GW7, GW8, GW9, GW10 | GW9 | — |
| Havertz | ARS | Forward | £7.6m | 18.89 | GW6, GW7, GW8, GW9, GW10 | — | GW10 |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.55 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.18 | GW6, GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.23 | GW6, GW7, GW8, GW9, GW10 | GW6 | GW7 |
| Semenyo | MCI | Midfielder | £8.4m | 21.19 | GW6, GW7, GW8, GW9, GW10 | GW7 | GW9 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.14 | GW6, GW7, GW8, GW9, GW10 | GW8 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 19.38 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Rogers | CHE | Midfielder | £7.7m | 17.69 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Branthwaite → Silva** (projected weighted XI+captain gain 1.93).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Branthwaite | Silva | £5.5m | £5.0m | £0.5m | 1.93 |
| Branthwaite | Truffert | £5.5m | £5.5m | £0.0m | 1.87 |
| Egan | Thomas | £4.1m | £4.0m | £0.1m | 1.01 |
| Egan | Davis | £4.1m | £4.0m | £0.1m | 0.74 |
| Egan | Giles | £4.1m | £4.0m | £0.1m | 0.56 |
| Branthwaite | Rúben | £5.5m | £5.5m | £0.0m | 0.32 |
| Egan | Diop | £4.1m | £4.0m | £0.1m | 0.29 |
| Horníček | Tzolakis | £5.0m | £4.6m | £0.4m | 0.27 |
| Egan | Dasilva | £4.1m | £4.0m | £0.1m | 0.24 |
| Bassey | Robinson | £4.5m | £4.5m | £0.0m | 0.10 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
