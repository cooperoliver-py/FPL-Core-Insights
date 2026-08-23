# FPL predictions: 2026-2027, GW2

Last generated: 2026-08-23 02:10 UTC

Data commit: `7c461ea1fb64a8287f69b4da0abe6adadd2922c4`

Forecasts use only the canonical 2025/26 `By Gameweek` player data, strictly lagged 3/5-GW form, and target Premier League fixtures. Five-GW weights are [1.0, 0.9, 0.8, 0.7, 0.6]; price and availability are held constant.

## Held-out evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.966 | 1.912 | 0.695 |
| Rolling points (5 GW) | 1.033 | 2.129 | 0.683 |
| Lagged FPL ep_next | 1.008 | 2.116 | 0.671 |

## Top GW2 player forecasts

| Player | Club | Pos | GW2 | GW3 | GW4 | GW5 | GW6 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 6.13 | 5.92 | 3.93 | 5.77 | 6.16 | 22.34 | 1.86 | high | 5-GW avg pts 7.20; mins 90; xGI 0.62; fixture Elo diff +109 |
| Szoboszlai | LIV | Midfielder | 5.38 | 5.47 | 5.23 | 4.04 | 3.83 | 19.62 | 2.80 | high | 5-GW avg pts 5.40; mins 90; xGI 0.45; fixture Elo diff +82 |
| Mbeumo | MUN | Midfielder | 4.74 | 3.98 | 3.93 | 3.98 | 4.66 | 17.05 | 2.13 | high | 5-GW avg pts 4.40; mins 63; xGI 0.89; fixture Elo diff +109 |
| Palmer | CHE | Midfielder | 4.51 | 1.97 | 4.44 | 4.40 | 3.68 | 15.12 | 1.59 | high | 5-GW avg pts 2.40; mins 72; xGI 0.34; fixture Elo diff -25 |
| Haaland | MCI | Forward | 4.42 | 5.04 | 4.01 | 4.95 | 4.01 | 18.04 | 1.16 | high | 5-GW avg pts 5.40; mins 54; xGI 0.52; fixture Elo diff +165 |
| Enzo | CHE | Midfielder | 4.24 | 1.89 | 4.32 | 4.07 | 3.51 | 14.35 | 2.05 | high | 5-GW avg pts 4.80; mins 72; xGI 0.27; fixture Elo diff -25 |
| Maguire | MUN | Defender | 4.17 | 3.21 | 2.57 | 3.21 | 3.57 | 13.50 | 2.70 | high | 5-GW avg pts 5.40; mins 90; xGI 0.12; fixture Elo diff +109 |
| Thiago | BRE | Forward | 4.05 | 4.55 | 3.58 | 4.53 | 2.97 | 15.96 | 1.99 | high | 5-GW avg pts 2.60; mins 90; xGI 0.31; fixture Elo diff +6 |
| Virgil | LIV | Defender | 3.96 | 3.86 | 4.02 | 2.93 | 2.90 | 14.44 | 2.22 | high | 5-GW avg pts 4.60; mins 90; xGI 0.20; fixture Elo diff +82 |
| Cunha | MUN | Midfielder | 3.94 | 3.51 | 3.34 | 3.51 | 3.87 | 14.55 | 1.82 | high | 5-GW avg pts 3.60; mins 51; xGI 0.27; fixture Elo diff +109 |
| Gallagher | TOT | Midfielder | 3.81 | 3.80 | 4.06 | 3.48 | 3.24 | 14.87 | 2.70 | high | 5-GW avg pts 4.00; mins 88; xGI 0.15; fixture Elo diff -83 |
| Anderson | MCI | Midfielder | 3.80 | 4.53 | 3.36 | 3.85 | 3.36 | 15.28 | 2.35 | high | 5-GW avg pts 7.20; mins 76; xGI 0.30; fixture Elo diff +165 |
| Lacroix | CHE | Defender | 3.75 | 2.11 | 4.51 | 3.62 | 3.38 | 13.82 | 2.30 | high | 5-GW avg pts 2.20; mins 84; xGI 0.08; fixture Elo diff -25 |
| Mainoo | MUN | Midfielder | 3.75 | 3.31 | 2.70 | 3.31 | 3.53 | 13.32 | 2.42 | high | 5-GW avg pts 4.80; mins 90; xGI 0.13; fixture Elo diff +109 |
| Rayan | BOU | Midfielder | 3.74 | 3.42 | 3.71 | 3.39 | 3.45 | 14.23 | 2.19 | high | 5-GW avg pts 4.40; mins 64; xGI 0.27; fixture Elo diff +28 |
| Gakpo | LIV | Midfielder | 3.74 | 3.81 | 3.74 | 2.82 | 2.70 | 13.75 | 1.96 | high | 5-GW avg pts 2.80; mins 84; xGI 0.27; fixture Elo diff +82 |
| Rogers | CHE | Midfielder | 3.73 | 2.35 | 3.91 | 3.42 | 3.62 | 13.54 | 1.80 | high | 5-GW avg pts 3.40; mins 72; xGI 0.14; fixture Elo diff -25 |
| Groß | BHA | Midfielder | 3.72 | 4.01 | 4.10 | 2.74 | 3.95 | 14.89 | 2.71 | high | 5-GW avg pts 2.60; mins 72; xGI 0.28; fixture Elo diff +23 |
| Foden | MCI | Midfielder | 3.70 | 4.28 | 3.36 | 4.17 | 3.36 | 15.17 | 2.17 | high | 5-GW avg pts 3.40; mins 50; xGI 0.29; fixture Elo diff +165 |
| Saka | ARS | Midfielder | 3.67 | 4.61 | 4.36 | 4.06 | 4.61 | 16.92 | 1.78 | high | 5-GW avg pts 4.80; mins 45; xGI 0.40; fixture Elo diff +239 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 15.66 | GW2, GW3, GW5, GW6 | — | — |
| Danso | TOT | Defender | £5.0m | 14.59 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Tarkowski | EVE | Defender | £6.0m | 14.54 | GW4, GW5, GW6 | — | GW5 |
| Virgil | LIV | Defender | £6.5m | 14.44 | GW2, GW3, GW4 | — | — |
| Thiaw | NEW | Defender | £5.0m | 14.20 | GW2, GW5, GW6 | — | — |
| Watkins | AVL | Forward | £8.0m | 18.42 | GW3, GW4, GW5, GW6 | — | GW4, GW6 |
| Thiago | BRE | Forward | £8.0m | 15.96 | GW2, GW3, GW4, GW5 | — | — |
| Mheuka | CHE | Forward | £4.5m | 2.09 | Bench | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 13.75 | GW3, GW4, GW5, GW6 | — | — |
| Lammens | MUN | Goalkeeper | £5.0m | 12.52 | GW2 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.34 | GW2, GW3, GW4, GW5, GW6 | GW2, GW3, GW5, GW6 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 19.62 | GW2, GW3, GW4, GW5, GW6 | GW4 | GW2, GW3 |
| Mbeumo | MUN | Midfielder | £8.0m | 17.05 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Saka | ARS | Midfielder | £9.5m | 16.92 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Groß | BHA | Midfielder | £5.5m | 14.89 | GW2, GW3, GW4, GW6 | — | — |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 15.66 | GW2, GW3, GW4, GW5, GW6 | — | GW5 |
| Virgil | LIV | Defender | £6.5m | 14.44 | GW2, GW3, GW4 | — | — |
| Muñoz | CRY | Defender | £5.5m | 14.12 | GW3, GW4, GW5, GW6 | — | — |
| Maguire | MUN | Defender | £5.0m | 13.50 | GW2, GW6 | — | — |
| Mitchell | CRY | Defender | £4.5m | 13.08 | GW3, GW5, GW6 | — | — |
| Watkins | AVL | Forward | £8.0m | 18.42 | GW2, GW3, GW4, GW5, GW6 | — | GW4, GW6 |
| Thiago | BRE | Forward | £8.0m | 15.96 | GW2, GW3, GW4, GW5 | — | — |
| Mheuka | CHE | Forward | £4.5m | 2.09 | Bench | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 13.75 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.78 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.34 | GW2, GW3, GW4, GW5, GW6 | GW2, GW3, GW5, GW6 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 19.62 | GW2, GW3, GW4, GW5, GW6 | GW4 | GW2, GW3 |
| Mbeumo | MUN | Midfielder | £8.0m | 17.05 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Saka | ARS | Midfielder | £9.5m | 16.92 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Enzo | CHE | Midfielder | £7.0m | 14.35 | GW2, GW4, GW5, GW6 | — | — |

Squad cost: £100.0m.

## One-transfer recommendation

**Mitchell → Robinson** (projected weighted XI+captain gain 0.35).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Mitchell | Robinson | £4.5m | £4.5m | £0.0m | 0.35 |
| Maguire | Danso | £5.0m | £5.0m | £0.0m | 0.31 |
| Maguire | Thiaw | £5.0m | £5.0m | £0.0m | 0.19 |
| Leno | Verbruggen | £4.5m | £4.5m | £0.0m | 0.12 |
| Leno | Kinsky | £4.5m | £4.5m | £0.0m | 0.11 |
| Muñoz | Danso | £5.5m | £5.0m | £0.5m | 0.08 |
| Muñoz | Keane | £5.5m | £5.0m | £0.5m | 0.04 |
| Maguire | Keane | £5.0m | £5.0m | £0.0m | 0.02 |
| Muñoz | Thiaw | £5.5m | £5.0m | £0.5m | 0.01 |
| Leno | Forster | £4.5m | £4.0m | £0.5m | 0.00 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
