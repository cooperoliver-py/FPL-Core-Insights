# FPL predictions: 2026-2027, GW4

Last generated: 2026-09-05 04:50 UTC

Data commit: `a7fed41e88eabe90a085b876f9385cfd2fab1d85`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW3: 1/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, BHA, BOU, BRE, CHE, COV, CRY, EVE, FUL, HUL, LEE, MCI, MUN, NEW, NFO, SUN, TOT are deferred.

Incomplete Gameweeks are not scored in live performance reporting until the official data is finished and checked.

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

## Top GW4 player forecasts

| Player | Club | Pos | GW4 | GW5 | GW6 | GW7 | GW8 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| João Pedro | CHE | Forward | 5.76 | 5.41 | 4.87 | 5.17 | 5.50 | 21.45 | 2.79 | high | 5-GW avg pts 4.60; mins 72; xGI 0.55; current GWs 2; fixture Elo diff +40 |
| B.Fernandes | MUN | Midfielder | 5.10 | 6.28 | 6.86 | 6.28 | 5.55 | 23.97 | 2.00 | high | 5-GW avg pts 10.20; mins 90; xGI 0.86; current GWs 2; fixture Elo diff +69 |
| Szoboszlai | LIV | Midfielder | 5.00 | 4.18 | 3.97 | 4.80 | 5.03 | 18.32 | 2.62 | high | 5-GW avg pts 5.20; mins 90; xGI 0.58; current GWs 3; fixture Elo diff +44 |
| Rogers | CHE | Midfielder | 4.90 | 4.43 | 4.32 | 4.43 | 4.61 | 18.21 | 2.43 | high | 5-GW avg pts 5.40; mins 70; xGI 0.54; current GWs 2; fixture Elo diff +40 |
| Isak | LIV | Forward | 4.74 | 4.01 | 3.89 | 4.32 | 4.84 | 17.39 | 1.93 | high | 5-GW avg pts 4.60; mins 49; xGI 0.47; current GWs 3; fixture Elo diff +44 |
| Thiago | BRE | Forward | 4.66 | 5.43 | 4.02 | 4.26 | 5.36 | 18.96 | 2.37 | high | 5-GW avg pts 1.60; mins 88; xGI 0.46; current GWs 2; fixture Elo diff -3 |
| Groß | BHA | Midfielder | 4.47 | 2.81 | 4.01 | 4.07 | 3.16 | 14.95 | 2.72 | high | 5-GW avg pts 5.20; mins 90; xGI 0.32; current GWs 2; fixture Elo diff +6 |
| Haaland | MCI | Forward | 4.44 | 5.64 | 4.44 | 5.39 | 4.44 | 19.50 | 1.26 | high | 5-GW avg pts 7.00; mins 72; xGI 0.70; current GWs 2; fixture Elo diff +141 |
| Palmer | CHE | Midfielder | 4.37 | 4.28 | 4.03 | 4.28 | 4.46 | 17.12 | 1.78 | high | 5-GW avg pts 6.40; mins 88; xGI 0.37; current GWs 2; fixture Elo diff +40 |
| Gakpo | LIV | Midfielder | 4.36 | 3.63 | 3.07 | 3.97 | 4.29 | 15.44 | 2.17 | high | 5-GW avg pts 6.40; mins 83; xGI 0.47; current GWs 3; fixture Elo diff +44 |
| Wirtz | LIV | Midfielder | 4.11 | 3.65 | 3.05 | 3.99 | 4.11 | 15.09 | 2.04 | high | 5-GW avg pts 2.20; mins 57; xGI 0.34; current GWs 3; fixture Elo diff +44 |
| Rayan | BOU | Midfielder | 4.10 | 3.61 | 3.97 | 4.13 | 3.45 | 15.48 | 2.38 | high | 5-GW avg pts 3.60; mins 82; xGI 0.20; current GWs 2; fixture Elo diff +26 |
| Semenyo | MCI | Midfielder | 4.07 | 4.76 | 4.07 | 5.32 | 4.07 | 17.77 | 2.09 | high | 5-GW avg pts 5.20; mins 94; xGI 0.31; current GWs 2; fixture Elo diff +141 |
| Havertz | ARS | Forward | 4.01 | 3.84 | 3.90 | 3.81 | 3.90 | 15.60 | 2.08 | high | 5-GW avg pts 4.20; mins 64; xGI 0.33; current GWs 2; fixture Elo diff +264 |
| Foden | MCI | Midfielder | 4.01 | 4.95 | 4.01 | 5.60 | 4.01 | 18.00 | 2.57 | high | 5-GW avg pts 5.20; mins 81; xGI 0.65; current GWs 2; fixture Elo diff +141 |
| De Cuyper | BHA | Defender | 3.99 | 2.85 | 3.70 | 3.86 | 3.19 | 14.14 | 3.01 | high | 5-GW avg pts 6.80; mins 78; xGI 0.74; current GWs 2; fixture Elo diff +6 |
| Marmoush | TOT | Forward | 3.97 | 3.59 | 3.30 | 3.98 | 3.57 | 14.77 | 2.11 | high | 5-GW avg pts 3.40; mins 42; xGI 0.17; current GWs 2; fixture Elo diff -50 |
| Tarkowski | EVE | Defender | 3.89 | 4.46 | 4.40 | 3.82 | 1.85 | 15.21 | 2.53 | high | 5-GW avg pts 7.80; mins 90; xGI 0.21; current GWs 2; fixture Elo diff +2 |
| Calvert-Lewin | LEE | Forward | 3.87 | 4.08 | 2.17 | 3.38 | 4.30 | 14.23 | 2.37 | high | 5-GW avg pts 5.00; mins 86; xGI 0.50; current GWs 2; fixture Elo diff -74 |
| Wharton | CRY | Midfielder | 3.86 | 3.15 | 3.33 | 3.14 | 3.33 | 13.55 | 2.46 | high | 5-GW avg pts 4.60; mins 81; xGI 0.24; current GWs 2; fixture Elo diff +11 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tarkowski | EVE | Defender | £6.0m | 15.21 | GW4, GW5, GW6, GW7 | — | — |
| Hill | BOU | Defender | £5.5m | 14.74 | GW4, GW7, GW8 | — | — |
| Dedić | NEW | Defender | £4.5m | 14.70 | GW5, GW6 | — | — |
| Muharemović | LEE | Defender | £5.0m | 14.51 | GW4, GW5, GW8 | — | — |
| Robinson | FUL | Defender | £4.5m | 13.97 | GW6, GW7, GW8 | — | — |
| João Pedro | CHE | Forward | £7.7m | 21.45 | GW4, GW5, GW6, GW7, GW8 | GW4 | GW6, GW8 |
| Thiago | BRE | Forward | £8.0m | 18.96 | GW4, GW5, GW6, GW8 | — | GW5 |
| Gonzalo | FUL | Forward | £6.0m | 16.30 | GW6, GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 14.15 | GW4, GW5, GW6 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.91 | GW7, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 23.97 | GW4, GW5, GW6, GW7, GW8 | GW5, GW6, GW7, GW8 | GW4 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.32 | GW4, GW5, GW7, GW8 | — | — |
| Rogers | CHE | Midfielder | £7.5m | 18.21 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Foden | MCI | Midfielder | £7.0m | 18.00 | GW4, GW5, GW6, GW7 | — | GW7 |
| Semenyo | MCI | Midfielder | £8.5m | 17.77 | GW4, GW5, GW6, GW7, GW8 | — | — |

