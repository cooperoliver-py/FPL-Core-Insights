# FPL predictions: 2026-2027, GW12

Last generated: 2026-11-21 21:49 UTC

Data commit: `b893f13e39b2abf6decb1a0c81411d5c39568c29`

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
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | 5.30 | 5.47 | 6.60 | 5.70 | 3.63 | 21.67 | 1.87 | high | 5-GW avg pts 2.80; mins 72; xGI 0.45; current GWs 10; fixture Elo diff +75 |
| Calvert-Lewin | GW7: 9, GW8: 2, GW9: 2, GW10: 2, GW11: 9 | LEE | Forward | 5.10 | 3.41 | 4.93 | 3.04 | 4.17 | 16.74 | 2.79 | high | 5-GW avg pts 4.80; mins 89; xGI 0.60; current GWs 11; fixture Elo diff -2 |
| Muharemović | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | LEE | Defender | 5.07 | 3.11 | 4.72 | 2.77 | 3.76 | 15.85 | 3.11 | high | 5-GW avg pts 5.80; mins 90; xGI 0.07; current GWs 11; fixture Elo diff -2 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | 4.97 | 4.77 | 4.99 | 5.22 | 6.87 | 21.03 | 3.34 | high | 5-GW avg pts 4.60; mins 86; xGI 0.52; current GWs 10; fixture Elo diff +47 |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | 4.92 | 5.46 | 4.57 | 5.14 | 5.26 | 20.24 | 2.50 | high | 5-GW avg pts 3.60; mins 82; xGI 0.39; current GWs 8; fixture Elo diff +122 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | 4.89 | 4.52 | 5.58 | 4.79 | 2.61 | 18.34 | 2.35 | high | 5-GW avg pts 4.20; mins 88; xGI 0.41; current GWs 10; fixture Elo diff +75 |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | CHE | Midfielder | 4.84 | 4.96 | 4.44 | 3.15 | 4.45 | 17.73 | 2.16 | high | 5-GW avg pts 3.80; mins 90; xGI 0.32; current GWs 11; fixture Elo diff -55 |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | 4.83 | 5.39 | 4.56 | 4.91 | 5.05 | 19.80 | 2.13 | high | 5-GW avg pts 5.60; mins 67; xGI 0.31; current GWs 10; fixture Elo diff +122 |
| Bogle | GW7: 2, GW8: 5, GW9: 1, GW10: 7, GW11: 4 | LEE | Defender | 4.81 | 2.67 | 5.00 | 2.80 | 3.95 | 15.54 | 3.24 | high | 5-GW avg pts 3.80; mins 89; xGI 0.24; current GWs 11; fixture Elo diff -2 |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | 4.68 | 5.58 | 4.69 | 4.64 | 4.75 | 19.56 | 2.51 | high | 5-GW avg pts 2.20; mins 72; xGI 0.36; current GWs 11; fixture Elo diff +73 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | 4.65 | 4.17 | 4.17 | 4.76 | 3.60 | 17.23 | 2.39 | high | 5-GW avg pts 7.40; mins 84; xGI 0.58; current GWs 11; fixture Elo diff +173 |
| Wirtz | GW6: 2, GW7: 5, GW8: 6, GW9: 2, GW10: 13 | LIV | Midfielder | 4.57 | 4.71 | 4.37 | 4.24 | 4.48 | 17.97 | 2.46 | high | 5-GW avg pts 5.60; mins 78; xGI 0.33; current GWs 10; fixture Elo diff +122 |
| Mitchell | GW7: 0, GW8: 1, GW9: 3, GW10: 1, GW11: 1 | CRY | Defender | 4.55 | 2.71 | 2.04 | 2.40 | 2.94 | 12.07 | 2.74 | high | 5-GW avg pts 1.20; mins 90; xGI 0.18; current GWs 11; fixture Elo diff +17 |
| Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | FUL | Midfielder | 4.52 | 5.41 | 5.33 | 4.88 | 5.33 | 20.27 | 3.75 | high | 5-GW avg pts 4.60; mins 79; xGI 0.50; current GWs 11; fixture Elo diff -4 |
| Haaland | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | MCI | Forward | 4.49 | 6.17 | 5.74 | 5.96 | 6.65 | 22.80 | 1.44 | high | 5-GW avg pts 5.40; mins 90; xGI 0.73; current GWs 11; fixture Elo diff +158 |
| Palmer | GW7: 2, GW8: -1, GW9: 8, GW10: 2, GW11: 2 | CHE | Midfielder | 4.48 | 4.49 | 3.98 | 2.97 | 3.99 | 16.18 | 1.65 | high | 5-GW avg pts 2.60; mins 88; xGI 0.33; current GWs 11; fixture Elo diff -55 |
| Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | BOU | Forward | 4.47 | 4.42 | 6.35 | 3.11 | 6.41 | 19.55 | 3.01 | high | 5-GW avg pts 8.40; mins 83; xGI 0.89; current GWs 11; fixture Elo diff +89 |
| Cunha | GW6: 10, GW7: 1, GW8: 1, GW9: 2, GW10: 5 | MUN | Midfielder | 4.43 | 4.23 | 5.56 | 4.32 | 2.59 | 17.26 | 2.21 | high | 5-GW avg pts 3.80; mins 59; xGI 0.27; current GWs 10; fixture Elo diff +75 |
| Rice | GW7: 9, GW8: 3, GW9: 8, GW10: 3, GW11: 1 | ARS | Midfielder | 4.37 | 4.46 | 4.85 | 4.87 | 4.83 | 18.58 | 2.48 | high | 5-GW avg pts 4.80; mins 82; xGI 0.44; current GWs 11; fixture Elo diff +190 |
| Virgil | GW6: 0, GW7: 4, GW8: 9, GW9: 1, GW10: 4 | LIV | Defender | 4.36 | 4.66 | 4.00 | 4.42 | 4.58 | 17.60 | 2.75 | high | 5-GW avg pts 3.60; mins 90; xGI 0.08; current GWs 10; fixture Elo diff +122 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.0m**. Current squad selling value: **£97.9m**. Total available funds: **£98.9m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | £8.1m | 18.06 | GW12, GW13, GW14, GW15, GW16 | — | — |
| De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | BHA | Defender | £5.5m | 17.28 | GW13, GW15, GW16 | — | — |
| Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | BHA | Defender | £5.3m | 17.10 | GW14, GW15, GW16 | — | — |
| Muharemović | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | LEE | Defender | £5.1m | 15.85 | GW12, GW14 | — | — |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | £5.1m | 15.53 | GW12, GW13, GW15 | — | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 19.80 | GW12, GW13, GW15, GW16 | — | — |
| Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | BOU | Forward | £6.5m | 19.55 | GW13, GW14, GW16 | — | GW14, GW16 |
| Calvert-Lewin | GW7: 9, GW8: 2, GW9: 2, GW10: 2, GW11: 9 | LEE | Forward | £6.0m | 16.74 | GW12, GW14, GW16 | — | GW12 |
| Petrović | GW7: 6, GW8: 7, GW9: 6, GW10: 2, GW11: 6 | BOU | Goalkeeper | £4.5m | 14.49 | GW12, GW14, GW16 | — | — |
| Kinsky | GW7: 2, GW8: 9, GW9: 6, GW10: 2, GW11: 7 | TOT | Goalkeeper | £4.4m | 12.37 | GW13, GW15 | — | — |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | £11.6m | 21.67 | GW12, GW13, GW14, GW15 | GW12, GW14, GW15 | GW13 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | £6.3m | 21.03 | GW12, GW13, GW14, GW15, GW16 | GW16 | GW15 |
| Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | FUL | Midfielder | £5.4m | 20.27 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | £8.1m | 20.24 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | £7.8m | 19.56 | GW12, GW13, GW14, GW15, GW16 | GW13 | — |

