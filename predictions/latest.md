# FPL predictions: 2026-2027, GW8

Last generated: 2026-10-20 13:48 UTC

Data commit: `bc3335bca96caae08ef2057526498c7c7e0ea1f6`

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

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW8 player forecasts

| Player | Club | Pos | GW8 | GW9 | GW10 | GW11 | GW12 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 5.81 | 6.12 | 5.63 | 5.53 | 5.88 | 23.23 | 1.97 | high | 5-GW avg pts 1.60; mins 90; xGI 0.26; current GWs 7; fixture Elo diff +41 |
| Palmer | CHE | Midfielder | 5.62 | 4.94 | 5.52 | 5.64 | 5.56 | 21.76 | 2.24 | high | 5-GW avg pts 3.60; mins 89; xGI 0.22; current GWs 7; fixture Elo diff +21 |
| Isak | LIV | Forward | 5.53 | 4.64 | 5.02 | 5.45 | 5.08 | 20.59 | 2.29 | high | 5-GW avg pts 6.40; mins 62; xGI 0.38; current GWs 7; fixture Elo diff +25 |
| João Pedro | CHE | Forward | 5.24 | 4.62 | 4.83 | 5.24 | 4.86 | 19.85 | 2.51 | high | 5-GW avg pts 5.40; mins 68; xGI 0.28; current GWs 7; fixture Elo diff +21 |
| Gabriel | ARS | Defender | 5.06 | 4.90 | 5.64 | 5.01 | 4.27 | 20.05 | 2.54 | high | 5-GW avg pts 4.40; mins 90; xGI 0.19; current GWs 7; fixture Elo diff +253 |
| Iwobi | FUL | Midfielder | 5.05 | 3.18 | 3.79 | 3.09 | 3.61 | 15.27 | 2.83 | high | 5-GW avg pts 5.00; mins 81; xGI 0.51; current GWs 7; fixture Elo diff -39 |
| Thiago | BRE | Forward | 4.95 | 4.74 | 4.51 | 4.66 | 3.92 | 18.45 | 2.37 | high | 5-GW avg pts 3.20; mins 90; xGI 0.46; current GWs 7; fixture Elo diff +53 |
| Wirtz | LIV | Midfielder | 4.95 | 4.07 | 4.36 | 4.78 | 4.38 | 18.07 | 2.51 | high | 5-GW avg pts 3.80; mins 81; xGI 0.24; current GWs 7; fixture Elo diff +25 |
| Murillo | NFO | Defender | 4.93 | 4.38 | 3.70 | 4.18 | 4.39 | 17.39 | 3.16 | high | 5-GW avg pts 4.40; mins 90; xGI 0.20; current GWs 7; fixture Elo diff -8 |
| Saka | ARS | Midfielder | 4.86 | 4.47 | 5.93 | 4.47 | 4.21 | 19.28 | 2.01 | high | 5-GW avg pts 3.40; mins 88; xGI 0.69; current GWs 7; fixture Elo diff +253 |
| Rogers | CHE | Midfielder | 4.83 | 4.36 | 4.83 | 4.90 | 4.82 | 18.95 | 2.37 | high | 5-GW avg pts 5.40; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +21 |
| Ajer | BRE | Defender | 4.65 | 3.70 | 3.41 | 3.69 | 3.10 | 15.16 | 3.37 | high | 5-GW avg pts 3.80; mins 90; xGI 0.09; current GWs 7; fixture Elo diff +53 |
| Bassey | FUL | Defender | 4.59 | 2.65 | 3.34 | 2.42 | 3.18 | 13.25 | 2.94 | high | 5-GW avg pts 4.60; mins 90; xGI 0.07; current GWs 7; fixture Elo diff -39 |
| Barcola | LIV | Midfielder | 4.56 | 3.30 | 4.45 | 4.41 | 4.52 | 16.89 | 2.11 | high | 5-GW avg pts 2.60; mins 69; xGI 0.24; current GWs 5; fixture Elo diff +25 |
| Mbeumo | MUN | Midfielder | 4.44 | 4.14 | 4.49 | 4.44 | 4.35 | 17.48 | 2.24 | high | 5-GW avg pts 5.60; mins 90; xGI 0.43; current GWs 7; fixture Elo diff +41 |
| Richards | CRY | Defender | 4.38 | 4.54 | 3.81 | 5.11 | 4.83 | 17.99 | 3.67 | high | 5-GW avg pts 3.40; mins 90; xGI 0.04; current GWs 7; fixture Elo diff +60 |
| Mukiele | SUN | Defender | 4.38 | 4.72 | 4.01 | 3.56 | 4.50 | 17.03 | 3.15 | high | 5-GW avg pts 2.00; mins 90; xGI 0.23; current GWs 7; fixture Elo diff -62 |
| Rice | ARS | Midfielder | 4.33 | 3.94 | 5.23 | 4.02 | 3.48 | 16.97 | 2.32 | high | 5-GW avg pts 5.60; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +253 |
| Khalaili | CRY | Defender | 4.20 | 4.36 | 3.81 | 4.73 | 4.53 | 17.19 | 3.44 | high | 5-GW avg pts 3.60; mins 90; xGI 0.32; current GWs 7; fixture Elo diff +60 |
| Ampadu | LEE | Midfielder | 4.19 | 3.60 | 4.24 | 3.67 | 4.99 | 16.38 | 3.03 | high | 5-GW avg pts 3.20; mins 90; xGI 0.06; current GWs 7; fixture Elo diff +22 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£98.9m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.05 | GW8, GW9, GW10, GW11, GW12 | GW10 | — |
| Richards | CRY | Defender | £4.9m | 17.99 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Van Hecke | TOT | Defender | £4.9m | 16.53 | GW9, GW10, GW11, GW12 | — | — |
| Rúben | MCI | Defender | £5.5m | 16.19 | GW9, GW10, GW11 | — | — |
| Ajer | BRE | Defender | £4.5m | 15.16 | GW8 | — | — |
| Isak | LIV | Forward | £9.0m | 20.59 | GW8, GW9, GW10, GW11, GW12 | — | — |
| João Pedro | CHE | Forward | £7.9m | 19.85 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Kusi-Asare | FUL | Forward | £4.4m | 0.28 | Bench | — | — |
| Donnarumma | MCI | Goalkeeper | £5.5m | 15.03 | GW9, GW10, GW11, GW12 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.12 | GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £11.8m | 23.23 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW12 | GW10, GW11 |
| Palmer | CHE | Midfielder | £9.7m | 21.76 | GW8, GW9, GW10, GW11, GW12 | GW11 | GW8, GW9, GW12 |
| Rogers | CHE | Midfielder | £8.0m | 18.95 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Wharton | CRY | Midfielder | £5.4m | 16.71 | GW8, GW9, GW11, GW12 | — | — |
| Ampadu | LEE | Midfielder | £5.4m | 16.38 | GW8, GW10, GW12 | — | — |

