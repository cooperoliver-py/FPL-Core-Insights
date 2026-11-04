# FPL predictions: 2026-2027, GW10

Last generated: 2026-11-04 16:30 UTC

Data commit: `707eb4fd6b3ac1178d106968b645bc61f62bb353`

## Data freshness

All scheduled Premier League fixtures before GW10 are complete.

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

Ranked by recorded FPL points in GW5–GW9. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| N.Jackson | AVL | Forward | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | 39 | 7.80 | 5 |
| Konsa | ARS | Defender | GW5: 1, GW6: 4, GW7: 9, GW8: 14, GW9: 10 | 38 | 7.60 | 5 |
| De Cuyper | BHA | Defender | GW5: 6, GW6: 15, GW7: 6, GW8: 1, GW9: 9 | 37 | 7.40 | 5 |
| Manzambi | AVL | Midfielder | GW5: 13, GW6: 5, GW7: 11, GW8: 1, GW9: 7 | 37 | 7.40 | 5 |
| Evanilson | BOU | Forward | GW5: 2, GW6: 7, GW7: 12, GW8: 6, GW9: 9 | 36 | 7.20 | 5 |
| Haaland | MCI | Forward | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | 35 | 7.00 | 5 |
| Van Hecke | TOT | Defender | GW5: 6, GW6: 3, GW7: 4, GW8: 7, GW9: 15 | 35 | 7.00 | 5 |
| Gabriel | ARS | Defender | GW5: 1, GW6: 2, GW7: 8, GW8: 17, GW9: 6 | 34 | 6.80 | 5 |
| Verbruggen | BHA | Goalkeeper | GW5: 6, GW6: 9, GW7: 6, GW8: 2, GW9: 11 | 34 | 6.80 | 5 |
| Vuskovic | BHA | Defender | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | 34 | 6.80 | 5 |
| Ayari | BHA | Midfielder | GW5: 3, GW6: 3, GW7: 13, GW8: 2, GW9: 10 | 31 | 6.20 | 5 |
| Hill | BOU | Defender | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | 30 | 6.00 | 5 |
| Iwobi | FUL | Midfielder | GW5: 5, GW6: 4, GW7: 11, GW8: 3, GW9: 6 | 29 | 5.80 | 5 |
| Rudoni | COV | Midfielder | GW5: 5, GW6: 7, GW7: 6, GW8: 2, GW9: 9 | 29 | 5.80 | 5 |
| Rice | ARS | Midfielder | GW5: 1, GW6: 7, GW7: 9, GW8: 3, GW9: 8 | 28 | 5.60 | 5 |
| Isak | LIV | Forward | GW5: 8, GW6: 0, GW7: 9, GW8: 9, GW9: 2 | 28 | 5.60 | 5 |
| Neto | CHE | Midfielder | GW5: 2, GW6: 5, GW7: 15, GW8: 3, GW9: 3 | 28 | 5.60 | 5 |
| Groß | BHA | Midfielder | GW5: 14, GW6: 6, GW7: 5, GW8: 0, GW9: 2 | 27 | 5.40 | 5 |
| Silva | BOU | Defender | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | 27 | 5.40 | 5 |
| Thiago | BRE | Forward | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | 27 | 5.40 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW10 player forecasts

