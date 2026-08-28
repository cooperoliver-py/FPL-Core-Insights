# FPL predictions: 2026-2027, GW3

Last generated: 2026-08-28 20:19 UTC

Data commit: `cf9c82251fcb7d2cad996bac900dec5c358f864b`

Forecasts use only the canonical 2025/26 `By Gameweek` player data, strictly lagged 3/5-GW form, and target Premier League fixtures. Five-GW weights are [1.0, 0.9, 0.8, 0.7, 0.6]; price and availability are held constant.

## Held-out evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.966 | 1.912 | 0.695 |
| Rolling points (5 GW) | 1.033 | 2.129 | 0.683 |
| Lagged FPL ep_next | 1.008 | 2.116 | 0.671 |

## Top GW3 player forecasts

| Player | Club | Pos | GW3 | GW4 | GW5 | GW6 | GW7 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 5.72 | 4.04 | 5.58 | 6.07 | 5.72 | 21.50 | 1.79 | high | 5-GW avg pts 6.60; mins 90; xGI 0.56; fixture Elo diff +83 |
| Szoboszlai | LIV | Midfielder | 5.26 | 4.98 | 3.81 | 3.71 | 4.97 | 18.36 | 2.62 | high | 5-GW avg pts 6.80; mins 90; xGI 0.62; fixture Elo diff +79 |
| Haaland | MCI | Forward | 5.10 | 4.44 | 5.16 | 4.44 | 5.10 | 19.40 | 1.25 | high | 5-GW avg pts 5.80; mins 72; xGI 0.67; fixture Elo diff +192 |
| M.Sangaré | BRE | Midfielder | 4.83 | 3.24 | 4.44 | 3.04 | 3.54 | 15.55 | 2.78 | low | 5-GW avg pts 14.00; mins 75; xGI 0.38; fixture Elo diff -17 |
| Semenyo | MCI | Midfielder | 4.81 | 3.28 | 4.05 | 3.28 | 4.81 | 16.18 | 1.90 | high | 5-GW avg pts 4.60; mins 91; xGI 0.22; fixture Elo diff +192 |
| Gonzalo | FUL | Forward | 4.72 | 3.55 | 3.62 | 5.33 | 5.78 | 18.02 | 3.00 | low | 5-GW avg pts 6.00; mins 90; xGI 0.74; fixture Elo diff +21 |
| Schade | BRE | Midfielder | 4.45 | 3.57 | 4.00 | 3.44 | 3.53 | 15.39 | 2.57 | high | 5-GW avg pts 3.20; mins 75; xGI 0.33; fixture Elo diff -17 |
| Gakpo | LIV | Midfielder | 4.43 | 4.45 | 3.24 | 3.13 | 4.21 | 15.75 | 2.25 | high | 5-GW avg pts 4.80; mins 84; xGI 0.36; fixture Elo diff +79 |
| Saka | ARS | Midfielder | 4.41 | 3.92 | 3.82 | 4.34 | 3.82 | 16.32 | 1.72 | high | 5-GW avg pts 6.40; mins 56; xGI 0.53; fixture Elo diff +258 |
| Thiago | BRE | Forward | 4.40 | 3.17 | 4.02 | 2.73 | 2.89 | 14.11 | 1.76 | high | 5-GW avg pts 2.40; mins 88; xGI 0.52; fixture Elo diff -17 |
| Gibbs-White | NFO | Midfielder | 4.21 | 2.80 | 4.47 | 4.05 | 2.07 | 14.38 | 1.80 | high | 5-GW avg pts 4.40; mins 58; xGI 0.44; fixture Elo diff -24 |
| Mbeumo | MUN | Midfielder | 4.17 | 3.11 | 4.17 | 4.37 | 4.14 | 15.85 | 1.98 | high | 5-GW avg pts 4.20; mins 66; xGI 1.03; fixture Elo diff +83 |
| Groß | BHA | Midfielder | 4.07 | 4.42 | 2.97 | 4.01 | 4.01 | 15.64 | 2.84 | high | 5-GW avg pts 3.00; mins 90; xGI 0.33; fixture Elo diff +29 |
| Virgil | LIV | Defender | 4.06 | 4.02 | 2.94 | 2.93 | 3.90 | 14.43 | 2.22 | high | 5-GW avg pts 4.20; mins 90; xGI 0.25; fixture Elo diff +79 |
| Isak | LIV | Forward | 4.05 | 3.84 | 3.49 | 3.49 | 3.72 | 14.97 | 1.66 | high | 5-GW avg pts 0.60; mins 23; xGI 0.22; fixture Elo diff +79 |
| Janelt | BRE | Midfielder | 4.01 | 3.26 | 3.80 | 3.03 | 3.27 | 14.06 | 2.81 | high | 5-GW avg pts 2.60; mins 54; xGI 0.19; fixture Elo diff -17 |
| Cherki | MCI | Midfielder | 3.99 | 3.51 | 3.96 | 3.51 | 3.99 | 15.16 | 2.02 | high | 5-GW avg pts 4.00; mins 51; xGI 0.37; fixture Elo diff +192 |
| Silva | BOU | Defender | 3.92 | 4.06 | 3.85 | 4.00 | 4.36 | 16.08 | 3.22 | low | 5-GW avg pts 2.00; mins 90; xGI 0.00; fixture Elo diff +41 |
| Guéhi | MCI | Defender | 3.92 | 2.73 | 3.41 | 2.73 | 3.92 | 13.38 | 2.23 | high | 5-GW avg pts 6.20; mins 90; xGI 0.31; fixture Elo diff +192 |
| Wirtz | LIV | Midfielder | 3.90 | 3.78 | 3.34 | 3.33 | 3.74 | 14.55 | 1.94 | high | 5-GW avg pts 1.20; mins 39; xGI 0.24; fixture Elo diff +79 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 16.08 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Dedić | NEW | Defender | £4.5m | 14.97 | GW4, GW5, GW6 | — | — |
| Botman | NEW | Defender | £5.0m | 14.87 | GW5, GW6 | — | — |
| De Cuyper | BHA | Defender | £4.6m | 14.26 | GW3, GW4, GW7 | — | — |
| Bijol | LEE | Defender | £5.0m | 14.02 | GW3, GW4, GW5, GW7 | — | — |
| Haaland | MCI | Forward | £15.5m | 19.40 | GW3, GW4, GW5, GW6, GW7 | — | GW5 |
| Gonzalo | FUL | Forward | £6.0m | 18.02 | GW3, GW4, GW5, GW6, GW7 | GW7 | GW6 |
| Emersonn | IPS | Forward | £5.5m | 13.24 | GW3, GW6 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 15.51 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Matthews | CRY | Goalkeeper | £4.0m | 0.52 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 21.50 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6 | GW7 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.36 | GW3, GW4, GW5, GW6, GW7 | — | GW3, GW4 |
| Palmer | CHE | Midfielder | £9.5m | 15.85 | GW4, GW5, GW6, GW7 | GW4 | — |
| Groß | BHA | Midfielder | £5.5m | 15.64 | GW3, GW4, GW6, GW7 | — | — |
| M.Sangaré | BRE | Midfielder | £5.6m | 15.55 | GW3, GW5, GW7 | — | — |

