# FPL predictions: 2026-2027, GW5

Last generated: 2026-09-18 10:44 UTC

Data commit: `40e335833dc0a94e1e983acc498668c567fb828b`

## Data freshness

All scheduled Premier League fixtures before GW5 are complete.

The model learns from 2025/26 and completed, checked current-season Gameweeks. An equal-weight blend balances the original features with recent participation, longer-window per-90 rates, set-piece roles and observed workload across league, cup, European and friendly matches. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; prices remain fixed. Dated suspensions expire and later injury-return forecasts use a conservative historical recovery rate.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.849 | 1.846 | 0.752 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.016 and Spearman is 0.368.

The predicted top 20 averaged 4.78 actual points versus 1.69 for the selectable pool.

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
| Gibbs-White | NFO | Midfielder | 7.78 | 5.98 | 3.12 | 7.77 | 5.65 | 24.49 | 3.06 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff +21 |
| Haaland | MCI | Forward | 7.21 | 5.37 | 7.68 | 5.37 | 6.09 | 25.61 | 1.64 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +161 |
| B.Fernandes | MUN | Midfielder | 6.99 | 7.41 | 7.20 | 6.14 | 6.76 | 27.78 | 2.31 | high | 5-GW avg pts 8.60; mins 90; xGI 0.73; current GWs 4; fixture Elo diff +97 |
| Saka | ARS | Midfielder | 6.05 | 5.88 | 5.99 | 5.83 | 5.95 | 23.79 | 2.50 | high | 5-GW avg pts 6.00; mins 67; xGI 0.66; current GWs 4; fixture Elo diff +229 |
| Isak | LIV | Forward | 5.62 | 4.64 | 5.70 | 5.83 | 3.18 | 20.34 | 2.24 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Mbeumo | MUN | Midfielder | 5.43 | 5.66 | 5.63 | 5.31 | 5.41 | 22.00 | 2.78 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +97 |
| Semenyo | MCI | Midfielder | 5.35 | 4.92 | 6.29 | 4.90 | 5.20 | 21.37 | 2.54 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +161 |
| Gabriel | ARS | Defender | 5.26 | 5.46 | 5.48 | 5.37 | 5.27 | 21.47 | 2.68 | high | 5-GW avg pts 5.00; mins 81; xGI 0.11; current GWs 4; fixture Elo diff +229 |
| Palmer | CHE | Midfielder | 5.15 | 5.07 | 5.17 | 5.25 | 4.86 | 20.44 | 2.11 | high | 5-GW avg pts 6.80; mins 88; xGI 0.40; current GWs 4; fixture Elo diff -10 |
| Havertz | ARS | Forward | 5.15 | 5.22 | 5.19 | 5.22 | 5.01 | 20.66 | 2.72 | high | 5-GW avg pts 4.20; mins 78; xGI 0.36; current GWs 4; fixture Elo diff +229 |
| Rogers | CHE | Midfielder | 5.05 | 4.94 | 5.12 | 5.14 | 4.66 | 19.99 | 2.60 | high | 5-GW avg pts 5.40; mins 69; xGI 0.51; current GWs 4; fixture Elo diff -10 |
| Thiago | BRE | Forward | 4.92 | 4.48 | 4.51 | 5.38 | 5.03 | 19.33 | 2.48 | high | 5-GW avg pts 1.40; mins 88; xGI 0.52; current GWs 4; fixture Elo diff +33 |
| Szoboszlai | LIV | Midfielder | 4.90 | 3.94 | 5.07 | 4.85 | 2.80 | 17.57 | 2.51 | high | 5-GW avg pts 4.00; mins 90; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Murillo | NFO | Defender | 4.84 | 4.22 | 2.65 | 4.79 | 3.69 | 16.32 | 2.97 | high | 5-GW avg pts 3.80; mins 72; xGI 0.13; current GWs 4; fixture Elo diff +21 |
| Tarkowski | EVE | Defender | 4.81 | 4.65 | 3.87 | 2.31 | 3.71 | 15.93 | 2.61 | high | 5-GW avg pts 6.40; mins 90; xGI 0.05; current GWs 4; fixture Elo diff +22 |
| Cunha | MUN | Midfielder | 4.70 | 4.87 | 4.67 | 4.70 | 4.54 | 18.83 | 2.38 | high | 5-GW avg pts 3.20; mins 63; xGI 0.20; current GWs 4; fixture Elo diff +97 |
| Branthwaite | EVE | Defender | 4.64 | 4.68 | 4.05 | 2.64 | 3.89 | 16.27 | 2.96 | high | 5-GW avg pts 3.80; mins 72; xGI 0.04; current GWs 4; fixture Elo diff +22 |
| Stach | LEE | Midfielder | 4.46 | 2.53 | 3.54 | 4.71 | 3.82 | 15.15 | 2.53 | high | 5-GW avg pts 4.40; mins 71; xGI 0.23; current GWs 4; fixture Elo diff -81 |
| Garner | EVE | Midfielder | 4.43 | 4.04 | 4.00 | 2.77 | 3.87 | 15.53 | 2.59 | high | 5-GW avg pts 2.40; mins 66; xGI 0.10; current GWs 4; fixture Elo diff +22 |
| Cherki | MCI | Midfielder | 4.42 | 3.91 | 4.98 | 3.89 | 4.21 | 17.17 | 2.20 | high | 5-GW avg pts 5.40; mins 50; xGI 0.42; current GWs 4; fixture Elo diff +161 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.47 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Murillo | NFO | Defender | £5.5m | 16.32 | GW5, GW6, GW8, GW9 | — | — |
| Branthwaite | EVE | Defender | £5.5m | 16.27 | GW5, GW6, GW7, GW9 | — | — |
| Egan | HUL | Defender | £4.1m | 14.79 | GW5, GW7, GW8, GW9 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.57 | GW6, GW7, GW8 | — | — |
| Havertz | ARS | Forward | £7.6m | 20.66 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Kusi-Asare | FUL | Forward | £4.5m | 0.45 | Bench | — | — |
| Danns | LIV | Forward | £4.5m | 0.33 | Bench | — | — |
| Donnarumma | MCI | Goalkeeper | £5.5m | 15.55 | GW5, GW7, GW9 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.68 | GW6, GW8 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 27.78 | GW5, GW6, GW7, GW8, GW9 | GW6, GW7, GW9 | GW5, GW8 |
| Gibbs-White | NFO | Midfielder | £8.0m | 24.49 | GW5, GW6, GW7, GW8, GW9 | GW5, GW8 | GW6 |
| Saka | ARS | Midfielder | £9.5m | 23.79 | GW5, GW6, GW7, GW8, GW9 | — | GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 22.00 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Semenyo | MCI | Midfielder | £8.4m | 21.37 | GW5, GW6, GW7, GW8, GW9 | — | GW7 |

