# FPL predictions: 2026-2027, GW11

Last generated: 2026-11-08 06:33 UTC

Data commit: `e4c78337daa27e67b7bd8ab0c4a7e0547e2ab491`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW10: 5/10 fixtures finished. Completed clubs contribute current-season form; AVL, BHA, BOU, BRE, CHE, CRY, IPS, LIV, MUN, SUN are deferred.

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
| Konsa | ARS | Defender | GW6: 4, GW7: 9, GW8: 14, GW9: 10, GW10: 8 | 45 | 9.00 | 5 |
| Gabriel | ARS | Defender | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | 41 | 8.20 | 5 |
| Barry | EVE | Forward | GW6: 6, GW7: 2, GW8: 2, GW9: 9, GW10: 16 | 35 | 7.00 | 5 |
| Evanilson | BOU | Forward | GW6: 7, GW7: 12, GW8: 6, GW9: 9 | 34 | 8.50 | 4 |
| Van Hecke | TOT | Defender | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | 33 | 6.60 | 5 |
| N.Jackson | AVL | Forward | GW6: 9, GW7: 2, GW8: 13, GW9: 9 | 33 | 8.25 | 4 |
| Haaland | MCI | Forward | GW6: 6, GW7: 13, GW8: 8, GW9: 2, GW10: 2 | 31 | 6.20 | 5 |
| De Cuyper | BHA | Defender | GW6: 15, GW7: 6, GW8: 1, GW9: 9 | 31 | 7.75 | 4 |
| Raya | ARS | Goalkeeper | GW6: 3, GW7: 9, GW8: 7, GW9: 5, GW10: 6 | 30 | 6.00 | 5 |
| Rice | ARS | Midfielder | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | 30 | 6.00 | 5 |
| Dewsbury-Hall | EVE | Midfielder | GW6: 13, GW7: 2, GW8: 2, GW9: 4, GW10: 9 | 30 | 6.00 | 5 |
| Muharemović | LEE | Defender | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | 29 | 5.80 | 5 |
| Calafiori | ARS | Defender | GW6: 9, GW7: 6, GW8: 1, GW9: 6, GW10: 6 | 28 | 5.60 | 5 |
| Verbruggen | BHA | Goalkeeper | GW6: 9, GW7: 6, GW8: 2, GW9: 11 | 28 | 7.00 | 4 |
| Ayari | BHA | Midfielder | GW6: 3, GW7: 13, GW8: 2, GW9: 10 | 28 | 7.00 | 4 |
| Iwobi | FUL | Midfielder | GW6: 4, GW7: 11, GW8: 3, GW9: 6, GW10: 2 | 26 | 5.20 | 5 |
| Neto | CHE | Midfielder | GW6: 5, GW7: 15, GW8: 3, GW9: 3 | 26 | 6.50 | 4 |
| Trafford | LEE | Goalkeeper | GW6: 2, GW7: 2, GW8: 10, GW9: 2, GW10: 10 | 26 | 5.20 | 5 |
| Hill | BOU | Defender | GW6: 2, GW7: 7, GW8: 11, GW9: 6 | 26 | 6.50 | 4 |
| Rudoni | COV | Midfielder | GW6: 7, GW7: 6, GW8: 2, GW9: 9, GW10: 2 | 26 | 5.20 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW11 player forecasts

