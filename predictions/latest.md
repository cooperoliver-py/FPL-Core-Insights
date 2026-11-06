# FPL predictions: 2026-2027, GW11

Last generated: 2026-11-06 21:43 UTC

Data commit: `258e5c244ac52ffb7685a2892ffbf2e39cce7a35`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW10: 0/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, BHA, BOU, BRE, CHE, COV, CRY, EVE, FUL, HUL, IPS, LEE, LIV, MCI, MUN, NEW, NFO, SUN, TOT are deferred.

Incomplete Gameweeks are not scored in live performance reporting until the official data is finished and checked.

The model learns from 2025/26 and completed, checked current-season Gameweeks. An equal-weight blend balances the original features with recent participation, longer-window per-90 rates, set-piece roles and observed workload across league, cup, European and friendly matches. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; prices remain fixed. Dated suspensions expire and later injury-return forecasts use a conservative historical recovery rate.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.851 | 1.847 | 0.753 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.018 and Spearman is 0.370.

The predicted top 20 averaged 4.99 actual points versus 1.69 for the selectable pool.

## Live-season performance

| GW | MAE | RMSE | Spearman | Top 20 | Pool | XI + captain | FPL avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.528 | 2.580 | 0.553 | 3.40 | 1.88 | 39 | 50 |
| 2 | 1.211 | 2.131 | 0.697 | 6.60 | 1.74 | 112 | 81 |
| 3 | 1.211 | 2.030 | 0.750 | 4.25 | 1.83 | 44 | 51 |
| 4 | 1.278 | 2.257 | 0.711 | 5.40 | 1.91 | 72 | 69 |
| 5 | 1.240 | 2.245 | 0.746 | 5.15 | 2.02 | 47 | 48 |
| 6 | 1.120 | 2.092 | 0.724 | 4.70 | 1.85 | 55 | 58 |
| 7 | 1.190 | 2.075 | 0.708 | 4.40 | 1.80 | 81 | 59 |
| 8 | 1.198 | 2.107 | 0.720 | 4.40 | 1.89 | 71 | 45 |
| 9 | 1.100 | 1.908 | 0.760 | 5.25 | 1.78 | 62 | 47 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top 20 players over the last 5 Gameweeks

Ranked by recorded FPL points in GW6–GW10. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Konsa | ARS | Defender | GW6: 4, GW7: 9, GW8: 14, GW9: 10 | 37 | 9.25 | 4 |
| Evanilson | BOU | Forward | GW6: 7, GW7: 12, GW8: 6, GW9: 9 | 34 | 8.50 | 4 |
| Gabriel | ARS | Defender | GW6: 2, GW7: 8, GW8: 17, GW9: 6 | 33 | 8.25 | 4 |
| N.Jackson | AVL | Forward | GW6: 9, GW7: 2, GW8: 13, GW9: 9 | 33 | 8.25 | 4 |
| De Cuyper | BHA | Defender | GW6: 15, GW7: 6, GW8: 1, GW9: 9 | 31 | 7.75 | 4 |
| Haaland | MCI | Forward | GW6: 6, GW7: 13, GW8: 8, GW9: 2 | 29 | 7.25 | 4 |
| Van Hecke | TOT | Defender | GW6: 3, GW7: 4, GW8: 7, GW9: 15 | 29 | 7.25 | 4 |
| Verbruggen | BHA | Goalkeeper | GW6: 9, GW7: 6, GW8: 2, GW9: 11 | 28 | 7.00 | 4 |
| Ayari | BHA | Midfielder | GW6: 3, GW7: 13, GW8: 2, GW9: 10 | 28 | 7.00 | 4 |
| Rice | ARS | Midfielder | GW6: 7, GW7: 9, GW8: 3, GW9: 8 | 27 | 6.75 | 4 |
| Neto | CHE | Midfielder | GW6: 5, GW7: 15, GW8: 3, GW9: 3 | 26 | 6.50 | 4 |
| Hill | BOU | Defender | GW6: 2, GW7: 7, GW8: 11, GW9: 6 | 26 | 6.50 | 4 |
| Vuskovic | BHA | Defender | GW6: 8, GW7: 11, GW8: 1, GW9: 6 | 26 | 6.50 | 4 |
| Iwobi | FUL | Midfielder | GW6: 4, GW7: 11, GW8: 3, GW9: 6 | 24 | 6.00 | 4 |
| Raya | ARS | Goalkeeper | GW6: 3, GW7: 9, GW8: 7, GW9: 5 | 24 | 6.00 | 4 |
| Tavernier | BOU | Midfielder | GW6: 1, GW7: 10, GW8: 10, GW9: 3 | 24 | 6.00 | 4 |
| Rudoni | COV | Midfielder | GW6: 7, GW7: 6, GW8: 2, GW9: 9 | 24 | 6.00 | 4 |
| Silva | BOU | Defender | GW6: 0, GW7: 8, GW8: 8, GW9: 8 | 24 | 6.00 | 4 |
| Manzambi | AVL | Midfielder | GW6: 5, GW7: 11, GW8: 1, GW9: 7 | 24 | 6.00 | 4 |
| Henderson | CHE | Midfielder | GW6: 18, GW7: 3, GW8: 2, GW9: 0 | 23 | 5.75 | 4 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW11 player forecasts

