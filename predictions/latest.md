# FPL predictions: 2026-2027, GW3

Last generated: 2026-08-30 19:24 UTC

Data commit: `c9b594cc740d1352903327e88527a24ea88a60e9`

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
| Haaland | MCI | Forward | 5.17 | 4.55 | 5.27 | 4.55 | 4.91 | 19.60 | 1.26 | high | 5-GW avg pts 5.80; mins 72; xGI 0.67; fixture Elo diff +198 |
| Szoboszlai | LIV | Midfielder | 4.98 | 4.98 | 3.81 | 3.71 | 4.97 | 18.08 | 2.58 | high | 5-GW avg pts 6.80; mins 90; xGI 0.62; fixture Elo diff +84 |
| Semenyo | MCI | Midfielder | 4.87 | 3.38 | 4.16 | 3.38 | 4.62 | 16.39 | 1.93 | high | 5-GW avg pts 4.60; mins 91; xGI 0.22; fixture Elo diff +198 |
| M.Sangaré | BRE | Midfielder | 4.83 | 3.24 | 4.44 | 3.04 | 3.54 | 15.55 | 2.78 | low | 5-GW avg pts 14.00; mins 75; xGI 0.38; fixture Elo diff -18 |
| Gonzalo | FUL | Forward | 4.72 | 3.55 | 3.62 | 4.59 | 5.41 | 17.28 | 2.88 | low | 5-GW avg pts 6.00; mins 90; xGI 0.74; fixture Elo diff +53 |
| Schade | BRE | Midfielder | 4.60 | 3.57 | 4.00 | 3.44 | 3.53 | 15.54 | 2.59 | high | 5-GW avg pts 3.20; mins 75; xGI 0.33; fixture Elo diff -18 |
| Thiago | BRE | Forward | 4.55 | 3.17 | 4.02 | 2.73 | 2.89 | 14.26 | 1.78 | high | 5-GW avg pts 2.40; mins 88; xGI 0.52; fixture Elo diff -18 |
| Saka | ARS | Midfielder | 4.41 | 3.92 | 3.82 | 4.34 | 3.82 | 16.32 | 1.72 | high | 5-GW avg pts 6.40; mins 56; xGI 0.53; fixture Elo diff +258 |
| Gibbs-White | NFO | Midfielder | 4.21 | 2.80 | 4.47 | 4.05 | 2.07 | 14.38 | 1.82 | high | 5-GW avg pts 4.40; mins 58; xGI 0.44; fixture Elo diff -23 |
| Mbeumo | MUN | Midfielder | 4.17 | 3.11 | 4.17 | 4.37 | 4.14 | 15.85 | 1.98 | high | 5-GW avg pts 4.20; mins 66; xGI 1.03; fixture Elo diff +83 |
| Groß | BHA | Midfielder | 4.07 | 4.38 | 2.97 | 4.01 | 4.01 | 15.60 | 2.84 | high | 5-GW avg pts 3.00; mins 90; xGI 0.33; fixture Elo diff +30 |
| Janelt | BRE | Midfielder | 4.01 | 3.26 | 3.80 | 3.03 | 3.27 | 14.06 | 2.81 | high | 5-GW avg pts 2.60; mins 54; xGI 0.19; fixture Elo diff -18 |
| Gakpo | LIV | Midfielder | 3.95 | 4.27 | 3.07 | 2.96 | 4.04 | 14.75 | 2.11 | high | 5-GW avg pts 4.80; mins 84; xGI 0.36; fixture Elo diff +84 |
| Silva | BOU | Defender | 3.92 | 4.06 | 3.85 | 4.00 | 4.36 | 16.08 | 3.22 | low | 5-GW avg pts 2.00; mins 90; xGI 0.00; fixture Elo diff +42 |
| Foden | MCI | Midfielder | 3.91 | 3.28 | 3.74 | 3.28 | 3.65 | 14.35 | 2.05 | high | 5-GW avg pts 3.60; mins 66; xGI 0.39; fixture Elo diff +198 |
| Guéhi | MCI | Defender | 3.88 | 2.73 | 3.41 | 2.73 | 3.50 | 13.09 | 2.18 | high | 5-GW avg pts 6.20; mins 90; xGI 0.31; fixture Elo diff +198 |
| Havertz | ARS | Forward | 3.84 | 3.53 | 3.42 | 3.75 | 3.42 | 14.44 | 1.92 | high | 5-GW avg pts 3.80; mins 46; xGI 0.32; fixture Elo diff +258 |
| Castagne | FUL | Defender | 3.82 | 2.59 | 2.85 | 3.05 | 3.33 | 12.57 | 2.79 | high | 5-GW avg pts 4.40; mins 88; xGI 0.22; fixture Elo diff +53 |
| Cherki | MCI | Midfielder | 3.81 | 3.33 | 3.78 | 3.33 | 3.62 | 14.33 | 1.89 | high | 5-GW avg pts 4.00; mins 51; xGI 0.37; fixture Elo diff +198 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 16.08 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Dedić | NEW | Defender | £4.5m | 14.63 | GW4, GW5, GW6 | — | — |
| Botman | NEW | Defender | £5.0m | 14.29 | GW5, GW6 | — | — |
| De Cuyper | BHA | Defender | £4.6m | 14.26 | GW3, GW4, GW7 | — | — |
| Bijol | LEE | Defender | £5.0m | 14.02 | GW3, GW4, GW5, GW7 | — | — |
| Haaland | MCI | Forward | £15.5m | 19.60 | GW3, GW4, GW5, GW6, GW7 | — | GW3, GW5 |
| Gonzalo | FUL | Forward | £6.0m | 17.28 | GW3, GW4, GW5, GW6, GW7 | — | GW6, GW7 |
| Emersonn | IPS | Forward | £5.5m | 13.37 | GW3, GW6 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 15.64 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Davies | LIV | Goalkeeper | £4.0m | 0.42 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 21.50 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.08 | GW3, GW4, GW5, GW6, GW7 | — | GW4 |
| Palmer | CHE | Midfielder | £9.6m | 15.64 | GW4, GW5, GW6, GW7 | GW4 | — |
| Groß | BHA | Midfielder | £5.5m | 15.60 | GW3, GW4, GW6, GW7 | — | — |
| M.Sangaré | BRE | Midfielder | £5.6m | 15.55 | GW3, GW5, GW7 | — | — |

