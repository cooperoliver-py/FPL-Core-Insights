# FPL predictions: 2026-2027, GW5

Last generated: 2026-09-18 11:07 UTC

Data commit: `3d75be39c74dde9d1a3bc9d2ea235fa27063773f`

## Data freshness

All scheduled Premier League fixtures before GW5 are complete.

The model learns from 2025/26 and completed, checked current-season Gameweeks. An equal-weight blend balances the original features with recent participation, longer-window per-90 rates, set-piece roles and observed workload across league, cup, European and friendly matches. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; prices remain fixed. Dated suspensions expire and later injury-return forecasts use a conservative historical recovery rate.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.852 | 1.848 | 0.752 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.022 and Spearman is 0.369.

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
| Gibbs-White | NFO | Midfielder | 8.35 | 5.80 | 3.00 | 8.01 | 5.54 | 24.90 | 3.11 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff +21 |
| Haaland | MCI | Forward | 7.48 | 5.37 | 8.57 | 5.37 | 6.15 | 26.63 | 1.71 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +161 |
| B.Fernandes | MUN | Midfielder | 7.42 | 7.49 | 7.63 | 6.18 | 7.28 | 28.96 | 2.41 | high | 5-GW avg pts 8.60; mins 90; xGI 0.73; current GWs 4; fixture Elo diff +97 |
| Saka | ARS | Midfielder | 5.96 | 5.95 | 5.93 | 5.92 | 5.72 | 23.64 | 2.49 | high | 5-GW avg pts 6.00; mins 67; xGI 0.66; current GWs 4; fixture Elo diff +229 |
| Isak | LIV | Forward | 5.65 | 4.98 | 5.79 | 6.14 | 3.59 | 21.22 | 2.33 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Semenyo | MCI | Midfielder | 5.54 | 5.00 | 7.06 | 5.00 | 5.29 | 22.36 | 2.66 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +161 |
| Gabriel | ARS | Defender | 5.52 | 5.68 | 5.81 | 5.65 | 5.35 | 22.45 | 2.81 | high | 5-GW avg pts 5.00; mins 81; xGI 0.11; current GWs 4; fixture Elo diff +229 |
| Mbeumo | MUN | Midfielder | 5.31 | 5.24 | 5.49 | 5.04 | 5.32 | 21.15 | 2.68 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +97 |
| Tarkowski | EVE | Defender | 5.15 | 4.86 | 3.93 | 2.55 | 3.92 | 16.81 | 2.76 | high | 5-GW avg pts 6.40; mins 90; xGI 0.05; current GWs 4; fixture Elo diff +22 |
| Palmer | CHE | Midfielder | 5.11 | 4.87 | 5.08 | 5.10 | 4.59 | 19.89 | 2.05 | high | 5-GW avg pts 6.80; mins 88; xGI 0.40; current GWs 4; fixture Elo diff -10 |
| Havertz | ARS | Forward | 5.01 | 5.09 | 5.09 | 5.06 | 4.81 | 20.10 | 2.64 | high | 5-GW avg pts 4.20; mins 78; xGI 0.36; current GWs 4; fixture Elo diff +229 |
| Thiago | BRE | Forward | 4.98 | 4.52 | 4.54 | 5.98 | 5.11 | 19.94 | 2.56 | high | 5-GW avg pts 1.40; mins 88; xGI 0.52; current GWs 4; fixture Elo diff +33 |
| Rogers | CHE | Midfielder | 4.86 | 4.68 | 4.96 | 4.92 | 4.35 | 19.09 | 2.48 | high | 5-GW avg pts 5.40; mins 69; xGI 0.51; current GWs 4; fixture Elo diff -10 |
| Szoboszlai | LIV | Midfielder | 4.83 | 3.71 | 5.07 | 4.70 | 2.84 | 17.22 | 2.46 | high | 5-GW avg pts 4.00; mins 90; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Garner | EVE | Midfielder | 4.65 | 4.29 | 4.20 | 2.95 | 4.01 | 16.34 | 2.72 | high | 5-GW avg pts 2.40; mins 66; xGI 0.10; current GWs 4; fixture Elo diff +22 |
| Cunha | MUN | Midfielder | 4.64 | 4.77 | 4.60 | 4.56 | 4.50 | 18.51 | 2.34 | high | 5-GW avg pts 3.20; mins 63; xGI 0.20; current GWs 4; fixture Elo diff +97 |
| Branthwaite | EVE | Defender | 4.64 | 4.55 | 3.87 | 2.47 | 3.72 | 15.80 | 2.87 | high | 5-GW avg pts 3.80; mins 72; xGI 0.04; current GWs 4; fixture Elo diff +22 |
| Dewsbury-Hall | EVE | Midfielder | 4.60 | 4.40 | 3.98 | 2.68 | 4.07 | 16.07 | 2.47 | high | 5-GW avg pts 3.80; mins 89; xGI 0.23; current GWs 4; fixture Elo diff +22 |
| Ødegaard | ARS | Midfielder | 4.39 | 4.40 | 4.33 | 4.40 | 4.27 | 17.46 | 2.57 | high | 5-GW avg pts 5.40; mins 61; xGI 0.46; current GWs 4; fixture Elo diff +229 |
| Guéhi | MCI | Defender | 4.39 | 3.48 | 4.58 | 3.48 | 3.79 | 15.89 | 2.65 | high | 5-GW avg pts 5.20; mins 72; xGI 0.25; current GWs 4; fixture Elo diff +161 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## ML-optimal £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 22.45 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Egan | HUL | Defender | £4.1m | 14.78 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.26 | GW6, GW7, GW8 | — | — |
| Davis | IPS | Defender | £4.0m | 13.36 | GW5, GW9 | — | — |
| Thomas | COV | Defender | £4.0m | 12.67 | GW7 | — | — |
| Havertz | ARS | Forward | £7.6m | 20.10 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 19.94 | GW5, GW6, GW7, GW8, GW9 | — | — |
| J.Angulo | SUN | Forward | £4.5m | 0.36 | Bench | — | — |
| Donnarumma | MCI | Goalkeeper | £5.5m | 15.23 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Davies | LIV | Goalkeeper | £4.0m | 0.35 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 28.96 | GW5, GW6, GW7, GW8, GW9 | GW6, GW7, GW9 | GW5, GW8 |
| Gibbs-White | NFO | Midfielder | £8.0m | 24.90 | GW5, GW6, GW8, GW9 | GW5, GW8 | — |
| Saka | ARS | Midfielder | £9.5m | 23.64 | GW5, GW6, GW7, GW8, GW9 | — | GW6, GW9 |
| Semenyo | MCI | Midfielder | £8.4m | 22.36 | GW5, GW6, GW7, GW8, GW9 | — | GW7 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.15 | GW5, GW6, GW7, GW8, GW9 | — | — |