Squad cost: £99.3m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.05 | GW8, GW9, GW10, GW11, GW12 | GW10 | GW8, GW9, GW11 |
| Branthwaite | EVE | Defender | £5.5m | 14.53 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.25 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Egan | HUL | Defender | £4.1m | 12.66 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.77 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 18.45 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Havertz | ARS | Forward | £7.5m | 14.98 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.31 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.12 | GW8, GW10 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.62 | GW9, GW11, GW12 | — | — |
| B.Fernandes | MUN | Midfielder | £11.8m | 23.23 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW11, GW12 | GW10 |
| Rogers | CHE | Midfielder | £8.0m | 18.95 | GW8, GW9, GW10, GW11, GW12 | — | GW12 |
| Cherki | MCI | Midfielder | £8.0m | 12.76 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Gibbs-White | NFO | Midfielder | £7.9m | 6.23 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 0.00 | Bench | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Gibbs-White → Wirtz** (projected weighted XI+captain gain 11.84).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Gibbs-White | Wirtz | £7.9m | £7.2m | £0.9m | 11.84 |
| Semenyo | Wirtz | £8.3m | £7.2m | £1.3m | 11.84 |
| Gibbs-White | Mbeumo | £7.9m | £7.8m | £0.3m | 11.25 |
| Semenyo | Mbeumo | £8.3m | £7.8m | £0.7m | 11.25 |
| Gibbs-White | Rice | £7.9m | £7.3m | £0.8m | 10.74 |
| Semenyo | Rice | £8.3m | £7.3m | £1.2m | 10.74 |
| Gibbs-White | Barcola | £7.9m | £8.0m | £0.1m | 10.66 |
| Semenyo | Barcola | £8.3m | £8.0m | £0.5m | 10.66 |
| Gibbs-White | Wharton | £7.9m | £5.4m | £2.7m | 10.48 |
| Semenyo | Wharton | £8.3m | £5.4m | £3.1m | 10.48 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
