# FPL predictions: 2026-2027, GW3

Last generated: 2026-09-03 04:53 UTC

Data commit: `8b8351bec5fede578ee18031aa4116ee2aab9f19`

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
| 2 | 1.211 | 2.131 | 0.697 | 6.60 | 1.74 | 112 | 81 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics.

## Top GW3 player forecasts

| Player | Club | Pos | GW3 | GW4 | GW5 | GW6 | GW7 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 6.28 | 5.10 | 6.28 | 6.86 | 6.28 | 24.47 | 2.04 | high | 5-GW avg pts 10.20; mins 90; xGI 0.86; current GWs 2; fixture Elo diff +83 |
| Foden | MCI | Midfielder | 5.60 | 4.01 | 4.95 | 4.01 | 5.60 | 19.33 | 2.76 | high | 5-GW avg pts 5.20; mins 81; xGI 0.65; current GWs 2; fixture Elo diff +192 |
| Thiago | BRE | Forward | 5.59 | 4.66 | 5.43 | 4.02 | 4.26 | 19.50 | 2.44 | high | 5-GW avg pts 1.60; mins 88; xGI 0.46; current GWs 2; fixture Elo diff -17 |
| Haaland | MCI | Forward | 5.39 | 4.44 | 5.64 | 4.44 | 5.39 | 20.24 | 1.31 | high | 5-GW avg pts 7.00; mins 72; xGI 0.70; current GWs 2; fixture Elo diff +192 |
| Semenyo | MCI | Midfielder | 5.32 | 4.07 | 4.76 | 4.07 | 5.32 | 18.82 | 2.21 | high | 5-GW avg pts 5.20; mins 94; xGI 0.31; current GWs 2; fixture Elo diff +192 |
| Cherki | MCI | Midfielder | 5.27 | 3.86 | 5.02 | 3.86 | 5.27 | 18.61 | 2.42 | high | 5-GW avg pts 5.80; mins 49; xGI 0.45; current GWs 2; fixture Elo diff +192 |
| Szoboszlai | LIV | Midfielder | 4.90 | 4.79 | 4.02 | 3.81 | 4.69 | 17.91 | 2.56 | high | 5-GW avg pts 5.00; mins 90; xGI 0.61; current GWs 2; fixture Elo diff +79 |
| Isak | LIV | Forward | 4.73 | 5.19 | 4.59 | 4.40 | 4.81 | 19.04 | 2.12 | high | 5-GW avg pts 2.20; mins 41; xGI 0.42; current GWs 2; fixture Elo diff +79 |
| M.Sangaré | BRE | Midfielder | 4.73 | 3.51 | 4.39 | 3.07 | 3.36 | 15.56 | 2.73 | low | 5-GW avg pts 9.00; mins 82; xGI 0.31; current GWs 2; fixture Elo diff -17 |
| Ndiaye | MCI | Midfielder | 4.68 | 3.03 | 3.58 | 3.03 | 4.68 | 15.19 | 2.53 | high | 5-GW avg pts 3.80; mins 90; xGI 0.25; current GWs 2; fixture Elo diff +192 |
| Gibbs-White | NFO | Midfielder | 4.66 | 3.58 | 4.88 | 4.33 | 2.86 | 16.54 | 2.09 | high | 5-GW avg pts 6.20; mins 72; xGI 0.49; current GWs 2; fixture Elo diff -24 |
| Anderson | MCI | Midfielder | 4.60 | 3.61 | 4.24 | 3.61 | 4.60 | 16.53 | 2.58 | high | 5-GW avg pts 6.20; mins 77; xGI 0.36; current GWs 2; fixture Elo diff +192 |
| Guéhi | MCI | Defender | 4.57 | 3.34 | 3.90 | 3.34 | 4.57 | 15.77 | 2.63 | high | 5-GW avg pts 5.80; mins 90; xGI 0.30; current GWs 2; fixture Elo diff +192 |
| Mbeumo | MUN | Midfielder | 4.50 | 3.53 | 4.50 | 4.71 | 4.50 | 17.27 | 2.16 | high | 5-GW avg pts 6.00; mins 69; xGI 1.25; current GWs 2; fixture Elo diff +83 |
| Iwobi | FUL | Midfielder | 4.35 | 2.99 | 3.22 | 4.29 | 4.46 | 15.30 | 2.78 | high | 5-GW avg pts 1.80; mins 67; xGI 0.25; current GWs 2; fixture Elo diff +21 |
| Saka | ARS | Midfielder | 4.25 | 3.64 | 3.53 | 4.19 | 3.54 | 15.41 | 1.62 | high | 5-GW avg pts 6.40; mins 65; xGI 0.43; current GWs 2; fixture Elo diff +258 |
| Rúben | MCI | Defender | 4.22 | 3.54 | 4.03 | 3.54 | 4.22 | 15.65 | 2.85 | high | 5-GW avg pts 1.00; mins 54; xGI 0.16; current GWs 2; fixture Elo diff +192 |
| Wirtz | LIV | Midfielder | 4.19 | 4.44 | 4.04 | 3.36 | 4.26 | 16.32 | 2.18 | high | 5-GW avg pts 1.60; mins 39; xGI 0.30; current GWs 2; fixture Elo diff +79 |
| Virgil | LIV | Defender | 4.17 | 3.97 | 3.21 | 3.07 | 3.88 | 14.79 | 2.28 | high | 5-GW avg pts 4.20; mins 90; xGI 0.25; current GWs 2; fixture Elo diff +79 |
| Gonzalo | FUL | Forward | 4.15 | 3.24 | 3.38 | 4.73 | 4.84 | 15.99 | 2.66 | low | 5-GW avg pts 4.00; mins 90; xGI 0.51; current GWs 2; fixture Elo diff +21 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Guéhi | MCI | Defender | £6.0m | 15.77 | GW3, GW5, GW7 | — | — |
| Tarkowski | EVE | Defender | £6.0m | 15.29 | GW4, GW5, GW6, GW7 | — | — |
| De Cuyper | BHA | Defender | £4.7m | 14.65 | GW3, GW4, GW6, GW7 | — | — |
| Dedić | NEW | Defender | £4.5m | 14.40 | GW5, GW6 | — | — |
| Muharemović | LEE | Defender | £5.0m | 14.08 | GW3, GW4 | — | — |
| Thiago | BRE | Forward | £8.0m | 19.50 | GW3, GW4, GW5, GW6, GW7 | — | GW5 |
| Isak | LIV | Forward | £9.0m | 19.04 | GW3, GW4, GW5, GW6, GW7 | — | GW4 |
| João Pedro | CHE | Forward | £7.7m | 18.65 | GW4, GW5, GW6, GW7 | GW4 | GW6 |
| Horníček | NEW | Goalkeeper | £5.0m | 14.00 | GW3, GW4, GW5, GW6 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.43 | GW7 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.47 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | — |
| Foden | MCI | Midfielder | £7.0m | 19.33 | GW3, GW4, GW5, GW6, GW7 | — | GW3, GW7 |
| Cherki | MCI | Midfielder | £7.7m | 18.61 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.91 | GW3, GW4, GW6, GW7 | — | — |
| M.Sangaré | BRE | Midfielder | £5.7m | 15.56 | GW3, GW5 | — | — |

