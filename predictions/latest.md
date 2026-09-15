# FPL predictions: 2026-2027, GW5

Last generated: 2026-09-15 13:48 UTC

Data commit: `c276843ee2b90d41ba20e8839dd900284c48b4af`

## Data freshness

All scheduled Premier League fixtures before GW5 are complete.

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

## Top GW5 player forecasts

| Player | Club | Pos | GW5 | GW6 | GW7 | GW8 | GW9 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | 6.49 | 4.83 | 6.34 | 4.83 | 6.44 | 23.15 | 1.49 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +156 |
| B.Fernandes | MUN | Midfielder | 6.30 | 6.52 | 6.30 | 5.61 | 6.30 | 24.92 | 2.08 | high | 5-GW avg pts 8.60; mins 90; xGI 0.73; current GWs 4; fixture Elo diff +97 |
| Gibbs-White | NFO | Midfielder | 5.96 | 5.18 | 3.29 | 5.46 | 5.32 | 20.27 | 2.57 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff +15 |
| Thiago | BRE | Forward | 4.86 | 3.78 | 3.98 | 4.92 | 4.72 | 17.73 | 2.24 | high | 5-GW avg pts 1.40; mins 88; xGI 0.52; current GWs 4; fixture Elo diff +7 |
| João Pedro | CHE | Forward | 4.84 | 4.57 | 4.61 | 4.89 | 4.11 | 18.53 | 2.38 | high | 5-GW avg pts 6.80; mins 90; xGI 0.59; current GWs 4; fixture Elo diff -10 |
| Gabriel | ARS | Defender | 4.81 | 4.96 | 4.71 | 4.96 | 3.90 | 18.85 | 2.36 | high | 5-GW avg pts 5.00; mins 81; xGI 0.11; current GWs 4; fixture Elo diff +229 |
| Palmer | CHE | Midfielder | 4.73 | 4.60 | 4.49 | 5.03 | 3.98 | 18.37 | 1.89 | high | 5-GW avg pts 6.80; mins 88; xGI 0.40; current GWs 4; fixture Elo diff -10 |
| Semenyo | MCI | Midfielder | 4.67 | 3.76 | 4.96 | 3.63 | 4.29 | 17.14 | 2.04 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +156 |
| Mbeumo | MUN | Midfielder | 4.67 | 4.88 | 4.67 | 4.42 | 4.77 | 18.75 | 2.37 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +97 |
| Schlager | NFO | Midfielder | 4.61 | 3.59 | 2.61 | 5.20 | 3.50 | 15.66 | 3.13 | medium | 5-GW avg pts 2.75; mins 72; xGI 0.05; current GWs 4; fixture Elo diff +15 |
| Dewsbury-Hall | EVE | Midfielder | 4.41 | 4.11 | 4.11 | 2.25 | 3.95 | 15.35 | 2.36 | high | 5-GW avg pts 3.80; mins 89; xGI 0.23; current GWs 4; fixture Elo diff -10 |
| Barry | EVE | Forward | 4.40 | 4.27 | 4.12 | 2.31 | 3.96 | 15.53 | 2.77 | high | 5-GW avg pts 3.20; mins 82; xGI 0.63; current GWs 4; fixture Elo diff -10 |
| Saka | ARS | Midfielder | 4.40 | 4.78 | 4.50 | 4.78 | 3.84 | 17.95 | 1.89 | high | 5-GW avg pts 6.00; mins 67; xGI 0.66; current GWs 4; fixture Elo diff +229 |
| Rogers | CHE | Midfielder | 4.38 | 4.06 | 4.38 | 4.63 | 3.71 | 17.01 | 2.21 | high | 5-GW avg pts 5.40; mins 69; xGI 0.51; current GWs 4; fixture Elo diff -10 |
| Isak | LIV | Forward | 4.37 | 3.76 | 4.72 | 5.07 | 3.05 | 16.91 | 1.86 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Stach | LEE | Midfielder | 4.35 | 2.37 | 3.33 | 4.02 | 3.21 | 13.89 | 2.32 | high | 5-GW avg pts 4.40; mins 71; xGI 0.23; current GWs 4; fixture Elo diff -81 |
| Tarkowski | EVE | Defender | 4.35 | 4.38 | 3.91 | 2.05 | 3.78 | 15.12 | 2.48 | high | 5-GW avg pts 6.40; mins 90; xGI 0.05; current GWs 4; fixture Elo diff -10 |
| Szoboszlai | LIV | Midfielder | 4.14 | 3.93 | 4.84 | 4.97 | 3.28 | 17.00 | 2.43 | high | 5-GW avg pts 4.00; mins 90; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Havertz | ARS | Forward | 4.13 | 4.21 | 4.04 | 4.21 | 3.71 | 16.32 | 2.15 | high | 5-GW avg pts 4.20; mins 78; xGI 0.36; current GWs 4; fixture Elo diff +229 |
| Pickford | EVE | Goalkeeper | 4.10 | 4.15 | 3.48 | 2.20 | 3.44 | 14.22 | 2.59 | high | 5-GW avg pts 3.80; mins 90; xGI 0.01; current GWs 4; fixture Elo diff -10 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 18.85 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Khalaili | CRY | Defender | £5.0m | 15.86 | GW5, GW6, GW8, GW9 | — | — |
| Silva | BOU | Defender | £5.0m | 15.44 | GW7, GW9 | — | — |
| Tarkowski | EVE | Defender | £6.1m | 15.12 | GW5, GW6, GW7, GW9 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.61 | GW6, GW7, GW8 | — | — |
| João Pedro | CHE | Forward | £7.8m | 18.53 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Thiago | BRE | Forward | £7.9m | 17.73 | GW5, GW7, GW8, GW9 | — | — |
| Barry | EVE | Forward | £5.6m | 15.53 | GW5, GW6, GW7, GW9 | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 14.22 | GW5, GW6, GW9 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.90 | GW7, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.92 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW8, GW9 | — |
| Gibbs-White | NFO | Midfielder | £7.9m | 20.27 | GW5, GW6, GW8, GW9 | — | GW5, GW6, GW8, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.75 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.00 | GW6, GW7, GW8 | — | GW7 |
| Schlager | NFO | Midfielder | £5.0m | 15.66 | GW5, GW8 | — | — |