Squad cost: £99.8m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maguire | MUN | Defender | £4.9m | 15.17 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Botman | NEW | Defender | £5.0m | 14.54 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Virgil | LIV | Defender | £6.5m | 12.71 | GW5, GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 12.44 | GW6, GW7, GW9 | — | — |
| Muñoz | NFO | Defender | £5.4m | 11.88 | GW5, GW8, GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 19.94 | GW5, GW6, GW7, GW8, GW9 | — | GW8 |
| João Pedro | CHE | Forward | £7.8m | 12.37 | GW6, GW9 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.36 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.36 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.09 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 28.96 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW8, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 23.64 | GW5, GW6, GW7, GW8, GW9 | — | GW5, GW6, GW7, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.15 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.22 | GW5, GW6, GW7, GW8 | — | — |
| Gakpo | LIV | Midfielder | £7.2m | 13.45 | GW5, GW6, GW7, GW8, GW9 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**João Pedro → Havertz** (projected weighted XI+captain gain 7.56).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| João Pedro | Havertz | £7.6m | £7.6m | £0.2m | 7.56 |
| Mbeumo | Gibbs-White | £7.9m | £8.0m | £0.1m | 5.99 |
| Virgil | Tarkowski | £6.5m | £6.1m | £0.6m | 4.11 |
| Gakpo | Ødegaard | £7.2m | £6.8m | £0.6m | 4.00 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 3.70 |
| Saka | Gibbs-White | £9.5m | £8.0m | £1.7m | 3.50 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.1m | 3.35 |
| João Pedro | Barry | £7.6m | £5.6m | £2.2m | 3.23 |
| Virgil | Branthwaite | £6.5m | £5.5m | £1.2m | 3.16 |
| Gakpo | Garner | £7.2m | £6.0m | £1.4m | 3.05 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