| Player | Last 5 GW points | Club | Pos | GW11 | GW12 | GW13 | GW14 | GW15 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW5: 1, GW6: 2, GW7: 8, GW8: 17, GW9: 6 | ARS | Defender | 6.16 | 5.82 | 6.16 | 6.84 | 7.30 | 25.50 | 3.19 | high | 5-GW avg pts 6.80; mins 90; xGI 0.23; current GWs 9; fixture Elo diff +205 |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | 5.85 | 5.25 | 5.82 | 5.10 | 3.68 | 21.02 | 2.56 | high | 5-GW avg pts 4.60; mins 89; xGI 0.33; current GWs 9; fixture Elo diff -30 |
| N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | AVL | Forward | 5.38 | 5.31 | 4.78 | 4.78 | 5.28 | 20.50 | 2.93 | high | 5-GW avg pts 7.80; mins 88; xGI 0.44; current GWs 9; fixture Elo diff +192 |
| Ayari | GW5: 3, GW6: 3, GW7: 13, GW8: 2, GW9: 10 | BHA | Midfielder | 5.06 | 4.04 | 3.91 | 4.36 | 4.46 | 17.55 | 3.25 | high | 5-GW avg pts 6.20; mins 84; xGI 0.32; current GWs 9; fixture Elo diff +68 |
| Barcola | GW5: 3, GW6: 2, GW7: 4, GW8: 6, GW9: 1 | LIV | Midfielder | 4.89 | 4.55 | 5.25 | 4.39 | 5.02 | 19.27 | 2.38 | high | 5-GW avg pts 3.20; mins 83; xGI 0.30; current GWs 7; fixture Elo diff +94 |
| Palmer | GW5: 2, GW6: 8, GW7: 2, GW8: -1, GW9: 8 | CHE | Midfielder | 4.87 | 4.69 | 4.87 | 4.42 | 3.43 | 18.14 | 1.85 | high | 5-GW avg pts 3.80; mins 87; xGI 0.37; current GWs 9; fixture Elo diff -30 |
| Vuskovic | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | BHA | Defender | 4.86 | 3.66 | 3.57 | 4.15 | 4.26 | 16.47 | 3.17 | high | 5-GW avg pts 6.80; mins 90; xGI 0.18; current GWs 9; fixture Elo diff +68 |
| Tonali | GW5: 2, GW6: 7, GW7: 4, GW8: 5, GW9: 3 | TOT | Midfielder | 4.86 | 4.02 | 4.06 | 2.61 | 4.58 | 16.31 | 3.08 | high | 5-GW avg pts 4.20; mins 89; xGI 0.23; current GWs 9; fixture Elo diff +20 |
| Haaland | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | MCI | Forward | 4.85 | 3.97 | 4.85 | 4.64 | 4.71 | 18.38 | 1.16 | high | 5-GW avg pts 7.00; mins 88; xGI 0.71; current GWs 9; fixture Elo diff +102 |
| Van Hecke | GW5: 6, GW6: 3, GW7: 4, GW8: 7, GW9: 15 | TOT | Defender | 4.84 | 4.47 | 4.18 | 2.67 | 4.56 | 16.82 | 3.36 | high | 5-GW avg pts 7.00; mins 90; xGI 0.37; current GWs 9; fixture Elo diff +20 |
| Richards | GW5: 8, GW6: 4, GW7: 2, GW8: 3, GW9: 3 | CRY | Defender | 4.75 | 4.63 | 3.27 | 2.79 | 3.04 | 15.31 | 3.12 | high | 5-GW avg pts 4.00; mins 90; xGI 0.03; current GWs 9; fixture Elo diff +31 |
| Isak | GW5: 8, GW6: 0, GW7: 9, GW8: 9, GW9: 2 | LIV | Forward | 4.72 | 4.37 | 5.11 | 4.40 | 4.70 | 18.63 | 2.03 | high | 5-GW avg pts 5.60; mins 65; xGI 0.35; current GWs 9; fixture Elo diff +94 |
| Kudus | GW5: 4, GW6: 3, GW7: 6, GW8: 3, GW9: 7 | TOT | Midfielder | 4.68 | 4.00 | 4.41 | 3.16 | 4.27 | 16.57 | 2.51 | high | 5-GW avg pts 4.60; mins 75; xGI 0.36; current GWs 9; fixture Elo diff +20 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | 4.60 | 3.86 | 3.14 | 3.44 | 4.38 | 15.62 | 2.00 | high | 5-GW avg pts 5.40; mins 90; xGI 0.56; current GWs 9; fixture Elo diff -77 |
| Verbruggen | GW5: 6, GW6: 9, GW7: 6, GW8: 2, GW9: 11 | BHA | Goalkeeper | 4.59 | 3.32 | 3.28 | 3.62 | 3.71 | 14.96 | 3.25 | high | 5-GW avg pts 6.80; mins 90; xGI 0.00; current GWs 9; fixture Elo diff +68 |
| Doku | GW5: 1, GW6: 12, GW7: 6, GW8: 2, GW9: 2 | MCI | Midfielder | 4.56 | 3.72 | 4.56 | 4.26 | 4.53 | 17.26 | 2.30 | high | 5-GW avg pts 4.60; mins 61; xGI 0.47; current GWs 9; fixture Elo diff +102 |
| Konsa | GW5: 1, GW6: 4, GW7: 9, GW8: 14, GW9: 10 | ARS | Defender | 4.54 | 4.00 | 4.54 | 5.24 | 4.84 | 18.33 | 3.82 | high | 5-GW avg pts 7.60; mins 90; xGI 0.13; current GWs 9; fixture Elo diff +205 |
| Gomez | GW5: 8, GW6: 5, GW7: 8, GW8: 2, GW9: 3 | BHA | Midfielder | 4.50 | 3.64 | 3.55 | 3.89 | 3.98 | 15.73 | 3.15 | high | 5-GW avg pts 5.20; mins 87; xGI 0.15; current GWs 9; fixture Elo diff +68 |
| De Cuyper | GW5: 6, GW6: 15, GW7: 6, GW8: 1, GW9: 9 | BHA | Defender | 4.48 | 3.37 | 3.21 | 3.57 | 3.68 | 14.79 | 2.74 | high | 5-GW avg pts 7.40; mins 82; xGI 0.24; current GWs 9; fixture Elo diff +68 |
| Groß | GW5: 14, GW6: 6, GW7: 5, GW8: 0, GW9: 2 | BHA | Midfielder | 4.48 | 3.85 | 3.66 | 3.94 | 4.04 | 16.04 | 2.59 | high | 5-GW avg pts 5.40; mins 86; xGI 0.29; current GWs 9; fixture Elo diff +68 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.3m**. Current squad selling value: **£98.7m**. Total available funds: **£99.0m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW5: 1, GW6: 2, GW7: 8, GW8: 17, GW9: 6 | ARS | Defender | £8.0m | 25.50 | GW11, GW12, GW13, GW14, GW15 | GW11, GW12, GW13, GW14, GW15 | — |
| Konsa | GW5: 1, GW6: 4, GW7: 9, GW8: 14, GW9: 10 | ARS | Defender | £4.8m | 18.33 | GW11, GW13, GW14, GW15 | — | GW14 |
| Virgil | GW5: 8, GW6: 0, GW7: 4, GW8: 9, GW9: 1 | LIV | Defender | £6.4m | 17.61 | GW12, GW13, GW15 | — | — |
| Van Hecke | GW5: 6, GW6: 3, GW7: 4, GW8: 7, GW9: 15 | TOT | Defender | £5.0m | 16.82 | GW11, GW12, GW13, GW15 | — | — |
| Muharemović | GW5: 6, GW6: 2, GW7: 5, GW8: 9, GW9: 3 | LEE | Defender | £5.1m | 15.63 | GW12, GW14 | — | — |
| N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | AVL | Forward | £7.0m | 20.50 | GW11, GW12, GW13, GW14, GW15 | — | GW12, GW15 |
| Isak | GW5: 8, GW6: 0, GW7: 9, GW8: 9, GW9: 2 | LIV | Forward | £9.2m | 18.63 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Havertz | GW5: 2, GW6: 2, GW7: 2, GW8: 1, GW9: 9 | ARS | Forward | £7.4m | 17.60 | GW12, GW13, GW14, GW15 | — | — |
| Suzuki | GW5: 2, GW6: 2, GW7: 8, GW8: 4, GW9: 1 | AVL | Goalkeeper | £5.0m | 15.81 | GW12, GW13, GW14, GW15 | — | — |
| Verbruggen | GW5: 6, GW6: 9, GW7: 6, GW8: 2, GW9: 11 | BHA | Goalkeeper | £4.6m | 14.96 | GW11 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | £8.2m | 21.02 | GW11, GW12, GW13, GW14 | — | GW11, GW13 |
| Barcola | GW5: 3, GW6: 2, GW7: 4, GW8: 6, GW9: 1 | LIV | Midfielder | £8.1m | 19.27 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Palmer | GW5: 2, GW6: 8, GW7: 2, GW8: -1, GW9: 8 | CHE | Midfielder | £9.8m | 18.14 | GW11, GW12, GW13, GW14 | — | — |
| Ayari | GW5: 3, GW6: 3, GW7: 13, GW8: 2, GW9: 10 | BHA | Midfielder | £5.4m | 17.55 | GW11, GW14, GW15 | — | — |
| Tonali | GW5: 2, GW6: 7, GW7: 4, GW8: 5, GW9: 3 | TOT | Midfielder | £5.3m | 16.31 | GW11, GW15 | — | — |

