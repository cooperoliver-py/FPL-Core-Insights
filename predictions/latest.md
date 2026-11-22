# FPL predictions: 2026-2027, GW12

Last generated: 2026-11-22 16:34 UTC

Data commit: `d72eb563e0bd4dc06ee5b0c11627b448f5165523`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW11: 7/10 fixtures finished. Completed clubs contribute current-season form; BHA, BRE, EVE, HUL, LIV, MUN are deferred.

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
| Konsa | ARS | Defender | GW7: 9, GW8: 14, GW9: 10, GW10: 8, GW11: 1 | 42 | 8.40 | 5 |
| Evanilson | BOU | Forward | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | 42 | 8.40 | 5 |
| Hill | BOU | Defender | GW7: 7, GW8: 11, GW9: 6, GW10: 4, GW11: 14 | 42 | 8.40 | 5 |
| Gabriel | ARS | Defender | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | 40 | 8.00 | 5 |
| N.Jackson | AVL | Forward | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | 37 | 7.40 | 5 |
| Van Hecke | TOT | Defender | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | 36 | 7.20 | 5 |
| Silva | BOU | Defender | GW7: 8, GW8: 8, GW9: 8, GW10: 3, GW11: 8 | 35 | 7.00 | 5 |
| Tavernier | BOU | Midfielder | GW7: 10, GW8: 10, GW9: 3, GW10: 3, GW11: 8 | 34 | 6.80 | 5 |
| Roefs | SUN | Goalkeeper | GW7: 2, GW8: 9, GW9: 1, GW10: 9, GW11: 11 | 32 | 6.40 | 5 |
| Truffert | BOU | Defender | GW7: 6, GW8: 10, GW9: 6, GW10: 2, GW11: 6 | 30 | 6.00 | 5 |
| Vuskovic | BHA | Defender | GW7: 11, GW8: 1, GW9: 6, GW10: 12 | 30 | 7.50 | 4 |
| Rudoni | COV | Midfielder | GW7: 6, GW8: 2, GW9: 9, GW10: 2, GW11: 10 | 29 | 5.80 | 5 |
| E.Le Fée | SUN | Midfielder | GW7: 4, GW8: 3, GW9: 8, GW10: 11, GW11: 3 | 29 | 5.80 | 5 |
| Muharemović | LEE | Defender | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | 29 | 5.80 | 5 |
| Barry | EVE | Forward | GW7: 2, GW8: 2, GW9: 9, GW10: 16 | 29 | 7.25 | 4 |
| Raya | ARS | Goalkeeper | GW7: 9, GW8: 7, GW9: 5, GW10: 6, GW11: 1 | 28 | 5.60 | 5 |
| Isak | LIV | Forward | GW7: 9, GW8: 9, GW9: 2, GW10: 8 | 28 | 7.00 | 4 |
| Ayari | BHA | Midfielder | GW7: 13, GW8: 2, GW9: 10, GW10: 3 | 28 | 7.00 | 4 |
| Haaland | MCI | Forward | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | 27 | 5.40 | 5 |
| Petrović | BOU | Goalkeeper | GW7: 6, GW8: 7, GW9: 6, GW10: 2, GW11: 6 | 27 | 5.40 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW12 player forecasts

