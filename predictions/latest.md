# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-26 13:20 UTC

Data commit: `49bcf446efe16408ed9f297a2318daf7c9b7bf37`

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
| B.Fernandes | MUN | Midfielder | 5.78 | 5.25 | 5.52 | 5.03 | 5.25 | 21.58 | 1.81 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +76 |
| Gabriel | ARS | Defender | 5.55 | 4.89 | 5.55 | 4.49 | 6.82 | 21.62 | 2.70 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Gibbs-White | NFO | Midfielder | 5.50 | 4.45 | 6.67 | 5.17 | 4.81 | 21.35 | 2.67 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| Haaland | MCI | Forward | 5.26 | 7.91 | 5.31 | 6.17 | 6.01 | 24.56 | 1.57 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +144 |
| Cunha | MUN | Midfielder | 4.89 | 4.21 | 4.87 | 4.12 | 4.64 | 18.24 | 2.31 | high | 5-GW avg pts 5.20; mins 81; xGI 0.29; current GWs 5; fixture Elo diff +76 |
| Dewsbury-Hall | EVE | Midfielder | 4.89 | 4.04 | 3.05 | 3.91 | 4.99 | 16.69 | 2.53 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Mykolenko | EVE | Defender | 4.76 | 3.39 | 2.47 | 3.31 | 5.07 | 15.14 | 3.29 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Pickford | EVE | Goalkeeper | 4.75 | 3.29 | 2.49 | 3.21 | 5.20 | 15.07 | 2.74 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 5; fixture Elo diff +18 |
| Mbeumo | MUN | Midfielder | 4.67 | 4.38 | 4.77 | 4.38 | 4.59 | 18.24 | 2.31 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +76 |
| Saka | ARS | Midfielder | 4.54 | 4.27 | 4.54 | 4.14 | 6.14 | 18.59 | 1.96 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Tarkowski | EVE | Defender | 4.49 | 3.69 | 2.51 | 3.49 | 4.84 | 15.17 | 2.49 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Rogers | CHE | Midfielder | 4.46 | 4.29 | 4.43 | 4.19 | 4.29 | 17.36 | 2.26 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Branthwaite | EVE | Defender | 4.44 | 3.84 | 2.65 | 3.68 | 4.63 | 15.37 | 2.79 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Thiago | BRE | Forward | 4.43 | 4.77 | 5.54 | 5.21 | 4.75 | 19.65 | 2.52 | high | 5-GW avg pts 2.00; mins 88; xGI 0.66; current GWs 5; fixture Elo diff +31 |
| Barry | EVE | Forward | 4.43 | 4.07 | 2.39 | 3.80 | 4.51 | 15.37 | 2.74 | high | 5-GW avg pts 4.00; mins 83; xGI 0.73; current GWs 5; fixture Elo diff +18 |
| Murillo | NFO | Defender | 4.36 | 2.99 | 4.35 | 3.68 | 3.15 | 15.00 | 2.73 | high | 5-GW avg pts 4.60; mins 90; xGI 0.16; current GWs 5; fixture Elo diff -41 |
| Barnes | NEW | Midfielder | 4.31 | 3.52 | 4.10 | 4.08 | 4.24 | 16.16 | 2.65 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Iwobi | FUL | Midfielder | 4.30 | 4.69 | 4.16 | 2.97 | 3.23 | 15.87 | 2.94 | high | 5-GW avg pts 2.80; mins 82; xGI 0.32; current GWs 5; fixture Elo diff +95 |
| Garner | EVE | Midfielder | 4.30 | 4.07 | 2.95 | 3.92 | 4.26 | 15.62 | 2.60 | high | 5-GW avg pts 2.20; mins 66; xGI 0.07; current GWs 5; fixture Elo diff +18 |
| Wissa | NEW | Forward | 4.26 | 3.50 | 3.84 | 3.90 | 3.93 | 15.57 | 2.51 | high | 5-GW avg pts 3.00; mins 88; xGI 0.48; current GWs 5; fixture Elo diff +37 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.0m**. Current squad selling value: **£99.3m**. Total available funds: **£99.3m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.62 | GW6, GW7, GW8, GW9, GW10 | GW6, GW10 | GW8 |
| Silva | BOU | Defender | £5.0m | 17.24 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Van Hecke | TOT | Defender | £4.9m | 15.36 | GW7, GW8, GW9, GW10 | — | — |
| Mykolenko | EVE | Defender | £4.6m | 15.14 | GW6, GW10 | — | — |
| Giles | HUL | Defender | £4.0m | 12.29 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 24.56 | GW6, GW7, GW8, GW9, GW10 | GW7, GW9 | GW10 |
| Thiago | BRE | Forward | £7.8m | 19.65 | GW6, GW7, GW8, GW9, GW10 | — | GW9 |
| Salia | NEW | Forward | £4.5m | 0.45 | Bench | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 15.07 | GW6, GW9, GW10 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.29 | GW7, GW8 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.35 | GW6, GW7, GW8, GW9, GW10 | GW8 | GW6 |
| Cherki | MCI | Midfielder | £7.8m | 18.25 | GW6, GW7, GW8, GW9, GW10 | — | GW7 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.24 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Groß | BHA | Midfielder | £5.8m | 16.37 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 15.87 | GW6, GW7, GW8 | — | — |

Squad cost: £99.3m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.62 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW6, GW7, GW8 |
| Branthwaite | EVE | Defender | £5.5m | 15.37 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.95 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 11.98 | GW6, GW7, GW8, GW9 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.99 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.65 | GW6, GW7, GW8, GW9, GW10 | GW9 | — |
| Havertz | ARS | Forward | £7.6m | 11.55 | GW6, GW8, GW10 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.29 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.13 | GW6, GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 21.58 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7 | GW10 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.35 | GW6, GW7, GW8, GW9, GW10 | GW8 | GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.24 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Rogers | CHE | Midfielder | £7.7m | 17.36 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Semenyo | MCI | Midfielder | £8.4m | 12.50 | GW7, GW9, GW10 | — | — |

Squad cost: £99.3m.

## One-transfer recommendation

**Semenyo → Cherki** (projected weighted XI+captain gain 5.70).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Semenyo | Cherki | £8.4m | £7.8m | £0.6m | 5.70 |
| Semenyo | Cunha | £8.4m | £7.9m | £0.5m | 5.17 |
| Semenyo | Dewsbury-Hall | £8.4m | £6.6m | £1.8m | 3.61 |
| Havertz | Gonzalo | £7.6m | £6.0m | £1.6m | 3.57 |
| Havertz | Wissa | £7.6m | £6.2m | £1.4m | 3.54 |
| Havertz | Barry | £7.6m | £5.6m | £2.0m | 3.42 |
| Semenyo | Groß | £8.4m | £5.8m | £2.6m | 3.30 |
| Havertz | Evanilson | £7.6m | £6.0m | £1.6m | 3.20 |
| Semenyo | Gakpo | £8.4m | £7.2m | £1.2m | 3.17 |
| Semenyo | Barnes | £8.4m | £6.1m | £2.3m | 3.08 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