| Player | Last 5 GW points | Club | Pos | GW11 | GW12 | GW13 | GW14 | GW15 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | 5.83 | 5.24 | 5.76 | 5.09 | 3.60 | 20.88 | 2.55 | high | 5-GW avg pts 4.60; mins 89; xGI 0.33; current GWs 9; fixture Elo diff -30 |
| Haaland | GW6: 6, GW7: 13, GW8: 8, GW9: 2, GW10: 2 | MCI | Forward | 5.75 | 4.13 | 5.75 | 5.21 | 5.67 | 21.11 | 1.34 | high | 5-GW avg pts 6.20; mins 88; xGI 0.60; current GWs 10; fixture Elo diff +102 |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | 5.58 | 5.23 | 5.58 | 6.26 | 6.72 | 23.16 | 2.86 | high | 5-GW avg pts 8.20; mins 90; xGI 0.20; current GWs 10; fixture Elo diff +205 |
| N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | AVL | Forward | 5.49 | 5.38 | 4.90 | 4.90 | 5.35 | 20.89 | 2.94 | high | 5-GW avg pts 7.80; mins 88; xGI 0.44; current GWs 9; fixture Elo diff +192 |
| Barcola | GW5: 3, GW6: 2, GW7: 4, GW8: 6, GW9: 1 | LIV | Midfielder | 4.89 | 4.55 | 5.25 | 4.39 | 5.02 | 19.27 | 2.38 | high | 5-GW avg pts 3.20; mins 83; xGI 0.30; current GWs 7; fixture Elo diff +94 |
| Vuskovic | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | BHA | Defender | 4.86 | 3.68 | 3.56 | 4.14 | 4.28 | 16.48 | 3.17 | high | 5-GW avg pts 6.80; mins 90; xGI 0.18; current GWs 9; fixture Elo diff +68 |
| Doku | GW6: 12, GW7: 6, GW8: 2, GW9: 2, GW10: 2 | MCI | Midfielder | 4.80 | 3.80 | 4.80 | 4.50 | 4.76 | 18.06 | 2.41 | high | 5-GW avg pts 4.80; mins 76; xGI 0.40; current GWs 10; fixture Elo diff +102 |
| Ayari | GW5: 3, GW6: 3, GW7: 13, GW8: 2, GW9: 10 | BHA | Midfielder | 4.73 | 3.89 | 3.72 | 4.15 | 4.17 | 16.62 | 3.02 | high | 5-GW avg pts 6.20; mins 84; xGI 0.32; current GWs 9; fixture Elo diff +68 |
| Palmer | GW5: 2, GW6: 8, GW7: 2, GW8: -1, GW9: 8 | CHE | Midfielder | 4.73 | 4.67 | 4.73 | 4.38 | 3.41 | 17.82 | 1.82 | high | 5-GW avg pts 3.80; mins 87; xGI 0.37; current GWs 9; fixture Elo diff -30 |
| Isak | GW5: 8, GW6: 0, GW7: 9, GW8: 9, GW9: 2 | LIV | Forward | 4.69 | 4.34 | 5.08 | 4.37 | 4.68 | 18.53 | 2.01 | high | 5-GW avg pts 5.60; mins 65; xGI 0.35; current GWs 9; fixture Elo diff +94 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | 4.69 | 3.90 | 3.20 | 3.51 | 4.42 | 15.87 | 2.03 | high | 5-GW avg pts 5.40; mins 90; xGI 0.56; current GWs 9; fixture Elo diff -77 |
| Richards | GW5: 8, GW6: 4, GW7: 2, GW8: 3, GW9: 3 | CRY | Defender | 4.64 | 4.45 | 3.11 | 2.67 | 2.92 | 14.76 | 3.01 | high | 5-GW avg pts 4.00; mins 90; xGI 0.03; current GWs 9; fixture Elo diff +31 |
| Verbruggen | GW5: 6, GW6: 9, GW7: 6, GW8: 2, GW9: 11 | BHA | Goalkeeper | 4.55 | 3.32 | 3.25 | 3.58 | 3.71 | 14.87 | 3.23 | high | 5-GW avg pts 6.80; mins 90; xGI 0.00; current GWs 9; fixture Elo diff +68 |
| Tonali | GW6: 7, GW7: 4, GW8: 5, GW9: 3, GW10: 1 | TOT | Midfielder | 4.55 | 4.01 | 3.81 | 2.51 | 4.48 | 15.66 | 2.95 | high | 5-GW avg pts 4.00; mins 90; xGI 0.18; current GWs 10; fixture Elo diff +20 |
| De Cuyper | GW5: 6, GW6: 15, GW7: 6, GW8: 1, GW9: 9 | BHA | Defender | 4.54 | 3.35 | 3.16 | 3.52 | 3.66 | 14.75 | 2.73 | high | 5-GW avg pts 7.40; mins 82; xGI 0.24; current GWs 9; fixture Elo diff +68 |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | 4.43 | 4.39 | 3.89 | 2.47 | 4.64 | 16.00 | 3.20 | high | 5-GW avg pts 6.60; mins 90; xGI 0.26; current GWs 10; fixture Elo diff +20 |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | MCI | Midfielder | 4.43 | 3.47 | 4.43 | 4.21 | 4.43 | 16.69 | 2.11 | high | 5-GW avg pts 4.00; mins 52; xGI 0.30; current GWs 10; fixture Elo diff +102 |
| Gomez | GW5: 8, GW6: 5, GW7: 8, GW8: 2, GW9: 3 | BHA | Midfielder | 4.41 | 3.56 | 3.45 | 3.79 | 3.90 | 15.37 | 3.07 | high | 5-GW avg pts 5.20; mins 87; xGI 0.15; current GWs 9; fixture Elo diff +68 |
| Groß | GW5: 14, GW6: 6, GW7: 5, GW8: 0, GW9: 2 | BHA | Midfielder | 4.38 | 3.84 | 3.61 | 3.89 | 4.03 | 15.86 | 2.52 | high | 5-GW avg pts 5.40; mins 86; xGI 0.29; current GWs 9; fixture Elo diff +68 |
| Ndiaye | GW6: 1, GW7: 5, GW8: 5, GW9: 2, GW10: 2 | MCI | Midfielder | 4.33 | 3.05 | 4.33 | 3.95 | 4.10 | 15.76 | 2.72 | high | 5-GW avg pts 3.00; mins 76; xGI 0.38; current GWs 10; fixture Elo diff +102 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.3m**. Current squad selling value: **£98.7m**. Total available funds: **£99.0m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.4m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | £8.1m | 23.16 | GW11, GW12, GW13, GW14, GW15 | GW14, GW15 | GW11, GW13 |
| Virgil | GW5: 8, GW6: 0, GW7: 4, GW8: 9, GW9: 1 | LIV | Defender | £6.4m | 17.59 | GW12, GW13, GW15 | — | — |
| Vuskovic | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | BHA | Defender | £5.2m | 16.48 | GW11, GW14, GW15 | — | — |
| Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | LEE | Defender | £5.1m | 16.23 | GW12, GW14 | — | GW12, GW14 |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | £5.0m | 16.00 | GW11, GW12, GW13, GW15 | — | — |
| N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | AVL | Forward | £7.1m | 20.89 | GW11, GW12, GW13, GW14, GW15 | GW12 | GW15 |
| Isak | GW5: 8, GW6: 0, GW7: 9, GW8: 9, GW9: 2 | LIV | Forward | £9.2m | 18.53 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Calvert-Lewin | GW6: 2, GW7: 9, GW8: 2, GW9: 2, GW10: 2 | LEE | Forward | £6.0m | 16.55 | GW12, GW14 | — | — |
| Suzuki | GW5: 2, GW6: 2, GW7: 8, GW8: 4, GW9: 1 | AVL | Goalkeeper | £5.0m | 15.63 | GW11, GW13, GW15 | — | — |
| Trafford | GW6: 2, GW7: 2, GW8: 10, GW9: 2, GW10: 10 | LEE | Goalkeeper | £5.0m | 13.16 | GW12, GW14 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | £8.2m | 20.88 | GW11, GW12, GW13, GW14 | GW11, GW13 | — |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 19.34 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Barcola | GW5: 3, GW6: 2, GW7: 4, GW8: 6, GW9: 1 | LIV | Midfielder | £8.1m | 19.27 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Doku | GW6: 12, GW7: 6, GW8: 2, GW9: 2, GW10: 2 | MCI | Midfielder | £7.5m | 18.06 | GW11, GW13, GW14, GW15 | — | — |
| Tonali | GW6: 7, GW7: 4, GW8: 5, GW9: 3, GW10: 1 | TOT | Midfielder | £5.3m | 15.66 | GW11, GW13, GW15 | — | — |