Squad cost: £99.0m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | £8.1m | 18.06 | GW12, GW13, GW14, GW15, GW16 | — | GW15, GW16 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | FUL | Defender | £4.5m | 13.35 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | EVE | Defender | £5.5m | 12.15 | GW12, GW14, GW15, GW16 | — | — |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | HUL | Defender | £4.1m | 10.48 | GW13 | — | — |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | IPS | Defender | £3.9m | 7.44 | Bench | — | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 19.80 | GW12, GW13, GW14, GW15, GW16 | GW15, GW16 | GW13 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | £7.2m | 17.23 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | ARS | Forward | £7.4m | 17.15 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Leno | GW7: 6, GW8: 8, GW9: 2, GW10: 3, GW11: 2 | FUL | Goalkeeper | £4.5m | 13.54 | GW12, GW13, GW14, GW16 | — | — |
| Horníček | GW7: 2, GW8: 8, GW9: 3, GW10: 3, GW11: 1 | NEW | Goalkeeper | £5.0m | 12.38 | GW15 | — | — |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | £7.8m | 19.56 | GW12, GW13, GW14, GW15, GW16 | GW13 | — |
| Rice | GW7: 9, GW8: 3, GW9: 8, GW10: 3, GW11: 1 | ARS | Midfielder | £7.5m | 18.58 | GW12, GW13, GW14, GW15, GW16 | — | GW14 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | £7.8m | 18.34 | GW12, GW13, GW14, GW15 | GW12, GW14 | — |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | CHE | Midfielder | £8.2m | 17.73 | GW12, GW13, GW14, GW15, GW16 | — | GW12 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | MCI | Midfielder | £7.9m | 10.72 | GW16 | — | — |

Squad cost: £98.7m.

## One-transfer recommendation

**Cherki → Groß** (projected weighted XI+captain gain 7.41).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.8m | £6.3m | £2.5m | 7.41 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | £5.5m | £5.5m | £1.0m | 5.75 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | £7.8m | £8.1m | £0.7m | 5.55 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | £7.8m | £5.4m | £3.4m | 5.43 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Virgil | GW6: 0, GW7: 4, GW8: 9, GW9: 1, GW10: 4 | £5.5m | £6.4m | £0.1m | 5.26 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | £5.5m | £5.3m | £1.2m | 4.93 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | £4.5m | £5.5m | £0.0m | 4.73 |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.9m | £6.3m | £2.6m | 4.68 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | £7.8m | £7.5m | £1.3m | 4.63 |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | £4.1m | £5.1m | £0.0m | 4.18 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
