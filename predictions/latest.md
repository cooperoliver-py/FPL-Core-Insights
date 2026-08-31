# FPL predictions: 2026-2027, GW3

Last generated: 2026-08-31 15:37 UTC

Data commit: `ca9f902dba0a551f7010f2afceb6fbc5a1e10681`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW2: 9/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL are deferred.

Incomplete Gameweeks are not scored in live performance reporting until the official data is finished and checked.

The model is fitted on canonical 2025/26 data; completed 2026/27 results update strictly lagged 3/5-GW and exponentially weighted recent form. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; price and availability are held constant.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.845 | 1.829 | 0.753 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.000 and Spearman is 0.377.

The predicted top 20 averaged 5.14 actual points versus 1.69 for the selectable pool.

## Live-season performance

| GW | MAE | RMSE | Spearman | Top 20 | Pool | XI + captain | FPL avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.528 | 2.580 | 0.553 | 3.40 | 1.88 | 39 | 50 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics.

## Top GW3 player forecasts

| Player | Club | Pos | GW3 | GW4 | GW5 | GW6 | GW7 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 6.05 | 5.16 | 6.05 | 6.71 | 6.05 | 23.87 | 1.99 | high | 5-GW avg pts 10.20; mins 90; xGI 0.80; current GWs 2; fixture Elo diff +83 |
| Haaland | MCI | Forward | 5.40 | 4.23 | 5.37 | 4.23 | 5.40 | 19.71 | 1.27 | high | 5-GW avg pts 7.00; mins 72; xGI 0.70; current GWs 2; fixture Elo diff +192 |
| Mbeumo | MUN | Midfielder | 5.14 | 3.99 | 5.14 | 5.35 | 5.14 | 19.67 | 2.46 | high | 5-GW avg pts 6.00; mins 69; xGI 1.22; current GWs 2; fixture Elo diff +83 |
| Cherki | MCI | Midfielder | 5.11 | 3.72 | 4.80 | 3.72 | 5.11 | 17.96 | 2.36 | high | 5-GW avg pts 5.80; mins 49; xGI 0.45; current GWs 2; fixture Elo diff +192 |
| Semenyo | MCI | Midfielder | 5.08 | 4.09 | 4.74 | 4.09 | 5.08 | 18.48 | 2.17 | high | 5-GW avg pts 5.20; mins 94; xGI 0.31; current GWs 2; fixture Elo diff +192 |
| Foden | MCI | Midfielder | 5.08 | 3.66 | 4.55 | 3.66 | 5.08 | 17.63 | 2.52 | high | 5-GW avg pts 5.20; mins 81; xGI 0.65; current GWs 2; fixture Elo diff +192 |
| Thiago | BRE | Forward | 4.80 | 4.10 | 4.63 | 3.40 | 3.51 | 16.68 | 2.08 | high | 5-GW avg pts 1.60; mins 88; xGI 0.46; current GWs 2; fixture Elo diff -17 |
| Szoboszlai | LIV | Midfielder | 4.64 | 4.52 | 3.82 | 3.69 | 4.45 | 17.01 | 2.43 | high | 5-GW avg pts 5.00; mins 90; xGI 0.61; current GWs 2; fixture Elo diff +79 |
| Gibbs-White | NFO | Midfielder | 4.60 | 3.56 | 4.80 | 4.27 | 2.71 | 16.27 | 2.06 | high | 5-GW avg pts 6.20; mins 72; xGI 0.49; current GWs 2; fixture Elo diff -24 |
| M.Sangaré | BRE | Midfielder | 4.51 | 3.36 | 4.18 | 2.92 | 3.09 | 14.78 | 2.64 | low | 5-GW avg pts 9.00; mins 82; xGI 0.31; current GWs 2; fixture Elo diff -17 |
| Rúben | MCI | Defender | 4.42 | 3.43 | 4.17 | 3.43 | 4.42 | 15.90 | 2.89 | high | 5-GW avg pts 1.00; mins 54; xGI 0.16; current GWs 2; fixture Elo diff +192 |
| Isak | LIV | Forward | 4.38 | 4.63 | 4.28 | 3.83 | 4.47 | 17.33 | 1.93 | high | 5-GW avg pts 2.20; mins 41; xGI 0.42; current GWs 2; fixture Elo diff +79 |
| Anderson | MCI | Midfielder | 4.32 | 3.29 | 4.00 | 3.29 | 4.32 | 15.39 | 2.40 | high | 5-GW avg pts 6.20; mins 77; xGI 0.36; current GWs 2; fixture Elo diff +192 |
| Iwobi | FUL | Midfielder | 4.30 | 3.00 | 3.17 | 4.34 | 4.45 | 15.24 | 2.77 | high | 5-GW avg pts 1.80; mins 67; xGI 0.25; current GWs 2; fixture Elo diff +21 |
| Havertz | ARS | Forward | 4.29 | 4.05 | 4.01 | 4.10 | 3.92 | 16.37 | 2.18 | high | 5-GW avg pts 3.80; mins 46; xGI 0.32; current GWs 1; fixture Elo diff +258 |
| Guéhi | MCI | Defender | 4.25 | 3.12 | 3.84 | 3.12 | 4.25 | 14.86 | 2.48 | high | 5-GW avg pts 5.80; mins 90; xGI 0.30; current GWs 2; fixture Elo diff +192 |
| Wirtz | LIV | Midfielder | 4.15 | 4.25 | 3.92 | 3.16 | 4.14 | 15.81 | 2.11 | high | 5-GW avg pts 1.60; mins 39; xGI 0.30; current GWs 2; fixture Elo diff +79 |
| Virgil | LIV | Defender | 4.09 | 3.68 | 2.94 | 2.80 | 3.53 | 13.84 | 2.13 | high | 5-GW avg pts 4.20; mins 90; xGI 0.25; current GWs 2; fixture Elo diff +79 |
| Gonzalo | FUL | Forward | 4.08 | 3.27 | 3.41 | 4.88 | 4.98 | 16.16 | 2.69 | low | 5-GW avg pts 4.00; mins 90; xGI 0.51; current GWs 2; fixture Elo diff +21 |
| Groß | BHA | Midfielder | 3.90 | 4.32 | 2.70 | 3.83 | 4.03 | 15.05 | 2.74 | high | 5-GW avg pts 5.20; mins 90; xGI 0.32; current GWs 2; fixture Elo diff +29 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rúben | MCI | Defender | £5.5m | 15.90 | GW3, GW4, GW5, GW7 | — | — |
| Mosquera | ARS | Defender | £5.5m | 15.43 | GW3, GW4, GW5, GW6 | — | — |
| De Cuyper | BHA | Defender | £4.6m | 14.52 | GW3, GW4, GW6, GW7 | — | — |
| Dedić | NEW | Defender | £4.5m | 14.18 | GW5, GW6 | — | — |
| Robinson | FUL | Defender | £4.5m | 12.96 | GW6, GW7 | — | — |
| João Pedro | CHE | Forward | £7.6m | 18.05 | GW4, GW5, GW6, GW7 | GW4 | GW5, GW7 |
| Thiago | BRE | Forward | £8.0m | 16.68 | GW3, GW4, GW5 | — | — |
| Gonzalo | FUL | Forward | £6.0m | 16.16 | GW3, GW6, GW7 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.56 | GW4, GW5, GW6 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.49 | GW3, GW7 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 23.87 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | GW4 |
| Mbeumo | MUN | Midfielder | £8.0m | 19.67 | GW3, GW4, GW5, GW6, GW7 | — | GW3, GW6 |
| Semenyo | MCI | Midfielder | £8.5m | 18.48 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Cherki | MCI | Midfielder | £7.6m | 17.96 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.01 | GW3, GW4, GW5, GW7 | — | — |

