# FPL predictions: 2026-2027, GW8

Last generated: 2026-10-18 04:59 UTC

Data commit: `a1982cad3a446fb738e3f4236bde3a06a78f39bf`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW7: 5/10 fixtures finished. Completed clubs contribute current-season form; ARS, BHA, BOU, COV, CRY, LEE, MUN, NFO, SUN, TOT are deferred.

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
| 5 | 1.240 | 2.245 | 0.746 | 5.15 | 2.02 | 47 | 48 |
| 6 | 1.120 | 2.092 | 0.724 | 4.70 | 1.85 | 55 | 58 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW8 player forecasts

| Player | Club | Pos | GW8 | GW9 | GW10 | GW11 | GW12 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | 6.07 | 7.08 | 6.89 | 7.50 | 5.72 | 26.63 | 1.70 | high | 5-GW avg pts 8.60; mins 88; xGI 1.03; current GWs 7; fixture Elo diff +78 |
| Palmer | CHE | Midfielder | 6.04 | 5.48 | 5.92 | 6.06 | 6.01 | 23.54 | 2.43 | high | 5-GW avg pts 3.60; mins 89; xGI 0.22; current GWs 7; fixture Elo diff +21 |
| Iwobi | FUL | Midfielder | 5.40 | 3.64 | 4.29 | 3.64 | 4.12 | 17.14 | 3.17 | high | 5-GW avg pts 5.00; mins 81; xGI 0.51; current GWs 7; fixture Elo diff -39 |
| Isak | LIV | Forward | 5.30 | 4.49 | 5.07 | 5.23 | 5.13 | 20.14 | 2.24 | high | 5-GW avg pts 6.40; mins 62; xGI 0.38; current GWs 7; fixture Elo diff +25 |
| Thiago | BRE | Forward | 5.24 | 5.39 | 5.09 | 5.30 | 4.62 | 20.65 | 2.65 | high | 5-GW avg pts 3.20; mins 90; xGI 0.46; current GWs 7; fixture Elo diff +53 |
| João Pedro | CHE | Forward | 5.04 | 4.55 | 4.64 | 5.04 | 4.75 | 19.24 | 2.47 | high | 5-GW avg pts 5.40; mins 68; xGI 0.28; current GWs 7; fixture Elo diff +21 |
| B.Fernandes | MUN | Midfielder | 5.04 | 4.68 | 4.88 | 4.70 | 4.99 | 19.43 | 1.65 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +41 |
| Gabriel | ARS | Defender | 5.03 | 4.56 | 5.64 | 4.74 | 3.88 | 19.28 | 2.44 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +253 |
| Calvert-Lewin | LEE | Forward | 5.00 | 3.73 | 4.24 | 3.89 | 4.89 | 17.41 | 2.90 | high | 5-GW avg pts 4.60; mins 84; xGI 0.59; current GWs 6; fixture Elo diff +22 |
| McAtee | NFO | Midfielder | 4.89 | 3.58 | 3.10 | 3.14 | 3.43 | 14.85 | 2.70 | high | 5-GW avg pts 2.60; mins 87; xGI 0.25; current GWs 6; fixture Elo diff -8 |
| Mbeumo | MUN | Midfielder | 4.88 | 4.30 | 4.72 | 4.52 | 4.65 | 18.48 | 2.37 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +41 |
| Rogers | CHE | Midfielder | 4.86 | 4.30 | 4.85 | 4.93 | 4.82 | 18.95 | 2.40 | high | 5-GW avg pts 5.40; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +21 |
| Ajer | BRE | Defender | 4.79 | 3.77 | 3.51 | 3.85 | 3.28 | 15.65 | 3.48 | high | 5-GW avg pts 3.80; mins 90; xGI 0.09; current GWs 7; fixture Elo diff +53 |
| Bassey | FUL | Defender | 4.70 | 2.86 | 3.47 | 2.64 | 3.36 | 13.91 | 3.09 | high | 5-GW avg pts 4.60; mins 90; xGI 0.07; current GWs 7; fixture Elo diff -39 |
| Rice | ARS | Midfielder | 4.66 | 4.13 | 4.86 | 4.20 | 3.90 | 17.55 | 2.40 | high | 5-GW avg pts 4.80; mins 87; xGI 0.15; current GWs 6; fixture Elo diff +253 |
| N.Williams | NFO | Defender | 4.60 | 3.30 | 2.72 | 3.26 | 3.39 | 14.07 | 2.81 | high | 5-GW avg pts 3.60; mins 90; xGI 0.29; current GWs 6; fixture Elo diff -8 |
| Wirtz | LIV | Midfielder | 4.60 | 3.80 | 4.32 | 4.53 | 4.35 | 17.26 | 2.40 | high | 5-GW avg pts 3.80; mins 81; xGI 0.24; current GWs 7; fixture Elo diff +25 |
| Cunha | MUN | Midfielder | 4.60 | 4.41 | 4.43 | 4.28 | 4.58 | 17.85 | 2.26 | high | 5-GW avg pts 6.80; mins 84; xGI 0.26; current GWs 6; fixture Elo diff +41 |
| Muharemović | LEE | Defender | 4.56 | 3.68 | 4.58 | 3.77 | 5.19 | 17.30 | 3.46 | high | 5-GW avg pts 4.60; mins 90; xGI 0.09; current GWs 6; fixture Elo diff +22 |
| Stach | LEE | Midfielder | 4.53 | 3.67 | 4.47 | 3.82 | 4.54 | 16.80 | 2.80 | high | 5-GW avg pts 3.20; mins 89; xGI 0.25; current GWs 6; fixture Elo diff +22 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£99.0m**. Total available funds: **£99.2m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 19.61 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Rúben | MCI | Defender | £5.5m | 18.41 | GW8, GW9, GW10, GW11 | — | — |
| Muharemović | LEE | Defender | £5.0m | 17.30 | GW8, GW10, GW12 | — | — |
| Richards | CRY | Defender | £4.9m | 16.24 | GW8, GW9, GW11, GW12 | — | — |
| Davis | IPS | Defender | £4.0m | 14.76 | GW9 | — | — |
| Haaland | MCI | Forward | £15.7m | 26.63 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW10, GW11 | GW12 |
| Thiago | BRE | Forward | £7.8m | 20.65 | GW8, GW9, GW10, GW11, GW12 | — | — |
| João Pedro | CHE | Forward | £7.8m | 19.24 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Donnarumma | MCI | Goalkeeper | £5.5m | 16.20 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Balcombe | BRE | Goalkeeper | £4.0m | 0.28 | Bench | — | — |
| Palmer | CHE | Midfielder | £9.7m | 23.54 | GW8, GW9, GW10, GW11, GW12 | GW12 | GW8, GW9, GW10, GW11 |
| Rogers | CHE | Midfielder | £7.9m | 18.95 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Groß | BHA | Midfielder | £6.1m | 17.46 | GW10, GW11, GW12 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 17.14 | GW8, GW10 | — | — |
| Timber | CRY | Midfielder | £5.0m | 15.81 | GW9, GW11, GW12 | — | — |