| Player | Last 5 GW points | Club | Pos | GW12 | GW13 | GW14 | GW15 | GW16 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Muharemović | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | LEE | Defender | 5.23 | 3.39 | 4.79 | 3.00 | 4.04 | 16.63 | 3.26 | high | 5-GW avg pts 5.80; mins 90; xGI 0.07; current GWs 11; fixture Elo diff -2 |
| Calvert-Lewin | GW7: 9, GW8: 2, GW9: 2, GW10: 2, GW11: 9 | LEE | Forward | 5.17 | 3.73 | 4.97 | 3.31 | 4.43 | 17.48 | 2.91 | high | 5-GW avg pts 4.80; mins 89; xGI 0.60; current GWs 11; fixture Elo diff -2 |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | 5.12 | 5.28 | 5.13 | 5.09 | 5.23 | 20.67 | 2.65 | high | 5-GW avg pts 2.20; mins 72; xGI 0.37; current GWs 11; fixture Elo diff +73 |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | CHE | Midfielder | 5.11 | 5.26 | 4.72 | 3.44 | 4.73 | 18.86 | 2.27 | high | 5-GW avg pts 3.80; mins 90; xGI 0.32; current GWs 11; fixture Elo diff -55 |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | 5.08 | 5.24 | 6.39 | 5.46 | 3.58 | 20.88 | 1.80 | high | 5-GW avg pts 2.80; mins 72; xGI 0.45; current GWs 10; fixture Elo diff +75 |
| Bogle | GW7: 2, GW8: 5, GW9: 1, GW10: 7, GW11: 4 | LEE | Defender | 5.02 | 2.84 | 5.10 | 2.92 | 4.21 | 16.23 | 3.38 | high | 5-GW avg pts 3.80; mins 89; xGI 0.24; current GWs 11; fixture Elo diff -2 |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | 4.89 | 5.42 | 4.55 | 5.10 | 5.22 | 20.10 | 2.48 | high | 5-GW avg pts 3.60; mins 82; xGI 0.39; current GWs 8; fixture Elo diff +122 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | 4.85 | 4.47 | 5.57 | 4.74 | 2.64 | 18.23 | 2.34 | high | 5-GW avg pts 4.20; mins 88; xGI 0.41; current GWs 10; fixture Elo diff +75 |
| Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | BOU | Forward | 4.82 | 4.82 | 6.55 | 3.47 | 6.67 | 20.83 | 3.16 | high | 5-GW avg pts 8.40; mins 83; xGI 0.91; current GWs 11; fixture Elo diff +89 |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | 4.77 | 5.32 | 4.51 | 4.84 | 4.98 | 19.54 | 2.10 | high | 5-GW avg pts 5.60; mins 67; xGI 0.31; current GWs 10; fixture Elo diff +122 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | 4.65 | 4.48 | 4.71 | 4.90 | 6.37 | 19.71 | 3.13 | high | 5-GW avg pts 4.60; mins 86; xGI 0.52; current GWs 10; fixture Elo diff +47 |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | 4.64 | 4.28 | 4.79 | 5.09 | 5.11 | 18.96 | 2.34 | high | 5-GW avg pts 8.00; mins 90; xGI 0.20; current GWs 11; fixture Elo diff +190 |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | 4.62 | 4.81 | 2.92 | 5.27 | 3.18 | 16.88 | 3.25 | high | 5-GW avg pts 7.20; mins 90; xGI 0.28; current GWs 11; fixture Elo diff -34 |
| Palmer | GW7: 2, GW8: -1, GW9: 8, GW10: 2, GW11: 2 | CHE | Midfielder | 4.58 | 4.61 | 4.08 | 3.10 | 4.09 | 16.62 | 1.70 | high | 5-GW avg pts 2.60; mins 88; xGI 0.33; current GWs 11; fixture Elo diff -55 |
| Mitchell | GW7: 0, GW8: 1, GW9: 3, GW10: 1, GW11: 1 | CRY | Defender | 4.57 | 2.89 | 2.22 | 2.59 | 3.14 | 12.65 | 2.87 | high | 5-GW avg pts 1.20; mins 90; xGI 0.16; current GWs 11; fixture Elo diff +17 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | 4.56 | 4.28 | 4.28 | 4.66 | 3.62 | 17.27 | 2.40 | high | 5-GW avg pts 7.40; mins 84; xGI 0.57; current GWs 11; fixture Elo diff +173 |
| Wirtz | GW6: 2, GW7: 5, GW8: 6, GW9: 2, GW10: 13 | LIV | Midfielder | 4.55 | 4.73 | 4.35 | 4.22 | 4.49 | 17.94 | 2.46 | high | 5-GW avg pts 5.60; mins 78; xGI 0.33; current GWs 10; fixture Elo diff +122 |
| Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | FUL | Midfielder | 4.52 | 5.41 | 5.33 | 4.88 | 5.33 | 20.27 | 3.75 | high | 5-GW avg pts 4.60; mins 79; xGI 0.50; current GWs 11; fixture Elo diff -4 |
| Justin | GW7: 2, GW8: 6, GW9: 2, GW10: 9, GW11: 4 | LEE | Defender | 4.51 | 2.60 | 4.74 | 2.61 | 3.76 | 14.73 | 3.27 | high | 5-GW avg pts 4.60; mins 89; xGI 0.18; current GWs 11; fixture Elo diff -2 |
| Haaland | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | MCI | Forward | 4.49 | 6.17 | 5.74 | 5.96 | 6.65 | 22.80 | 1.44 | high | 5-GW avg pts 5.40; mins 90; xGI 0.73; current GWs 11; fixture Elo diff +158 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.0m**. Current squad selling value: **£98.0m**. Total available funds: **£99.0m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.5m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Murillo | GW7: 2, GW8: 1, GW9: 3, GW10: 4, GW11: 0 | NFO | Defender | £5.5m | 17.01 | GW13, GW15, GW16 | — | — |
| De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | BHA | Defender | £5.5m | 16.90 | GW13, GW14, GW15, GW16 | — | — |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | £5.2m | 16.88 | GW12, GW13, GW15 | — | GW15 |
| Muharemović | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | LEE | Defender | £5.1m | 16.63 | GW12, GW14 | GW12 | — |
| Bogle | GW7: 2, GW8: 5, GW9: 1, GW10: 7, GW11: 4 | LEE | Defender | £4.8m | 16.23 | GW12, GW14, GW16 | — | — |
| Haaland | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | MCI | Forward | £15.8m | 22.80 | GW12, GW13, GW14, GW15, GW16 | GW13, GW15 | GW14, GW16 |
| Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | BOU | Forward | £6.6m | 20.83 | GW12, GW13, GW14, GW15, GW16 | GW14, GW16 | — |
| Calvert-Lewin | GW7: 9, GW8: 2, GW9: 2, GW10: 2, GW11: 9 | LEE | Forward | £6.0m | 17.48 | GW12, GW14 | — | GW12 |
| Petrović | GW7: 6, GW8: 7, GW9: 6, GW10: 2, GW11: 6 | BOU | Goalkeeper | £4.5m | 14.63 | GW12, GW14, GW16 | — | — |
| Kinsky | GW7: 2, GW8: 9, GW9: 6, GW10: 2, GW11: 7 | TOT | Goalkeeper | £4.4m | 13.04 | GW13, GW15 | — | — |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | £7.8m | 20.67 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | FUL | Midfielder | £5.4m | 20.27 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | £8.1m | 20.10 | GW12, GW13, GW15, GW16 | — | GW13 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | £6.3m | 19.71 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | MCI | Midfielder | £7.5m | 18.78 | GW13, GW14, GW15, GW16 | — | — |