Squad cost: £98.7m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 13.37 | GW4, GW5, GW6, GW8 | — | — |
| Virgil | LIV | Defender | £6.5m | 13.13 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Maguire | MUN | Defender | £5.0m | 12.48 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 11.41 | GW4, GW6, GW7, GW8 | — | — |
| Muñoz | NFO | Defender | £5.4m | 9.00 | Bench | — | — |
| João Pedro | CHE | Forward | £7.7m | 21.45 | GW4, GW5, GW6, GW7, GW8 | GW4 | GW6, GW7, GW8 |
| Thiago | BRE | Forward | £8.0m | 18.96 | GW4, GW5, GW6, GW7, GW8 | — | GW5 |
| Mheuka | CHE | Forward | £4.5m | 0.57 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.91 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 6.37 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 23.97 | GW4, GW5, GW6, GW7, GW8 | GW5, GW6, GW7, GW8 | GW4 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.32 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 17.07 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Saka | ARS | Midfielder | £9.5m | 15.16 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Enzo | MCI | Midfielder | £6.9m | 11.05 | GW5, GW7 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Enzo → Foden** (projected weighted XI+captain gain 6.53).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Enzo | Foden | £6.9m | £7.0m | £0.4m | 6.53 |
| Enzo | Anderson | £6.9m | £6.4m | £1.0m | 4.24 |
| Enzo | M.Sangaré | £6.9m | £5.7m | £1.7m | 4.06 |
| Enzo | Rayan | £6.9m | £6.5m | £0.9m | 4.02 |
| Enzo | Gakpo | £6.9m | £7.1m | £0.3m | 3.97 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.4m | 3.76 |
| Enzo | Wirtz | £6.9m | £7.4m | £0.0m | 3.63 |
| Enzo | Dewsbury-Hall | £6.9m | £6.5m | £0.9m | 3.60 |
| Muñoz | Hill | £5.4m | £5.5m | £0.4m | 3.55 |
| Enzo | Iwobi | £6.9m | £5.5m | £1.9m | 3.55 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