Squad cost: £99.7m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 14.87 | GW3, GW4, GW5, GW6, GW7 | — | GW5, GW6 |
| Virgil | LIV | Defender | £6.5m | 14.43 | GW3, GW4, GW6, GW7 | — | — |
| Maguire | MUN | Defender | £5.0m | 13.24 | GW3, GW5, GW6, GW7 | — | — |
| Muñoz | CRY | Defender | £5.5m | 12.99 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Mitchell | CRY | Defender | £4.5m | 10.63 | GW3 | — | — |
| Thiago | BRE | Forward | £8.0m | 14.11 | GW3, GW4, GW5 | — | — |
| João Pedro | CHE | Forward | £7.6m | 14.10 | GW4, GW5, GW6, GW7 | — | GW4 |
| Mheuka | CHE | Forward | £4.5m | 1.56 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.02 | GW3, GW6, GW7 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 10.06 | GW4, GW5 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 21.50 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.36 | GW3, GW4, GW5, GW6, GW7 | GW4 | GW3, GW7 |
| Saka | ARS | Midfielder | £9.5m | 16.32 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Mbeumo | MUN | Midfielder | £8.0m | 15.85 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Enzo | CHE | Midfielder | £7.0m | 13.72 | GW4, GW5, GW6, GW7 | — | — |

Squad cost: £99.6m.

## One-transfer recommendation

**Mitchell → Silva** (projected weighted XI+captain gain 4.43).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Mitchell | Silva | £4.5m | £5.0m | £0.0m | 4.43 |
| Thiago | Gonzalo | £8.0m | £6.0m | £2.5m | 3.76 |
| João Pedro | Gonzalo | £7.5m | £6.0m | £2.0m | 3.71 |
| Pope | Horníček | £5.0m | £5.0m | £0.5m | 3.38 |
| Mitchell | Dedić | £4.5m | £4.5m | £0.5m | 3.36 |
| Leno | Horníček | £4.5m | £5.0m | £0.0m | 3.28 |
| Muñoz | Silva | £5.5m | £5.0m | £1.0m | 3.09 |
| Mitchell | Bijol | £4.5m | £5.0m | £0.0m | 2.87 |
| Mitchell | De Cuyper | £4.5m | £4.6m | £0.4m | 2.84 |
| Maguire | Silva | £5.0m | £5.0m | £0.5m | 2.62 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
