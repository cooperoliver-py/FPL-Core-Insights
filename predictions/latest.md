# FPL predictions: 2026-2027, GW6

Last generated: 2026-09-21 12:55 UTC

Data commit: `6aca7d9a5d06578a911b9591a2727f56124faae2`

## Data freshness

All scheduled Premier League fixtures before GW6 are complete.

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
| Gabriel | ARS | Defender | 6.13 | 6.06 | 5.93 | 5.23 | 6.64 | 23.98 | 3.00 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Gibbs-White | NFO | Midfielder | 5.97 | 2.94 | 8.12 | 5.76 | 4.02 | 21.56 | 2.70 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| Mbeumo | MUN | Midfielder | 5.91 | 6.15 | 5.73 | 5.88 | 5.66 | 23.54 | 2.98 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +76 |
| B.Fernandes | MUN | Midfielder | 5.76 | 6.11 | 5.31 | 5.63 | 5.25 | 22.60 | 1.88 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +76 |
| Saka | ARS | Midfielder | 5.55 | 5.32 | 5.51 | 5.22 | 6.67 | 22.41 | 2.36 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Havertz | ARS | Forward | 5.48 | 5.17 | 5.44 | 4.85 | 6.11 | 21.55 | 2.84 | high | 5-GW avg pts 3.80; mins 87; xGI 0.41; current GWs 5; fixture Elo diff +291 |
| Palmer | CHE | Midfielder | 5.23 | 5.25 | 5.28 | 5.00 | 5.25 | 20.82 | 2.15 | high | 5-GW avg pts 5.60; mins 88; xGI 0.42; current GWs 5; fixture Elo diff +10 |
| Haaland | MCI | Forward | 4.99 | 7.55 | 4.99 | 5.40 | 5.89 | 23.09 | 1.48 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +144 |
| Barnes | NEW | Midfielder | 4.96 | 3.53 | 3.98 | 3.97 | 4.20 | 16.62 | 2.72 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Dewsbury-Hall | EVE | Midfielder | 4.83 | 4.64 | 2.75 | 4.31 | 5.20 | 17.35 | 2.63 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Botman | NEW | Defender | 4.82 | 3.27 | 3.58 | 3.55 | 3.62 | 15.29 | 3.06 | high | 5-GW avg pts 3.00; mins 90; xGI 0.05; current GWs 5; fixture Elo diff +37 |
| Cunha | MUN | Midfielder | 4.81 | 4.64 | 4.67 | 4.56 | 4.62 | 18.68 | 2.36 | high | 5-GW avg pts 5.20; mins 81; xGI 0.29; current GWs 5; fixture Elo diff +76 |
| Semenyo | MCI | Midfielder | 4.79 | 7.38 | 4.79 | 5.01 | 5.77 | 22.25 | 2.65 | high | 5-GW avg pts 6.60; mins 90; xGI 0.30; current GWs 5; fixture Elo diff +144 |
| Rogers | CHE | Midfielder | 4.78 | 4.97 | 4.89 | 4.52 | 5.04 | 19.35 | 2.51 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Wissa | NEW | Forward | 4.71 | 3.69 | 4.17 | 4.13 | 4.25 | 16.82 | 2.71 | high | 5-GW avg pts 3.00; mins 88; xGI 0.48; current GWs 5; fixture Elo diff +37 |
| Tarkowski | EVE | Defender | 4.58 | 3.64 | 2.72 | 3.52 | 4.93 | 15.46 | 2.53 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Rice | ARS | Midfielder | 4.36 | 4.25 | 4.37 | 3.98 | 4.78 | 17.33 | 2.34 | high | 5-GW avg pts 4.00; mins 82; xGI 0.16; current GWs 5; fixture Elo diff +291 |
| Branthwaite | EVE | Defender | 4.35 | 3.89 | 2.79 | 3.82 | 4.61 | 15.54 | 2.82 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Isak | LIV | Forward | 4.30 | 4.91 | 5.32 | 2.88 | 5.08 | 18.03 | 1.98 | high | 5-GW avg pts 6.60; mins 83; xGI 0.72; current GWs 5; fixture Elo diff +7 |
| Murillo | NFO | Defender | 4.20 | 2.76 | 4.95 | 3.91 | 3.13 | 15.26 | 2.77 | high | 5-GW avg pts 4.60; mins 90; xGI 0.16; current GWs 5; fixture Elo diff -41 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.0m**. Current squad selling value: **£99.4m**. Total available funds: **£99.4m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 23.98 | GW6, GW7, GW8, GW9, GW10 | GW6 | GW8, GW10 |
| Truffert | BOU | Defender | £5.5m | 16.97 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Silva | BOU | Defender | £5.0m | 15.96 | GW7, GW9, GW10 | — | — |
| Botman | NEW | Defender | £5.0m | 15.29 | GW6 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.09 | GW7, GW8 | — | — |
| Havertz | ARS | Forward | £7.6m | 21.55 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Thiago | BRE | Forward | £7.8m | 18.35 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Walle Egeli | IPS | Forward | £4.5m | 0.84 | Bench | — | — |
| Donnarumma | MCI | Goalkeeper | £5.5m | 14.05 | GW7, GW9, GW10 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.20 | GW6, GW8 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 23.54 | GW6, GW7, GW8, GW9, GW10 | GW9 | GW7 |
| Saka | ARS | Midfielder | £9.5m | 22.41 | GW6, GW7, GW8, GW9, GW10 | GW10 | — |
| Semenyo | MCI | Midfielder | £8.4m | 22.25 | GW6, GW7, GW8, GW9, GW10 | GW7 | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.56 | GW6, GW8, GW9, GW10 | GW8 | GW6, GW9 |
| Rogers | CHE | Midfielder | £7.7m | 19.35 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.4m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 23.98 | GW6, GW7, GW8, GW9, GW10 | GW6, GW10 | GW8 |
| Branthwaite | EVE | Defender | £5.5m | 15.54 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.09 | GW6, GW7, GW8, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 10.67 | GW9 | — | — |
| Furlong | IPS | Defender | £3.9m | 1.16 | Bench | — | — |
| Havertz | ARS | Forward | £7.6m | 21.55 | GW6, GW7, GW8, GW9, GW10 | — | GW10 |
| Thiago | BRE | Forward | £7.8m | 18.35 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.20 | GW7, GW8, GW10 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 12.96 | GW6, GW9 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 23.54 | GW6, GW7, GW8, GW9, GW10 | GW9 | GW7 |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.60 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Semenyo | MCI | Midfielder | £8.4m | 22.25 | GW6, GW7, GW8, GW9, GW10 | GW7 | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.56 | GW6, GW7, GW8, GW9, GW10 | GW8 | GW6, GW9 |
| Rogers | CHE | Midfielder | £7.7m | 19.35 | GW6, GW7, GW8, GW9, GW10 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Branthwaite → Truffert** (projected weighted XI+captain gain 1.44).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Branthwaite | Truffert | £5.5m | £5.5m | £0.0m | 1.44 |
| Egan | Davis | £4.1m | £4.0m | £0.1m | 0.83 |
| Egan | Diop | £4.1m | £4.0m | £0.1m | 0.81 |
| Branthwaite | Silva | £5.5m | £5.0m | £0.5m | 0.42 |
| Egan | O'Shea | £4.1m | £4.0m | £0.1m | 0.29 |
| Branthwaite | Rúben | £5.5m | £5.5m | £0.0m | 0.29 |
| Egan | Thomas | £4.1m | £4.0m | £0.1m | 0.23 |
| Egan | Giles | £4.1m | £4.0m | £0.1m | 0.08 |
| Furlong | Davies | £3.9m | £3.9m | £0.0m | 0.00 |
| Furlong | O'Nien | £3.9m | £3.9m | £0.0m | 0.00 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
