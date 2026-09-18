# FPL predictions: 2026-2027, GW5

Last generated: 2026-09-18 11:30 UTC

Data commit: `40e335833dc0a94e1e983acc498668c567fb828b`

## Data freshness

All scheduled Premier League fixtures before GW5 are complete.

The model learns from 2025/26 and completed, checked current-season Gameweeks. An equal-weight blend balances the original features with recent participation, longer-window per-90 rates, set-piece roles and observed workload across league, cup, European and friendly matches. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; prices remain fixed. Dated suspensions expire and later injury-return forecasts use a conservative historical recovery rate.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.852 | 1.847 | 0.753 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.020 and Spearman is 0.370.

The predicted top 20 averaged 4.87 actual points versus 1.69 for the selectable pool.

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
| Gibbs-White | NFO | Midfielder | 7.76 | 5.68 | 3.02 | 7.87 | 5.49 | 24.09 | 3.01 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff +21 |
| Haaland | MCI | Forward | 7.62 | 5.43 | 8.15 | 5.43 | 6.15 | 26.51 | 1.70 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +161 |
| B.Fernandes | MUN | Midfielder | 7.11 | 7.34 | 7.52 | 5.49 | 6.80 | 27.66 | 2.30 | high | 5-GW avg pts 8.60; mins 90; xGI 0.73; current GWs 4; fixture Elo diff +97 |
| Saka | ARS | Midfielder | 5.95 | 5.81 | 5.96 | 5.77 | 5.76 | 23.45 | 2.47 | high | 5-GW avg pts 6.00; mins 67; xGI 0.66; current GWs 4; fixture Elo diff +229 |
| Gabriel | ARS | Defender | 5.89 | 6.11 | 6.05 | 6.08 | 5.70 | 23.91 | 2.99 | high | 5-GW avg pts 5.00; mins 81; xGI 0.11; current GWs 4; fixture Elo diff +229 |
| Isak | LIV | Forward | 5.59 | 4.72 | 5.74 | 5.96 | 3.26 | 20.56 | 2.26 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Mbeumo | MUN | Midfielder | 5.56 | 5.35 | 5.65 | 5.02 | 5.44 | 21.68 | 2.74 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +97 |
| Semenyo | MCI | Midfielder | 5.55 | 4.98 | 7.10 | 4.98 | 5.23 | 22.34 | 2.66 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +161 |
| Palmer | CHE | Midfielder | 5.18 | 5.01 | 5.17 | 5.20 | 4.78 | 20.34 | 2.10 | high | 5-GW avg pts 6.80; mins 88; xGI 0.40; current GWs 4; fixture Elo diff -10 |
| Havertz | ARS | Forward | 5.15 | 5.42 | 5.15 | 5.38 | 4.96 | 20.88 | 2.75 | high | 5-GW avg pts 4.20; mins 78; xGI 0.36; current GWs 4; fixture Elo diff +229 |
| Rogers | CHE | Midfielder | 5.11 | 4.80 | 5.18 | 5.07 | 4.54 | 19.85 | 2.58 | high | 5-GW avg pts 5.40; mins 69; xGI 0.51; current GWs 4; fixture Elo diff -10 |
| Thiago | BRE | Forward | 5.06 | 4.58 | 4.66 | 6.12 | 5.16 | 20.30 | 2.60 | high | 5-GW avg pts 1.40; mins 88; xGI 0.52; current GWs 4; fixture Elo diff +33 |
| Tarkowski | EVE | Defender | 4.98 | 4.74 | 3.87 | 2.60 | 3.76 | 16.42 | 2.69 | high | 5-GW avg pts 6.40; mins 90; xGI 0.05; current GWs 4; fixture Elo diff +22 |
| Cunha | MUN | Midfielder | 4.91 | 5.05 | 4.86 | 4.90 | 4.77 | 19.63 | 2.49 | high | 5-GW avg pts 3.20; mins 63; xGI 0.20; current GWs 4; fixture Elo diff +97 |
| Szoboszlai | LIV | Midfielder | 4.84 | 3.75 | 5.09 | 4.57 | 2.86 | 17.19 | 2.46 | high | 5-GW avg pts 4.00; mins 90; xGI 0.57; current GWs 4; fixture Elo diff -6 |
| Branthwaite | EVE | Defender | 4.78 | 4.66 | 4.10 | 2.57 | 3.78 | 16.32 | 2.97 | high | 5-GW avg pts 3.80; mins 72; xGI 0.04; current GWs 4; fixture Elo diff +22 |
| Murillo | NFO | Defender | 4.73 | 4.09 | 2.61 | 4.58 | 3.88 | 16.04 | 2.92 | high | 5-GW avg pts 3.80; mins 72; xGI 0.13; current GWs 4; fixture Elo diff +21 |
| Cherki | MCI | Midfielder | 4.41 | 3.72 | 5.50 | 3.72 | 4.20 | 17.28 | 2.22 | high | 5-GW avg pts 5.40; mins 50; xGI 0.42; current GWs 4; fixture Elo diff +161 |
| Dewsbury-Hall | EVE | Midfielder | 4.33 | 4.26 | 3.96 | 2.75 | 3.94 | 15.62 | 2.40 | high | 5-GW avg pts 3.80; mins 89; xGI 0.23; current GWs 4; fixture Elo diff +22 |
| Garner | EVE | Midfielder | 4.33 | 3.93 | 3.93 | 2.75 | 3.73 | 15.17 | 2.53 | high | 5-GW avg pts 2.40; mins 66; xGI 0.10; current GWs 4; fixture Elo diff +22 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£99.2m**. Total available funds: **£99.4m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 23.91 | GW5, GW6, GW7, GW8, GW9 | — | GW6, GW9 |
| Branthwaite | EVE | Defender | £5.5m | 16.32 | GW5, GW6, GW7, GW9 | — | — |
| Egan | HUL | Defender | £4.1m | 15.16 | GW5, GW7, GW8, GW9 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.95 | GW6, GW7, GW8 | — | — |
| Furlong | IPS | Defender | £3.9m | 1.80 | Bench | — | — |
| Havertz | ARS | Forward | £7.6m | 20.88 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 20.30 | GW5, GW6, GW7, GW8, GW9 | — | GW8 |
| Mheuka | CHE | Forward | £4.5m | 0.37 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.94 | GW6, GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.87 | GW5, GW9 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 27.66 | GW5, GW6, GW7, GW8, GW9 | GW6, GW7, GW9 | GW5 |
| Gibbs-White | NFO | Midfielder | £8.0m | 24.09 | GW5, GW6, GW8, GW9 | GW5, GW8 | — |
| Semenyo | MCI | Midfielder | £8.4m | 22.34 | GW5, GW6, GW7, GW8, GW9 | — | GW7 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.68 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Rogers | CHE | Midfielder | £7.7m | 19.85 | GW5, GW6, GW7, GW8, GW9 | — | — |