Squad cost: £99.0m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | £8.1m | 23.16 | GW11, GW12, GW13, GW14, GW15 | GW14, GW15 | GW11, GW12, GW13 |
| Bassey | GW6: 2, GW7: 8, GW8: 8, GW9: 1, GW10: 2 | FUL | Defender | £4.5m | 12.81 | GW12, GW13, GW14, GW15 | — | — |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | EVE | Defender | £5.5m | 11.93 | GW11, GW12, GW14, GW15 | — | — |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | HUL | Defender | £4.1m | 11.20 | GW11, GW13 | — | — |
| Furlong | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | IPS | Defender | £3.9m | 0.66 | Bench | — | — |
| Isak | GW5: 8, GW6: 0, GW7: 9, GW8: 9, GW9: 2 | LIV | Forward | £9.2m | 18.53 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | £7.8m | 15.87 | GW11, GW12, GW14, GW15 | — | — |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | ARS | Forward | £7.4m | 13.96 | GW12, GW13, GW15 | — | — |
| Horníček | GW6: 0, GW7: 2, GW8: 8, GW9: 3, GW10: 3 | NEW | Goalkeeper | £5.0m | 12.47 | GW11, GW12, GW14, GW15 | — | — |
| Leno | GW6: 2, GW7: 6, GW8: 8, GW9: 2, GW10: 3 | FUL | Goalkeeper | £4.5m | 11.83 | GW13 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | £8.2m | 20.88 | GW11, GW12, GW13, GW14 | GW11, GW12, GW13 | GW14 |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 19.34 | GW11, GW12, GW13, GW14, GW15 | — | GW15 |
| Mbeumo | GW5: 2, GW6: 8, GW7: 8, GW8: 2, GW9: 1 | MUN | Midfielder | £7.9m | 16.81 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | MCI | Midfielder | £7.9m | 16.69 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | ARS | Midfielder | £7.5m | 13.83 | GW11, GW13, GW14, GW15 | — | — |

Squad cost: £99.3m.

## One-transfer recommendation

**Havertz → N.Jackson** (projected weighted XI+captain gain 6.68).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | £7.4m | £7.1m | £0.6m | 6.68 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | £7.8m | £7.1m | £1.0m | 5.12 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Vuskovic | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | £5.5m | £5.2m | £0.6m | 4.38 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Murillo | GW6: 2, GW7: 2, GW8: 1, GW9: 3, GW10: 4 | £5.5m | £5.5m | £0.3m | 4.24 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | £5.5m | £5.1m | £0.7m | 4.16 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | £5.5m | £5.0m | £0.8m | 3.99 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | £5.5m | £5.6m | £0.2m | 3.98 |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | Doku | GW6: 12, GW7: 6, GW8: 2, GW9: 2, GW10: 2 | £7.4m | £7.5m | £0.2m | 3.89 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | £5.5m | £5.1m | £0.7m | 3.79 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Rúben | GW6: 6, GW7: 1, GW8: 1, GW9: 2, GW10: 1 | £5.5m | £5.5m | £0.3m | 3.18 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
