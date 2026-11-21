# FPL predictions: 2026-2027, GW12

Last generated: 2026-11-21 16:20 UTC

Data commit: `46543c39638e0530fc7ef3b3b6c26529df321a52`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW11: 1/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, BHA, BOU, BRE, CHE, COV, CRY, EVE, HUL, IPS, LEE, LIV, MUN, NEW, NFO, SUN, TOT are deferred.

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
| 10 | 1.148 | 2.067 | 0.759 | 4.80 | 1.83 | 70 | 55 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top 20 players over the last 5 Gameweeks

Ranked by recorded FPL points in GW7–GW11. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Konsa | ARS | Defender | GW7: 9, GW8: 14, GW9: 10, GW10: 8 | 41 | 10.25 | 4 |
| Gabriel | ARS | Defender | GW7: 8, GW8: 17, GW9: 6, GW10: 8 | 39 | 9.75 | 4 |
| Evanilson | BOU | Forward | GW7: 12, GW8: 6, GW9: 9, GW10: 9 | 36 | 9.00 | 4 |
| N.Jackson | AVL | Forward | GW7: 2, GW8: 13, GW9: 9, GW10: 11 | 35 | 8.75 | 4 |
| Van Hecke | TOT | Defender | GW7: 4, GW8: 7, GW9: 15, GW10: 4 | 30 | 7.50 | 4 |
| Vuskovic | BHA | Defender | GW7: 11, GW8: 1, GW9: 6, GW10: 12 | 30 | 7.50 | 4 |
| Barry | EVE | Forward | GW7: 2, GW8: 2, GW9: 9, GW10: 16 | 29 | 7.25 | 4 |
| Isak | LIV | Forward | GW7: 9, GW8: 9, GW9: 2, GW10: 8 | 28 | 7.00 | 4 |
| Hill | BOU | Defender | GW7: 7, GW8: 11, GW9: 6, GW10: 4 | 28 | 7.00 | 4 |
| Ayari | BHA | Midfielder | GW7: 13, GW8: 2, GW9: 10, GW10: 3 | 28 | 7.00 | 4 |
| Raya | ARS | Goalkeeper | GW7: 9, GW8: 7, GW9: 5, GW10: 6 | 27 | 6.75 | 4 |
| Haaland | MCI | Forward | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | 27 | 5.40 | 5 |
| Silva | BOU | Defender | GW7: 8, GW8: 8, GW9: 8, GW10: 3 | 27 | 6.75 | 4 |
| Muharemović | LEE | Defender | GW7: 5, GW8: 9, GW9: 3, GW10: 10 | 27 | 6.75 | 4 |
| Tavernier | BOU | Midfielder | GW7: 10, GW8: 10, GW9: 3, GW10: 3 | 26 | 6.50 | 4 |
| E.Le Fée | SUN | Midfielder | GW7: 4, GW8: 3, GW9: 8, GW10: 11 | 26 | 6.50 | 4 |
| Wirtz | LIV | Midfielder | GW7: 5, GW8: 6, GW9: 2, GW10: 13 | 26 | 6.50 | 4 |
| Bobb | FUL | Midfielder | GW7: 3, GW8: 11, GW9: 2, GW10: 3, GW11: 6 | 25 | 5.00 | 5 |
| Verbruggen | BHA | Goalkeeper | GW7: 6, GW8: 2, GW9: 11, GW10: 6 | 25 | 6.25 | 4 |
| Castagne | FUL | Defender | GW7: 8, GW8: 7, GW9: 2, GW10: 7, GW11: 0 | 24 | 4.80 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW12 player forecasts

