# FPL predictions: 2026-2027, GW5

Last generated: 2026-09-12 18:37 UTC

Data commit: `349ffd62a458f0dfcac72901aabdfe55f16a8050`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW4: 5/10 fixtures finished. Completed clubs contribute current-season form; ARS, BHA, COV, EVE, LEE, MCI, MUN, NEW, SUN, TOT are deferred.

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
| B.Fernandes | MUN | Midfielder | 6.37 | 6.95 | 6.37 | 5.67 | 6.37 | 25.52 | 2.13 | high | 5-GW avg pts 10.00; mins 90; xGI 0.87; current GWs 3; fixture Elo diff +97 |
| Gibbs-White | NFO | Midfielder | 6.26 | 5.55 | 3.55 | 5.76 | 5.58 | 21.48 | 2.72 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff +15 |
| Haaland | MCI | Forward | 5.89 | 4.33 | 5.73 | 4.33 | 5.88 | 20.94 | 1.35 | high | 5-GW avg pts 6.60; mins 72; xGI 0.74; current GWs 3; fixture Elo diff +156 |
| João Pedro | CHE | Forward | 4.87 | 4.57 | 4.64 | 4.92 | 4.11 | 18.61 | 2.42 | high | 5-GW avg pts 6.80; mins 90; xGI 0.59; current GWs 4; fixture Elo diff -10 |
| Palmer | CHE | Midfielder | 4.73 | 4.60 | 4.49 | 4.92 | 3.98 | 18.30 | 1.89 | high | 5-GW avg pts 6.80; mins 88; xGI 0.41; current GWs 4; fixture Elo diff -10 |
| Thiago | BRE | Forward | 4.66 | 3.68 | 3.81 | 4.87 | 4.52 | 17.14 | 2.17 | high | 5-GW avg pts 1.40; mins 88; xGI 0.52; current GWs 4; fixture Elo diff +7 |
| Gabriel | ARS | Defender | 4.62 | 4.56 | 4.52 | 4.56 | 3.86 | 17.85 | 2.23 | high | 5-GW avg pts 4.40; mins 81; xGI 0.12; current GWs 3; fixture Elo diff +229 |
| Semenyo | MCI | Midfielder | 4.60 | 3.87 | 4.75 | 3.88 | 4.56 | 17.34 | 2.06 | high | 5-GW avg pts 4.00; mins 76; xGI 0.27; current GWs 3; fixture Elo diff +156 |
| Isak | LIV | Forward | 4.52 | 3.92 | 4.87 | 5.23 | 3.21 | 17.53 | 1.93 | high | 5-GW avg pts 5.00; mins 67; xGI 0.58; current GWs 4; fixture Elo diff -6 |
| Mbeumo | MUN | Midfielder | 4.52 | 4.72 | 4.52 | 4.27 | 4.62 | 18.14 | 2.30 | high | 5-GW avg pts 7.40; mins 84; xGI 1.26; current GWs 3; fixture Elo diff +97 |
| Rogers | CHE | Midfielder | 4.38 | 4.06 | 4.38 | 4.63 | 3.71 | 17.01 | 2.24 | high | 5-GW avg pts 5.40; mins 69; xGI 0.51; current GWs 4; fixture Elo diff -10 |
| Anderson | MCI | Midfielder | 4.37 | 3.65 | 5.04 | 3.65 | 4.11 | 16.71 | 2.65 | high | 5-GW avg pts 4.40; mins 77; xGI 0.36; current GWs 3; fixture Elo diff +156 |
| Dewsbury-Hall | EVE | Midfielder | 4.34 | 4.04 | 4.01 | 2.00 | 3.85 | 14.90 | 2.29 | high | 5-GW avg pts 3.80; mins 89; xGI 0.27; current GWs 3; fixture Elo diff -10 |
| Tarkowski | EVE | Defender | 4.30 | 4.37 | 3.79 | 2.03 | 3.67 | 14.89 | 2.48 | high | 5-GW avg pts 5.40; mins 90; xGI 0.07; current GWs 3; fixture Elo diff -10 |
| Saka | ARS | Midfielder | 4.30 | 4.48 | 4.31 | 4.48 | 3.87 | 17.23 | 1.81 | high | 5-GW avg pts 6.40; mins 67; xGI 0.47; current GWs 3; fixture Elo diff +229 |
| Barry | EVE | Forward | 4.29 | 4.18 | 4.11 | 2.29 | 3.97 | 15.32 | 2.74 | high | 5-GW avg pts 3.00; mins 67; xGI 0.49; current GWs 3; fixture Elo diff -10 |
| Horníček | NEW | Goalkeeper | 4.18 | 3.87 | 2.92 | 3.14 | 3.42 | 14.25 | 2.85 | medium | 5-GW avg pts 3.33; mins 90; xGI 0.00; current GWs 3; fixture Elo diff +66 |
| Tavernier | BOU | Midfielder | 4.04 | 4.13 | 4.49 | 3.79 | 4.38 | 16.63 | 2.77 | high | 5-GW avg pts 7.80; mins 88; xGI 0.58; current GWs 4; fixture Elo diff +34 |
| Pickford | EVE | Goalkeeper | 3.99 | 4.04 | 3.41 | 2.01 | 3.36 | 13.78 | 2.51 | high | 5-GW avg pts 2.80; mins 90; xGI 0.01; current GWs 3; fixture Elo diff -10 |
| Hall | NEW | Defender | 3.96 | 3.71 | 2.69 | 3.04 | 3.16 | 13.48 | 2.59 | high | 5-GW avg pts 4.00; mins 90; xGI 0.20; current GWs 3; fixture Elo diff +66 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 17.85 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Silva | BOU | Defender | £5.0m | 15.65 | GW6, GW7, GW8, GW9 | — | — |
| Tarkowski | EVE | Defender | £6.0m | 14.89 | GW5, GW6, GW7 | — | — |
| Muharemović | LEE | Defender | £5.0m | 13.07 | GW5, GW8 | — | — |
| Davis | IPS | Defender | £4.0m | 12.17 | GW9 | — | — |
| João Pedro | CHE | Forward | £7.7m | 18.61 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Isak | LIV | Forward | £9.1m | 17.53 | GW5, GW6, GW7, GW8 | — | — |
| Barry | EVE | Forward | £5.6m | 15.32 | GW5, GW6, GW7, GW9 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 14.25 | GW5, GW9 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.80 | GW6, GW7, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 25.52 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW9 | GW8 |
| Gibbs-White | NFO | Midfielder | £7.9m | 21.48 | GW5, GW6, GW8, GW9 | GW8 | GW5, GW6, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.14 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Anderson | MCI | Midfielder | £6.3m | 16.71 | GW5, GW7, GW8, GW9 | — | GW7 |
| Tavernier | BOU | Midfielder | £6.0m | 16.63 | GW6, GW7, GW8, GW9 | — | — |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maguire | MUN | Defender | £4.9m | 13.16 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Botman | NEW | Defender | £5.0m | 12.95 | GW5, GW6, GW8, GW9 | — | — |
| Virgil | LIV | Defender | £6.5m | 11.88 | GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 11.14 | GW6, GW7 | — | — |
| Muñoz | NFO | Defender | £5.4m | 10.93 | GW5, GW9 | — | — |
| João Pedro | CHE | Forward | £7.7m | 18.61 | GW5, GW6, GW7, GW8, GW9 | — | GW5, GW7, GW8 |
| Thiago | BRE | Forward | £7.9m | 17.14 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.80 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.46 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 25.52 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW8, GW9 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 18.14 | GW5, GW6, GW7, GW8, GW9 | — | GW6, GW9 |
| Saka | ARS | Midfielder | £9.5m | 17.23 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 15.56 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Gakpo | LIV | Midfielder | £7.2m | 12.22 | GW5, GW6, GW7, GW8, GW9 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Gakpo → Anderson** (projected weighted XI+captain gain 4.49).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Gakpo | Anderson | £7.2m | £6.3m | £1.1m | 4.49 |
| Gakpo | Tavernier | £7.2m | £6.0m | £1.4m | 4.41 |
| Saka | Gibbs-White | £9.5m | £7.9m | £1.8m | 4.31 |
| Muñoz | Silva | £5.4m | £5.0m | £0.6m | 4.28 |
| Muñoz | Khalaili | £5.4m | £5.0m | £0.6m | 3.90 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 3.55 |
| Mbeumo | Gibbs-White | £7.9m | £7.9m | £0.2m | 3.40 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.5m | £0.9m | 3.35 |
| Virgil | Silva | £6.5m | £5.0m | £1.7m | 3.22 |
| Muñoz | Hill | £5.4m | £5.5m | £0.1m | 3.18 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
