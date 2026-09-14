# FPL predictions: 2026-2027, GW5

Last generated: 2026-09-14 15:11 UTC

Data commit: `83db79496726440aeedf8476520dbfce733c1a18`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW4: 9/10 fixtures finished. Completed clubs contribute current-season form; LEE, NEW are deferred.

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
| 3 | 1.211 | 2.030 | 0.750 | 4.25 | 1.83 | 44 | 51 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics.

## Top GW5 player forecasts

| Player | Club | Pos | GW5 | GW6 | GW7 | GW8 | GW9 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 6.42 | 6.64 | 6.42 | 5.72 | 6.42 | 25.38 | 2.11 | high | 5-GW avg pts 8.60; mins 90; xGI 0.73; current GWs 4; fixture Elo diff +97 |
| Haaland | MCI | Forward | 6.31 | 4.64 | 6.15 | 4.64 | 6.25 | 22.40 | 1.45 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +156 |
| Gibbs-White | NFO | Midfielder | 6.26 | 5.55 | 3.55 | 5.76 | 5.58 | 21.48 | 2.72 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff +15 |
| João Pedro | CHE | Forward | 4.87 | 4.57 | 4.64 | 4.92 | 4.11 | 18.61 | 2.39 | high | 5-GW avg pts 6.80; mins 90; xGI 0.59; current GWs 4; fixture Elo diff -10 |
| Thiago | BRE | Forward | 4.76 | 3.76 | 3.89 | 4.96 | 4.62 | 17.50 | 2.22 | high | 5-GW avg pts 1.40; mins 88; xGI 0.52; current GWs 4; fixture Elo diff +7 |
| Palmer | CHE | Midfielder | 4.73 | 4.60 | 4.49 | 5.03 | 3.98 | 18.37 | 1.89 | high | 5-GW avg pts 6.80; mins 88; xGI 0.40; current GWs 4; fixture Elo diff -10 |
| Gabriel | ARS | Defender | 4.71 | 4.83 | 4.61 | 4.83 | 3.85 | 18.44 | 2.30 | high | 5-GW avg pts 5.00; mins 81; xGI 0.11; current GWs 4; fixture Elo diff +229 |
| Mbeumo | MUN | Midfielder | 4.67 | 4.88 | 4.67 | 4.42 | 4.77 | 18.75 | 2.37 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +97 |
| Barry | EVE | Forward | 4.67 | 4.68 | 4.39 | 2.51 | 4.23 | 16.69 | 2.98 | high | 5-GW avg pts 3.20; mins 82; xGI 0.63; current GWs 4; fixture Elo diff -10 |
| Saka | ARS | Midfielder | 4.57 | 4.86 | 4.57 | 4.86 | 4.02 | 18.41 | 1.94 | high | 5-GW avg pts 6.00; mins 67; xGI 0.66; current GWs 4; fixture Elo diff +229 |
| Isak | LIV | Forward | 4.52 | 3.92 | 4.87 | 5.23 | 3.21 | 17.53 | 1.93 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Semenyo | MCI | Midfielder | 4.52 | 3.71 | 4.80 | 3.58 | 4.13 | 16.67 | 1.99 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +156 |
| Rogers | CHE | Midfielder | 4.38 | 4.06 | 4.38 | 4.63 | 3.71 | 17.01 | 2.21 | high | 5-GW avg pts 5.40; mins 69; xGI 0.51; current GWs 4; fixture Elo diff -10 |
| Dewsbury-Hall | EVE | Midfielder | 4.32 | 4.02 | 4.02 | 2.20 | 3.86 | 15.01 | 2.31 | high | 5-GW avg pts 3.80; mins 89; xGI 0.23; current GWs 4; fixture Elo diff -10 |
| Schlager | NFO | Midfielder | 4.23 | 3.31 | 2.56 | 4.80 | 3.31 | 14.60 | 2.92 | medium | 5-GW avg pts 2.75; mins 72; xGI 0.05; current GWs 4; fixture Elo diff +15 |
| Cunha | MUN | Midfielder | 4.21 | 4.28 | 4.21 | 4.01 | 4.21 | 16.75 | 2.12 | high | 5-GW avg pts 3.20; mins 63; xGI 0.20; current GWs 4; fixture Elo diff +97 |
| Tarkowski | EVE | Defender | 4.20 | 4.31 | 3.75 | 2.04 | 3.70 | 14.73 | 2.41 | high | 5-GW avg pts 6.40; mins 90; xGI 0.05; current GWs 4; fixture Elo diff -10 |
| Horníček | NEW | Goalkeeper | 4.18 | 3.87 | 2.92 | 3.14 | 3.42 | 14.25 | 2.85 | medium | 5-GW avg pts 3.33; mins 90; xGI 0.00; current GWs 3; fixture Elo diff +66 |
| Havertz | ARS | Forward | 4.13 | 4.21 | 4.04 | 4.21 | 3.71 | 16.32 | 2.15 | high | 5-GW avg pts 4.20; mins 78; xGI 0.36; current GWs 4; fixture Elo diff +229 |
| Pickford | EVE | Goalkeeper | 4.10 | 4.15 | 3.48 | 2.20 | 3.44 | 14.22 | 2.59 | high | 5-GW avg pts 3.80; mins 90; xGI 0.01; current GWs 4; fixture Elo diff -10 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 18.44 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Khalaili | CRY | Defender | £5.0m | 15.26 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Rúben | MCI | Defender | £5.5m | 14.32 | GW5, GW7, GW9 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.54 | GW6, GW7, GW8 | — | — |
| Kipré | IPS | Defender | £3.9m | 0.38 | Bench | — | — |
| João Pedro | CHE | Forward | £7.8m | 18.61 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Thiago | BRE | Forward | £7.9m | 17.50 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Barry | EVE | Forward | £5.6m | 16.69 | GW5, GW6, GW7, GW9 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 14.25 | GW5, GW9 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.90 | GW6, GW7, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 25.38 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW9 | GW8 |
| Gibbs-White | NFO | Midfielder | £7.9m | 21.48 | GW5, GW6, GW8, GW9 | GW8 | GW5, GW6, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.75 | GW5, GW6, GW7, GW8, GW9 | — | GW7 |
| Saka | ARS | Midfielder | £9.5m | 18.41 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Schlager | NFO | Midfielder | £5.0m | 14.60 | GW8 | — | — |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 12.95 | GW5, GW6, GW8, GW9 | — | — |
| Maguire | MUN | Defender | £4.9m | 12.72 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Virgil | LIV | Defender | £6.5m | 11.88 | GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 11.14 | GW6, GW7 | — | — |
| Muñoz | NFO | Defender | £5.4m | 10.93 | GW5, GW9 | — | — |
| João Pedro | CHE | Forward | £7.8m | 18.61 | GW5, GW6, GW7, GW8, GW9 | — | GW5 |
| Thiago | BRE | Forward | £7.9m | 17.50 | GW5, GW6, GW7, GW8, GW9 | — | GW8 |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.90 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.46 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 25.38 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW8, GW9 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 18.75 | GW5, GW6, GW7, GW8, GW9 | — | GW6, GW7, GW9 |
| Saka | ARS | Midfielder | £9.5m | 18.41 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 15.56 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Gakpo | LIV | Midfielder | £7.2m | 12.22 | GW5, GW6, GW7, GW8, GW9 | — | — |

Squad cost: £99.5m.

## One-transfer recommendation

**Gakpo → Tavernier** (projected weighted XI+captain gain 4.41).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Gakpo | Tavernier | £7.2m | £6.1m | £1.3m | 4.41 |
| Muñoz | Khalaili | £5.4m | £5.0m | £0.6m | 3.91 |
| Muñoz | Silva | £5.4m | £5.0m | £0.6m | 3.57 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.5m | £0.9m | 3.33 |
| Muñoz | Hill | £5.4m | £5.5m | £0.1m | 3.20 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 3.11 |
| Saka | Gibbs-White | £9.5m | £7.9m | £1.8m | 3.09 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.1m | 2.99 |
| Virgil | Tarkowski | £6.5m | £6.1m | £0.6m | 2.95 |
| Muñoz | Richards | £5.4m | £5.0m | £0.6m | 2.89 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