| Player | Last 5 GW points | Club | Pos | GW10 | GW11 | GW12 | GW13 | GW14 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW5: 1, GW6: 2, GW7: 8, GW8: 17, GW9: 6 | ARS | Defender | 8.02 | 5.80 | 5.56 | 5.80 | 6.45 | 25.62 | 3.20 | high | 5-GW avg pts 6.80; mins 90; xGI 0.23; current GWs 9; fixture Elo diff +273 |
| Havertz | GW5: 2, GW6: 2, GW7: 2, GW8: 1, GW9: 9 | ARS | Forward | 5.71 | 4.27 | 4.63 | 4.27 | 4.36 | 18.87 | 2.55 | high | 5-GW avg pts 3.20; mins 64; xGI 0.39; current GWs 9; fixture Elo diff +273 |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | 5.71 | 5.95 | 5.43 | 5.92 | 5.18 | 22.66 | 2.76 | high | 5-GW avg pts 4.60; mins 89; xGI 0.33; current GWs 9; fixture Elo diff +17 |
| Konsa | GW5: 1, GW6: 4, GW7: 9, GW8: 14, GW9: 10 | ARS | Defender | 5.49 | 4.44 | 3.84 | 4.44 | 5.15 | 18.77 | 3.91 | high | 5-GW avg pts 7.60; mins 90; xGI 0.13; current GWs 9; fixture Elo diff +273 |
| Tarkowski | GW5: 14, GW6: 3, GW7: 0, GW8: 2, GW9: 6 | EVE | Defender | 5.05 | 3.48 | 3.14 | 3.06 | 3.93 | 15.18 | 2.45 | high | 5-GW avg pts 5.00; mins 90; xGI 0.02; current GWs 9; fixture Elo diff -25 |
| Rice | GW5: 1, GW6: 7, GW7: 9, GW8: 3, GW9: 8 | ARS | Midfielder | 4.97 | 4.14 | 3.91 | 4.14 | 4.40 | 17.37 | 2.35 | high | 5-GW avg pts 5.60; mins 88; xGI 0.34; current GWs 9; fixture Elo diff +273 |
| Haaland | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | MCI | Forward | 4.85 | 4.92 | 3.57 | 4.92 | 4.65 | 18.37 | 1.16 | high | 5-GW avg pts 7.00; mins 88; xGI 0.71; current GWs 9; fixture Elo diff +104 |
| Dewsbury-Hall | GW5: 3, GW6: 13, GW7: 2, GW8: 2, GW9: 4 | EVE | Midfielder | 4.78 | 3.81 | 3.32 | 3.33 | 4.12 | 15.67 | 2.37 | high | 5-GW avg pts 4.80; mins 89; xGI 0.35; current GWs 9; fixture Elo diff -25 |
| Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | BOU | Defender | 4.76 | 4.20 | 4.01 | 3.81 | 4.99 | 17.40 | 3.16 | high | 5-GW avg pts 6.00; mins 90; xGI 0.04; current GWs 9; fixture Elo diff +142 |
| Garner | GW5: 3, GW6: 4, GW7: 2, GW8: 3, GW9: 3 | EVE | Midfielder | 4.75 | 3.68 | 3.30 | 3.23 | 4.04 | 15.38 | 2.56 | high | 5-GW avg pts 3.00; mins 90; xGI 0.20; current GWs 9; fixture Elo diff -25 |
| Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | BOU | Defender | 4.70 | 4.30 | 4.20 | 3.72 | 4.72 | 17.37 | 3.41 | high | 5-GW avg pts 5.40; mins 90; xGI 0.11; current GWs 9; fixture Elo diff +142 |
| Evanilson | GW5: 2, GW6: 7, GW7: 12, GW8: 6, GW9: 9 | BOU | Forward | 4.67 | 3.80 | 3.58 | 3.58 | 4.84 | 16.36 | 2.56 | high | 5-GW avg pts 7.20; mins 84; xGI 0.68; current GWs 9; fixture Elo diff +142 |
| Palmer | GW5: 2, GW6: 8, GW7: 2, GW8: -1, GW9: 8 | CHE | Midfielder | 4.55 | 4.87 | 4.69 | 4.87 | 4.42 | 18.75 | 1.91 | high | 5-GW avg pts 3.80; mins 87; xGI 0.37; current GWs 9; fixture Elo diff +17 |
| Barry | GW5: 6, GW6: 6, GW7: 2, GW8: 2, GW9: 9 | EVE | Forward | 4.50 | 3.38 | 3.24 | 3.08 | 3.69 | 14.51 | 2.59 | high | 5-GW avg pts 5.00; mins 87; xGI 0.73; current GWs 9; fixture Elo diff -25 |
| Raya | GW5: 1, GW6: 3, GW7: 9, GW8: 7, GW9: 5 | ARS | Goalkeeper | 4.49 | 3.77 | 3.28 | 3.77 | 4.32 | 15.74 | 2.54 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 9; fixture Elo diff +273 |
| Pickford | GW5: 8, GW6: 1, GW7: 2, GW8: 1, GW9: 7 | EVE | Goalkeeper | 4.46 | 3.14 | 2.76 | 2.69 | 3.41 | 13.43 | 2.44 | high | 5-GW avg pts 3.80; mins 90; xGI 0.00; current GWs 9; fixture Elo diff -25 |
| Barcola | GW5: 3, GW6: 2, GW7: 4, GW8: 6, GW9: 1 | LIV | Midfielder | 4.42 | 4.86 | 4.42 | 5.22 | 4.28 | 18.55 | 2.29 | high | 5-GW avg pts 3.20; mins 83; xGI 0.30; current GWs 7; fixture Elo diff +93 |
| Truffert | GW5: 2, GW6: -1, GW7: 6, GW8: 10, GW9: 6 | BOU | Defender | 4.39 | 3.93 | 3.86 | 3.65 | 4.47 | 16.25 | 3.01 | high | 5-GW avg pts 4.60; mins 89; xGI 0.17; current GWs 9; fixture Elo diff +142 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | 4.38 | 4.66 | 3.98 | 3.59 | 3.61 | 16.43 | 2.11 | high | 5-GW avg pts 5.40; mins 90; xGI 0.56; current GWs 9; fixture Elo diff -83 |
| N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | AVL | Forward | 4.38 | 5.38 | 5.32 | 4.78 | 4.78 | 19.68 | 2.81 | high | 5-GW avg pts 7.80; mins 88; xGI 0.44; current GWs 9; fixture Elo diff +141 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.3m**. Current squad selling value: **£98.8m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.7m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW5: 1, GW6: 2, GW7: 8, GW8: 17, GW9: 6 | ARS | Defender | £8.0m | 25.62 | GW10, GW11, GW12, GW13, GW14 | GW10, GW12, GW14 | GW11, GW13 |
| Konsa | GW5: 1, GW6: 4, GW7: 9, GW8: 14, GW9: 10 | ARS | Defender | £4.8m | 18.77 | GW10, GW11, GW13, GW14 | — | — |
| Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | BOU | Defender | £5.5m | 17.40 | GW10, GW11, GW14 | — | — |
| Van Hecke | GW5: 6, GW6: 3, GW7: 4, GW8: 7, GW9: 15 | TOT | Defender | £5.0m | 16.61 | GW10, GW11, GW12, GW13 | — | — |
| Muharemović | GW5: 6, GW6: 2, GW7: 5, GW8: 9, GW9: 3 | LEE | Defender | £5.1m | 16.05 | GW12, GW14 | — | — |
| N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | AVL | Forward | £7.0m | 19.68 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Havertz | GW5: 2, GW6: 2, GW7: 2, GW8: 1, GW9: 9 | ARS | Forward | £7.4m | 18.87 | GW10, GW11, GW12, GW13, GW14 | — | GW10 |
| Calvert-Lewin | GW5: 2, GW6: 2, GW7: 9, GW8: 2, GW9: 2 | LEE | Forward | £6.1m | 16.55 | GW10, GW12, GW14 | — | — |
| Suzuki | GW5: 2, GW6: 2, GW7: 8, GW8: 4, GW9: 1 | AVL | Goalkeeper | £5.0m | 15.14 | GW11, GW12, GW13, GW14 | — | — |
| Pickford | GW5: 8, GW6: 1, GW7: 2, GW8: 1, GW9: 7 | EVE | Goalkeeper | £5.5m | 13.43 | GW10 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | £8.2m | 22.66 | GW10, GW11, GW12, GW13, GW14 | GW11, GW13 | GW12, GW14 |
| Palmer | GW5: 2, GW6: 8, GW7: 2, GW8: -1, GW9: 8 | CHE | Midfielder | £9.8m | 18.75 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Barcola | GW5: 3, GW6: 2, GW7: 4, GW8: 6, GW9: 1 | LIV | Midfielder | £8.1m | 18.55 | GW10, GW11, GW12, GW13 | — | — |
| Gibbs-White | GW5: 2, GW6: 2, GW7: 0, GW8: 2, GW9: 2 | NFO | Midfielder | £7.9m | 17.19 | GW12, GW13, GW14 | — | — |
| Tonali | GW5: 2, GW6: 7, GW7: 4, GW8: 5, GW9: 3 | TOT | Midfielder | £5.3m | 15.88 | GW11, GW13 | — | — |

