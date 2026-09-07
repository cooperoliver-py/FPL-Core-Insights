# FPL predictions: 2026-2027, GW4

Last generated: 2026-09-07 05:05 UTC

Data commit: `11fdac375453f5f12ca4c114a3de53f38e1d95fd`

## Data freshness

All scheduled Premier League fixtures before GW4 are complete.

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
| Rogers | CHE | Midfielder | 5.14 | 4.65 | 4.28 | 4.65 | 4.84 | 18.91 | 2.49 | high | 5-GW avg pts 6.20; mins 69; xGI 0.53; current GWs 3; fixture Elo diff +40 |
| João Pedro | CHE | Forward | 5.05 | 4.88 | 4.46 | 4.64 | 4.90 | 19.19 | 2.49 | high | 5-GW avg pts 4.40; mins 72; xGI 0.52; current GWs 3; fixture Elo diff +40 |
| B.Fernandes | MUN | Midfielder | 5.04 | 6.37 | 6.95 | 6.37 | 5.67 | 24.20 | 2.02 | high | 5-GW avg pts 10.00; mins 90; xGI 0.87; current GWs 3; fixture Elo diff +69 |
| Szoboszlai | LIV | Midfielder | 5.00 | 4.18 | 3.97 | 4.80 | 5.03 | 18.32 | 2.62 | high | 5-GW avg pts 5.20; mins 90; xGI 0.59; current GWs 3; fixture Elo diff +44 |
| Isak | LIV | Forward | 4.74 | 4.01 | 3.89 | 4.32 | 4.84 | 17.39 | 1.93 | high | 5-GW avg pts 4.60; mins 49; xGI 0.47; current GWs 3; fixture Elo diff +44 |
| Haaland | MCI | Forward | 4.64 | 6.26 | 4.64 | 6.10 | 4.64 | 21.04 | 1.36 | high | 5-GW avg pts 6.60; mins 72; xGI 0.74; current GWs 3; fixture Elo diff +141 |
| Palmer | CHE | Midfielder | 4.55 | 4.46 | 4.18 | 4.46 | 4.64 | 17.81 | 1.86 | high | 5-GW avg pts 6.20; mins 88; xGI 0.39; current GWs 3; fixture Elo diff +40 |
| Thiago | BRE | Forward | 4.52 | 5.24 | 4.01 | 4.10 | 5.46 | 18.59 | 2.35 | high | 5-GW avg pts 1.60; mins 88; xGI 0.52; current GWs 3; fixture Elo diff -3 |
| Saka | ARS | Midfielder | 4.48 | 4.53 | 4.60 | 4.44 | 4.60 | 18.10 | 1.91 | high | 5-GW avg pts 6.40; mins 67; xGI 0.47; current GWs 3; fixture Elo diff +264 |
| Gabriel | ARS | Defender | 4.47 | 4.25 | 4.34 | 4.25 | 4.34 | 17.35 | 2.17 | high | 5-GW avg pts 4.40; mins 81; xGI 0.12; current GWs 3; fixture Elo diff +264 |
| Groß | BHA | Midfielder | 4.41 | 2.66 | 4.04 | 4.00 | 2.99 | 14.62 | 2.66 | high | 5-GW avg pts 4.20; mins 90; xGI 0.41; current GWs 3; fixture Elo diff +6 |
| Barry | EVE | Forward | 4.36 | 4.61 | 4.65 | 4.44 | 2.42 | 16.79 | 3.00 | high | 5-GW avg pts 3.00; mins 67; xGI 0.49; current GWs 3; fixture Elo diff +2 |
| Gakpo | LIV | Midfielder | 4.36 | 3.63 | 3.07 | 3.97 | 4.29 | 15.44 | 2.14 | high | 5-GW avg pts 6.40; mins 83; xGI 0.47; current GWs 3; fixture Elo diff +44 |
| Khalaili | CRY | Defender | 4.34 | 3.69 | 3.81 | 3.63 | 3.81 | 15.54 | 3.11 | medium | 5-GW avg pts 2.00; mins 66; xGI 0.30; current GWs 3; fixture Elo diff +11 |
| Wirtz | LIV | Midfielder | 4.11 | 3.65 | 3.05 | 3.99 | 4.11 | 15.09 | 2.04 | high | 5-GW avg pts 2.20; mins 57; xGI 0.34; current GWs 3; fixture Elo diff +44 |
| De Cuyper | BHA | Defender | 4.00 | 2.88 | 3.60 | 3.82 | 3.09 | 14.00 | 2.98 | high | 5-GW avg pts 4.60; mins 76; xGI 0.54; current GWs 3; fixture Elo diff +6 |
| Gomez | BHA | Midfielder | 4.00 | 2.61 | 3.76 | 3.75 | 2.86 | 13.70 | 2.74 | high | 5-GW avg pts 3.00; mins 70; xGI 0.46; current GWs 3; fixture Elo diff +6 |
| Havertz | ARS | Forward | 3.99 | 3.83 | 4.13 | 3.80 | 4.13 | 15.88 | 2.12 | high | 5-GW avg pts 5.60; mins 75; xGI 0.44; current GWs 3; fixture Elo diff +264 |
| Tavernier | BOU | Midfielder | 3.99 | 3.58 | 3.90 | 4.12 | 3.49 | 15.31 | 2.55 | high | 5-GW avg pts 6.60; mins 90; xGI 0.55; current GWs 3; fixture Elo diff +26 |
| Dewsbury-Hall | EVE | Midfielder | 3.93 | 4.46 | 4.16 | 4.14 | 2.12 | 15.44 | 2.38 | high | 5-GW avg pts 3.80; mins 89; xGI 0.27; current GWs 3; fixture Elo diff +2 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 17.35 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Khalaili | CRY | Defender | £5.0m | 15.54 | GW4, GW8 | — | — |
| Tarkowski | EVE | Defender | £6.0m | 15.08 | GW4, GW5, GW6, GW7 | — | — |
| Castagne | FUL | Defender | £4.5m | 14.45 | GW6, GW7, GW8 | — | GW7 |
| Milenković | NFO | Defender | £5.5m | 14.04 | GW5, GW8 | — | — |
| João Pedro | CHE | Forward | £7.7m | 19.19 | GW4, GW5, GW6, GW7, GW8 | — | GW4 |
| Thiago | BRE | Forward | £7.9m | 18.59 | GW4, GW5, GW6, GW7, GW8 | — | GW5, GW8 |
| Barry | EVE | Forward | £5.6m | 16.79 | GW4, GW5, GW6, GW7 | — | — |
| Henderson | CRY | Goalkeeper | £5.0m | 13.39 | GW4, GW5 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.07 | GW6, GW7, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.20 | GW4, GW5, GW6, GW7, GW8 | GW5, GW6, GW7, GW8 | — |
| Rogers | CHE | Midfielder | £7.6m | 18.91 | GW4, GW5, GW6, GW7, GW8 | GW4 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.32 | GW4, GW5, GW7, GW8 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 17.77 | GW5, GW6, GW7, GW8 | — | GW6 |
| Groß | BHA | Midfielder | £5.5m | 14.62 | GW4, GW6 | — | — |

