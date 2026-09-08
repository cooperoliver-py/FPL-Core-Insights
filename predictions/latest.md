# FPL predictions: 2026-2027, GW4

Last generated: 2026-09-08 05:02 UTC

Data commit: `ed638d38f6d79fdcd7c547ac9de07bca45b591c7`

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
| 3 | 1.211 | 2.030 | 0.750 | 4.25 | 1.83 | 44 | 51 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics.

## Top GW4 player forecasts

| Player | Club | Pos | GW4 | GW5 | GW6 | GW7 | GW8 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rogers | CHE | Midfielder | 5.14 | 4.65 | 4.28 | 4.65 | 4.84 | 18.91 | 2.49 | high | 5-GW avg pts 6.20; mins 69; xGI 0.53; current GWs 3; fixture Elo diff +40 |
| B.Fernandes | MUN | Midfielder | 5.04 | 6.37 | 6.95 | 6.37 | 5.67 | 24.20 | 2.02 | high | 5-GW avg pts 10.00; mins 90; xGI 0.87; current GWs 3; fixture Elo diff +69 |
| João Pedro | CHE | Forward | 4.96 | 4.79 | 4.38 | 4.55 | 4.81 | 18.85 | 2.45 | high | 5-GW avg pts 4.40; mins 72; xGI 0.52; current GWs 3; fixture Elo diff +40 |
| Szoboszlai | LIV | Midfielder | 4.92 | 4.09 | 3.93 | 4.67 | 4.95 | 17.99 | 2.57 | high | 5-GW avg pts 5.20; mins 90; xGI 0.59; current GWs 3; fixture Elo diff +44 |
| Khalaili | CRY | Defender | 4.76 | 3.86 | 4.10 | 3.84 | 4.10 | 16.67 | 3.33 | medium | 5-GW avg pts 2.00; mins 66; xGI 0.30; current GWs 3; fixture Elo diff +11 |
| Gabriel | ARS | Defender | 4.76 | 4.62 | 4.56 | 4.52 | 4.56 | 18.47 | 2.31 | high | 5-GW avg pts 4.40; mins 81; xGI 0.12; current GWs 3; fixture Elo diff +264 |
| Isak | LIV | Forward | 4.73 | 3.90 | 3.78 | 4.31 | 4.82 | 17.17 | 1.89 | high | 5-GW avg pts 4.60; mins 49; xGI 0.47; current GWs 3; fixture Elo diff +44 |
| Thiago | BRE | Forward | 4.60 | 5.45 | 4.15 | 4.36 | 5.38 | 19.11 | 2.42 | high | 5-GW avg pts 1.60; mins 88; xGI 0.52; current GWs 3; fixture Elo diff -3 |
| Groß | BHA | Midfielder | 4.37 | 2.62 | 4.00 | 3.96 | 2.95 | 14.46 | 2.63 | high | 5-GW avg pts 4.20; mins 90; xGI 0.41; current GWs 3; fixture Elo diff +6 |
| Palmer | CHE | Midfielder | 4.37 | 4.27 | 4.03 | 4.27 | 4.46 | 17.10 | 1.78 | high | 5-GW avg pts 6.20; mins 88; xGI 0.39; current GWs 3; fixture Elo diff +40 |
| Saka | ARS | Midfielder | 4.35 | 4.30 | 4.48 | 4.31 | 4.48 | 17.50 | 1.84 | high | 5-GW avg pts 6.40; mins 67; xGI 0.47; current GWs 3; fixture Elo diff +264 |
| Haaland | MCI | Forward | 4.33 | 5.89 | 4.33 | 5.73 | 4.33 | 19.71 | 1.27 | high | 5-GW avg pts 6.60; mins 72; xGI 0.74; current GWs 3; fixture Elo diff +141 |
| Gakpo | LIV | Midfielder | 4.28 | 3.55 | 2.99 | 3.89 | 4.21 | 15.13 | 2.10 | high | 5-GW avg pts 6.40; mins 83; xGI 0.47; current GWs 3; fixture Elo diff +44 |
| Wirtz | LIV | Midfielder | 4.10 | 3.60 | 3.03 | 3.92 | 4.20 | 15.04 | 2.03 | high | 5-GW avg pts 2.20; mins 57; xGI 0.34; current GWs 3; fixture Elo diff +44 |
| Yeremy | CRY | Midfielder | 4.05 | 3.46 | 3.69 | 3.40 | 3.69 | 14.72 | 2.68 | high | 5-GW avg pts 3.20; mins 56; xGI 0.28; current GWs 3; fixture Elo diff +11 |
| Barry | EVE | Forward | 4.03 | 4.29 | 4.18 | 4.11 | 2.29 | 15.48 | 2.76 | high | 5-GW avg pts 3.00; mins 67; xGI 0.49; current GWs 3; fixture Elo diff +2 |
| Rice | ARS | Midfielder | 4.02 | 3.63 | 3.88 | 3.63 | 3.88 | 15.26 | 2.06 | high | 5-GW avg pts 3.60; mins 66; xGI 0.08; current GWs 3; fixture Elo diff +264 |
| Kamada | CRY | Midfielder | 4.02 | 3.30 | 3.34 | 3.43 | 3.34 | 14.07 | 2.81 | high | 5-GW avg pts 3.00; mins 81; xGI 0.14; current GWs 3; fixture Elo diff +11 |
| Tzolis | ARS | Midfielder | 3.98 | 3.64 | 3.79 | 3.60 | 3.79 | 15.08 | 2.36 | medium | 5-GW avg pts 3.67; mins 70; xGI 0.18; current GWs 3; fixture Elo diff +264 |
| Lacroix | CHE | Defender | 3.95 | 3.63 | 3.24 | 3.47 | 3.54 | 14.36 | 2.39 | high | 5-GW avg pts 2.20; mins 66; xGI 0.06; current GWs 3; fixture Elo diff +40 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 18.47 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Khalaili | CRY | Defender | £5.0m | 16.67 | GW4, GW6, GW7, GW8 | — | — |
| Tarkowski | EVE | Defender | £6.0m | 15.10 | GW4, GW5, GW6 | — | — |
| Castagne | FUL | Defender | £4.5m | 15.00 | GW6, GW7, GW8 | — | GW7 |
| Dedić | NEW | Defender | £4.5m | 14.09 | GW5 | — | — |
| Thiago | BRE | Forward | £7.9m | 19.11 | GW4, GW5, GW6, GW7, GW8 | — | GW5, GW8 |
| João Pedro | CHE | Forward | £7.7m | 18.85 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Gonzalo | FUL | Forward | £6.0m | 16.24 | GW6, GW7, GW8 | — | GW6 |
| Horníček | NEW | Goalkeeper | £5.0m | 13.93 | GW4, GW5 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.07 | GW6, GW7, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.20 | GW4, GW5, GW6, GW7, GW8 | GW5, GW6, GW7, GW8 | GW4 |
| Rogers | CHE | Midfielder | £7.6m | 18.91 | GW4, GW5, GW6, GW7, GW8 | GW4 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.99 | GW4, GW5, GW7, GW8 | — | — |
| Anderson | MCI | Midfielder | £6.3m | 16.21 | GW4, GW5, GW7 | — | — |
| Gibbs-White | NFO | Midfielder | £7.9m | 16.19 | GW4, GW5, GW6, GW8 | — | — |

