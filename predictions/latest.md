# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-19 18:45 UTC

Data commit: `14f978d8c435703aeb33ab1289717b75862931be`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW5: 5/10 fixtures finished. Completed clubs contribute current-season form; BOU, COV, CRY, FUL, LEE, LIV, MCI, MUN, NFO, SUN are deferred.

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
| Gabriel | ARS | Defender | 6.15 | 6.08 | 5.95 | 5.25 | 6.68 | 24.07 | 3.01 | high | 5-GW avg pts 5.00; mins 90; xGI 0.12; current GWs 5; fixture Elo diff +291 |
| Gibbs-White | NFO | Midfielder | 5.62 | 2.95 | 7.81 | 5.45 | 3.94 | 20.71 | 2.59 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff -41 |
| Saka | ARS | Midfielder | 5.62 | 5.39 | 5.58 | 5.24 | 6.74 | 22.64 | 2.38 | high | 5-GW avg pts 6.40; mins 83; xGI 0.79; current GWs 5; fixture Elo diff +291 |
| Havertz | ARS | Forward | 5.50 | 5.18 | 5.46 | 4.87 | 6.18 | 21.65 | 2.85 | high | 5-GW avg pts 3.80; mins 87; xGI 0.42; current GWs 5; fixture Elo diff +291 |
| Haaland | MCI | Forward | 5.43 | 8.15 | 5.43 | 6.15 | 6.97 | 25.59 | 1.64 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +144 |
| Mbeumo | MUN | Midfielder | 5.35 | 5.65 | 5.02 | 5.44 | 5.03 | 21.28 | 2.69 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +76 |
| Palmer | CHE | Midfielder | 5.23 | 5.25 | 5.28 | 5.00 | 5.25 | 20.82 | 2.15 | high | 5-GW avg pts 5.60; mins 88; xGI 0.42; current GWs 5; fixture Elo diff +10 |
| Cunha | MUN | Midfielder | 5.05 | 4.86 | 4.90 | 4.77 | 4.85 | 19.60 | 2.48 | high | 5-GW avg pts 3.20; mins 63; xGI 0.20; current GWs 4; fixture Elo diff +76 |
| Semenyo | MCI | Midfielder | 4.98 | 7.10 | 4.98 | 5.23 | 5.30 | 22.19 | 2.64 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +144 |
| Barnes | NEW | Midfielder | 4.89 | 3.56 | 3.93 | 3.92 | 4.10 | 16.45 | 2.70 | high | 5-GW avg pts 5.60; mins 90; xGI 0.21; current GWs 5; fixture Elo diff +37 |
| Rogers | CHE | Midfielder | 4.78 | 4.97 | 4.89 | 4.52 | 5.04 | 19.35 | 2.51 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Botman | NEW | Defender | 4.72 | 3.24 | 3.62 | 3.52 | 3.67 | 15.20 | 3.04 | high | 5-GW avg pts 3.00; mins 90; xGI 0.05; current GWs 5; fixture Elo diff +37 |
| Tarkowski | EVE | Defender | 4.71 | 3.57 | 2.88 | 3.62 | 4.88 | 15.69 | 2.57 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Dewsbury-Hall | EVE | Midfielder | 4.70 | 4.53 | 2.75 | 4.18 | 5.08 | 16.96 | 2.57 | high | 5-GW avg pts 4.00; mins 90; xGI 0.37; current GWs 5; fixture Elo diff +18 |
| Wissa | NEW | Forward | 4.63 | 3.65 | 4.10 | 4.06 | 4.18 | 16.55 | 2.67 | high | 5-GW avg pts 3.00; mins 88; xGI 0.47; current GWs 5; fixture Elo diff +37 |
| Isak | LIV | Forward | 4.50 | 5.64 | 5.68 | 3.04 | 5.72 | 19.68 | 2.16 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff +7 |
| Rice | ARS | Midfielder | 4.37 | 4.26 | 4.38 | 4.03 | 4.88 | 17.45 | 2.36 | high | 5-GW avg pts 4.00; mins 82; xGI 0.16; current GWs 5; fixture Elo diff +291 |
| Bassey | FUL | Defender | 4.36 | 3.90 | 4.51 | 2.83 | 3.33 | 15.46 | 3.44 | high | 5-GW avg pts 3.00; mins 90; xGI 0.03; current GWs 4; fixture Elo diff +95 |
| Branthwaite | EVE | Defender | 4.36 | 3.88 | 2.78 | 3.83 | 4.60 | 15.52 | 2.82 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£99.2m**. Total available funds: **£99.4m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.3m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 24.07 | GW6, GW7, GW8, GW9, GW10 | — | GW6, GW8, GW10 |
| Silva | BOU | Defender | £5.0m | 16.01 | GW6, GW7, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 15.46 | GW6, GW7, GW8 | — | — |
| Robinson | FUL | Defender | £4.5m | 14.59 | GW7, GW8, GW10 | — | — |
| Diop | IPS | Defender | £4.0m | 11.90 | GW9 | — | — |
| Havertz | ARS | Forward | £7.6m | 21.65 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Wissa | NEW | Forward | £6.2m | 16.55 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Walle Egeli | IPS | Forward | £4.5m | 0.84 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 14.47 | GW6, GW7, GW8 | — | — |
| Petrović | BOU | Goalkeeper | £4.5m | 13.32 | GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 26.44 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 22.64 | GW6, GW7, GW8, GW9, GW10 | GW10 | — |
| Semenyo | MCI | Midfielder | £8.4m | 22.19 | GW6, GW7, GW8, GW9, GW10 | — | GW7 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.28 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 20.71 | GW6, GW8, GW9, GW10 | GW8 | GW9 |

Squad cost: £99.1m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Botman | NEW | Defender | £5.0m | 15.20 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Maguire | MUN | Defender | £4.9m | 15.01 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Virgil | LIV | Defender | £6.5m | 13.62 | GW6, GW7, GW8, GW10 | — | — |
| Mitchell | CRY | Defender | £4.5m | 12.20 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Muñoz | NFO | Defender | £5.4m | 11.10 | GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 18.35 | GW6, GW7, GW8, GW9, GW10 | — | GW8 |
| João Pedro | CHE | Forward | £7.8m | 6.43 | Bench | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 14.47 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 1.55 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 26.44 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 22.64 | GW6, GW7, GW8, GW9, GW10 | GW8, GW10 | GW6 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.28 | GW6, GW7, GW8, GW9, GW10 | — | GW7, GW9 |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.48 | GW6, GW7, GW8, GW9, GW10 | — | GW10 |
| Gakpo | LIV | Midfielder | £7.2m | 12.92 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**João Pedro → Havertz** (projected weighted XI+captain gain 9.78).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| João Pedro | Havertz | £7.6m | £7.6m | £0.2m | 9.78 |
| João Pedro | Wissa | £7.6m | £6.2m | £1.6m | 4.67 |
| Gakpo | Rice | £7.2m | £7.4m | £0.0m | 4.52 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.6m | £0.8m | 4.22 |
| Muñoz | Truffert | £5.4m | £5.5m | £0.1m | 4.14 |
| Muñoz | Silva | £5.4m | £5.0m | £0.6m | 4.13 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 3.90 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.1m | 3.70 |
| Gakpo | Schade | £7.2m | £6.1m | £1.3m | 3.67 |
| Muñoz | Bassey | £5.4m | £4.5m | £1.1m | 3.58 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