Squad cost: £99.3m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.28 | GW8, GW9, GW10, GW11, GW12 | GW10 | — |
| Branthwaite | EVE | Defender | £5.5m | 15.87 | GW8, GW9, GW10, GW11, GW12 | — | GW10 |
| Bassey | FUL | Defender | £4.5m | 13.91 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Egan | HUL | Defender | £4.1m | 12.56 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.77 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 20.65 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW11 | — |
| Havertz | ARS | Forward | £7.5m | 15.99 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.31 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.50 | GW8, GW10, GW11, GW12 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.36 | GW9 | — | — |
| B.Fernandes | MUN | Midfielder | £11.8m | 19.43 | GW8, GW9, GW10, GW11, GW12 | GW12 | GW8, GW9 |
| Rogers | CHE | Midfielder | £7.9m | 18.95 | GW8, GW9, GW10, GW11, GW12 | — | GW11, GW12 |
| Cherki | MCI | Midfielder | £8.0m | 13.21 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 12.91 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Semenyo | MCI | Midfielder | £8.3m | 6.00 | Bench | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Semenyo → Mbeumo** (projected weighted XI+captain gain 7.30).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Semenyo | Mbeumo | £8.3m | £7.8m | £0.7m | 7.30 |
| Semenyo | Cunha | £8.3m | £7.9m | £0.6m | 6.68 |
| Semenyo | Groß | £8.3m | £6.1m | £2.4m | 6.60 |
| Semenyo | Rice | £8.3m | £7.3m | £1.2m | 6.38 |
| B.Fernandes | Palmer | £11.8m | £9.7m | £2.3m | 6.34 |
| Semenyo | Iwobi | £8.3m | £5.4m | £3.1m | 6.13 |
| Semenyo | Wirtz | £8.3m | £7.2m | £1.3m | 6.08 |
| Semenyo | Stach | £8.3m | £6.0m | £2.5m | 5.63 |
| Gibbs-White | Mbeumo | £8.0m | £7.8m | £0.4m | 5.57 |
| Semenyo | Barcola | £8.3m | £8.0m | £0.5m | 5.34 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
