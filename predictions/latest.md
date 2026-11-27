# FPL predictions: 2026-2027, GW12

Last generated: 2026-11-27 18:23 UTC

Data commit: `3b5012e8eab0fbbe9e30b4bfee50dff3827dde25`

## Data freshness

All scheduled Premier League fixtures before GW12 are complete.

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
| 11 | 1.277 | 2.327 | 0.718 | 2.90 | 1.91 | 45 | 35 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top 20 players over the last 5 Gameweeks

Ranked by recorded FPL points in GW7–GW11. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Konsa | ARS | Defender | GW7: 9, GW8: 14, GW9: 10, GW10: 8, GW11: 1 | 42 | 8.40 | 5 |
| Evanilson | BOU | Forward | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | 42 | 8.40 | 5 |
| Hill | BOU | Defender | GW7: 7, GW8: 11, GW9: 6, GW10: 4, GW11: 14 | 42 | 8.40 | 5 |
| Gabriel | ARS | Defender | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | 40 | 8.00 | 5 |
| Wirtz | LIV | Midfielder | GW7: 5, GW8: 6, GW9: 2, GW10: 13, GW11: 14 | 40 | 8.00 | 5 |
| McBurnie | HUL | Forward | GW7: 2, GW8: 8, GW9: 12, GW10: 2, GW11: 13 | 37 | 7.40 | 5 |
| N.Jackson | AVL | Forward | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | 37 | 7.40 | 5 |
| Van Hecke | TOT | Defender | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | 36 | 7.20 | 5 |
| Silva | BOU | Defender | GW7: 8, GW8: 8, GW9: 8, GW10: 3, GW11: 8 | 35 | 7.00 | 5 |
| Tavernier | BOU | Midfielder | GW7: 10, GW8: 10, GW9: 3, GW10: 3, GW11: 8 | 34 | 6.80 | 5 |
| Isak | LIV | Forward | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | 33 | 6.60 | 5 |
| Roefs | SUN | Goalkeeper | GW7: 2, GW8: 9, GW9: 1, GW10: 9, GW11: 11 | 32 | 6.40 | 5 |
| Lewis-Potter | BRE | Midfielder | GW7: 9, GW8: 2, GW9: 3, GW10: 1, GW11: 16 | 31 | 6.20 | 5 |
| Ayari | BHA | Midfielder | GW7: 13, GW8: 2, GW9: 10, GW10: 3, GW11: 3 | 31 | 6.20 | 5 |
| Barry | EVE | Forward | GW7: 2, GW8: 2, GW9: 9, GW10: 16, GW11: 2 | 31 | 6.20 | 5 |
| Truffert | BOU | Defender | GW7: 6, GW8: 10, GW9: 6, GW10: 2, GW11: 6 | 30 | 6.00 | 5 |
| Vuskovic | BHA | Defender | GW7: 11, GW8: 1, GW9: 6, GW10: 12, GW11: 0 | 30 | 6.00 | 5 |
| Rudoni | COV | Midfielder | GW7: 6, GW8: 2, GW9: 9, GW10: 2, GW11: 10 | 29 | 5.80 | 5 |
| E.Le Fée | SUN | Midfielder | GW7: 4, GW8: 3, GW9: 8, GW10: 11, GW11: 3 | 29 | 5.80 | 5 |
| Muharemović | LEE | Defender | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | 29 | 5.80 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW12 player forecasts