Squad cost: £99.8m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 14.29 | GW3, GW4, GW5, GW6, GW7 | — | GW6 |
| Virgil | LIV | Defender | £6.5m | 13.83 | GW3, GW4, GW6, GW7 | — | — |
| Maguire | MUN | Defender | £5.0m | 13.24 | GW3, GW5, GW6, GW7 | — | — |
| Muñoz | CRY | Defender | £5.5m | 12.36 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Mitchell | CRY | Defender | £4.5m | 10.34 | GW3 | — | — |
| Thiago | BRE | Forward | £8.0m | 14.26 | GW3, GW4, GW5 | — | — |
| João Pedro | CHE | Forward | £7.6m | 13.42 | GW4, GW5, GW6, GW7 | — | — |
| Mheuka | CHE | Forward | £4.5m | 1.47 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.93 | GW3, GW5, GW6, GW7 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 9.77 | GW4 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 21.50 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | GW4 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.08 | GW3, GW4, GW5, GW6, GW7 | GW4 | GW3, GW7 |
| Saka | ARS | Midfielder | £9.5m | 16.32 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Mbeumo | MUN | Midfielder | £8.0m | 15.85 | GW3, GW4, GW5, GW6, GW7 | — | GW5 |
| Enzo | CHE | Midfielder | £6.9m | 10.91 | GW4, GW5, GW6, GW7 | — | — |

Squad cost: £99.5m.

## One-transfer recommendation

**Mitchell → Silva** (projected weighted XI+captain gain 4.54).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Mitchell | Silva | £4.5m | £5.0m | £0.0m | 4.54 |
| Enzo | Groß | £6.9m | £5.5m | £1.9m | 4.00 |
| Enzo | M.Sangaré | £6.9m | £5.6m | £1.8m | 3.95 |
| Enzo | Schade | £6.9m | £6.0m | £1.4m | 3.93 |
| Pope | Horníček | £5.0m | £5.0m | £0.5m | 3.74 |
| Muñoz | Silva | £5.5m | £5.0m | £1.0m | 3.72 |
| João Pedro | Gonzalo | £7.5m | £6.0m | £2.0m | 3.62 |
| Leno | Horníček | £4.5m | £5.0m | £0.0m | 3.58 |
| Enzo | Gakpo | £6.9m | £7.0m | £0.4m | 3.15 |
| Mitchell | Dedić | £4.5m | £4.5m | £0.5m | 3.13 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
