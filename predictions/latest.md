# FPL predictions: 2026-2027, GW4

Last generated: 2026-09-05 18:31 UTC

Data commit: `ce03f31b4032f3f89a1aa460ddc8a709ddeb56b6`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW3: 7/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, CHE, EVE, HUL, MUN are deferred.

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
| Szoboszlai | LIV | Midfielder | 5.00 | 4.18 | 3.97 | 4.80 | 5.03 | 18.32 | 2.62 | high | 5-GW avg pts 5.20; mins 90; xGI 0.59; current GWs 3; fixture Elo diff +44 |
| Rogers | CHE | Midfielder | 4.90 | 4.43 | 4.32 | 4.43 | 4.61 | 18.21 | 2.43 | high | 5-GW avg pts 5.40; mins 70; xGI 0.54; current GWs 2; fixture Elo diff +40 |
| Isak | LIV | Forward | 4.74 | 4.01 | 3.89 | 4.32 | 4.84 | 17.39 | 1.93 | high | 5-GW avg pts 4.60; mins 49; xGI 0.47; current GWs 3; fixture Elo diff +44 |
| Haaland | MCI | Forward | 4.64 | 6.26 | 4.64 | 6.10 | 4.64 | 21.04 | 1.36 | high | 5-GW avg pts 6.60; mins 72; xGI 0.68; current GWs 3; fixture Elo diff +141 |
| Thiago | BRE | Forward | 4.52 | 5.24 | 4.01 | 4.10 | 5.46 | 18.59 | 2.32 | high | 5-GW avg pts 1.60; mins 88; xGI 0.52; current GWs 3; fixture Elo diff -3 |
| Groß | BHA | Midfielder | 4.41 | 2.66 | 4.04 | 4.00 | 2.99 | 14.62 | 2.66 | high | 5-GW avg pts 4.20; mins 90; xGI 0.37; current GWs 3; fixture Elo diff +6 |
| Palmer | CHE | Midfielder | 4.37 | 4.28 | 4.03 | 4.28 | 4.46 | 17.12 | 1.78 | high | 5-GW avg pts 6.40; mins 88; xGI 0.37; current GWs 2; fixture Elo diff +40 |
| Gakpo | LIV | Midfielder | 4.36 | 3.63 | 3.07 | 3.97 | 4.29 | 15.44 | 2.17 | high | 5-GW avg pts 6.40; mins 83; xGI 0.47; current GWs 3; fixture Elo diff +44 |
| Khalaili | CRY | Defender | 4.34 | 3.69 | 3.81 | 3.63 | 3.81 | 15.54 | 3.11 | medium | 5-GW avg pts 2.00; mins 66; xGI 0.30; current GWs 3; fixture Elo diff +11 |
| Wirtz | LIV | Midfielder | 4.11 | 3.65 | 3.05 | 3.99 | 4.11 | 15.09 | 2.04 | high | 5-GW avg pts 2.20; mins 57; xGI 0.34; current GWs 3; fixture Elo diff +44 |
| Havertz | ARS | Forward | 4.01 | 3.84 | 3.90 | 3.81 | 3.90 | 15.60 | 2.08 | high | 5-GW avg pts 4.20; mins 64; xGI 0.33; current GWs 2; fixture Elo diff +264 |
| De Cuyper | BHA | Defender | 4.00 | 2.77 | 3.60 | 3.70 | 3.09 | 13.82 | 2.94 | high | 5-GW avg pts 4.60; mins 76; xGI 0.54; current GWs 3; fixture Elo diff +6 |
| Gomez | BHA | Midfielder | 4.00 | 2.61 | 3.76 | 3.75 | 2.86 | 13.70 | 2.74 | high | 5-GW avg pts 3.00; mins 70; xGI 0.46; current GWs 3; fixture Elo diff +6 |
| Tavernier | BOU | Midfielder | 3.99 | 3.58 | 3.90 | 4.12 | 3.49 | 15.31 | 2.55 | high | 5-GW avg pts 6.60; mins 90; xGI 0.55; current GWs 3; fixture Elo diff +26 |
| Semenyo | MCI | Midfielder | 3.91 | 4.65 | 3.91 | 4.80 | 3.92 | 16.94 | 1.99 | high | 5-GW avg pts 4.00; mins 76; xGI 0.27; current GWs 3; fixture Elo diff +141 |
| Tarkowski | EVE | Defender | 3.89 | 4.46 | 4.40 | 3.82 | 1.85 | 15.21 | 2.53 | high | 5-GW avg pts 7.80; mins 90; xGI 0.21; current GWs 2; fixture Elo diff +2 |
| Kamada | CRY | Midfielder | 3.87 | 3.24 | 3.26 | 3.22 | 3.26 | 13.59 | 2.72 | high | 5-GW avg pts 3.00; mins 81; xGI 0.14; current GWs 3; fixture Elo diff +11 |
| Yeremy | CRY | Midfielder | 3.81 | 3.29 | 3.48 | 3.24 | 3.48 | 13.91 | 2.53 | high | 5-GW avg pts 3.20; mins 56; xGI 0.26; current GWs 3; fixture Elo diff +11 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Khalaili | CRY | Defender | £5.0m | 15.54 | GW4, GW5, GW6, GW8 | — | — |
| Tarkowski | EVE | Defender | £6.0m | 15.21 | GW4, GW5, GW6, GW7 | — | — |
| Castagne | FUL | Defender | £4.5m | 14.45 | GW6, GW7, GW8 | — | — |
| Milenković | NFO | Defender | £5.5m | 13.89 | GW5, GW8 | — | — |
| De Cuyper | BHA | Defender | £4.7m | 13.82 | GW4, GW7 | — | — |
| João Pedro | CHE | Forward | £7.7m | 21.45 | GW4, GW5, GW6, GW7, GW8 | GW4 | GW5, GW6, GW7, GW8 |
| Thiago | BRE | Forward | £8.0m | 18.59 | GW4, GW5, GW6, GW8 | — | — |
| Gonzalo | FUL | Forward | £6.0m | 16.47 | GW6, GW7, GW8 | — | — |
| Henderson | CRY | Goalkeeper | £5.0m | 13.39 | GW4, GW5 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.07 | GW6, GW7, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 23.97 | GW4, GW5, GW6, GW7, GW8 | GW5, GW6, GW7, GW8 | GW4 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.32 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Rogers | CHE | Midfielder | £7.5m | 18.21 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 17.07 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Semenyo | MCI | Midfielder | £8.5m | 16.94 | GW4, GW5, GW7 | — | — |

