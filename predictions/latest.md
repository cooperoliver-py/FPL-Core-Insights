# FPL predictions: 2026-2027, GW6

Last generated: 2026-10-04 19:47 UTC

Data commit: `56be5dec057296a4a571c83ab3c2d96b13b36432`

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
| B.Fernandes | MUN | Midfielder | 5.50 | 5.26 | 5.25 | 5.04 | 5.07 | 21.00 | 1.76 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +76 |
| Gabriel | ARS | Defender | 5.34 | 4.79 | 5.34 | 4.44 | 6.58 | 20.99 | 2.62 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Gibbs-White | NFO | Midfielder | 5.12 | 4.40 | 6.16 | 4.81 | 4.53 | 20.09 | 2.51 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| Haaland | MCI | Forward | 5.11 | 7.51 | 5.16 | 5.93 | 5.71 | 23.58 | 1.51 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +144 |
| Dewsbury-Hall | EVE | Midfielder | 4.84 | 4.03 | 3.20 | 3.96 | 4.94 | 16.76 | 2.54 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Pickford | EVE | Goalkeeper | 4.69 | 3.30 | 2.62 | 3.27 | 5.14 | 15.13 | 2.75 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 5; fixture Elo diff +18 |
| Cunha | MUN | Midfielder | 4.47 | 4.08 | 4.45 | 4.01 | 4.32 | 17.10 | 2.16 | high | 5-GW avg pts 5.20; mins 81; xGI 0.29; current GWs 5; fixture Elo diff +76 |
| Tarkowski | EVE | Defender | 4.47 | 3.72 | 2.65 | 3.54 | 4.81 | 15.30 | 2.47 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Mbeumo | MUN | Midfielder | 4.41 | 4.23 | 4.53 | 4.24 | 4.44 | 17.47 | 2.21 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +76 |
| Branthwaite | EVE | Defender | 4.40 | 3.89 | 2.79 | 3.73 | 4.79 | 15.62 | 2.84 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Botman | NEW | Defender | 4.36 | 3.38 | 3.84 | 3.98 | 3.85 | 15.56 | 3.11 | high | 5-GW avg pts 3.00; mins 90; xGI 0.05; current GWs 5; fixture Elo diff +37 |
| Murillo | NFO | Defender | 4.27 | 3.02 | 4.28 | 3.62 | 3.09 | 14.81 | 2.69 | high | 5-GW avg pts 4.60; mins 90; xGI 0.16; current GWs 5; fixture Elo diff -41 |
| Rogers | CHE | Midfielder | 4.23 | 4.09 | 4.20 | 3.97 | 4.09 | 16.51 | 2.14 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Silva | BOU | Defender | 4.23 | 5.39 | 3.99 | 4.95 | 5.05 | 18.77 | 3.75 | high | 5-GW avg pts 2.60; mins 90; xGI 0.23; current GWs 5; fixture Elo diff +88 |
| Thiago | BRE | Forward | 4.21 | 4.56 | 5.29 | 5.00 | 4.53 | 18.77 | 2.41 | high | 5-GW avg pts 2.00; mins 88; xGI 0.66; current GWs 5; fixture Elo diff +31 |
| Saka | ARS | Midfielder | 4.17 | 4.09 | 4.17 | 3.96 | 5.71 | 17.38 | 1.83 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Barry | EVE | Forward | 4.16 | 3.83 | 2.30 | 3.58 | 4.26 | 14.51 | 2.55 | high | 5-GW avg pts 4.00; mins 83; xGI 0.73; current GWs 5; fixture Elo diff +18 |
| Iwobi | FUL | Midfielder | 4.14 | 4.50 | 4.00 | 2.83 | 3.06 | 15.21 | 2.82 | high | 5-GW avg pts 2.80; mins 82; xGI 0.32; current GWs 5; fixture Elo diff +95 |
| Barnes | NEW | Midfielder | 4.09 | 3.33 | 3.92 | 3.85 | 4.06 | 15.35 | 2.52 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Cherki | MCI | Midfielder | 4.04 | 5.49 | 4.09 | 4.23 | 4.11 | 17.68 | 2.27 | high | 5-GW avg pts 6.80; mins 60; xGI 0.45; current GWs 5; fixture Elo diff +144 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.0m**. Current squad selling value: **£99.3m**. Total available funds: **£99.3m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 20.99 | GW6, GW7, GW8, GW9, GW10 | GW6, GW10 | GW8 |
| Silva | BOU | Defender | £5.0m | 18.77 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Branthwaite | EVE | Defender | £5.5m | 15.62 | GW6, GW7, GW9, GW10 | — | — |
| Botman | NEW | Defender | £5.0m | 15.56 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Muharemović | LEE | Defender | £5.0m | 14.94 | GW8, GW10 | — | — |
| Haaland | MCI | Forward | £15.6m | 23.58 | GW6, GW7, GW8, GW9, GW10 | GW7, GW9 | GW10 |
| Thiago | BRE | Forward | £7.8m | 18.77 | GW6, GW7, GW8, GW9, GW10 | — | GW9 |
| Walle Egeli | IPS | Forward | £4.5m | 0.63 | Bench | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 15.13 | GW6, GW9, GW10 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.69 | GW7, GW8 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 20.09 | GW6, GW7, GW8, GW9, GW10 | GW8 | GW6 |
| Cherki | MCI | Midfielder | £7.8m | 17.68 | GW6, GW7, GW8, GW9, GW10 | — | GW7 |
| Dewsbury-Hall | EVE | Midfielder | £6.6m | 16.76 | GW6, GW7, GW9, GW10 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 15.21 | GW6, GW7, GW8 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 14.55 | GW8, GW9 | — | — |

Squad cost: £99.2m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 20.99 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW6, GW7, GW8 |
| Branthwaite | EVE | Defender | £5.5m | 15.62 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.26 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 12.72 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.63 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 18.77 | GW6, GW7, GW8, GW9, GW10 | — | GW9 |
| Havertz | ARS | Forward | £7.6m | 10.89 | GW6, GW8, GW10 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.69 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 12.24 | GW6, GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 21.00 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7, GW9 | GW10 |
| Gibbs-White | NFO | Midfielder | £8.0m | 20.09 | GW6, GW7, GW8, GW9, GW10 | GW8 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 17.47 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Rogers | CHE | Midfielder | £7.7m | 16.51 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Semenyo | MCI | Midfielder | £8.4m | 11.53 | GW7, GW9 | — | — |

Squad cost: £99.3m.

## One-transfer recommendation

**Semenyo → Cherki** (projected weighted XI+captain gain 5.56).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Semenyo | Cherki | £8.4m | £7.8m | £0.6m | 5.56 |
| Semenyo | Cunha | £8.4m | £7.9m | £0.5m | 4.77 |
| Semenyo | Dewsbury-Hall | £8.4m | £6.6m | £1.8m | 4.44 |
| Semenyo | Scott | £8.4m | £6.1m | £2.3m | 3.66 |
| Semenyo | Anderson | £8.4m | £6.3m | £2.1m | 3.51 |
| Havertz | Gonzalo | £7.6m | £6.0m | £1.6m | 3.43 |
| Semenyo | Groß | £8.4m | £5.9m | £2.5m | 3.27 |
| Branthwaite | Silva | £5.5m | £5.0m | £0.5m | 3.27 |
| Semenyo | Barnes | £8.4m | £6.1m | £2.3m | 3.02 |
| Havertz | Wissa | £7.6m | £6.2m | £1.4m | 2.98 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
