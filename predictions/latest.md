# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-19 12:39 UTC

Data commit: `89ea571c75e27bf8e5587f3f8a1f7c8a798bcf3e`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW5: 1/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, BHA, BOU, COV, CRY, EVE, FUL, HUL, IPS, LEE, LIV, MCI, MUN, NEW, NFO, SUN, TOT are deferred.

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
| Gabriel | ARS | Defender | 6.13 | 6.07 | 6.09 | 5.72 | 6.35 | 24.28 | 3.04 | high | 5-GW avg pts 5.00; mins 81; xGI 0.11; current GWs 4; fixture Elo diff +291 |
| Saka | ARS | Midfielder | 5.81 | 5.96 | 5.77 | 5.76 | 7.07 | 24.07 | 2.53 | high | 5-GW avg pts 6.00; mins 67; xGI 0.66; current GWs 4; fixture Elo diff +291 |
| Gibbs-White | NFO | Midfielder | 5.68 | 3.02 | 7.87 | 5.49 | 4.01 | 20.94 | 2.62 | high | 5-GW avg pts 7.00; mins 90; xGI 0.62; current GWs 4; fixture Elo diff -41 |
| Haaland | MCI | Forward | 5.43 | 8.15 | 5.43 | 6.15 | 6.97 | 25.59 | 1.64 | high | 5-GW avg pts 6.60; mins 72; xGI 0.77; current GWs 4; fixture Elo diff +144 |
| Havertz | ARS | Forward | 5.42 | 5.15 | 5.38 | 4.96 | 6.34 | 21.63 | 2.85 | high | 5-GW avg pts 4.20; mins 78; xGI 0.36; current GWs 4; fixture Elo diff +291 |
| Mbeumo | MUN | Midfielder | 5.35 | 5.65 | 5.02 | 5.44 | 5.03 | 21.28 | 2.69 | high | 5-GW avg pts 6.40; mins 87; xGI 0.86; current GWs 4; fixture Elo diff +76 |
| Palmer | CHE | Midfielder | 5.23 | 5.25 | 5.28 | 5.00 | 5.25 | 20.82 | 2.15 | high | 5-GW avg pts 5.60; mins 88; xGI 0.42; current GWs 5; fixture Elo diff +10 |
| Cunha | MUN | Midfielder | 5.05 | 4.86 | 4.90 | 4.77 | 4.85 | 19.60 | 2.48 | high | 5-GW avg pts 3.20; mins 63; xGI 0.20; current GWs 4; fixture Elo diff +76 |
| Semenyo | MCI | Midfielder | 4.98 | 7.10 | 4.98 | 5.23 | 5.30 | 22.19 | 2.64 | high | 5-GW avg pts 4.40; mins 83; xGI 0.27; current GWs 4; fixture Elo diff +144 |
| Rogers | CHE | Midfielder | 4.78 | 4.97 | 4.89 | 4.52 | 5.04 | 19.35 | 2.51 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Tarkowski | EVE | Defender | 4.74 | 3.87 | 2.60 | 3.76 | 5.02 | 15.96 | 2.62 | high | 5-GW avg pts 6.40; mins 90; xGI 0.05; current GWs 4; fixture Elo diff +18 |
| Isak | LIV | Forward | 4.72 | 5.74 | 5.96 | 3.26 | 5.79 | 20.41 | 2.24 | high | 5-GW avg pts 5.00; mins 67; xGI 0.57; current GWs 4; fixture Elo diff +7 |
| Branthwaite | EVE | Defender | 4.66 | 4.10 | 2.57 | 3.78 | 4.90 | 16.00 | 2.91 | high | 5-GW avg pts 3.80; mins 72; xGI 0.04; current GWs 4; fixture Elo diff +18 |
| Dewsbury-Hall | EVE | Midfielder | 4.50 | 4.18 | 2.85 | 4.15 | 4.85 | 16.35 | 2.48 | high | 5-GW avg pts 3.80; mins 89; xGI 0.23; current GWs 4; fixture Elo diff +18 |
| Barnes | NEW | Midfielder | 4.43 | 3.48 | 3.99 | 3.98 | 4.07 | 15.98 | 2.62 | high | 5-GW avg pts 4.00; mins 81; xGI 0.20; current GWs 4; fixture Elo diff +37 |
| Bassey | FUL | Defender | 4.35 | 3.95 | 4.50 | 2.78 | 3.28 | 15.41 | 3.42 | high | 5-GW avg pts 3.00; mins 90; xGI 0.03; current GWs 4; fixture Elo diff +95 |
| Groß | BHA | Midfielder | 4.32 | 4.17 | 3.90 | 3.19 | 4.22 | 15.95 | 2.80 | high | 5-GW avg pts 7.00; mins 90; xGI 0.51; current GWs 4; fixture Elo diff -10 |
| Botman | NEW | Defender | 4.24 | 3.06 | 3.20 | 3.27 | 3.24 | 13.79 | 2.76 | high | 5-GW avg pts 2.80; mins 90; xGI 0.04; current GWs 4; fixture Elo diff +37 |
| Ødegaard | ARS | Midfielder | 4.22 | 3.85 | 4.18 | 3.84 | 4.84 | 16.62 | 2.44 | high | 5-GW avg pts 5.40; mins 61; xGI 0.46; current GWs 4; fixture Elo diff +291 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£99.2m**. Total available funds: **£99.4m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.3m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 24.28 | GW6, GW7, GW8, GW9, GW10 | — | GW6, GW8, GW10 |
| Branthwaite | EVE | Defender | £5.5m | 16.00 | GW6, GW7, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 15.41 | GW6, GW7, GW8 | — | — |
| Egan | HUL | Defender | £4.1m | 15.00 | GW6, GW8, GW9 | — | — |
| Robinson | FUL | Defender | £4.5m | 14.59 | GW7, GW8, GW10 | — | — |
| Havertz | ARS | Forward | £7.6m | 21.63 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Barry | EVE | Forward | £5.6m | 14.86 | GW7, GW9, GW10 | — | — |
| Walle Egeli | IPS | Forward | £4.5m | 0.88 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 14.36 | GW6, GW7, GW8 | — | — |
| Petrović | BOU | Goalkeeper | £4.5m | 13.32 | GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 26.44 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 24.07 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW9 |
| Semenyo | MCI | Midfielder | £8.4m | 22.19 | GW6, GW7, GW8, GW9, GW10 | — | GW7 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.28 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 20.94 | GW6, GW8, GW9, GW10 | GW8 | — |