Squad cost: £99.3m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW5: 1, GW6: 2, GW7: 8, GW8: 17, GW9: 6 | ARS | Defender | £8.0m | 25.50 | GW11, GW12, GW13, GW14, GW15 | GW11, GW12, GW13, GW14, GW15 | — |
| Bassey | GW5: 6, GW6: 2, GW7: 8, GW8: 8, GW9: 1 | FUL | Defender | £4.5m | 13.57 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | EVE | Defender | £5.5m | 11.58 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Egan | GW5: 1, GW6: 1, GW7: 4, GW8: 4, GW9: 1 | HUL | Defender | £4.1m | 9.41 | Bench | — | — |
| Furlong | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | IPS | Defender | £3.9m | 0.66 | Bench | — | — |
| Isak | GW5: 8, GW6: 0, GW7: 9, GW8: 9, GW9: 2 | LIV | Forward | £9.2m | 18.63 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Havertz | GW5: 2, GW6: 2, GW7: 2, GW8: 1, GW9: 9 | ARS | Forward | £7.4m | 17.60 | GW11, GW12, GW13, GW14, GW15 | — | GW15 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | £7.8m | 15.62 | GW11, GW12, GW14, GW15 | — | — |
| Horníček | GW5: 3, GW6: 0, GW7: 2, GW8: 8, GW9: 3 | NEW | Goalkeeper | £5.0m | 12.52 | GW12, GW14, GW15 | — | — |
| Leno | GW5: 3, GW6: 2, GW7: 6, GW8: 8, GW9: 2 | FUL | Goalkeeper | £4.5m | 11.87 | GW11, GW13 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | £8.2m | 21.02 | GW11, GW12, GW13, GW14, GW15 | — | GW11, GW12, GW13, GW14 |
| Gibbs-White | GW5: 2, GW6: 2, GW7: 0, GW8: 2, GW9: 2 | NFO | Midfielder | £7.8m | 18.50 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Mbeumo | GW5: 2, GW6: 8, GW7: 8, GW8: 2, GW9: 1 | MUN | Midfielder | £7.9m | 16.95 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Rice | GW5: 1, GW6: 7, GW7: 9, GW8: 3, GW9: 8 | ARS | Midfielder | £7.4m | 16.92 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Cherki | GW5: 8, GW6: 10, GW7: 0, GW8: 0, GW9: 1 | MCI | Midfielder | £7.9m | 12.66 | GW13 | — | — |