Squad cost: £98.8m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | LIV | Defender | £6.5m | 13.84 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Botman | NEW | Defender | £5.0m | 12.26 | GW3, GW4, GW5, GW6 | — | — |
| Maguire | MUN | Defender | £5.0m | 11.86 | GW3, GW5, GW6, GW7 | — | — |
| Mitchell | CRY | Defender | £4.5m | 10.70 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Muñoz | CRY | Defender | £5.4m | 8.78 | Bench | — | — |
| João Pedro | CHE | Forward | £7.6m | 18.05 | GW3, GW4, GW5, GW6, GW7 | GW4 | GW5, GW7 |
| Thiago | BRE | Forward | £8.0m | 16.68 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.57 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.49 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 6.36 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 23.87 | GW3, GW4, GW5, GW6, GW7 | GW3, GW5, GW6, GW7 | GW4 |
| Mbeumo | MUN | Midfielder | £8.0m | 19.67 | GW3, GW4, GW5, GW6, GW7 | — | GW3, GW6 |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.01 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Saka | ARS | Midfielder | £9.5m | 13.78 | GW3, GW4, GW5, GW6, GW7 | — | — |
| Enzo | CHE | Midfielder | £6.9m | 10.08 | GW4, GW7 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Enzo → Foden** (projected weighted XI+captain gain 7.15).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Enzo | Foden | £6.9m | £7.0m | £0.4m | 7.15 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.4m | 5.55 |
| Muñoz | Mosquera | £5.4m | £5.5m | £0.4m | 5.09 |
| Enzo | Anderson | £6.9m | £6.4m | £1.0m | 4.92 |
| Enzo | Rayan | £6.9m | £6.5m | £0.9m | 4.80 |
| Enzo | Iwobi | £6.9m | £5.5m | £1.9m | 4.76 |
| Saka | Semenyo | £9.5m | £8.5m | £1.5m | 4.70 |
| Enzo | Dewsbury-Hall | £6.9m | £6.5m | £0.9m | 4.67 |
| Enzo | Groß | £6.9m | £5.5m | £1.9m | 4.57 |
| Enzo | Tzolis | £6.9m | £6.5m | £0.9m | 4.51 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
