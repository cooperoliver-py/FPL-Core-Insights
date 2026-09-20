# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-20 13:11 UTC

Data commit: `2d5d12302676a344241fe21a908391a39efcbd6d`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW5: 6/10 fixtures finished. Completed clubs contribute current-season form; BOU, CRY, FUL, LEE, LIV, MCI, MUN, SUN are deferred.

Incomplete Gameweeks are not scored in live performance reporting until the official data is finished and checked.

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

## Top GW6 player forecasts

| Player | Club | Pos | GW6 | GW7 | GW8 | GW9 | GW10 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 7.30 | 7.48 | 5.49 | 6.80 | 5.43 | 26.44 | 2.20 | high | 5-GW avg pts 8.60; mins 90; xGI 0.73; current GWs 4; fixture Elo diff +76 |
| Gabriel | ARS | Defender | 6.18 | 6.11 | 5.98 | 5.28 | 6.64 | 24.15 | 3.02 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Gibbs-White | NFO | Midfielder | 6.02 | 2.99 | 8.12 | 5.81 | 4.07 | 21.72 | 2.71 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| Saka | ARS | Midfielder | 5.55 | 5.32 | 5.51 | 5.22 | 6.67 | 22.41 | 2.36 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Havertz | ARS | Forward | 5.48 | 5.17 | 5.44 | 4.85 | 6.11 | 21.55 | 2.84 | high | 5-GW avg pts 3.80; mins 87; xGI 0.41; current GWs 5; fixture Elo diff +291 |
| Haaland | MCI | Forward | 5.43 | 8.15 | 5.43 | 6.15 | 6.97 | 25.59 | 1.64 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +144 |
| Mbeumo | MUN | Midfielder | 5.35 | 5.65 | 5.02 | 5.44 | 5.03 | 21.28 | 2.69 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +76 |
| Palmer | CHE | Midfielder | 5.23 | 5.25 | 5.28 | 5.00 | 5.25 | 20.82 | 2.15 | high | 5-GW avg pts 5.60; mins 88; xGI 0.42; current GWs 5; fixture Elo diff +10 |
| Cunha | MUN | Midfielder | 5.07 | 4.88 | 4.91 | 4.79 | 4.85 | 19.66 | 2.49 | high | 5-GW avg pts 3.20; mins 63; xGI 0.20; current GWs 4; fixture Elo diff +76 |
| Semenyo | MCI | Midfielder | 4.98 | 7.10 | 4.98 | 5.23 | 5.30 | 22.19 | 2.64 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +144 |
| Barnes | NEW | Midfielder | 4.96 | 3.58 | 4.03 | 4.02 | 4.24 | 16.76 | 2.75 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Dewsbury-Hall | EVE | Midfielder | 4.83 | 4.69 | 2.80 | 4.36 | 5.20 | 17.46 | 2.65 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Botman | NEW | Defender | 4.82 | 3.32 | 3.63 | 3.60 | 3.67 | 15.43 | 3.09 | high | 5-GW avg pts 3.00; mins 90; xGI 0.05; current GWs 5; fixture Elo diff +37 |
| Rogers | CHE | Midfielder | 4.78 | 4.97 | 4.89 | 4.52 | 5.04 | 19.35 | 2.51 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Wissa | NEW | Forward | 4.71 | 3.69 | 4.17 | 4.13 | 4.25 | 16.82 | 2.71 | high | 5-GW avg pts 3.00; mins 88; xGI 0.48; current GWs 5; fixture Elo diff +37 |
| Tarkowski | EVE | Defender | 4.58 | 3.69 | 2.77 | 3.57 | 4.93 | 15.58 | 2.55 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Isak | LIV | Forward | 4.50 | 5.64 | 5.68 | 3.04 | 5.72 | 19.68 | 2.16 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff +7 |
| Bassey | FUL | Defender | 4.36 | 3.90 | 4.51 | 2.83 | 3.33 | 15.46 | 3.44 | high | 5-GW avg pts 3.00; mins 90; xGI 0.03; current GWs 4; fixture Elo diff +95 |
| Rice | ARS | Midfielder | 4.36 | 4.25 | 4.37 | 3.98 | 4.78 | 17.33 | 2.34 | high | 5-GW avg pts 4.00; mins 82; xGI 0.16; current GWs 5; fixture Elo diff +291 |
| Branthwaite | EVE | Defender | 4.35 | 3.94 | 2.84 | 3.87 | 4.61 | 15.65 | 2.85 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£99.2m**. Total available funds: **£99.4m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.3m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 24.15 | GW6, GW7, GW8, GW9, GW10 | — | GW6, GW8, GW10 |
| Silva | BOU | Defender | £5.0m | 15.85 | GW7, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 15.46 | GW6, GW7, GW8 | — | — |
| Robinson | FUL | Defender | £4.5m | 14.59 | GW6, GW7, GW8, GW10 | — | — |
| Diop | IPS | Defender | £4.0m | 12.19 | GW9 | — | — |
| Havertz | ARS | Forward | £7.6m | 21.55 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Wissa | NEW | Forward | £6.2m | 16.82 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 14.47 | GW6, GW7, GW8 | — | — |
| Petrović | BOU | Goalkeeper | £4.5m | 13.32 | GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 26.44 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 22.41 | GW6, GW7, GW8, GW9, GW10 | GW10 | — |
| Semenyo | MCI | Midfielder | £8.4m | 22.19 | GW6, GW7, GW8, GW9, GW10 | — | GW7 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.72 | GW6, GW8, GW9, GW10 | GW8 | GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.28 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 15.43 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Maguire | MUN | Defender | £4.9m | 14.77 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Virgil | LIV | Defender | £6.5m | 13.62 | GW6, GW7, GW8, GW10 | — | — |
| Mitchell | CRY | Defender | £4.5m | 12.20 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Muñoz | NFO | Defender | £5.4m | 10.32 | GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 18.35 | GW6, GW7, GW8, GW9, GW10 | GW8 | — |
| João Pedro | CHE | Forward | £7.8m | 6.43 | Bench | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 14.47 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 1.55 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 26.44 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 22.41 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW6, GW8 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.28 | GW6, GW7, GW8, GW9, GW10 | — | GW7, GW9 |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.41 | GW6, GW7, GW8, GW9, GW10 | — | GW10 |
| Gakpo | LIV | Midfielder | £7.2m | 12.92 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**João Pedro → Havertz** (projected weighted XI+captain gain 9.85).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| João Pedro | Havertz | £7.6m | £7.6m | £0.2m | 9.85 |
| João Pedro | Wissa | £7.6m | £6.2m | £1.6m | 5.12 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.6m | £0.8m | 4.54 |
| Gakpo | Rice | £7.2m | £7.4m | £0.0m | 4.40 |
| Muñoz | Truffert | £5.4m | £5.5m | £0.1m | 4.24 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 4.16 |
| Muñoz | Silva | £5.4m | £5.0m | £0.6m | 4.15 |
| Muñoz | Murillo | £5.4m | £5.5m | £0.1m | 3.93 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.1m | 3.88 |
| João Pedro | Barry | £7.6m | £5.6m | £2.2m | 3.85 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