Squad cost: £98.5m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | £8.1m | 18.96 | GW12, GW13, GW14, GW15, GW16 | GW15 | GW16 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | FUL | Defender | £4.5m | 13.35 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | EVE | Defender | £5.5m | 12.15 | GW12, GW14, GW15, GW16 | — | — |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | HUL | Defender | £4.1m | 10.48 | GW13 | — | — |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | IPS | Defender | £3.9m | 7.84 | Bench | — | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 19.54 | GW12, GW13, GW14, GW15, GW16 | GW13 | — |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | ARS | Forward | £7.4m | 17.53 | GW12, GW13, GW14, GW15, GW16 | — | — |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | £7.2m | 17.27 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Leno | GW7: 6, GW8: 8, GW9: 2, GW10: 3, GW11: 2 | FUL | Goalkeeper | £4.5m | 13.54 | GW12, GW13, GW14, GW16 | — | — |
| Horníček | GW7: 2, GW8: 8, GW9: 3, GW10: 3, GW11: 1 | NEW | Goalkeeper | £5.0m | 13.37 | GW15 | — | — |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | £7.8m | 20.67 | GW12, GW13, GW14, GW15, GW16 | GW12, GW16 | GW13, GW14, GW15 |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | CHE | Midfielder | £8.3m | 18.86 | GW12, GW13, GW14, GW15, GW16 | — | GW12 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | £7.8m | 18.23 | GW12, GW13, GW14, GW15 | GW14 | — |
| Rice | GW7: 9, GW8: 3, GW9: 8, GW10: 3, GW11: 3 | ARS | Midfielder | £7.5m | 17.31 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | MCI | Midfielder | £7.9m | 10.72 | GW16 | — | — |

Squad cost: £98.8m.

## One-transfer recommendation

**N.Jackson → Evanilson** (projected weighted XI+captain gain 5.21).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | £7.1m | £6.6m | £1.5m | 5.21 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | £5.5m | £5.5m | £1.0m | 5.20 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | £7.8m | £5.4m | £3.4m | 5.02 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.8m | £6.3m | £2.5m | 5.01 |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | £7.4m | £6.6m | £1.8m | 4.95 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Virgil | GW6: 0, GW7: 4, GW8: 9, GW9: 1, GW10: 4 | £5.5m | £6.4m | £0.1m | 4.81 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | £7.8m | £8.1m | £0.7m | 4.81 |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | Muharemović | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | £4.1m | £5.1m | £0.0m | 4.75 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Murillo | GW7: 2, GW8: 1, GW9: 3, GW10: 4, GW11: 0 | £5.5m | £5.5m | £1.0m | 4.67 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | £5.5m | £5.2m | £1.3m | 4.67 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
