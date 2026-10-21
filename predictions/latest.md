# FPL predictions: 2026-2027, GW8

Last generated: 2026-10-21 20:19 UTC

Data commit: `0c5bc558d79dbaa3f636d77276f9ea733f00f43f`

## Data freshness

All scheduled Premier League fixtures before GW8 are complete.

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
| 7 | 1.190 | 2.075 | 0.708 | 4.40 | 1.80 | 81 | 59 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW8 player forecasts

| Player | Club | Pos | GW8 | GW9 | GW10 | GW11 | GW12 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Isak | LIV | Forward | 6.01 | 4.38 | 5.12 | 5.97 | 5.12 | 21.30 | 2.37 | high | 5-GW avg pts 6.40; mins 62; xGI 0.38; current GWs 7; fixture Elo diff +25 |
| B.Fernandes | MUN | Midfielder | 5.94 | 5.43 | 5.80 | 5.34 | 5.94 | 22.77 | 1.93 | high | 5-GW avg pts 1.60; mins 90; xGI 0.26; current GWs 7; fixture Elo diff +41 |
| Iwobi | FUL | Midfielder | 5.89 | 3.51 | 4.35 | 3.31 | 3.79 | 17.11 | 3.17 | high | 5-GW avg pts 5.00; mins 81; xGI 0.51; current GWs 7; fixture Elo diff -39 |
| Thiago | BRE | Forward | 5.56 | 4.95 | 4.58 | 4.80 | 3.99 | 19.43 | 2.49 | high | 5-GW avg pts 3.20; mins 90; xGI 0.46; current GWs 7; fixture Elo diff +53 |
| Wirtz | LIV | Midfielder | 5.52 | 3.96 | 4.95 | 5.48 | 4.95 | 19.85 | 2.76 | high | 5-GW avg pts 3.80; mins 81; xGI 0.24; current GWs 7; fixture Elo diff +25 |
| Gibbs-White | NFO | Midfielder | 5.40 | 3.83 | 3.90 | 3.62 | 4.54 | 17.23 | 2.18 | high | 5-GW avg pts 3.00; mins 72; xGI 0.50; current GWs 7; fixture Elo diff -8 |
| Rice | ARS | Midfielder | 5.34 | 4.97 | 6.10 | 5.14 | 4.57 | 21.03 | 2.88 | high | 5-GW avg pts 5.60; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +253 |
| João Pedro | CHE | Forward | 5.21 | 4.46 | 4.54 | 5.24 | 4.56 | 19.27 | 2.44 | high | 5-GW avg pts 5.40; mins 68; xGI 0.28; current GWs 7; fixture Elo diff +21 |
| Palmer | CHE | Midfielder | 5.11 | 4.46 | 5.14 | 5.14 | 5.11 | 19.90 | 2.05 | high | 5-GW avg pts 3.60; mins 89; xGI 0.22; current GWs 7; fixture Elo diff +21 |
| N.Williams | NFO | Defender | 5.08 | 3.65 | 2.96 | 3.33 | 3.80 | 15.34 | 3.07 | high | 5-GW avg pts 3.00; mins 90; xGI 0.25; current GWs 7; fixture Elo diff -8 |
| Gabriel | ARS | Defender | 5.04 | 4.75 | 5.62 | 5.01 | 4.28 | 19.88 | 2.52 | high | 5-GW avg pts 4.40; mins 90; xGI 0.19; current GWs 7; fixture Elo diff +253 |
| Murillo | NFO | Defender | 4.97 | 3.94 | 2.98 | 3.56 | 3.96 | 15.76 | 2.87 | high | 5-GW avg pts 4.40; mins 90; xGI 0.20; current GWs 7; fixture Elo diff -8 |
| Barcola | LIV | Midfielder | 4.88 | 3.09 | 4.67 | 4.83 | 4.67 | 17.58 | 2.20 | high | 5-GW avg pts 2.60; mins 69; xGI 0.24; current GWs 5; fixture Elo diff +25 |
| Rogers | CHE | Midfielder | 4.86 | 4.22 | 4.71 | 4.84 | 4.64 | 18.60 | 2.32 | high | 5-GW avg pts 5.40; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +21 |
| Ødegaard | ARS | Midfielder | 4.68 | 4.21 | 4.83 | 4.26 | 3.94 | 17.67 | 2.60 | high | 5-GW avg pts 3.80; mins 82; xGI 0.61; current GWs 7; fixture Elo diff +253 |
| Haaland | MCI | Forward | 4.65 | 5.44 | 5.76 | 6.24 | 3.63 | 20.69 | 1.32 | high | 5-GW avg pts 8.60; mins 88; xGI 1.01; current GWs 7; fixture Elo diff +78 |
| Saka | ARS | Midfielder | 4.62 | 4.32 | 5.81 | 4.39 | 3.90 | 18.57 | 1.93 | high | 5-GW avg pts 3.40; mins 88; xGI 0.69; current GWs 7; fixture Elo diff +253 |
| McAtee | NFO | Midfielder | 4.55 | 3.74 | 3.01 | 3.37 | 3.80 | 14.96 | 2.72 | high | 5-GW avg pts 2.60; mins 85; xGI 0.26; current GWs 7; fixture Elo diff -8 |
| Stach | LEE | Midfielder | 4.47 | 3.62 | 4.39 | 3.96 | 4.79 | 16.88 | 2.81 | high | 5-GW avg pts 2.80; mins 89; xGI 0.33; current GWs 7; fixture Elo diff +22 |
| Bassey | FUL | Defender | 4.45 | 2.67 | 3.43 | 2.40 | 3.08 | 13.12 | 2.92 | high | 5-GW avg pts 4.60; mins 90; xGI 0.07; current GWs 7; fixture Elo diff -39 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£98.9m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.2m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.88 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Van Hecke | TOT | Defender | £4.9m | 17.22 | GW9, GW10, GW11, GW12 | — | — |
| Jacquet | LIV | Defender | £5.1m | 16.34 | GW8, GW10, GW11, GW12 | — | — |
| Richards | CRY | Defender | £4.9m | 16.29 | GW9, GW11, GW12 | — | — |
| N.Williams | NFO | Defender | £5.0m | 15.34 | GW8 | — | — |
| Isak | LIV | Forward | £9.0m | 21.30 | GW8, GW9, GW10, GW11, GW12 | GW8, GW11 | GW12 |
| Thiago | BRE | Forward | £7.8m | 19.43 | GW8, GW9, GW10, GW11 | — | — |
| João Pedro | CHE | Forward | £7.9m | 19.27 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Kinsky | TOT | Goalkeeper | £4.5m | 14.03 | GW9, GW10, GW11, GW12 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.19 | GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £11.8m | 22.77 | GW8, GW9, GW10, GW11, GW12 | GW9, GW12 | GW8, GW10 |
| Rice | ARS | Midfielder | £7.3m | 21.03 | GW8, GW9, GW10, GW11, GW12 | GW10 | GW9 |
| Wirtz | LIV | Midfielder | £7.2m | 19.85 | GW8, GW9, GW10, GW11, GW12 | — | GW11 |
| Iwobi | FUL | Midfielder | £5.4m | 17.11 | GW8, GW10 | — | — |
| E.Le Fée | SUN | Midfielder | £5.7m | 16.02 | GW9, GW12 | — | — |

