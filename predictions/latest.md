# FPL predictions: 2026-2027, GW3

Last generated: 2026-09-01 08:44 UTC

Data commit: `28b7f8f2c2d37fb990706ef3bc09c0229839db24`

## Data freshness

All scheduled Premier League fixtures before GW3 are complete.

The model is fitted on canonical 2025/26 data; completed 2026/27 results update strictly lagged 3/5-GW and exponentially weighted recent form. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; price and availability are held constant.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.845 | 1.831 | 0.752 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.002 and Spearman is 0.377.

The predicted top 20 averaged 5.20 actual points versus 1.69 for the selectable pool.

## Live-season performance

| GW | MAE | RMSE | Spearman | Top 20 | Pool | XI + captain | FPL avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.528 | 2.580 | 0.553 | 3.40 | 1.88 | 39 | 50 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics.

## Top GW3 player forecasts

| Player | Club | Pos | GW3 | GW4 | GW5 | GW6 | GW7 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 6.28 | 5.14 | 6.28 | 6.86 | 6.28 | 24.50 | 2.04 | high | 5-GW avg pts 10.20; mins 90; xGI 0.86; current GWs 2; fixture Elo diff +83 |
| Mbeumo | MUN | Midfielder | 5.52 | 4.41 | 5.52 | 5.73 | 5.52 | 21.23 | 2.65 | high | 5-GW avg pts 6.00; mins 69; xGI 1.25; current GWs 2; fixture Elo diff +83 |
| Haaland | MCI | Forward | 5.44 | 4.51 | 5.70 | 4.51 | 5.44 | 20.48 | 1.32 | high | 5-GW avg pts 7.00; mins 72; xGI 0.70; current GWs 2; fixture Elo diff +192 |
| Semenyo | MCI | Midfielder | 5.36 | 4.25 | 4.90 | 4.25 | 5.36 | 19.29 | 2.27 | high | 5-GW avg pts 5.20; mins 94; xGI 0.31; current GWs 2; fixture Elo diff +192 |
| Cherki | MCI | Midfielder | 5.25 | 3.84 | 5.00 | 3.84 | 5.25 | 18.53 | 2.41 | high | 5-GW avg pts 5.80; mins 49; xGI 0.45; current GWs 2; fixture Elo diff +192 |
| Foden | MCI | Midfielder | 5.23 | 3.65 | 4.58 | 3.65 | 5.23 | 17.87 | 2.55 | high | 5-GW avg pts 5.20; mins 81; xGI 0.65; current GWs 2; fixture Elo diff +192 |
| Thiago | BRE | Forward | 5.13 | 4.43 | 4.96 | 3.73 | 3.84 | 18.00 | 2.25 | high | 5-GW avg pts 1.60; mins 88; xGI 0.46; current GWs 2; fixture Elo diff -17 |
| Szoboszlai | LIV | Midfielder | 5.06 | 4.87 | 4.10 | 3.89 | 4.77 | 18.29 | 2.61 | high | 5-GW avg pts 5.00; mins 90; xGI 0.61; current GWs 2; fixture Elo diff +79 |
| Gibbs-White | NFO | Midfielder | 4.93 | 3.85 | 4.93 | 4.60 | 2.98 | 17.35 | 2.20 | high | 5-GW avg pts 6.20; mins 72; xGI 0.49; current GWs 2; fixture Elo diff -24 |
| M.Sangaré | BRE | Midfielder | 4.80 | 3.35 | 4.42 | 2.91 | 3.24 | 15.33 | 2.74 | low | 5-GW avg pts 9.00; mins 82; xGI 0.31; current GWs 2; fixture Elo diff -17 |
| Isak | LIV | Forward | 4.62 | 4.87 | 4.52 | 4.05 | 4.70 | 18.28 | 2.03 | high | 5-GW avg pts 2.20; mins 41; xGI 0.42; current GWs 2; fixture Elo diff +79 |
| Guéhi | MCI | Defender | 4.31 | 3.20 | 3.85 | 3.20 | 4.31 | 15.10 | 2.52 | high | 5-GW avg pts 5.80; mins 90; xGI 0.30; current GWs 2; fixture Elo diff +192 |
| Saka | ARS | Midfielder | 4.26 | 3.69 | 3.51 | 4.20 | 3.58 | 15.49 | 1.63 | high | 5-GW avg pts 6.40; mins 65; xGI 0.43; current GWs 2; fixture Elo diff +258 |
| Anderson | MCI | Midfielder | 4.26 | 3.46 | 4.08 | 3.46 | 4.26 | 15.60 | 2.44 | high | 5-GW avg pts 6.20; mins 77; xGI 0.36; current GWs 2; fixture Elo diff +192 |
| Iwobi | FUL | Midfielder | 4.25 | 2.95 | 3.12 | 4.27 | 4.37 | 15.01 | 2.73 | high | 5-GW avg pts 1.80; mins 67; xGI 0.25; current GWs 2; fixture Elo diff +21 |
| Rúben | MCI | Defender | 4.22 | 3.41 | 4.01 | 3.41 | 4.22 | 15.42 | 2.80 | high | 5-GW avg pts 1.00; mins 54; xGI 0.16; current GWs 2; fixture Elo diff +192 |
| Wirtz | LIV | Midfielder | 4.15 | 4.25 | 3.89 | 3.12 | 4.14 | 15.76 | 2.10 | high | 5-GW avg pts 1.60; mins 39; xGI 0.30; current GWs 2; fixture Elo diff +79 |
| Havertz | ARS | Forward | 4.07 | 4.01 | 3.84 | 3.90 | 3.81 | 15.77 | 2.10 | high | 5-GW avg pts 4.20; mins 64; xGI 0.33; current GWs 2; fixture Elo diff +258 |
| Gonzalo | FUL | Forward | 4.05 | 3.24 | 3.38 | 4.64 | 4.75 | 15.77 | 2.63 | low | 5-GW avg pts 4.00; mins 90; xGI 0.51; current GWs 2; fixture Elo diff +21 |
| Virgil | LIV | Defender | 4.05 | 3.86 | 3.10 | 2.87 | 3.80 | 14.29 | 2.20 | high | 5-GW avg pts 4.20; mins 90; xGI 0.25; current GWs 2; fixture Elo diff +79 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rúben | MCI | Defender | £5.5m | 15.42 | GW3, GW5, GW7 | — | — |
| De Cuyper | BHA | Defender | £4.7m | 14.95 | GW3, GW4, GW6, GW7 | — | — |
| Tarkowski | EVE | Defender | £6.0m | 14.80 | GW4, GW5, GW6 | — | — |
| Silva | BOU | Defender | £5.0m | 14.47 | GW3, GW4, GW7 | — | — |
| Dedić | NEW | Defender | £4.5m | 13.74 | GW5, GW6 | — | — |
| João Pedro | CHE | Forward | £7.6m | 18.94 | GW4, GW5, GW6, GW7 | GW4 | GW5 |
| Thiago | BRE | Forward | £8.0m | 18.00 | GW3, GW4, GW5 | — | — |
| Gonzalo | FUL | Forward | £6.0m | 15.77 | GW3, GW6, GW7 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.03 | GW4, GW5 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.43 | GW3, GW6, GW7 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.50 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | GW4 |
| Mbeumo | MUN | Midfielder | £8.0m | 21.23 | GW3, GW4, GW5, GW6, GW7 | — | GW3, GW6, GW7 |
| Semenyo | MCI | Midfielder | £8.5m | 19.29 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Cherki | MCI | Midfielder | £7.7m | 18.53 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.29 | GW3, GW4, GW5, GW6, GW7 | — | — |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | LIV | Defender | £6.5m | 14.29 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Botman | NEW | Defender | £5.0m | 13.10 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Maguire | MUN | Defender | £5.0m | 12.34 | GW3, GW5, GW6, GW7 | — | — |
| Mitchell | CRY | Defender | £4.5m | 10.78 | GW3, GW4, GW5, GW6 | — | — |
| Muñoz | CRY | Defender | £5.4m | 8.89 | Bench | — | — |
| João Pedro | CHE | Forward | £7.6m | 18.94 | GW3, GW4, GW5, GW6, GW7 | GW4 | GW5 |
| Thiago | BRE | Forward | £8.0m | 18.00 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.57 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.43 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 6.32 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.50 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | GW4 |
| Mbeumo | MUN | Midfielder | £8.0m | 21.23 | GW3, GW4, GW5, GW6, GW7 | — | GW3, GW6, GW7 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.29 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Saka | ARS | Midfielder | £9.5m | 15.49 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Enzo | CHE | Midfielder | £6.9m | 10.00 | GW4, GW7 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Enzo → Foden** (projected weighted XI+captain gain 7.31).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Enzo | Foden | £6.9m | £7.0m | £0.4m | 7.31 |
| Enzo | Anderson | £6.9m | £6.4m | £1.0m | 5.04 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.4m | 4.91 |
| Enzo | M.Sangaré | £6.9m | £5.6m | £1.8m | 4.77 |
| Enzo | Rayan | £6.9m | £6.5m | £0.9m | 4.70 |
| Enzo | Groß | £6.9m | £5.5m | £1.9m | 4.69 |
| Enzo | Dewsbury-Hall | £6.9m | £6.5m | £0.9m | 4.49 |
| Muñoz | Hill | £5.4m | £5.5m | £0.4m | 4.48 |
| Enzo | Iwobi | £6.9m | £5.5m | £1.9m | 4.45 |
| Muñoz | De Cuyper | £5.4m | £4.7m | £1.2m | 4.44 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