Squad cost: £99.9m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | LIV | Defender | £6.5m | 13.51 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Botman | NEW | Defender | £5.0m | 12.84 | GW4, GW5, GW6, GW8 | — | — |
| Maguire | MUN | Defender | £4.9m | 12.64 | GW5, GW6, GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 11.79 | GW4, GW6, GW7, GW8 | — | — |
| Muñoz | NFO | Defender | £5.4m | 8.51 | Bench | — | — |
| Thiago | BRE | Forward | £7.9m | 19.11 | GW4, GW5, GW6, GW7, GW8 | — | GW5, GW8 |
| João Pedro | CHE | Forward | £7.7m | 18.85 | GW4, GW5, GW6, GW7, GW8 | — | GW4 |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.07 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.46 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.20 | GW4, GW5, GW6, GW7, GW8 | GW4, GW5, GW6, GW7, GW8 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.99 | GW4, GW5, GW6, GW7, GW8 | — | GW7 |
| Saka | ARS | Midfielder | £9.5m | 17.50 | GW4, GW5, GW6, GW7, GW8 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 17.15 | GW4, GW5, GW6, GW7, GW8 | — | GW6 |
| Enzo | MCI | Midfielder | £6.9m | 12.31 | GW4, GW5, GW7 | — | — |

Squad cost: £99.1m.

## One-transfer recommendation

**Muñoz → Khalaili** (projected weighted XI+captain gain 5.17).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Muñoz | Khalaili | £5.4m | £5.0m | £0.9m | 5.17 |
| Mitchell | Khalaili | £4.5m | £5.0m | £0.0m | 4.64 |
| Maguire | Khalaili | £4.9m | £5.0m | £0.4m | 3.97 |
| Enzo | Anderson | £6.9m | £6.3m | £1.1m | 3.79 |
| Muñoz | Castagne | £5.4m | £4.5m | £1.4m | 3.76 |
| Botman | Khalaili | £5.0m | £5.0m | £0.5m | 3.69 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.4m | 3.33 |
| Mitchell | Castagne | £4.5m | £4.5m | £0.5m | 3.18 |
| Virgil | Khalaili | £6.5m | £5.0m | £2.0m | 3.16 |
| Enzo | Dewsbury-Hall | £6.9m | £6.5m | £0.9m | 3.09 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