Squad cost: £99.7m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 13.76 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Maguire | MUN | Defender | £4.9m | 13.18 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Virgil | LIV | Defender | £6.5m | 12.92 | GW6, GW7, GW8 | — | — |
| Muñoz | NFO | Defender | £5.4m | 11.59 | GW5, GW9 | — | — |
| Mitchell | CRY | Defender | £4.5m | 11.14 | Bench | — | — |
| João Pedro | CHE | Forward | £7.8m | 18.53 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Thiago | BRE | Forward | £7.9m | 17.73 | GW5, GW6, GW7, GW8, GW9 | — | GW5 |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.90 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.29 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 24.92 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW8, GW9 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 18.75 | GW5, GW6, GW7, GW8, GW9 | — | GW6, GW9 |
| Saka | ARS | Midfielder | £9.5m | 17.95 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.00 | GW5, GW6, GW7, GW8, GW9 | — | GW7, GW8 |
| Gakpo | LIV | Midfielder | £7.2m | 12.22 | GW5, GW6, GW7, GW8, GW9 | — | — |

Squad cost: £99.5m.

## One-transfer recommendation

**Muñoz → Khalaili** (projected weighted XI+captain gain 3.90).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Muñoz | Khalaili | £5.4m | £5.0m | £0.6m | 3.90 |
| Gakpo | Tavernier | £7.2m | £6.1m | £1.3m | 3.80 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.5m | £0.9m | 3.60 |
| Gakpo | Schlager | £7.2m | £5.0m | £2.4m | 3.52 |
| Muñoz | Silva | £5.4m | £5.0m | £0.6m | 3.48 |
| Gakpo | Rice | £7.2m | £7.4m | £0.0m | 3.35 |
| Gakpo | M.Sangaré | £7.2m | £5.7m | £1.7m | 3.30 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 2.82 |
| Virgil | Khalaili | £6.5m | £5.0m | £1.7m | 2.79 |
| Muñoz | Hill | £5.4m | £5.5m | £0.1m | 2.73 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