| Player | Last 5 GW points | Club | Pos | GW12 | GW13 | GW14 | GW15 | GW16 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calvert-Lewin | GW7: 9, GW8: 2, GW9: 2, GW10: 2, GW11: 9 | LEE | Forward | 5.53 | 3.16 | 5.53 | 3.29 | 4.51 | 17.81 | 2.97 | high | 5-GW avg pts 4.80; mins 89; xGI 0.60; current GWs 11; fixture Elo diff -2 |
| Wirtz | GW7: 5, GW8: 6, GW9: 2, GW10: 13, GW11: 14 | LIV | Midfielder | 5.33 | 6.05 | 4.91 | 5.46 | 5.68 | 21.93 | 2.92 | high | 5-GW avg pts 8.00; mins 83; xGI 0.55; current GWs 11; fixture Elo diff +122 |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | 4.84 | 5.86 | 4.56 | 5.25 | 5.47 | 20.73 | 2.20 | high | 5-GW avg pts 6.60; mins 84; xGI 0.58; current GWs 11; fixture Elo diff +122 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | 4.79 | 4.71 | 4.71 | 4.81 | 3.42 | 18.21 | 2.50 | high | 5-GW avg pts 7.40; mins 84; xGI 0.57; current GWs 11; fixture Elo diff +173 |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | 4.67 | 4.83 | 4.06 | 4.51 | 4.79 | 18.30 | 2.35 | high | 5-GW avg pts 2.20; mins 72; xGI 0.37; current GWs 11; fixture Elo diff +73 |
| Bogle | GW7: 2, GW8: 5, GW9: 1, GW10: 7, GW11: 4 | LEE | Defender | 4.58 | 2.78 | 4.58 | 2.88 | 4.20 | 15.29 | 3.19 | high | 5-GW avg pts 3.80; mins 89; xGI 0.24; current GWs 11; fixture Elo diff -2 |
| Groß | GW7: 5, GW8: 0, GW9: 2, GW10: 10, GW11: 4 | BHA | Midfielder | 4.47 | 4.00 | 4.68 | 4.76 | 5.56 | 18.48 | 2.93 | high | 5-GW avg pts 4.20; mins 86; xGI 0.52; current GWs 11; fixture Elo diff +47 |
| Palmer | GW7: 2, GW8: -1, GW9: 8, GW10: 2, GW11: 2 | CHE | Midfielder | 4.43 | 4.79 | 4.29 | 3.10 | 4.40 | 16.99 | 1.73 | high | 5-GW avg pts 2.60; mins 88; xGI 0.33; current GWs 11; fixture Elo diff -55 |
| Justin | GW7: 2, GW8: 6, GW9: 2, GW10: 9, GW11: 4 | LEE | Defender | 4.42 | 2.62 | 4.42 | 2.74 | 4.05 | 14.66 | 3.26 | high | 5-GW avg pts 4.60; mins 89; xGI 0.18; current GWs 11; fixture Elo diff -2 |
| Ampadu | GW7: 1, GW8: 2, GW9: 3, GW10: 3, GW11: 7 | LEE | Midfielder | 4.38 | 2.61 | 4.38 | 2.71 | 3.88 | 14.46 | 2.73 | high | 5-GW avg pts 3.20; mins 90; xGI 0.10; current GWs 11; fixture Elo diff -2 |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | 4.36 | 4.31 | 4.94 | 5.05 | 4.95 | 18.69 | 2.31 | high | 5-GW avg pts 8.00; mins 90; xGI 0.20; current GWs 11; fixture Elo diff +190 |
| Richards | GW7: 2, GW8: 3, GW9: 3, GW10: 1, GW11: 3 | CRY | Defender | 4.33 | 3.44 | 3.21 | 3.29 | 4.22 | 14.82 | 3.02 | high | 5-GW avg pts 2.40; mins 90; xGI 0.03; current GWs 11; fixture Elo diff +17 |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | 4.32 | 4.18 | 2.91 | 4.35 | 2.90 | 15.19 | 2.92 | high | 5-GW avg pts 7.20; mins 90; xGI 0.28; current GWs 11; fixture Elo diff -34 |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | CHE | Midfielder | 4.27 | 4.70 | 4.05 | 2.88 | 4.16 | 16.25 | 1.96 | high | 5-GW avg pts 3.80; mins 90; xGI 0.32; current GWs 11; fixture Elo diff -55 |
| E.Le Fée | GW7: 4, GW8: 3, GW9: 8, GW10: 11, GW11: 3 | SUN | Midfielder | 4.25 | 3.29 | 3.55 | 4.15 | 4.15 | 15.45 | 2.71 | high | 5-GW avg pts 5.80; mins 87; xGI 0.44; current GWs 11; fixture Elo diff -94 |
| Muharemović | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | LEE | Defender | 4.24 | 2.63 | 4.24 | 2.68 | 3.79 | 14.15 | 2.72 | high | 5-GW avg pts 5.80; mins 90; xGI 0.07; current GWs 11; fixture Elo diff -2 |
| Tavernier | GW7: 10, GW8: 10, GW9: 3, GW10: 3, GW11: 8 | BOU | Midfielder | 4.21 | 4.24 | 5.20 | 3.29 | 5.18 | 17.60 | 2.59 | high | 5-GW avg pts 6.80; mins 87; xGI 0.79; current GWs 11; fixture Elo diff +89 |
| Ødegaard | GW7: 3, GW8: 3, GW9: 3, GW10: 11, GW11: 5 | ARS | Midfielder | 4.13 | 4.56 | 5.11 | 4.61 | 4.46 | 18.22 | 2.72 | high | 5-GW avg pts 5.00; mins 89; xGI 0.39; current GWs 11; fixture Elo diff +190 |
| De Cuyper | GW7: 6, GW8: 1, GW9: 9, GW10: 6, GW11: 1 | BHA | Defender | 4.11 | 3.62 | 4.34 | 4.43 | 4.89 | 16.88 | 3.01 | high | 5-GW avg pts 4.60; mins 84; xGI 0.38; current GWs 11; fixture Elo diff +47 |
| Kudus | GW7: 6, GW8: 3, GW9: 7, GW10: 2, GW11: 2 | TOT | Midfielder | 4.08 | 4.07 | 2.98 | 4.28 | 3.07 | 14.96 | 2.27 | high | 5-GW avg pts 4.00; mins 87; xGI 0.33; current GWs 11; fixture Elo diff -34 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.3m**. Current squad selling value: **£97.8m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£1.7m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | £8.1m | 18.69 | GW12, GW13, GW14, GW15, GW16 | — | — |
| De Cuyper | GW7: 6, GW8: 1, GW9: 9, GW10: 6, GW11: 1 | BHA | Defender | £5.6m | 16.88 | GW14, GW15, GW16 | — | — |
| Konsa | GW7: 9, GW8: 14, GW9: 10, GW10: 8, GW11: 1 | ARS | Defender | £4.9m | 16.23 | GW13, GW14 | — | — |
| Bogle | GW7: 2, GW8: 5, GW9: 1, GW10: 7, GW11: 4 | LEE | Defender | £4.8m | 15.29 | GW12, GW14, GW16 | — | — |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | £5.2m | 15.19 | GW12, GW13, GW15 | — | — |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | £9.4m | 20.73 | GW12, GW13, GW14, GW15, GW16 | — | GW13, GW15 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | £7.3m | 18.21 | GW12, GW13, GW14, GW15 | — | — |
| Calvert-Lewin | GW7: 9, GW8: 2, GW9: 2, GW10: 2, GW11: 9 | LEE | Forward | £6.0m | 17.81 | GW12, GW14, GW16 | GW12, GW14 | — |
| A.Becker | GW7: 2, GW8: 6, GW9: 2, GW10: 4, GW11: 7 | LIV | Goalkeeper | £5.5m | 14.94 | GW13, GW15, GW16 | — | — |
| Trafford | GW7: 2, GW8: 10, GW9: 2, GW10: 10, GW11: 2 | LEE | Goalkeeper | £5.1m | 13.34 | GW12, GW14 | — | — |
| Wirtz | GW7: 5, GW8: 6, GW9: 2, GW10: 13, GW11: 14 | LIV | Midfielder | £7.5m | 21.93 | GW12, GW13, GW14, GW15, GW16 | GW13, GW15, GW16 | GW12 |
| Groß | GW7: 5, GW8: 0, GW9: 2, GW10: 10, GW11: 4 | BHA | Midfielder | £6.3m | 18.48 | GW12, GW13, GW14, GW15, GW16 | — | GW16 |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | £7.8m | 18.30 | GW12, GW13, GW15, GW16 | — | — |
| Ødegaard | GW7: 3, GW8: 3, GW9: 3, GW10: 11, GW11: 5 | ARS | Midfielder | £6.7m | 18.22 | GW12, GW13, GW14, GW15, GW16 | — | GW14 |
| Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | MCI | Midfielder | £7.5m | 17.54 | GW13, GW15, GW16 | — | — |

