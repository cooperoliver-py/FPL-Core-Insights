# FPL predictions: 2026-2027, GW8

Last generated: 2026-10-20 05:10 UTC

Data commit: `13b3934e801013157d40b1df574e0b8a1b89e937`

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
| B.Fernandes | MUN | Midfielder | 5.90 | 6.23 | 5.72 | 5.64 | 5.97 | 23.62 | 2.00 | high | 5-GW avg pts 1.60; mins 90; xGI 0.26; current GWs 7; fixture Elo diff +41 |
| Palmer | CHE | Midfielder | 5.80 | 5.13 | 5.66 | 5.82 | 5.75 | 22.47 | 2.32 | high | 5-GW avg pts 3.60; mins 89; xGI 0.22; current GWs 7; fixture Elo diff +21 |
| Iwobi | FUL | Midfielder | 5.39 | 3.54 | 4.31 | 3.49 | 4.14 | 16.95 | 3.14 | high | 5-GW avg pts 5.00; mins 81; xGI 0.51; current GWs 7; fixture Elo diff -39 |
| Isak | LIV | Forward | 5.37 | 4.56 | 4.99 | 5.29 | 5.05 | 20.20 | 2.24 | high | 5-GW avg pts 6.40; mins 62; xGI 0.38; current GWs 7; fixture Elo diff +25 |
| Gabriel | ARS | Defender | 5.25 | 5.01 | 5.76 | 5.14 | 4.35 | 20.57 | 2.60 | high | 5-GW avg pts 4.40; mins 90; xGI 0.19; current GWs 7; fixture Elo diff +253 |
| Thiago | BRE | Forward | 5.19 | 5.15 | 4.83 | 5.07 | 4.24 | 19.79 | 2.54 | high | 5-GW avg pts 3.20; mins 90; xGI 0.46; current GWs 7; fixture Elo diff +53 |
| João Pedro | CHE | Forward | 5.17 | 4.56 | 4.81 | 5.17 | 4.86 | 19.65 | 2.49 | high | 5-GW avg pts 5.40; mins 68; xGI 0.28; current GWs 7; fixture Elo diff +21 |
| Saka | ARS | Midfielder | 4.89 | 4.43 | 5.97 | 4.53 | 4.01 | 19.24 | 2.00 | high | 5-GW avg pts 3.40; mins 88; xGI 0.69; current GWs 7; fixture Elo diff +253 |
| Rogers | CHE | Midfielder | 4.87 | 4.19 | 4.93 | 4.94 | 4.79 | 18.92 | 2.36 | high | 5-GW avg pts 5.40; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +21 |
| Murillo | NFO | Defender | 4.87 | 4.22 | 3.45 | 4.02 | 4.22 | 16.77 | 3.05 | high | 5-GW avg pts 4.40; mins 90; xGI 0.20; current GWs 7; fixture Elo diff -8 |
| Mbeumo | MUN | Midfielder | 4.86 | 4.64 | 4.93 | 4.85 | 4.86 | 19.29 | 2.47 | high | 5-GW avg pts 5.60; mins 90; xGI 0.43; current GWs 7; fixture Elo diff +41 |
| Ajer | BRE | Defender | 4.64 | 3.64 | 3.35 | 3.66 | 3.10 | 15.01 | 3.34 | high | 5-GW avg pts 3.80; mins 90; xGI 0.09; current GWs 7; fixture Elo diff +53 |
| Wirtz | LIV | Midfielder | 4.56 | 3.62 | 4.26 | 4.39 | 4.29 | 16.87 | 2.34 | high | 5-GW avg pts 3.80; mins 81; xGI 0.24; current GWs 7; fixture Elo diff +25 |
| Bassey | FUL | Defender | 4.54 | 2.68 | 3.33 | 2.46 | 3.23 | 13.28 | 2.95 | high | 5-GW avg pts 4.60; mins 90; xGI 0.07; current GWs 7; fixture Elo diff -39 |
| Rice | ARS | Midfielder | 4.45 | 4.05 | 5.36 | 4.13 | 3.51 | 17.39 | 2.38 | high | 5-GW avg pts 5.60; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +253 |
| Barcola | LIV | Midfielder | 4.34 | 3.22 | 4.26 | 4.18 | 4.33 | 16.17 | 2.02 | high | 5-GW avg pts 2.60; mins 69; xGI 0.24; current GWs 5; fixture Elo diff +25 |
| N.Williams | NFO | Defender | 4.32 | 3.66 | 2.85 | 3.54 | 3.58 | 14.50 | 2.90 | high | 5-GW avg pts 3.00; mins 90; xGI 0.25; current GWs 7; fixture Elo diff -8 |
| Mukiele | SUN | Defender | 4.31 | 4.50 | 4.01 | 3.55 | 4.43 | 16.71 | 3.09 | high | 5-GW avg pts 2.00; mins 90; xGI 0.23; current GWs 7; fixture Elo diff -62 |
| Stach | LEE | Midfielder | 4.30 | 3.67 | 4.33 | 3.97 | 5.03 | 16.86 | 2.81 | high | 5-GW avg pts 2.80; mins 89; xGI 0.33; current GWs 7; fixture Elo diff +22 |
| Richards | CRY | Defender | 4.30 | 4.55 | 3.77 | 5.03 | 4.76 | 17.79 | 3.63 | high | 5-GW avg pts 3.40; mins 90; xGI 0.04; current GWs 7; fixture Elo diff +60 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£98.9m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.57 | GW8, GW9, GW10, GW11, GW12 | GW10 | — |
| Richards | CRY | Defender | £4.9m | 17.79 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Khalaili | CRY | Defender | £5.0m | 17.25 | GW8, GW9, GW11, GW12 | — | — |
| Rúben | MCI | Defender | £5.5m | 16.71 | GW9, GW10, GW11 | — | — |
| Diop | IPS | Defender | £3.9m | 12.60 | Bench | — | — |
| Isak | LIV | Forward | £9.0m | 20.20 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Thiago | BRE | Forward | £7.8m | 19.79 | GW8, GW9, GW10, GW11, GW12 | — | GW9 |
| João Pedro | CHE | Forward | £7.9m | 19.65 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Donnarumma | MCI | Goalkeeper | £5.5m | 15.04 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Bentley | COV | Goalkeeper | £4.0m | 0.97 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £11.8m | 23.62 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW12 | GW10, GW11 |
| Palmer | CHE | Midfielder | £9.7m | 22.47 | GW8, GW9, GW10, GW11, GW12 | GW11 | GW8, GW12 |
| Iwobi | FUL | Midfielder | £5.4m | 16.95 | GW8, GW10 | — | — |
| Wharton | CRY | Midfielder | £5.4m | 16.69 | GW9, GW11, GW12 | — | — |
| Ampadu | LEE | Midfielder | £5.4m | 16.52 | GW8, GW10, GW12 | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 20.57 | GW8, GW9, GW10, GW11, GW12 | GW10 | GW8, GW11 |
| Branthwaite | EVE | Defender | £5.5m | 14.56 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.28 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Egan | HUL | Defender | £4.1m | 12.34 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.77 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.79 | GW8, GW9, GW10, GW11, GW12 | — | GW9 |
| Havertz | ARS | Forward | £7.5m | 15.44 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.31 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.06 | GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.68 | GW9, GW10, GW11, GW12 | — | — |
| B.Fernandes | MUN | Midfielder | £11.8m | 23.62 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW11, GW12 | GW10 |
| Rogers | CHE | Midfielder | £8.0m | 18.92 | GW8, GW9, GW10, GW11, GW12 | — | GW12 |
| Cherki | MCI | Midfielder | £8.0m | 12.76 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Gibbs-White | NFO | Midfielder | £7.9m | 6.23 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 0.00 | Bench | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Gibbs-White → Mbeumo** (projected weighted XI+captain gain 13.06).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Gibbs-White | Mbeumo | £7.9m | £7.8m | £0.3m | 13.06 |
| Semenyo | Mbeumo | £8.3m | £7.8m | £0.7m | 13.06 |
| Gibbs-White | Rice | £7.9m | £7.3m | £0.8m | 11.16 |
| Semenyo | Rice | £8.3m | £7.3m | £1.2m | 11.16 |
| Gibbs-White | Iwobi | £7.9m | £5.4m | £2.7m | 10.72 |
| Semenyo | Iwobi | £8.3m | £5.4m | £3.1m | 10.72 |
| Gibbs-White | Wirtz | £7.9m | £7.2m | £0.9m | 10.64 |
| Semenyo | Wirtz | £8.3m | £7.2m | £1.3m | 10.64 |
| Gibbs-White | Stach | £7.9m | £6.0m | £2.1m | 10.63 |
| Semenyo | Stach | £8.3m | £6.0m | £2.5m | 10.63 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