Squad cost: £99.1m.

## One-transfer recommendation

**Branthwaite → Van Hecke** (projected weighted XI+captain gain 5.23).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Van Hecke | GW5: 6, GW6: 3, GW7: 4, GW8: 7, GW9: 15 | £5.5m | £5.0m | £0.8m | 5.23 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Vuskovic | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | £5.5m | £5.2m | £0.6m | 4.89 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | £7.8m | £7.0m | £1.1m | 4.76 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | £5.5m | £5.6m | £0.2m | 4.73 |
| Cherki | GW5: 8, GW6: 10, GW7: 0, GW8: 0, GW9: 1 | Barcola | GW5: 3, GW6: 2, GW7: 4, GW8: 6, GW9: 1 | £7.8m | £8.1m | £0.0m | 4.48 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Jacquet | GW5: 6, GW6: 3, GW7: 3, GW8: 8, GW9: 2 | £5.5m | £5.1m | £0.7m | 4.32 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Murillo | GW5: 4, GW6: 2, GW7: 2, GW8: 1, GW9: 3 | £5.5m | £5.5m | £0.3m | 4.23 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | £5.5m | £5.1m | £0.7m | 4.10 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Muharemović | GW5: 6, GW6: 2, GW7: 5, GW8: 9, GW9: 3 | £5.5m | £5.1m | £0.7m | 4.05 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Rúben | GW5: 1, GW6: 6, GW7: 1, GW8: 1, GW9: 2 | £5.5m | £5.5m | £0.3m | 3.92 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
