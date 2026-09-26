# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-26 19:19 UTC

Data commit: `10cbf876f08e32fd67e2a5466fd1aa6da0393d28`

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
| B.Fernandes | MUN | Midfielder | 5.79 | 5.26 | 5.53 | 5.04 | 5.26 | 21.62 | 1.82 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +76 |
| Gibbs-White | NFO | Midfielder | 5.57 | 4.60 | 6.74 | 5.24 | 4.96 | 21.75 | 2.72 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| Gabriel | ARS | Defender | 5.46 | 4.90 | 5.46 | 4.50 | 6.73 | 21.42 | 2.68 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Haaland | MCI | Forward | 5.39 | 8.03 | 5.44 | 6.28 | 6.14 | 25.05 | 1.61 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +144 |
| Dewsbury-Hall | EVE | Midfielder | 5.12 | 4.25 | 3.28 | 4.14 | 5.20 | 17.59 | 2.66 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Mykolenko | EVE | Defender | 4.98 | 3.59 | 2.69 | 3.54 | 5.27 | 16.00 | 3.48 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Pickford | EVE | Goalkeeper | 4.97 | 3.50 | 2.72 | 3.43 | 5.41 | 15.94 | 2.90 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 5; fixture Elo diff +18 |
| Cunha | MUN | Midfielder | 4.87 | 4.21 | 4.85 | 4.12 | 4.62 | 18.19 | 2.30 | high | 5-GW avg pts 5.20; mins 81; xGI 0.29; current GWs 5; fixture Elo diff +76 |
| Tarkowski | EVE | Defender | 4.71 | 3.90 | 2.73 | 3.71 | 5.04 | 16.03 | 2.63 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Mbeumo | MUN | Midfielder | 4.66 | 4.39 | 4.76 | 4.39 | 4.59 | 18.24 | 2.31 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +76 |
| Rogers | CHE | Midfielder | 4.44 | 4.26 | 4.41 | 4.17 | 4.26 | 17.27 | 2.24 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Thiago | BRE | Forward | 4.43 | 4.77 | 5.54 | 5.20 | 4.74 | 19.64 | 2.52 | high | 5-GW avg pts 2.00; mins 88; xGI 0.66; current GWs 5; fixture Elo diff +31 |
| Saka | ARS | Midfielder | 4.42 | 4.26 | 4.42 | 4.13 | 6.02 | 18.29 | 1.93 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Branthwaite | EVE | Defender | 4.41 | 3.82 | 2.64 | 3.65 | 4.78 | 15.38 | 2.80 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Barry | EVE | Forward | 4.40 | 4.02 | 2.38 | 3.77 | 4.46 | 15.24 | 2.72 | high | 5-GW avg pts 4.00; mins 83; xGI 0.73; current GWs 5; fixture Elo diff +18 |
| Murillo | NFO | Defender | 4.33 | 2.99 | 4.32 | 3.65 | 3.15 | 14.92 | 2.71 | high | 5-GW avg pts 4.60; mins 90; xGI 0.16; current GWs 5; fixture Elo diff -41 |
| Iwobi | FUL | Midfielder | 4.30 | 4.69 | 4.16 | 2.97 | 3.23 | 15.87 | 2.94 | high | 5-GW avg pts 2.80; mins 82; xGI 0.32; current GWs 5; fixture Elo diff +95 |
| Groß | BHA | Midfielder | 4.29 | 4.58 | 3.78 | 3.64 | 4.49 | 16.67 | 2.87 | high | 5-GW avg pts 9.40; mins 90; xGI 0.53; current GWs 5; fixture Elo diff -10 |
| Barnes | NEW | Midfielder | 4.26 | 3.51 | 4.10 | 4.06 | 4.23 | 16.08 | 2.64 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Garner | EVE | Midfielder | 4.17 | 4.01 | 2.91 | 3.88 | 4.11 | 15.29 | 2.55 | high | 5-GW avg pts 2.20; mins 66; xGI 0.07; current GWs 5; fixture Elo diff +18 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.0m**. Current squad selling value: **£99.3m**. Total available funds: **£99.3m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.42 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW6 |
| Silva | BOU | Defender | £5.0m | 17.28 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Mykolenko | EVE | Defender | £4.6m | 16.00 | GW6, GW10 | — | — |
| Van Hecke | TOT | Defender | £4.9m | 15.32 | GW7, GW8, GW9, GW10 | — | — |
| Davis | IPS | Defender | £4.0m | 13.67 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 25.05 | GW6, GW7, GW8, GW9, GW10 | GW7, GW9 | GW10 |
| Thiago | BRE | Forward | £7.8m | 19.64 | GW6, GW7, GW8, GW9, GW10 | — | GW8 |
| Gonzalo | FUL | Forward | £6.0m | 15.53 | GW6, GW7, GW8, GW10 | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 15.94 | GW6, GW7, GW9, GW10 | — | — |
| Kelleher | BRE | Goalkeeper | £5.0m | 13.35 | GW8 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.75 | GW6, GW7, GW8, GW9, GW10 | GW6, GW8 | GW9 |
| Cherki | MCI | Midfielder | £7.8m | 18.25 | GW6, GW7, GW8, GW9, GW10 | — | GW7 |
| Dewsbury-Hall | EVE | Midfielder | £6.6m | 17.59 | GW6, GW7, GW9, GW10 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 15.87 | GW6, GW7, GW8 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 14.39 | GW8, GW9 | — | — |

Squad cost: £99.2m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.42 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW7 |
| Branthwaite | EVE | Defender | £5.5m | 15.38 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.91 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 12.18 | GW6, GW7, GW8, GW9 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.99 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.64 | GW6, GW7, GW8, GW9, GW10 | — | GW8, GW9 |
| Havertz | ARS | Forward | £7.6m | 11.40 | GW6, GW8, GW10 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.29 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 12.81 | GW6, GW9, GW10 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.75 | GW6, GW7, GW8, GW9, GW10 | GW8, GW9 | GW6 |
| B.Fernandes | MUN | Midfielder | £11.9m | 21.62 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7 | GW10 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.24 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Rogers | CHE | Midfielder | £7.7m | 17.27 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Semenyo | MCI | Midfielder | £8.4m | 12.48 | GW7, GW9, GW10 | — | — |

Squad cost: £99.3m.

## One-transfer recommendation

**Semenyo → Cherki** (projected weighted XI+captain gain 5.79).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Semenyo | Cherki | £8.4m | £7.8m | £0.6m | 5.79 |
| Semenyo | Cunha | £8.4m | £7.9m | £0.5m | 5.22 |
| Semenyo | Dewsbury-Hall | £8.4m | £6.6m | £1.8m | 4.61 |
| Semenyo | Groß | £8.4m | £5.8m | £2.6m | 3.70 |
| Havertz | Gonzalo | £7.6m | £6.0m | £1.6m | 3.68 |
| Havertz | Wissa | £7.6m | £6.2m | £1.4m | 3.52 |
| Havertz | Barry | £7.6m | £5.6m | £2.0m | 3.48 |
| Havertz | Evanilson | £7.6m | £6.0m | £1.6m | 3.38 |
| Semenyo | Gakpo | £8.4m | £7.2m | £1.2m | 3.22 |
| Semenyo | Schade | £8.4m | £6.2m | £2.2m | 3.13 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