| Player | Last 5 GW points | Club | Pos | GW12 | GW13 | GW14 | GW15 | GW16 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | 6.01 | 4.28 | 4.28 | 5.94 | 4.16 | 19.94 | 2.77 | high | 5-GW avg pts 8.80; mins 87; xGI 0.62; current GWs 10; fixture Elo diff +173 |
| Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | LEE | Defender | 5.83 | 2.96 | 5.55 | 3.06 | 4.04 | 17.50 | 3.43 | high | 5-GW avg pts 5.80; mins 90; xGI 0.07; current GWs 10; fixture Elo diff -2 |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | 5.30 | 5.47 | 6.60 | 5.70 | 3.63 | 21.67 | 1.87 | high | 5-GW avg pts 2.80; mins 72; xGI 0.45; current GWs 10; fixture Elo diff +75 |
| Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | BOU | Forward | 5.24 | 4.98 | 6.78 | 3.54 | 6.83 | 21.72 | 3.34 | high | 5-GW avg pts 8.60; mins 83; xGI 0.82; current GWs 10; fixture Elo diff +89 |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | 5.12 | 5.26 | 4.68 | 3.44 | 4.69 | 18.82 | 2.29 | high | 5-GW avg pts 4.60; mins 89; xGI 0.32; current GWs 10; fixture Elo diff -55 |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | 5.10 | 6.35 | 5.15 | 5.24 | 5.43 | 21.86 | 2.80 | high | 5-GW avg pts 2.20; mins 72; xGI 0.38; current GWs 10; fixture Elo diff +73 |
| Bogle | GW6: 1, GW7: 2, GW8: 5, GW9: 1, GW10: 7 | LEE | Defender | 5.08 | 3.17 | 4.92 | 2.84 | 4.14 | 16.33 | 3.40 | high | 5-GW avg pts 3.20; mins 89; xGI 0.22; current GWs 10; fixture Elo diff -2 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | 4.97 | 4.77 | 4.99 | 5.22 | 6.87 | 21.03 | 3.34 | high | 5-GW avg pts 4.60; mins 86; xGI 0.52; current GWs 10; fixture Elo diff +47 |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | 4.92 | 5.46 | 4.57 | 5.14 | 5.26 | 20.24 | 2.50 | high | 5-GW avg pts 3.60; mins 82; xGI 0.39; current GWs 8; fixture Elo diff +122 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | 4.89 | 4.52 | 5.58 | 4.79 | 2.61 | 18.34 | 2.35 | high | 5-GW avg pts 4.20; mins 88; xGI 0.41; current GWs 10; fixture Elo diff +75 |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | 4.83 | 5.39 | 4.56 | 4.91 | 5.05 | 19.80 | 2.13 | high | 5-GW avg pts 5.60; mins 67; xGI 0.31; current GWs 10; fixture Elo diff +122 |
| Calvert-Lewin | GW6: 2, GW7: 9, GW8: 2, GW9: 2, GW10: 2 | LEE | Forward | 4.73 | 2.74 | 4.56 | 2.87 | 3.99 | 15.25 | 2.54 | high | 5-GW avg pts 3.40; mins 89; xGI 0.31; current GWs 10; fixture Elo diff -2 |
| Wirtz | GW6: 2, GW7: 5, GW8: 6, GW9: 2, GW10: 13 | LIV | Midfielder | 4.57 | 4.71 | 4.37 | 4.24 | 4.48 | 17.97 | 2.46 | high | 5-GW avg pts 5.60; mins 78; xGI 0.33; current GWs 10; fixture Elo diff +122 |
| Justin | GW6: 6, GW7: 2, GW8: 6, GW9: 2, GW10: 9 | LEE | Defender | 4.46 | 2.62 | 4.66 | 2.72 | 3.83 | 14.74 | 3.28 | high | 5-GW avg pts 5.00; mins 86; xGI 0.20; current GWs 10; fixture Elo diff -2 |
| Cunha | GW6: 10, GW7: 1, GW8: 1, GW9: 2, GW10: 5 | MUN | Midfielder | 4.43 | 4.23 | 5.56 | 4.32 | 2.59 | 17.26 | 2.21 | high | 5-GW avg pts 3.80; mins 59; xGI 0.27; current GWs 10; fixture Elo diff +75 |
| Mitchell | GW6: 4, GW7: 0, GW8: 1, GW9: 3, GW10: 1 | CRY | Defender | 4.43 | 2.94 | 2.24 | 2.75 | 3.29 | 12.77 | 2.90 | high | 5-GW avg pts 1.80; mins 90; xGI 0.14; current GWs 10; fixture Elo diff +17 |
| Haaland | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | MCI | Forward | 4.42 | 6.54 | 5.81 | 5.92 | 6.89 | 23.23 | 1.47 | high | 5-GW avg pts 5.40; mins 87; xGI 0.72; current GWs 11; fixture Elo diff +158 |
| Palmer | GW6: 8, GW7: 2, GW8: -1, GW9: 8, GW10: 2 | CHE | Midfielder | 4.40 | 4.55 | 3.98 | 2.87 | 3.99 | 16.08 | 1.64 | high | 5-GW avg pts 3.80; mins 87; xGI 0.33; current GWs 10; fixture Elo diff -55 |
| Wharton | GW6: 7, GW7: 2, GW8: 2, GW9: 4, GW10: 2 | CRY | Midfielder | 4.39 | 3.14 | 2.49 | 2.85 | 3.38 | 13.23 | 2.50 | high | 5-GW avg pts 3.40; mins 89; xGI 0.21; current GWs 10; fixture Elo diff +17 |
| Virgil | GW6: 0, GW7: 4, GW8: 9, GW9: 1, GW10: 4 | LIV | Defender | 4.36 | 4.66 | 4.00 | 4.42 | 4.58 | 17.60 | 2.75 | high | 5-GW avg pts 3.60; mins 90; xGI 0.08; current GWs 10; fixture Elo diff +122 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.0m**. Current squad selling value: **£97.9m**. Total available funds: **£98.9m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.8m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | GW6: 0, GW7: 4, GW8: 9, GW9: 1, GW10: 4 | LIV | Defender | £6.4m | 17.60 | GW12, GW13, GW15, GW16 | — | — |
| Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | LEE | Defender | £5.1m | 17.50 | GW12, GW14 | — | GW12 |
| De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | BHA | Defender | £5.5m | 17.28 | GW13, GW14, GW15, GW16 | — | — |
| Bogle | GW6: 1, GW7: 2, GW8: 5, GW9: 1, GW10: 7 | LEE | Defender | £4.8m | 16.33 | GW12, GW14, GW16 | — | — |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | £5.1m | 15.40 | GW13, GW15 | — | — |
| Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | BOU | Forward | £6.5m | 21.72 | GW12, GW13, GW14, GW16 | GW14 | GW16 |
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | £7.2m | 19.94 | GW12, GW15, GW16 | GW12, GW15 | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 19.80 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Verbruggen | GW6: 9, GW7: 6, GW8: 2, GW9: 11, GW10: 6 | BHA | Goalkeeper | £4.7m | 14.86 | GW12, GW13, GW15, GW16 | — | — |
| Petrović | GW6: 0, GW7: 6, GW8: 7, GW9: 6, GW10: 2 | BOU | Goalkeeper | £4.5m | 13.52 | GW14 | — | — |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 21.86 | GW12, GW13, GW14, GW15, GW16 | GW13 | — |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | £11.6m | 21.67 | GW12, GW13, GW14, GW15 | — | GW13, GW14, GW15 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | £6.3m | 21.03 | GW12, GW13, GW14, GW15, GW16 | GW16 | — |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | £8.1m | 20.24 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | FUL | Midfielder | £5.4m | 19.59 | GW13, GW14, GW15, GW16 | — | — |