Squad cost: £99.7m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | LIV | Defender | £6.5m | 13.13 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Botman | NEW | Defender | £5.0m | 12.84 | GW4, GW5, GW6, GW8 | — | — |
| Maguire | MUN | Defender | £5.0m | 12.25 | GW5, GW6, GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 11.15 | GW4, GW6, GW7, GW8 | — | — |
| Muñoz | NFO | Defender | £5.4m | 8.25 | Bench | — | — |
| João Pedro | CHE | Forward | £7.7m | 19.19 | GW4, GW5, GW6, GW7, GW8 | GW4 | — |
| Thiago | BRE | Forward | £7.9m | 18.59 | GW4, GW5, GW6, GW7, GW8 | — | GW5, GW8 |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.07 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.46 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.20 | GW4, GW5, GW6, GW7, GW8 | GW5, GW6, GW7, GW8 | GW4 |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.32 | GW4, GW5, GW6, GW7, GW8 | — | GW7 |
| Saka | ARS | Midfielder | £9.5m | 18.10 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 17.77 | GW4, GW5, GW6, GW7, GW8 | — | GW6 |
| Enzo | MCI | Midfielder | £6.9m | 11.36 | GW4, GW5, GW7 | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Muñoz → Khalaili** (projected weighted XI+captain gain 4.66).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Muñoz | Khalaili | £5.4m | £5.0m | £0.9m | 4.66 |
| Enzo | Dewsbury-Hall | £6.9m | £6.5m | £0.9m | 4.40 |
| Mitchell | Khalaili | £4.5m | £5.0m | £0.0m | 4.15 |
| Enzo | Anderson | £6.9m | £6.3m | £1.1m | 4.15 |
| Enzo | Gakpo | £6.9m | £7.2m | £0.2m | 4.02 |
| Muñoz | Castagne | £5.4m | £4.5m | £1.4m | 3.90 |
| Enzo | Tavernier | £6.9m | £6.0m | £1.4m | 3.89 |
| Enzo | Wirtz | £6.9m | £7.4m | £0.0m | 3.67 |
| Muñoz | Silva | £5.4m | £5.0m | £0.9m | 3.64 |
| Muñoz | White | £5.4m | £5.5m | £0.4m | 3.47 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