Squad cost: £99.8m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | LIV | Defender | £6.5m | 13.13 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Botman | NEW | Defender | £5.0m | 12.84 | GW4, GW5, GW6, GW8 | — | — |
| Maguire | MUN | Defender | £5.0m | 12.48 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 11.15 | GW4, GW6, GW7, GW8 | — | — |
| Muñoz | NFO | Defender | £5.4m | 8.25 | Bench | — | — |
| João Pedro | CHE | Forward | £7.7m | 21.45 | GW4, GW5, GW6, GW7, GW8 | GW4 | GW5, GW6, GW7, GW8 |
| Thiago | BRE | Forward | £8.0m | 18.59 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.57 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.07 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 2.42 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 23.97 | GW4, GW5, GW6, GW7, GW8 | GW5, GW6, GW7, GW8 | GW4 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.32 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 17.07 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Saka | ARS | Midfielder | £9.5m | 15.16 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Enzo | MCI | Midfielder | £6.9m | 11.36 | GW5, GW7 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Muñoz → Khalaili** (projected weighted XI+captain gain 4.52).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Muñoz | Khalaili | £5.4m | £5.0m | £0.9m | 4.52 |
| Mitchell | Khalaili | £4.5m | £5.0m | £0.0m | 4.15 |
| Enzo | Anderson | £6.9m | £6.4m | £1.0m | 4.01 |
| Muñoz | Castagne | £5.4m | £4.5m | £1.4m | 3.90 |
| Enzo | Gakpo | £6.9m | £7.1m | £0.3m | 3.88 |
| Enzo | Tavernier | £6.9m | £6.0m | £1.4m | 3.75 |
| Enzo | Wirtz | £6.9m | £7.4m | £0.0m | 3.53 |
| Muñoz | Silva | £5.4m | £5.0m | £0.9m | 3.50 |
| Enzo | Dewsbury-Hall | £6.9m | £6.5m | £0.9m | 3.43 |
| Mitchell | Castagne | £4.5m | £4.5m | £0.5m | 3.39 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