Squad cost: £99.8m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | LIV | Defender | £6.5m | 14.79 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Botman | NEW | Defender | £5.0m | 13.14 | GW3, GW4, GW5, GW6 | — | — |
| Maguire | MUN | Defender | £5.0m | 12.58 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Mitchell | CRY | Defender | £4.5m | 11.17 | GW4, GW6, GW7 | — | — |
| Muñoz | NFO | Defender | £5.4m | 9.11 | Bench | — | — |
| Thiago | BRE | Forward | £8.0m | 19.50 | GW3, GW4, GW5, GW6, GW7 | — | GW3, GW5 |
| João Pedro | CHE | Forward | £7.7m | 18.65 | GW3, GW4, GW5, GW6, GW7 | GW4 | GW6, GW7 |
| Mheuka | CHE | Forward | £4.5m | 0.57 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.43 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 6.32 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.47 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | GW4 |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.91 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Mbeumo | MUN | Midfielder | £8.0m | 17.27 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Saka | ARS | Midfielder | £9.5m | 15.41 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Enzo | MCI | Midfielder | £6.9m | 11.28 | GW3, GW5, GW7 | — | — |

Squad cost: £99.5m.

## One-transfer recommendation

**Enzo → Foden** (projected weighted XI+captain gain 7.75).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Enzo | Foden | £6.9m | £7.0m | £0.4m | 7.75 |
| Enzo | Anderson | £6.9m | £6.4m | £1.0m | 4.94 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.4m | 4.59 |
| Enzo | Rayan | £6.9m | £6.5m | £0.9m | 4.22 |
| Enzo | M.Sangaré | £6.9m | £5.7m | £1.7m | 3.98 |
| Saka | Foden | £9.5m | £7.0m | £3.0m | 3.92 |
| Muñoz | Hill | £5.4m | £5.5m | £0.4m | 3.88 |
| Enzo | Groß | £6.9m | £5.5m | £1.9m | 3.87 |
| Enzo | Iwobi | £6.9m | £5.5m | £1.9m | 3.71 |
| Muñoz | De Cuyper | £5.4m | £4.7m | £1.2m | 3.62 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
