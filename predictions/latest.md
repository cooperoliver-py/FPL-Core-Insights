# FPL predictions: 2026-2027, GW2

Last generated: 2026-08-25 17:07 UTC

Data commit: `6bd5d7b91de858db5bbe3d92166ba8ca249e0516`

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
| B.Fernandes | MUN | Midfielder | 6.18 | 5.72 | 4.04 | 5.58 | 6.07 | 22.11 | 1.84 | high | 5-GW avg pts 6.60; mins 90; xGI 0.56; fixture Elo diff +109 |
| Szoboszlai | LIV | Midfielder | 5.13 | 5.26 | 4.98 | 3.81 | 3.71 | 18.73 | 2.68 | high | 5-GW avg pts 6.80; mins 90; xGI 0.62; fixture Elo diff +82 |
| Palmer | CHE | Midfielder | 4.90 | 1.86 | 5.34 | 4.60 | 3.92 | 16.41 | 1.73 | high | 5-GW avg pts 5.00; mins 88; xGI 0.43; fixture Elo diff -25 |
| Gonzalo | FUL | Forward | 4.62 | 4.72 | 3.55 | 3.62 | 5.33 | 17.45 | 2.91 | low | 5-GW avg pts 6.00; mins 90; xGI 0.74; fixture Elo diff +7 |
| Haaland | MCI | Forward | 4.59 | 5.10 | 4.44 | 5.16 | 4.44 | 19.02 | 1.23 | high | 5-GW avg pts 5.80; mins 72; xGI 0.67; fixture Elo diff +165 |
| Gakpo | LIV | Midfielder | 4.45 | 4.43 | 4.45 | 3.24 | 3.13 | 16.14 | 2.31 | high | 5-GW avg pts 4.80; mins 84; xGI 0.36; fixture Elo diff +82 |
| Mbeumo | MUN | Midfielder | 4.39 | 4.17 | 3.11 | 4.17 | 4.37 | 16.17 | 2.02 | high | 5-GW avg pts 4.20; mins 66; xGI 1.03; fixture Elo diff +109 |
| Silva | BOU | Defender | 4.28 | 3.92 | 4.06 | 3.85 | 4.00 | 16.16 | 3.23 | low | 5-GW avg pts 2.00; mins 90; xGI 0.00; fixture Elo diff +28 |
| M.Sangaré | BRE | Midfielder | 4.28 | 4.83 | 3.24 | 4.44 | 3.04 | 16.15 | 2.94 | low | 5-GW avg pts 14.00; mins 75; xGI 0.38; fixture Elo diff +6 |
| João Pedro | CHE | Forward | 4.21 | 2.30 | 4.32 | 3.64 | 4.01 | 14.70 | 1.96 | high | 5-GW avg pts 4.40; mins 72; xGI 0.40; fixture Elo diff -25 |
| Thomas | COV | Defender | 4.16 | 2.35 | 3.47 | 3.01 | 3.47 | 13.24 | 3.31 | low | 5-GW avg pts 3.00; mins 90; xGI 0.03; fixture Elo diff -162 |
| Cunha | MUN | Midfielder | 4.10 | 3.61 | 3.47 | 3.61 | 4.02 | 15.05 | 1.88 | high | 5-GW avg pts 4.00; mins 67; xGI 0.36; fixture Elo diff +109 |
| Schade | BRE | Midfielder | 4.02 | 4.45 | 3.57 | 4.00 | 3.44 | 15.74 | 2.62 | high | 5-GW avg pts 3.20; mins 75; xGI 0.33; fixture Elo diff +6 |
| Maguire | MUN | Defender | 4.00 | 3.39 | 2.86 | 3.39 | 3.64 | 13.89 | 2.78 | high | 5-GW avg pts 4.20; mins 90; xGI 0.15; fixture Elo diff +109 |
| Virgil | LIV | Defender | 3.95 | 4.06 | 4.02 | 2.94 | 2.93 | 14.65 | 2.25 | high | 5-GW avg pts 4.20; mins 90; xGI 0.25; fixture Elo diff +82 |
| Horníček | NEW | Goalkeeper | 3.94 | 3.68 | 3.68 | 4.50 | 4.07 | 15.79 | 3.16 | low | 5-GW avg pts 1.00; mins 90; xGI 0.00; fixture Elo diff +82 |
| Thiago | BRE | Forward | 3.92 | 4.40 | 3.17 | 4.02 | 2.73 | 14.87 | 1.86 | high | 5-GW avg pts 2.40; mins 88; xGI 0.52; fixture Elo diff +6 |
| Enzo | CHE | Midfielder | 3.89 | 2.30 | 4.21 | 3.64 | 3.62 | 14.05 | 2.01 | high | 5-GW avg pts 5.00; mins 77; xGI 0.28; fixture Elo diff -25 |
| Bijol | LEE | Defender | 3.85 | 3.77 | 3.85 | 4.00 | 2.21 | 14.45 | 2.89 | high | 5-GW avg pts 5.80; mins 86; xGI 0.05; fixture Elo diff -80 |
| Isak | LIV | Forward | 3.84 | 4.05 | 3.84 | 3.49 | 3.49 | 15.08 | 1.68 | high | 5-GW avg pts 0.60; mins 23; xGI 0.22; fixture Elo diff +82 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 16.16 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Dedić | NEW | Defender | £4.5m | 15.49 | GW2, GW4, GW5, GW6 | — | — |
| Botman | NEW | Defender | £5.0m | 15.02 | GW5, GW6 | — | — |
| Bijol | LEE | Defender | £5.0m | 14.45 | GW2, GW3, GW4, GW5 | — | — |
| Maguire | MUN | Defender | £5.0m | 13.89 | GW2, GW3, GW6 | — | — |
| Haaland | MCI | Forward | £15.5m | 19.02 | GW2, GW3, GW4, GW5, GW6 | — | GW5 |
| Watkins | AVL | Forward | £8.0m | 17.92 | GW3, GW4, GW5, GW6 | GW4 | — |
| Gonzalo | FUL | Forward | £6.0m | 17.45 | GW2, GW3, GW4, GW5, GW6 | — | GW6 |
| Horníček | NEW | Goalkeeper | £5.0m | 15.79 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Woodman | LIV | Goalkeeper | £4.0m | 1.57 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.11 | GW2, GW3, GW4, GW5, GW6 | GW2, GW3, GW5, GW6 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.73 | GW2, GW3, GW4, GW5, GW6 | — | GW2, GW3, GW4 |
| M.Sangaré | BRE | Midfielder | £5.5m | 16.15 | GW2, GW3, GW5 | — | — |
| Gakpo | LIV | Midfielder | £7.0m | 16.14 | GW2, GW3, GW4 | — | — |
| Groß | BHA | Midfielder | £5.5m | 15.43 | GW4, GW6 | — | — |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 15.02 | GW2, GW3, GW4, GW5, GW6 | — | GW5, GW6 |
| Virgil | LIV | Defender | £6.5m | 14.65 | GW2, GW3, GW4, GW6 | — | — |
| Maguire | MUN | Defender | £5.0m | 13.89 | GW2, GW3, GW5, GW6 | — | — |
| Muñoz | CRY | Defender | £5.5m | 12.60 | GW3, GW4, GW5, GW6 | — | — |
| Mitchell | CRY | Defender | £4.5m | 10.30 | GW3 | — | — |
| Thiago | BRE | Forward | £8.0m | 14.87 | GW2, GW3, GW4, GW5 | — | — |
| João Pedro | CHE | Forward | £7.5m | 14.70 | GW2, GW4, GW5, GW6 | — | GW4 |
| Mheuka | CHE | Forward | £4.5m | 1.57 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.75 | GW2, GW3, GW6 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 10.18 | GW4, GW5 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.11 | GW2, GW3, GW4, GW5, GW6 | GW2, GW3, GW5, GW6 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.73 | GW2, GW3, GW4, GW5, GW6 | GW4 | GW2, GW3 |
| Mbeumo | MUN | Midfielder | £8.0m | 16.17 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Saka | ARS | Midfielder | £9.5m | 15.80 | GW2, GW3, GW4, GW5, GW6 | — | — |
| Enzo | CHE | Midfielder | £7.0m | 14.05 | GW2, GW4, GW5, GW6 | — | — |

Squad cost: £99.5m.

## One-transfer recommendation

**Mitchell → Silva** (projected weighted XI+captain gain 4.04).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Mitchell | Silva | £4.5m | £5.0m | £0.0m | 4.04 |
| Leno | Horníček | £4.5m | £5.0m | £0.0m | 3.85 |
| Pope | Horníček | £5.0m | £5.0m | £0.5m | 3.85 |
| Mitchell | Dedić | £4.5m | £4.5m | £0.5m | 3.36 |
| João Pedro | Watkins | £7.5m | £8.0m | £0.0m | 3.23 |
| Thiago | Watkins | £8.0m | £8.0m | £0.5m | 3.15 |
| Muñoz | Silva | £5.5m | £5.0m | £1.0m | 2.92 |
| Mitchell | Bijol | £4.5m | £5.0m | £0.0m | 2.76 |
| João Pedro | Gonzalo | £7.5m | £6.0m | £2.0m | 2.53 |
| Thiago | Gonzalo | £8.0m | £6.0m | £2.5m | 2.46 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
