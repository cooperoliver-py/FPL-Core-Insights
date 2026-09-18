# FPL predictions: 2026-2027, GW5

Last generated: 2026-09-18 10:40 UTC

Data commit: `dd9b0c9710fd270123600531e17f3287ab6c9403`

## Data freshness

All scheduled Premier League fixtures before GW5 are complete.

The model learns from 2025/26 and completed, checked current-season Gameweeks. An equal-weight blend balances the original features with recent participation, longer-window per-90 rates, set-piece roles and observed workload across league, cup, European and friendly matches. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; prices remain fixed. Dated suspensions expire and later injury-return forecasts use a conservative historical recovery rate.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.850 | 1.847 | 0.752 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.020 and Spearman is 0.365.

The predicted top 20 averaged 4.82 actual points versus 1.69 for the selectable pool.

## Live-season performance

| GW | MAE | RMSE | Spearman | Top 20 | Pool | XI + captain | FPL avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.528 | 2.580 | 0.553 | 3.40 | 1.88 | 39 | 50 |
| 2 | 1.211 | 2.131 | 0.697 | 6.60 | 1.74 | 112 | 81 |
| 3 | 1.211 | 2.030 | 0.750 | 4.25 | 1.83 | 44 | 51 |
| 4 | 1.278 | 2.257 | 0.711 | 5.40 | 1.91 | 72 | 69 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW5 player forecasts