Squad cost: £99.4m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maguire | MUN | Defender | £4.9m | 15.36 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Botman | NEW | Defender | £5.0m | 14.54 | GW5, GW6, GW8, GW9 | — | — |
| Virgil | LIV | Defender | £6.5m | 13.12 | GW5, GW7, GW8 | — | — |
| Mitchell | CRY | Defender | £4.5m | 12.73 | GW6, GW7, GW9 | — | — |
| Muñoz | NFO | Defender | £5.4m | 12.10 | GW5, GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 20.30 | GW5, GW6, GW7, GW8, GW9 | GW8 | — |
| João Pedro | CHE | Forward | £7.8m | 12.88 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.37 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.94 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.28 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 27.66 | GW5, GW6, GW7, GW8, GW9 | GW5, GW6, GW7, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 23.45 | GW5, GW6, GW7, GW8, GW9 | — | GW5, GW6, GW7, GW8, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.68 | GW5, GW6, GW7, GW8, GW9 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.19 | GW5, GW6, GW7, GW8 | — | — |
| Gakpo | LIV | Midfielder | £7.2m | 12.81 | GW6, GW7, GW8, GW9 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**João Pedro → Havertz** (projected weighted XI+captain gain 8.00).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| João Pedro | Havertz | £7.6m | £7.6m | £0.2m | 8.00 |
| Mbeumo | Gibbs-White | £7.9m | £8.0m | £0.1m | 4.32 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 3.93 |
| Muñoz | Murillo | £5.4m | £5.5m | £0.1m | 3.62 |
| Virgil | Tarkowski | £6.5m | £6.1m | £0.6m | 3.24 |
| Virgil | Branthwaite | £6.5m | £5.5m | £1.2m | 3.16 |
| Gakpo | Ødegaard | £7.2m | £6.8m | £0.6m | 3.11 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.5m | £0.9m | 3.05 |
| Gakpo | Barnes | £7.2m | £6.0m | £1.4m | 2.97 |
| Gakpo | Schade | £7.2m | £6.1m | £1.3m | 2.96 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