Squad cost: £99.1m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maguire | MUN | Defender | £4.9m | 15.01 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Botman | NEW | Defender | £5.0m | 13.79 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Virgil | LIV | Defender | £6.5m | 13.37 | GW7, GW8, GW10 | — | — |
| Mitchell | CRY | Defender | £4.5m | 12.20 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Muñoz | NFO | Defender | £5.4m | 11.42 | GW6, GW9 | — | — |
| Thiago | BRE | Forward | £7.8m | 18.35 | GW6, GW7, GW8, GW9, GW10 | — | GW8 |
| João Pedro | CHE | Forward | £7.8m | 7.25 | Bench | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 14.36 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Pope | NEW | Goalkeeper | £4.9m | 2.27 | Bench | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 26.44 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7, GW9 | — |
| Saka | ARS | Midfielder | £9.5m | 24.07 | GW6, GW7, GW8, GW9, GW10 | GW8, GW10 | GW6, GW7, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 21.28 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 17.26 | GW6, GW7, GW8, GW9, GW10 | — | GW10 |
| Gakpo | LIV | Midfielder | £7.2m | 12.92 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**João Pedro → Havertz** (projected weighted XI+captain gain 9.67).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| João Pedro | Havertz | £7.6m | £7.6m | £0.2m | 9.67 |
| Muñoz | Branthwaite | £5.4m | £5.5m | £0.1m | 4.41 |
| Muñoz | Truffert | £5.4m | £5.5m | £0.1m | 4.01 |
| Muñoz | Silva | £5.4m | £5.0m | £0.6m | 4.00 |
| Gakpo | Ødegaard | £7.2m | £6.8m | £0.6m | 3.70 |
| Gakpo | Schade | £7.2m | £6.1m | £1.3m | 3.67 |
| Gakpo | Dewsbury-Hall | £7.2m | £6.6m | £0.8m | 3.61 |
| Muñoz | Rúben | £5.4m | £5.5m | £0.1m | 3.57 |
| João Pedro | Barry | £7.6m | £5.6m | £2.2m | 3.46 |
| Muñoz | Bassey | £5.4m | £4.5m | £1.1m | 3.40 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