Squad cost: £97.7m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | £8.1m | 18.69 | GW12, GW13, GW14, GW15, GW16 | GW14 | — |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | FUL | Defender | £4.5m | 13.49 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Branthwaite | GW7: 1, GW8: 0, GW9: 9, GW10: 3, GW11: 2 | EVE | Defender | £5.5m | 12.91 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | IPS | Defender | £3.9m | 8.79 | Bench | — | — |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | HUL | Defender | £4.0m | 6.22 | Bench | — | — |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | £9.4m | 20.73 | GW12, GW13, GW14, GW15, GW16 | — | GW12, GW13, GW15, GW16 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | £7.3m | 18.21 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | ARS | Forward | £7.4m | 16.97 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Leno | GW7: 6, GW8: 8, GW9: 2, GW10: 3, GW11: 2 | FUL | Goalkeeper | £4.5m | 12.85 | GW12, GW13, GW16 | — | — |
| Horníček | GW7: 2, GW8: 8, GW9: 3, GW10: 3, GW11: 1 | NEW | Goalkeeper | £5.0m | 12.83 | GW14, GW15 | — | — |
| Wirtz | GW7: 5, GW8: 6, GW9: 2, GW10: 13, GW11: 14 | LIV | Midfielder | £7.5m | 21.93 | GW12, GW13, GW14, GW15, GW16 | GW12, GW13, GW15, GW16 | GW14 |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | £7.8m | 18.30 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Rice | GW7: 9, GW8: 3, GW9: 8, GW10: 3, GW11: 3 | ARS | Midfielder | £7.5m | 16.84 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | CHE | Midfielder | £8.3m | 16.25 | GW12, GW13, GW14, GW16 | — | — |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | MUN | Midfielder | £7.8m | 13.53 | GW15 | — | — |