Squad cost: £98.9m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.88 | GW8, GW9, GW10, GW11, GW12 | — | GW10, GW11 |
| Branthwaite | EVE | Defender | £5.5m | 14.33 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.12 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Egan | HUL | Defender | £4.1m | 11.09 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.77 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.43 | GW8, GW9, GW10, GW11, GW12 | — | GW8, GW9 |
| Havertz | ARS | Forward | £7.5m | 15.59 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.43 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.19 | GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.76 | GW9, GW10, GW11, GW12 | — | — |
| B.Fernandes | MUN | Midfielder | £11.8m | 22.77 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW10, GW11, GW12 | — |
| Rogers | CHE | Midfielder | £8.0m | 18.60 | GW8, GW9, GW10, GW11, GW12 | — | GW12 |
| Gibbs-White | NFO | Midfielder | £7.9m | 17.23 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Cherki | MCI | Midfielder | £8.0m | 13.35 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 0.00 | Bench | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Semenyo → Rice** (projected weighted XI+captain gain 11.37).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Semenyo | Rice | £8.3m | £7.3m | £1.2m | 11.37 |
| Semenyo | Wirtz | £8.3m | £7.2m | £1.3m | 10.04 |
| Semenyo | Doku | £8.3m | £7.5m | £1.0m | 8.49 |
| Cherki | Rice | £7.9m | £7.3m | £0.8m | 7.92 |
| Semenyo | Ødegaard | £8.3m | £6.8m | £1.7m | 7.77 |
| Semenyo | Barcola | £8.3m | £8.0m | £0.5m | 7.68 |
| Semenyo | Iwobi | £8.3m | £5.4m | £3.1m | 7.21 |
| Semenyo | Stach | £8.3m | £6.0m | £2.5m | 6.98 |
| Cherki | Wirtz | £7.9m | £7.2m | £0.9m | 6.59 |
| Semenyo | Mbeumo | £8.3m | £7.8m | £0.7m | 6.54 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