Squad cost: £100.0m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maguire | MUN | Defender | £4.9m | 14.63 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Botman | NEW | Defender | £5.0m | 14.35 | GW5, GW6, GW9 | — | — |
| Mitchell | CRY | Defender | £4.5m | 13.19 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Virgil | LIV | Defender | £6.5m | 12.98 | GW5, GW6, GW7, GW8 | — | — |
| Muñoz | NFO | Defender | £5.4m | 11.68 | GW8, GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 19.33 | GW5, GW6, GW7, GW8, GW9 | — | — |
| João Pedro | CHE | Forward | £7.8m | 13.21 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.68 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.24 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 27.78 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW8, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 23.79 | GW5, GW6, GW7, GW8, GW9 | — | GW5, GW6, GW7, GW8, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 22.00 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.57 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Gakpo | LIV | Midfielder | £7.2m | 11.31 | GW7 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**João Pedro → Havertz** (projected weighted XI+captain gain 7.46).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| João Pedro | Havertz | £7.6m | £7.6m | £0.2m | 7.46 |
| Gakpo | Rice | £7.2m | £7.4m | £0.0m | 4.76 |
| Mbeumo | Gibbs-White | £7.9m | £8.0m | £0.1m | 4.42 |
| Muñoz | Murillo | £5.4m | £5.5m | £0.1m | 4.19 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 4.17 |
| Gakpo | Groß | £7.2m | £5.7m | £1.7m | 3.72 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.5m | £0.9m | 3.63 |
| Gakpo | Ødegaard | £7.2m | £6.8m | £0.6m | 3.54 |
| Gakpo | Wirtz | £7.2m | £7.3m | £0.1m | 3.44 |
| Gakpo | Garner | £7.2m | £6.0m | £1.4m | 3.43 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