| Player | Club | Pos | GW5 | GW6 | GW7 | GW8 | GW9 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | 7.92 | 5.36 | 8.16 | 5.36 | 6.34 | 26.82 | 1.72 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +161 |
| Gibbs-White | NFO | Midfielder | 7.34 | 5.50 | 3.00 | 7.18 | 5.29 | 22.89 | 2.86 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff +21 |
| B.Fernandes | MUN | Midfielder | 7.21 | 7.73 | 7.44 | 6.10 | 7.01 | 28.60 | 2.38 | high | 5-GW avg pts 8.60; mins 90; xGI 0.73; current GWs 4; fixture Elo diff +97 |
| Saka | ARS | Midfielder | 6.31 | 6.44 | 6.36 | 6.45 | 6.09 | 25.37 | 2.67 | high | 5-GW avg pts 6.00; mins 67; xGI 0.66; current GWs 4; fixture Elo diff +229 |
| Isak | LIV | Forward | 5.58 | 4.62 | 5.64 | 5.75 | 3.15 | 20.16 | 2.22 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Gabriel | ARS | Defender | 5.44 | 5.68 | 5.69 | 5.57 | 5.48 | 22.29 | 2.79 | high | 5-GW avg pts 5.00; mins 81; xGI 0.11; current GWs 4; fixture Elo diff +229 |
| Semenyo | MCI | Midfielder | 5.35 | 4.85 | 6.24 | 4.85 | 5.04 | 21.12 | 2.51 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +161 |
| Mbeumo | MUN | Midfielder | 5.15 | 5.56 | 5.40 | 5.10 | 5.12 | 21.13 | 2.67 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +97 |
| Havertz | ARS | Forward | 5.10 | 5.31 | 5.24 | 5.30 | 4.99 | 20.78 | 2.73 | high | 5-GW avg pts 4.20; mins 78; xGI 0.36; current GWs 4; fixture Elo diff +229 |
| Rogers | CHE | Midfielder | 4.99 | 4.88 | 5.04 | 5.05 | 4.62 | 19.72 | 2.56 | high | 5-GW avg pts 5.40; mins 69; xGI 0.51; current GWs 4; fixture Elo diff -10 |
| Tarkowski | EVE | Defender | 4.92 | 4.70 | 3.90 | 2.45 | 3.71 | 16.21 | 2.66 | high | 5-GW avg pts 6.40; mins 90; xGI 0.05; current GWs 4; fixture Elo diff +22 |
| Palmer | CHE | Midfielder | 4.91 | 4.80 | 4.92 | 4.95 | 4.60 | 19.40 | 2.00 | high | 5-GW avg pts 6.80; mins 88; xGI 0.40; current GWs 4; fixture Elo diff -10 |
| Thiago | BRE | Forward | 4.89 | 4.51 | 4.53 | 5.46 | 5.01 | 19.41 | 2.49 | high | 5-GW avg pts 1.40; mins 88; xGI 0.52; current GWs 4; fixture Elo diff +33 |
| Szoboszlai | LIV | Midfielder | 4.74 | 4.08 | 4.95 | 4.84 | 3.09 | 17.62 | 2.52 | high | 5-GW avg pts 4.00; mins 90; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Cunha | MUN | Midfielder | 4.70 | 4.89 | 4.72 | 4.68 | 4.55 | 18.89 | 2.39 | high | 5-GW avg pts 3.20; mins 63; xGI 0.20; current GWs 4; fixture Elo diff +97 |
| Cherki | MCI | Midfielder | 4.65 | 3.95 | 5.07 | 3.95 | 4.29 | 17.60 | 2.26 | high | 5-GW avg pts 5.40; mins 50; xGI 0.42; current GWs 4; fixture Elo diff +161 |
| Murillo | NFO | Defender | 4.61 | 4.11 | 2.63 | 4.58 | 3.65 | 15.80 | 2.87 | high | 5-GW avg pts 3.80; mins 72; xGI 0.13; current GWs 4; fixture Elo diff +21 |
| Dewsbury-Hall | EVE | Midfielder | 4.55 | 4.28 | 4.19 | 2.67 | 4.01 | 16.03 | 2.47 | high | 5-GW avg pts 3.80; mins 89; xGI 0.23; current GWs 4; fixture Elo diff +22 |
| Branthwaite | EVE | Defender | 4.55 | 4.49 | 4.09 | 2.54 | 3.90 | 15.98 | 2.90 | high | 5-GW avg pts 3.80; mins 72; xGI 0.04; current GWs 4; fixture Elo diff +22 |
| Stach | LEE | Midfielder | 4.52 | 2.50 | 3.44 | 4.79 | 3.79 | 15.16 | 2.53 | high | 5-GW avg pts 4.40; mins 71; xGI 0.23; current GWs 4; fixture Elo diff -81 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 22.29 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Branthwaite | EVE | Defender | £5.5m | 15.98 | GW5, GW6, GW7, GW9 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.64 | GW6, GW7, GW8 | — | — |
| Robinson | FUL | Defender | £4.5m | 14.26 | GW7, GW8 | — | — |
| Davis | IPS | Defender | £4.0m | 13.50 | GW5, GW8, GW9 | — | — |
| Havertz | ARS | Forward | £7.6m | 20.78 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Barry | EVE | Forward | £5.6m | 14.70 | GW5, GW6, GW7, GW9 | — | — |
| J.Angulo | SUN | Forward | £4.5m | 0.37 | Bench | — | — |
| Donnarumma | MCI | Goalkeeper | £5.5m | 15.09 | GW5, GW7, GW9 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.91 | GW6, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 28.60 | GW5, GW6, GW7, GW8, GW9 | GW6, GW7, GW9 | GW5 |
| Saka | ARS | Midfielder | £9.5m | 25.37 | GW5, GW6, GW7, GW8, GW9 | — | GW6, GW7, GW8, GW9 |
| Gibbs-White | NFO | Midfielder | £8.0m | 22.89 | GW5, GW6, GW8, GW9 | GW5, GW8 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 21.13 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Semenyo | MCI | Midfielder | £8.4m | 21.12 | GW5, GW6, GW7, GW8, GW9 | — | — |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 14.90 | GW5, GW6, GW8, GW9 | — | — |
| Maguire | MUN | Defender | £4.9m | 14.87 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Virgil | LIV | Defender | £6.5m | 13.24 | GW5, GW6, GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 12.66 | GW6, GW7, GW8, GW9 | — | — |
| Muñoz | NFO | Defender | £5.4m | 11.70 | GW5, GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 19.41 | GW5, GW6, GW7, GW8, GW9 | — | — |
| João Pedro | CHE | Forward | £7.8m | 12.66 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.39 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.91 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.23 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 28.60 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW9 | GW8 |
| Saka | ARS | Midfielder | £9.5m | 25.37 | GW5, GW6, GW7, GW8, GW9 | GW8 | GW5, GW6, GW7, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.13 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.62 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Gakpo | LIV | Midfielder | £7.2m | 11.46 | GW7 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**João Pedro → Havertz** (projected weighted XI+captain gain 8.12).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| João Pedro | Havertz | £7.6m | £7.6m | £0.2m | 8.12 |
| Gakpo | Wirtz | £7.2m | £7.3m | £0.1m | 4.21 |
| Gakpo | Ødegaard | £7.2m | £6.8m | £0.6m | 3.97 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.5m | £0.9m | 3.94 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 3.89 |
| Gakpo | Rice | £7.2m | £7.4m | £0.0m | 3.88 |
| Muñoz | Truffert | £5.4m | £5.5m | £0.1m | 3.64 |
| Muñoz | Murillo | £5.4m | £5.5m | £0.1m | 3.63 |
| Gakpo | Barnes | £7.2m | £6.0m | £1.4m | 3.48 |
| Gakpo | Stach | £7.2m | £6.0m | £1.4m | 3.30 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
