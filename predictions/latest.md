# FPL predictions: 2026-2027, GW2

Last generated: 2026-08-26 18:17 UTC

Data commit: `0d089b23aad6f2685b707b0d7fb98b06c8706c59`

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
| B.Fernandes | MUN | Midfielder | 5.90 | 5.72 | 4.04 | 5.58 | 6.07 | 21.83 | 1.82 | high | 5-GW avg pts 6.60; mins 90; xGI 0.56; fixture Elo diff +114 |
| Szoboszlai | LIV | Midfielder | 5.13 | 4.98 | 4.98 | 3.81 | 3.71 | 18.48 | 2.64 | high | 5-GW avg pts 6.80; mins 90; xGI 0.62; fixture Elo diff +87 |
| Palmer | CHE | Midfielder | 4.90 | 1.86 | 5.11 | 4.60 | 3.92 | 16.22 | 1.71 | high | 5-GW avg pts 5.00; mins 88; xGI 0.43; fixture Elo diff +2 |
| Haaland | MCI | Forward | 4.70 | 5.17 | 4.55 | 5.27 | 4.55 | 19.40 | 1.25 | high | 5-GW avg pts 5.80; mins 72; xGI 0.67; fixture Elo diff +165 |
| Gonzalo | FUL | Forward | 4.62 | 4.72 | 3.55 | 3.62 | 4.59 | 17.01 | 2.83 | low | 5-GW avg pts 6.00; mins 90; xGI 0.74; fixture Elo diff +12 |
| Silva | BOU | Defender | 4.36 | 3.92 | 4.06 | 3.85 | 4.00 | 16.25 | 3.25 | low | 5-GW avg pts 2.00; mins 90; xGI 0.00; fixture Elo diff +28 |
| Gakpo | LIV | Midfielder | 4.27 | 3.95 | 4.27 | 3.07 | 2.96 | 15.18 | 2.17 | high | 5-GW avg pts 4.80; mins 84; xGI 0.36; fixture Elo diff +87 |
| João Pedro | CHE | Forward | 4.21 | 2.30 | 3.56 | 3.64 | 4.01 | 14.09 | 1.88 | high | 5-GW avg pts 4.40; mins 72; xGI 0.40; fixture Elo diff +2 |
| Dasilva | COV | Defender | 4.17 | 2.45 | 3.12 | 2.69 | 3.12 | 12.63 | 3.16 | low | 5-GW avg pts 1.00; mins 90; xGI 0.02; fixture Elo diff -140 |
| van Ewijk | COV | Defender | 4.17 | 2.45 | 3.12 | 2.69 | 3.12 | 12.63 | 3.16 | low | 5-GW avg pts 1.00; mins 90; xGI 0.01; fixture Elo diff -140 |
| Thomas | COV | Defender | 4.14 | 2.35 | 3.47 | 3.01 | 3.47 | 13.23 | 3.31 | low | 5-GW avg pts 3.00; mins 90; xGI 0.03; fixture Elo diff -140 |
| Mbeumo | MUN | Midfielder | 4.07 | 4.17 | 3.11 | 4.17 | 4.37 | 15.85 | 1.98 | high | 5-GW avg pts 4.20; mins 66; xGI 1.03; fixture Elo diff +114 |
| Amenda | COV | Defender | 3.95 | 2.36 | 2.96 | 2.61 | 2.96 | 12.04 | 3.01 | low | 5-GW avg pts 1.00; mins 90; xGI 0.01; fixture Elo diff -140 |
| Virgil | LIV | Defender | 3.95 | 3.53 | 4.02 | 2.94 | 2.93 | 14.17 | 2.18 | high | 5-GW avg pts 4.20; mins 90; xGI 0.25; fixture Elo diff +87 |
| Horníček | NEW | Goalkeeper | 3.94 | 3.68 | 3.68 | 4.66 | 4.07 | 15.90 | 3.18 | low | 5-GW avg pts 1.00; mins 90; xGI 0.00; fixture Elo diff +109 |
| Enzo | CHE | Midfielder | 3.89 | 2.30 | 3.64 | 3.64 | 3.62 | 13.59 | 1.94 | high | 5-GW avg pts 5.00; mins 77; xGI 0.28; fixture Elo diff +2 |
| Bijol | LEE | Defender | 3.85 | 3.77 | 3.85 | 4.00 | 2.21 | 14.45 | 2.89 | high | 5-GW avg pts 5.80; mins 86; xGI 0.05; fixture Elo diff -79 |
| Schade | BRE | Midfielder | 3.84 | 4.60 | 3.57 | 4.00 | 3.44 | 15.70 | 2.62 | high | 5-GW avg pts 3.20; mins 75; xGI 0.33; fixture Elo diff +5 |
| Isak | LIV | Forward | 3.84 | 3.42 | 3.84 | 3.49 | 3.49 | 14.52 | 1.61 | high | 5-GW avg pts 0.60; mins 23; xGI 0.22; fixture Elo diff +87 |
| Dedić | NEW | Defender | 3.84 | 3.17 | 3.62 | 4.17 | 4.47 | 15.18 | 3.37 | low | 5-GW avg pts 1.00; mins 90; xGI 0.03; fixture Elo diff +109 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 16.25 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Dedić | NEW | Defender | £4.5m | 15.18 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Bijol | LEE | Defender | £5.0m | 14.45 | GW2, GW3, GW4, GW5 | — | — |
| Thomas | COV | Defender | £4.0m | 13.23 | GW2, GW6 | — | — |
| Dasilva | COV | Defender | £4.0m | 12.63 | GW2 | — | — |
| Haaland | MCI | Forward | £15.5m | 19.40 | GW2, GW3, GW4, GW5, GW6 | — | GW3, GW5 |
| Watkins | AVL | Forward | £8.0m | 17.51 | GW3, GW4, GW5, GW6 | GW4 | GW6 |
| Gonzalo | FUL | Forward | £6.0m | 17.01 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 15.90 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Steele | BHA | Goalkeeper | £4.0m | 0.50 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 21.83 | GW2, GW3, GW4, GW5, GW6 | GW2, GW3, GW5, GW6 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.48 | GW2, GW3, GW4, GW5, GW6 | — | GW2 |
| Palmer | CHE | Midfielder | £9.5m | 16.22 | GW2, GW4, GW5, GW6 | — | GW4 |
| Groß | BHA | Midfielder | £5.5m | 15.40 | GW3, GW4, GW6 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 14.08 | GW3, GW5 | — | — |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 14.51 | GW2, GW3, GW4, GW5, GW6 | — | GW6 |
| Virgil | LIV | Defender | £6.5m | 14.17 | GW2, GW3, GW4, GW6 | — | — |
| Maguire | MUN | Defender | £5.0m | 13.55 | GW2, GW3, GW5, GW6 | — | — |
| Muñoz | CRY | Defender | £5.5m | 12.04 | GW3, GW4, GW5, GW6 | — | — |
| Mitchell | CRY | Defender | £4.5m | 10.04 | GW3 | — | — |
| Thiago | BRE | Forward | £8.0m | 14.78 | GW2, GW3, GW4, GW5 | — | — |
| João Pedro | CHE | Forward | £7.5m | 14.09 | GW2, GW4, GW5, GW6 | — | — |
| Mheuka | CHE | Forward | £4.5m | 1.49 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.63 | GW2, GW3, GW5, GW6 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 9.92 | GW4 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 21.83 | GW2, GW3, GW4, GW5, GW6 | GW2, GW3, GW5, GW6 | GW4 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.48 | GW2, GW3, GW4, GW5, GW6 | GW4 | GW2, GW3 |
| Mbeumo | MUN | Midfielder | £8.0m | 15.85 | GW2, GW3, GW4, GW5, GW6 | — | GW5 |
| Saka | ARS | Midfielder | £9.5m | 15.80 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Enzo | CHE | Midfielder | £7.0m | 13.59 | GW2, GW4, GW5, GW6 | — | — |

Squad cost: £99.5m.

## One-transfer recommendation

**Leno → Horníček** (projected weighted XI+captain gain 4.16).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Leno | Horníček | £4.5m | £5.0m | £0.0m | 4.16 |
| Pope | Horníček | £5.0m | £5.0m | £0.5m | 4.16 |
| Mitchell | Silva | £4.5m | £5.0m | £0.0m | 4.15 |
| Muñoz | Silva | £5.5m | £5.0m | £1.0m | 3.57 |
| João Pedro | Watkins | £7.5m | £8.0m | £0.0m | 3.50 |
| Mitchell | Dedić | £4.5m | £4.5m | £0.5m | 3.09 |
| Thiago | Watkins | £8.0m | £8.0m | £0.5m | 2.91 |
| Mitchell | Bijol | £4.5m | £5.0m | £0.0m | 2.79 |
| João Pedro | Gonzalo | £7.5m | £6.0m | £2.0m | 2.70 |
| Maguire | Silva | £5.0m | £5.0m | £0.5m | 2.52 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