Squad cost: £98.3m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | £8.1m | 16.37 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | EVE | Defender | £5.5m | 12.15 | GW12, GW14, GW15, GW16 | — | — |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | FUL | Defender | £4.5m | 10.73 | GW12, GW13, GW14, GW16 | — | — |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | HUL | Defender | £4.1m | 10.48 | GW13, GW15 | — | — |
| Furlong | GW6: 0, GW7: 0, GW8: 0, GW9: 0, GW10: 0 | IPS | Defender | £3.9m | 0.56 | Bench | — | — |
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | £7.2m | 19.94 | GW12, GW13, GW14, GW15, GW16 | GW12, GW15 | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 19.80 | GW12, GW13, GW14, GW15, GW16 | — | GW13, GW16 |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | ARS | Forward | £7.4m | 12.49 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Horníček | GW6: 0, GW7: 2, GW8: 8, GW9: 3, GW10: 3 | NEW | Goalkeeper | £5.0m | 12.48 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Leno | GW7: 6, GW8: 8, GW9: 2, GW10: 3, GW11: 2 | FUL | Goalkeeper | £4.5m | 10.85 | Bench | — | — |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 21.86 | GW12, GW13, GW14, GW15, GW16 | GW13, GW16 | GW14, GW15 |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | £8.2m | 18.82 | GW12, GW13, GW14, GW15, GW16 | — | GW12 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | £7.8m | 18.34 | GW12, GW13, GW14, GW15 | GW14 | — |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | ARS | Midfielder | £7.5m | 15.12 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | MCI | Midfielder | £7.9m | 10.17 | GW16 | — | — |

Squad cost: £98.7m.

## One-transfer recommendation

**Havertz → Evanilson** (projected weighted XI+captain gain 11.03).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | £7.4m | £6.5m | £1.9m | 11.03 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.8m | £6.3m | £2.5m | 9.82 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | £7.8m | £8.1m | £0.7m | 8.17 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | £7.8m | £5.4m | £3.4m | 7.52 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | £4.5m | £5.5m | £0.0m | 7.06 |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.4m | £6.3m | £2.1m | 6.77 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | £4.5m | £5.1m | £0.4m | 6.70 |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | £4.1m | £5.1m | £0.0m | 6.62 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | £4.5m | £5.3m | £0.2m | 6.27 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Wirtz | GW6: 2, GW7: 5, GW8: 6, GW9: 2, GW10: 13 | £7.8m | £7.3m | £1.5m | 5.89 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
