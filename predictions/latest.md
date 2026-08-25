# FPL predictions: 2026-2027, GW2

Last generated: 2026-08-25 10:08 UTC

Data commit: `89c1639f4cbd77ec08d3d4c3f3133f19213aed3e`

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
| B.Fernandes | MUN | Midfielder | 6.24 | 5.92 | 4.04 | 5.77 | 6.27 | 22.59 | 1.88 | high | 5-GW avg pts 6.60; mins 90; xGI 0.56; fixture Elo diff +109 |
| Szoboszlai | LIV | Midfielder | 5.28 | 5.41 | 5.13 | 3.96 | 3.86 | 19.33 | 2.76 | high | 5-GW avg pts 6.80; mins 90; xGI 0.62; fixture Elo diff +82 |
| Haaland | MCI | Forward | 4.58 | 5.01 | 4.43 | 5.08 | 4.43 | 18.84 | 1.22 | high | 5-GW avg pts 5.80; mins 72; xGI 0.67; fixture Elo diff +165 |
| Mbeumo | MUN | Midfielder | 4.54 | 4.19 | 3.21 | 4.19 | 4.43 | 16.47 | 2.06 | high | 5-GW avg pts 4.20; mins 66; xGI 1.03; fixture Elo diff +109 |
| Gonzalo | FUL | Forward | 4.30 | 3.47 | 3.02 | 2.78 | 5.19 | 14.91 | 2.49 | low | 5-GW avg pts 6.00; mins 90; xGI 0.74; fixture Elo diff +7 |
| Gakpo | LIV | Midfielder | 4.05 | 4.20 | 4.05 | 2.83 | 2.68 | 14.65 | 2.09 | high | 5-GW avg pts 4.80; mins 84; xGI 0.36; fixture Elo diff +82 |
| Maguire | MUN | Defender | 4.04 | 3.33 | 2.62 | 3.33 | 3.57 | 13.62 | 2.72 | high | 5-GW avg pts 4.20; mins 90; xGI 0.15; fixture Elo diff +109 |
| Cunha | MUN | Midfielder | 3.98 | 3.58 | 3.44 | 3.58 | 3.92 | 14.81 | 1.85 | high | 5-GW avg pts 4.00; mins 67; xGI 0.36; fixture Elo diff +109 |
| Virgil | LIV | Defender | 3.93 | 4.04 | 4.00 | 2.92 | 2.91 | 14.56 | 2.24 | high | 5-GW avg pts 4.20; mins 90; xGI 0.25; fixture Elo diff +82 |
| Thiago | BRE | Forward | 3.92 | 4.40 | 3.17 | 4.02 | 2.73 | 14.87 | 1.86 | high | 5-GW avg pts 2.40; mins 88; xGI 0.52; fixture Elo diff +6 |
| M.Sangaré | BRE | Midfielder | 3.92 | 4.19 | 2.88 | 3.56 | 2.77 | 14.15 | 2.57 | low | 5-GW avg pts 14.00; mins 75; xGI 0.38; fixture Elo diff +6 |
| Enzo | CHE | Midfielder | 3.72 | 2.13 | 4.05 | 3.47 | 3.46 | 13.38 | 1.91 | high | 5-GW avg pts 5.00; mins 77; xGI 0.28; fixture Elo diff -25 |
| Calvert-Lewin | LEE | Forward | 3.72 | 3.43 | 3.72 | 3.61 | 1.77 | 13.38 | 2.23 | high | 5-GW avg pts 4.60; mins 86; xGI 0.40; fixture Elo diff -80 |
| Truffert | BOU | Defender | 3.67 | 3.57 | 3.91 | 3.52 | 3.50 | 14.57 | 2.65 | high | 5-GW avg pts 5.40; mins 90; xGI 0.16; fixture Elo diff +28 |
| Lammens | MUN | Goalkeeper | 3.67 | 3.14 | 2.53 | 3.14 | 3.34 | 12.72 | 2.54 | high | 5-GW avg pts 3.80; mins 90; xGI 0.00; fixture Elo diff +109 |
| Semenyo | MCI | Midfielder | 3.67 | 4.91 | 3.42 | 4.31 | 3.42 | 15.89 | 1.87 | high | 5-GW avg pts 4.60; mins 91; xGI 0.22; fixture Elo diff +165 |
| Isak | LIV | Forward | 3.62 | 3.83 | 3.62 | 3.36 | 3.36 | 14.34 | 1.59 | high | 5-GW avg pts 0.60; mins 23; xGI 0.22; fixture Elo diff +82 |
| Schade | BRE | Midfielder | 3.59 | 3.59 | 3.32 | 3.22 | 3.20 | 13.64 | 2.27 | high | 5-GW avg pts 3.20; mins 75; xGI 0.33; fixture Elo diff +6 |
| Groß | BHA | Midfielder | 3.59 | 3.85 | 4.31 | 2.77 | 3.93 | 14.80 | 2.69 | high | 5-GW avg pts 3.00; mins 90; xGI 0.33; fixture Elo diff +23 |
| Shaw | MUN | Defender | 3.57 | 2.97 | 2.60 | 2.97 | 3.31 | 12.39 | 2.75 | high | 5-GW avg pts 4.20; mins 88; xGI 0.16; fixture Elo diff +109 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Truffert | BOU | Defender | £5.5m | 14.57 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Virgil | LIV | Defender | £6.5m | 14.56 | GW2, GW3, GW4 | — | — |
| Botman | NEW | Defender | £5.0m | 14.28 | GW4, GW5, GW6 | — | — |
| Tarkowski | EVE | Defender | £6.0m | 13.84 | GW4, GW5, GW6 | — | GW5 |
| Maguire | MUN | Defender | £5.0m | 13.62 | GW2, GW3, GW5, GW6 | — | — |
| Watkins | AVL | Forward | £8.0m | 17.92 | GW3, GW4, GW5, GW6 | GW4 | GW6 |
| Gonzalo | FUL | Forward | £6.0m | 14.91 | GW2, GW6 | — | — |
| Thiago | BRE | Forward | £8.0m | 14.87 | GW2, GW3, GW5 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.37 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Austin | TOT | Goalkeeper | £4.0m | 0.52 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.59 | GW2, GW3, GW4, GW5, GW6 | GW2, GW3, GW5, GW6 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 19.33 | GW2, GW3, GW4, GW5, GW6 | — | GW2, GW3, GW4 |
| Mbeumo | MUN | Midfielder | £8.0m | 16.47 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Semenyo | MCI | Midfielder | £8.5m | 15.89 | GW2, GW3, GW4, GW5 | — | — |
| Groß | BHA | Midfielder | £5.5m | 14.80 | GW2, GW3, GW4, GW6 | — | — |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | LIV | Defender | £6.5m | 14.56 | GW2, GW3, GW4, GW6 | — | — |
| Botman | NEW | Defender | £5.0m | 14.28 | GW2, GW3, GW4, GW5, GW6 | — | GW5 |
| Maguire | MUN | Defender | £5.0m | 13.62 | GW2, GW3, GW5, GW6 | — | — |
| Muñoz | CRY | Defender | £5.5m | 12.60 | GW3, GW4, GW5, GW6 | — | — |
| Mitchell | CRY | Defender | £4.5m | 10.04 | GW3 | — | — |
| Thiago | BRE | Forward | £8.0m | 14.87 | GW2, GW3, GW4, GW5 | — | — |
| João Pedro | CHE | Forward | £7.5m | 12.33 | GW2, GW4, GW5, GW6 | — | — |
| Mheuka | CHE | Forward | £4.5m | 1.57 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.75 | GW2, GW3, GW6 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 10.18 | GW4, GW5 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.59 | GW2, GW3, GW4, GW5, GW6 | GW2, GW3, GW5, GW6 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 19.33 | GW2, GW3, GW4, GW5, GW6 | GW4 | GW2, GW3 |
| Mbeumo | MUN | Midfielder | £8.0m | 16.47 | GW2, GW3, GW4, GW5, GW6 | — | GW6 |
| Saka | ARS | Midfielder | £9.5m | 14.26 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Enzo | CHE | Midfielder | £7.0m | 13.38 | GW2, GW4, GW5, GW6 | — | GW4 |

Squad cost: £99.5m.

## One-transfer recommendation

**João Pedro → Watkins** (projected weighted XI+captain gain 5.67).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| João Pedro | Watkins | £7.5m | £8.0m | £0.0m | 5.67 |
| Thiago | Watkins | £8.0m | £8.0m | £0.5m | 3.05 |
| João Pedro | Gonzalo | £7.5m | £6.0m | £2.0m | 2.66 |
| João Pedro | Havertz | £7.5m | £7.5m | £0.5m | 2.30 |
| Mitchell | Thiaw | £4.5m | £5.0m | £0.0m | 2.01 |
| Mitchell | Hall | £4.5m | £5.0m | £0.0m | 1.88 |
| Mitchell | Bijol | £4.5m | £5.0m | £0.0m | 1.78 |
| Muñoz | Truffert | £5.5m | £5.5m | £0.5m | 1.69 |
| Pope | Horníček | £5.0m | £5.0m | £0.5m | 1.69 |
| Saka | Semenyo | £9.5m | £8.5m | £1.5m | 1.63 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
