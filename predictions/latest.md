# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-21 15:17 UTC

Data commit: `4e7f1a719b2bb2a423ba1cb14a067ec4964e590d`

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

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW6 player forecasts

| Player | Club | Pos | GW6 | GW7 | GW8 | GW9 | GW10 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gibbs-White | NFO | Midfielder | 7.15 | 3.62 | 9.54 | 6.51 | 4.70 | 25.42 | 3.18 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| B.Fernandes | MUN | Midfielder | 6.99 | 7.29 | 6.17 | 6.76 | 6.11 | 26.89 | 2.24 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +76 |
| Gabriel | ARS | Defender | 6.22 | 6.09 | 6.02 | 5.41 | 6.98 | 24.48 | 3.06 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Mbeumo | MUN | Midfielder | 5.63 | 5.93 | 5.35 | 5.71 | 5.34 | 22.45 | 2.84 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +76 |
| Havertz | ARS | Forward | 5.33 | 5.17 | 5.30 | 4.86 | 5.99 | 21.23 | 2.79 | high | 5-GW avg pts 3.80; mins 87; xGI 0.41; current GWs 5; fixture Elo diff +291 |
| Cunha | MUN | Midfielder | 5.21 | 5.03 | 5.07 | 4.95 | 5.03 | 20.27 | 2.57 | high | 5-GW avg pts 5.20; mins 81; xGI 0.29; current GWs 5; fixture Elo diff +76 |
| Saka | ARS | Midfielder | 5.17 | 4.94 | 5.13 | 4.84 | 6.38 | 20.93 | 2.20 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Botman | NEW | Defender | 5.10 | 3.43 | 3.76 | 3.78 | 3.80 | 16.11 | 3.22 | high | 5-GW avg pts 3.00; mins 90; xGI 0.05; current GWs 5; fixture Elo diff +37 |
| Barnes | NEW | Midfielder | 5.00 | 3.46 | 4.09 | 4.08 | 4.25 | 16.80 | 2.75 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Haaland | MCI | Forward | 4.99 | 7.55 | 4.99 | 5.40 | 5.83 | 23.05 | 1.48 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +144 |
| Palmer | CHE | Midfielder | 4.99 | 5.02 | 5.05 | 4.76 | 5.01 | 19.88 | 2.05 | high | 5-GW avg pts 5.60; mins 88; xGI 0.42; current GWs 5; fixture Elo diff +10 |
| Semenyo | MCI | Midfielder | 4.93 | 7.80 | 4.93 | 5.20 | 5.96 | 23.11 | 2.75 | high | 5-GW avg pts 6.60; mins 90; xGI 0.30; current GWs 5; fixture Elo diff +144 |
| Cherki | MCI | Midfielder | 4.91 | 6.54 | 4.91 | 5.24 | 5.40 | 21.64 | 2.77 | high | 5-GW avg pts 6.80; mins 60; xGI 0.45; current GWs 5; fixture Elo diff +144 |
| Dewsbury-Hall | EVE | Midfielder | 4.91 | 4.74 | 2.81 | 4.31 | 5.36 | 17.65 | 2.67 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Rogers | CHE | Midfielder | 4.84 | 5.03 | 4.95 | 4.58 | 5.10 | 19.60 | 2.55 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Tarkowski | EVE | Defender | 4.81 | 3.83 | 2.68 | 3.74 | 5.06 | 16.05 | 2.63 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Thiago | BRE | Forward | 4.69 | 4.75 | 6.07 | 5.37 | 5.26 | 20.74 | 2.66 | high | 5-GW avg pts 2.00; mins 88; xGI 0.66; current GWs 5; fixture Elo diff +31 |
| Wissa | NEW | Forward | 4.62 | 3.65 | 4.08 | 4.04 | 4.15 | 16.48 | 2.66 | high | 5-GW avg pts 3.00; mins 88; xGI 0.48; current GWs 5; fixture Elo diff +37 |
| Branthwaite | EVE | Defender | 4.57 | 3.96 | 2.70 | 3.89 | 4.76 | 15.86 | 2.88 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Murillo | NFO | Defender | 4.37 | 2.67 | 4.97 | 4.02 | 3.22 | 15.49 | 2.82 | high | 5-GW avg pts 4.60; mins 90; xGI 0.16; current GWs 5; fixture Elo diff -41 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.0m**. Current squad selling value: **£99.4m**. Total available funds: **£99.4m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 24.48 | GW6, GW7, GW8, GW9, GW10 | GW10 | — |
| Silva | BOU | Defender | £5.0m | 16.71 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Robinson | FUL | Defender | £4.5m | 14.95 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Kipré | IPS | Defender | £3.9m | 0.84 | Bench | — | — |
| Davies | TOT | Defender | £3.9m | 0.59 | Bench | — | — |
| Havertz | ARS | Forward | £7.6m | 21.23 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Thiago | BRE | Forward | £7.8m | 20.74 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Danns | LIV | Forward | £4.5m | 0.42 | Bench | — | — |
| Raya | ARS | Goalkeeper | £6.1m | 16.40 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Matthews | CRY | Goalkeeper | £4.0m | 0.42 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 26.89 | GW6, GW7, GW8, GW9, GW10 | GW9 | GW6, GW7, GW8, GW10 |
| Gibbs-White | NFO | Midfielder | £8.0m | 25.42 | GW6, GW7, GW8, GW9, GW10 | GW6, GW8 | GW9 |
| Semenyo | MCI | Midfielder | £8.4m | 23.11 | GW6, GW7, GW8, GW9, GW10 | GW7 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 22.45 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Cherki | MCI | Midfielder | £7.8m | 21.64 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.4m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 24.48 | GW6, GW7, GW8, GW9, GW10 | GW10 | — |
| Branthwaite | EVE | Defender | £5.5m | 15.86 | GW6, GW7, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.17 | GW6, GW7, GW8, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 10.67 | GW8, GW9 | — | — |
| Furlong | IPS | Defender | £3.9m | 1.16 | Bench | — | — |
| Havertz | ARS | Forward | £7.6m | 21.23 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Thiago | BRE | Forward | £7.8m | 20.74 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.22 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.13 | GW6, GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 26.89 | GW6, GW7, GW8, GW9, GW10 | GW9 | GW6, GW7, GW8, GW10 |
| Gibbs-White | NFO | Midfielder | £8.0m | 25.42 | GW6, GW7, GW8, GW9, GW10 | GW6, GW8 | GW9 |
| Semenyo | MCI | Midfielder | £8.4m | 23.11 | GW6, GW7, GW8, GW9, GW10 | GW7 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 22.45 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Rogers | CHE | Midfielder | £7.7m | 19.60 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Branthwaite → Truffert** (projected weighted XI+captain gain 1.12).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Branthwaite | Truffert | £5.5m | £5.5m | £0.0m | 1.12 |
| Egan | Diop | £4.1m | £4.0m | £0.1m | 0.88 |
| Egan | Davis | £4.1m | £4.0m | £0.1m | 0.83 |
| Branthwaite | Silva | £5.5m | £5.0m | £0.5m | 0.78 |
| Egan | Thomas | £4.1m | £4.0m | £0.1m | 0.62 |
| Bassey | Robinson | £4.5m | £4.5m | £0.0m | 0.53 |
| Egan | O'Shea | £4.1m | £4.0m | £0.1m | 0.44 |
| Egan | Giles | £4.1m | £4.0m | £0.1m | 0.30 |
| Egan | Dasilva | £4.1m | £4.0m | £0.1m | 0.24 |
| Branthwaite | Botman | £5.5m | £5.0m | £0.5m | 0.18 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