Squad cost: £98.7m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW5: 1, GW6: 2, GW7: 8, GW8: 17, GW9: 6 | ARS | Defender | £8.0m | 25.62 | GW10, GW11, GW12, GW13, GW14 | GW10, GW12, GW14 | GW11, GW13 |
| Bassey | GW5: 6, GW6: 2, GW7: 8, GW8: 8, GW9: 1 | FUL | Defender | £4.5m | 13.94 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | EVE | Defender | £5.5m | 12.17 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Egan | GW5: 1, GW6: 1, GW7: 4, GW8: 4, GW9: 1 | HUL | Defender | £4.1m | 9.03 | Bench | — | — |
| Furlong | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | IPS | Defender | £3.9m | 0.67 | Bench | — | — |
| Havertz | GW5: 2, GW6: 2, GW7: 2, GW8: 1, GW9: 9 | ARS | Forward | £7.4m | 18.87 | GW10, GW11, GW12, GW13, GW14 | — | GW10 |
| Isak | GW5: 8, GW6: 0, GW7: 9, GW8: 9, GW9: 2 | LIV | Forward | £9.2m | 17.68 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | £7.8m | 16.43 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Horníček | GW5: 3, GW6: 0, GW7: 2, GW8: 8, GW9: 3 | NEW | Goalkeeper | £5.0m | 12.47 | GW10, GW11, GW12, GW14 | — | — |
| Leno | GW5: 3, GW6: 2, GW7: 6, GW8: 8, GW9: 2 | FUL | Goalkeeper | £4.5m | 11.99 | GW13 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | £8.2m | 22.66 | GW10, GW11, GW12, GW13, GW14 | GW11, GW13 | GW12, GW14 |
| Rice | GW5: 1, GW6: 7, GW7: 9, GW8: 3, GW9: 8 | ARS | Midfielder | £7.4m | 17.37 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Gibbs-White | GW5: 2, GW6: 2, GW7: 0, GW8: 2, GW9: 2 | NFO | Midfielder | £7.9m | 17.19 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Mbeumo | GW5: 2, GW6: 8, GW7: 8, GW8: 2, GW9: 1 | MUN | Midfielder | £7.9m | 16.95 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Cherki | GW5: 8, GW6: 10, GW7: 0, GW8: 0, GW9: 1 | MCI | Midfielder | £7.9m | 12.80 | Bench | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Branthwaite → Hill** (projected weighted XI+captain gain 5.23).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | £5.5m | £5.5m | £0.3m | 5.23 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | £5.5m | £5.1m | £0.7m | 5.20 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Van Hecke | GW5: 6, GW6: 3, GW7: 4, GW8: 7, GW9: 15 | £5.5m | £5.0m | £0.8m | 4.44 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Truffert | GW5: 2, GW6: -1, GW7: 6, GW8: 10, GW9: 6 | £5.5m | £5.4m | £0.4m | 4.08 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Muharemović | GW5: 6, GW6: 2, GW7: 5, GW8: 9, GW9: 3 | £5.5m | £5.1m | £0.7m | 3.88 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Vuskovic | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | £5.5m | £5.2m | £0.6m | 3.74 |
| Cherki | GW5: 8, GW6: 10, GW7: 0, GW8: 0, GW9: 1 | Barcola | GW5: 3, GW6: 2, GW7: 4, GW8: 6, GW9: 1 | £7.8m | £8.1m | £0.0m | 3.73 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Rúben | GW5: 1, GW6: 6, GW7: 1, GW8: 1, GW9: 2 | £5.5m | £5.5m | £0.3m | 3.45 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | £7.8m | £7.0m | £1.1m | 3.25 |
| Branthwaite | GW5: 8, GW6: 3, GW7: 1, GW8: 0, GW9: 9 | Jacquet | GW5: 6, GW6: 3, GW7: 3, GW8: 8, GW9: 2 | £5.5m | £5.1m | £0.7m | 3.06 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