Squad cost: £98.5m.

## One-transfer recommendation

**Branthwaite → De Cuyper** (projected weighted XI+captain gain 3.97).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Branthwaite | GW7: 1, GW8: 0, GW9: 9, GW10: 3, GW11: 2 | De Cuyper | GW7: 6, GW8: 1, GW9: 9, GW10: 6, GW11: 1 | £5.5m | £5.6m | £1.2m | 3.97 |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | Jacquet | GW7: 3, GW8: 8, GW9: 2, GW10: 4, GW11: 6 | £4.0m | £5.1m | £0.2m | 3.80 |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | Jacquet | GW7: 3, GW8: 8, GW9: 2, GW10: 4, GW11: 6 | £3.9m | £5.1m | £0.1m | 3.80 |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | Silva | GW7: 8, GW8: 8, GW9: 8, GW10: 3, GW11: 8 | £4.0m | £5.1m | £0.2m | 3.71 |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | Silva | GW7: 8, GW8: 8, GW9: 8, GW10: 3, GW11: 8 | £3.9m | £5.1m | £0.1m | 3.71 |
| Branthwaite | GW7: 1, GW8: 0, GW9: 9, GW10: 3, GW11: 2 | Virgil | GW7: 4, GW8: 9, GW9: 1, GW10: 4, GW11: 6 | £5.5m | £6.4m | £0.4m | 3.55 |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | £4.0m | £5.2m | £0.1m | 3.54 |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | £3.9m | £5.2m | £0.0m | 3.54 |
| Branthwaite | GW7: 1, GW8: 0, GW9: 9, GW10: 3, GW11: 2 | Araujo | GW7: 1, GW8: 10, GW9: 4, GW10: 7, GW11: 6 | £5.5m | £5.5m | £1.3m | 3.51 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | De Cuyper | GW7: 6, GW8: 1, GW9: 9, GW10: 6, GW11: 1 | £4.5m | £5.6m | £0.2m | 3.39 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
