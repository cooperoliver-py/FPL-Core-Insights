# FPL predictions: 2026-2027, GW12

Last generated: 2026-11-23 08:01 UTC

Data commit: `bb27a765d3dff355d8cb1e4cf697fe92514feec3`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW11: 9/10 fixtures finished. Completed clubs contribute current-season form; BRE, EVE are deferred.

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
| Wirtz | LIV | Midfielder | GW7: 5, GW8: 6, GW9: 2, GW10: 13, GW11: 14 | 40 | 8.00 | 5 |
| McBurnie | HUL | Forward | GW7: 2, GW8: 8, GW9: 12, GW10: 2, GW11: 13 | 37 | 7.40 | 5 |
| N.Jackson | AVL | Forward | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | 37 | 7.40 | 5 |
| Van Hecke | TOT | Defender | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | 36 | 7.20 | 5 |
| Silva | BOU | Defender | GW7: 8, GW8: 8, GW9: 8, GW10: 3, GW11: 8 | 35 | 7.00 | 5 |
| Tavernier | BOU | Midfielder | GW7: 10, GW8: 10, GW9: 3, GW10: 3, GW11: 8 | 34 | 6.80 | 5 |
| Isak | LIV | Forward | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | 33 | 6.60 | 5 |
| Roefs | SUN | Goalkeeper | GW7: 2, GW8: 9, GW9: 1, GW10: 9, GW11: 11 | 32 | 6.40 | 5 |
| Ayari | BHA | Midfielder | GW7: 13, GW8: 2, GW9: 10, GW10: 3, GW11: 3 | 31 | 6.20 | 5 |
| Truffert | BOU | Defender | GW7: 6, GW8: 10, GW9: 6, GW10: 2, GW11: 6 | 30 | 6.00 | 5 |
| Vuskovic | BHA | Defender | GW7: 11, GW8: 1, GW9: 6, GW10: 12, GW11: 0 | 30 | 6.00 | 5 |
| Rudoni | COV | Midfielder | GW7: 6, GW8: 2, GW9: 9, GW10: 2, GW11: 10 | 29 | 5.80 | 5 |
| E.Le Fée | SUN | Midfielder | GW7: 4, GW8: 3, GW9: 8, GW10: 11, GW11: 3 | 29 | 5.80 | 5 |
| Muharemović | LEE | Defender | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | 29 | 5.80 | 5 |
| Barry | EVE | Forward | GW7: 2, GW8: 2, GW9: 9, GW10: 16 | 29 | 7.25 | 4 |
| Raya | ARS | Goalkeeper | GW7: 9, GW8: 7, GW9: 5, GW10: 6, GW11: 1 | 28 | 5.60 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW12 player forecasts

| Player | Last 5 GW points | Club | Pos | GW12 | GW13 | GW14 | GW15 | GW16 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | 5.10 | 6.33 | 4.81 | 5.43 | 5.65 | 21.84 | 2.35 | high | 5-GW avg pts 6.60; mins 84; xGI 0.58; current GWs 11; fixture Elo diff +122 |
| Muharemović | GW7: 5, GW8: 9, GW9: 3, GW10: 10, GW11: 2 | LEE | Defender | 5.02 | 3.18 | 4.70 | 2.79 | 3.83 | 15.89 | 3.12 | high | 5-GW avg pts 5.80; mins 90; xGI 0.07; current GWs 11; fixture Elo diff -2 |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | 5.00 | 5.28 | 5.02 | 4.97 | 5.12 | 20.32 | 2.61 | high | 5-GW avg pts 2.20; mins 72; xGI 0.37; current GWs 11; fixture Elo diff +73 |
| Calvert-Lewin | GW7: 9, GW8: 2, GW9: 2, GW10: 2, GW11: 9 | LEE | Forward | 4.97 | 3.52 | 4.88 | 3.10 | 4.22 | 16.74 | 2.79 | high | 5-GW avg pts 4.80; mins 89; xGI 0.60; current GWs 11; fixture Elo diff -2 |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | CHE | Midfielder | 4.90 | 5.06 | 4.51 | 3.23 | 4.52 | 18.03 | 2.17 | high | 5-GW avg pts 3.80; mins 90; xGI 0.32; current GWs 11; fixture Elo diff -55 |
| Groß | GW7: 5, GW8: 0, GW9: 2, GW10: 10, GW11: 4 | BHA | Midfielder | 4.85 | 4.82 | 5.09 | 5.05 | 6.60 | 20.76 | 3.29 | high | 5-GW avg pts 4.20; mins 86; xGI 0.52; current GWs 11; fixture Elo diff +47 |
| Bogle | GW7: 2, GW8: 5, GW9: 1, GW10: 7, GW11: 4 | LEE | Defender | 4.81 | 2.64 | 5.00 | 2.71 | 4.01 | 15.49 | 3.23 | high | 5-GW avg pts 3.80; mins 89; xGI 0.24; current GWs 11; fixture Elo diff -2 |
| Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | BOU | Forward | 4.71 | 4.71 | 6.55 | 3.37 | 6.67 | 20.54 | 3.11 | high | 5-GW avg pts 8.40; mins 83; xGI 0.91; current GWs 11; fixture Elo diff +89 |
| Virgil | GW7: 4, GW8: 9, GW9: 1, GW10: 4, GW11: 6 | LIV | Defender | 4.65 | 4.79 | 4.29 | 4.69 | 4.84 | 18.58 | 2.90 | high | 5-GW avg pts 4.80; mins 90; xGI 0.13; current GWs 11; fixture Elo diff +122 |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | 4.64 | 4.28 | 4.79 | 5.09 | 5.11 | 18.96 | 2.34 | high | 5-GW avg pts 8.00; mins 90; xGI 0.20; current GWs 11; fixture Elo diff +190 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | 4.56 | 4.17 | 4.17 | 4.66 | 3.51 | 17.01 | 2.33 | high | 5-GW avg pts 7.40; mins 84; xGI 0.57; current GWs 11; fixture Elo diff +173 |
| Mitchell | GW7: 0, GW8: 1, GW9: 3, GW10: 1, GW11: 1 | CRY | Defender | 4.53 | 2.76 | 2.08 | 2.45 | 3.00 | 12.19 | 2.77 | high | 5-GW avg pts 1.20; mins 90; xGI 0.16; current GWs 11; fixture Elo diff +17 |
| B.Fernandes | GW7: 1, GW8: 0, GW9: 2, GW10: 10, GW11: 2 | MUN | Midfielder | 4.48 | 4.04 | 5.86 | 4.33 | 1.94 | 17.00 | 1.47 | high | 5-GW avg pts 3.00; mins 72; xGI 0.53; current GWs 11; fixture Elo diff +75 |
| Palmer | GW7: 2, GW8: -1, GW9: 8, GW10: 2, GW11: 2 | CHE | Midfielder | 4.47 | 4.50 | 3.97 | 2.98 | 3.98 | 16.16 | 1.65 | high | 5-GW avg pts 2.60; mins 88; xGI 0.33; current GWs 11; fixture Elo diff -55 |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | ARS | Forward | 4.43 | 3.99 | 4.32 | 4.67 | 4.64 | 17.53 | 2.37 | high | 5-GW avg pts 3.80; mins 64; xGI 0.28; current GWs 11; fixture Elo diff +190 |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | 4.41 | 4.60 | 2.73 | 5.17 | 2.98 | 16.14 | 3.10 | high | 5-GW avg pts 7.20; mins 90; xGI 0.28; current GWs 11; fixture Elo diff -34 |
| Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | FUL | Midfielder | 4.40 | 5.30 | 5.22 | 4.77 | 5.22 | 19.81 | 3.67 | high | 5-GW avg pts 4.60; mins 79; xGI 0.50; current GWs 11; fixture Elo diff -4 |
| Justin | GW7: 2, GW8: 6, GW9: 2, GW10: 9, GW11: 4 | LEE | Defender | 4.35 | 2.45 | 4.72 | 2.45 | 3.60 | 14.20 | 3.16 | high | 5-GW avg pts 4.60; mins 89; xGI 0.18; current GWs 11; fixture Elo diff -2 |
| Trafford | GW7: 2, GW8: 10, GW9: 2, GW10: 10, GW11: 2 | LEE | Goalkeeper | 4.30 | 3.14 | 4.25 | 2.71 | 3.59 | 14.57 | 2.86 | high | 5-GW avg pts 5.20; mins 90; xGI 0.00; current GWs 11; fixture Elo diff -2 |
| Haaland | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | MCI | Forward | 4.30 | 6.08 | 5.53 | 5.75 | 6.64 | 22.20 | 1.41 | high | 5-GW avg pts 5.40; mins 90; xGI 0.73; current GWs 11; fixture Elo diff +158 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.0m**. Current squad selling value: **£98.1m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | GW7: 4, GW8: 9, GW9: 1, GW10: 4, GW11: 6 | LIV | Defender | £6.4m | 18.58 | GW12, GW13, GW14, GW15, GW16 | — | — |
| De Cuyper | GW7: 6, GW8: 1, GW9: 9, GW10: 6, GW11: 1 | BHA | Defender | £5.5m | 16.97 | GW14, GW15, GW16 | — | — |
| Jacquet | GW7: 3, GW8: 8, GW9: 2, GW10: 4, GW11: 6 | LIV | Defender | £5.1m | 16.66 | GW12, GW13, GW15, GW16 | — | — |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | £5.2m | 16.14 | GW12, GW13, GW15 | — | — |
| Bogle | GW7: 2, GW8: 5, GW9: 1, GW10: 7, GW11: 4 | LEE | Defender | £4.8m | 15.49 | GW12, GW14 | — | — |
| Haaland | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | MCI | Forward | £15.8m | 22.20 | GW12, GW13, GW14, GW15, GW16 | GW15 | GW13, GW14, GW16 |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | £9.3m | 21.84 | GW12, GW13, GW14, GW15, GW16 | GW12, GW13 | GW15 |
| Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | BOU | Forward | £6.6m | 20.54 | GW12, GW13, GW14, GW16 | GW14, GW16 | — |
| Petrović | GW7: 6, GW8: 7, GW9: 6, GW10: 2, GW11: 6 | BOU | Goalkeeper | £4.5m | 14.27 | GW12, GW14, GW16 | — | — |
| Kinsky | GW7: 2, GW8: 9, GW9: 6, GW10: 2, GW11: 7 | TOT | Goalkeeper | £4.4m | 12.53 | GW13, GW15 | — | — |
| Groß | GW7: 5, GW8: 0, GW9: 2, GW10: 10, GW11: 4 | BHA | Midfielder | £6.3m | 20.76 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | £7.8m | 20.32 | GW12, GW13, GW14, GW15, GW16 | — | GW12 |
| Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | FUL | Midfielder | £5.4m | 19.81 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | MCI | Midfielder | £7.5m | 18.51 | GW13, GW14, GW15, GW16 | — | — |
| Slater | GW7: 1, GW8: 2, GW9: 2, GW10: 2, GW11: 3 | HUL | Midfielder | £4.5m | 10.79 | Bench | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | £8.1m | 18.96 | GW12, GW13, GW14, GW15, GW16 | — | GW15 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | FUL | Defender | £4.5m | 12.72 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | EVE | Defender | £5.5m | 12.15 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | IPS | Defender | £3.9m | 7.84 | Bench | — | — |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | HUL | Defender | £4.1m | 6.56 | Bench | — | — |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | £9.3m | 21.84 | GW12, GW13, GW14, GW15, GW16 | GW12, GW13, GW15, GW16 | GW14 |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | ARS | Forward | £7.4m | 17.53 | GW12, GW13, GW14, GW15, GW16 | — | — |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | £7.3m | 17.01 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Horníček | GW7: 2, GW8: 8, GW9: 3, GW10: 3, GW11: 1 | NEW | Goalkeeper | £5.0m | 13.37 | GW12, GW14, GW15 | — | — |
| Leno | GW7: 6, GW8: 8, GW9: 2, GW10: 3, GW11: 2 | FUL | Goalkeeper | £4.5m | 12.91 | GW13, GW16 | — | — |
| Gibbs-White | GW7: 0, GW8: 2, GW9: 2, GW10: 5, GW11: 2 | NFO | Midfielder | £7.8m | 20.32 | GW12, GW13, GW14, GW15, GW16 | GW14 | GW12, GW13, GW16 |
| Rogers | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | CHE | Midfielder | £8.3m | 18.03 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Rice | GW7: 9, GW8: 3, GW9: 8, GW10: 3, GW11: 3 | ARS | Midfielder | £7.5m | 17.31 | GW12, GW13, GW14, GW15, GW16 | — | — |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | MUN | Midfielder | £7.8m | 12.43 | GW12, GW13, GW14, GW15 | — | — |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | MCI | Midfielder | £7.8m | 10.72 | GW16 | — | — |

Squad cost: £98.8m.

## One-transfer recommendation

**Mbeumo → Groß** (projected weighted XI+captain gain 8.90).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | Groß | GW7: 5, GW8: 0, GW9: 2, GW10: 10, GW11: 4 | £7.8m | £6.3m | £2.5m | 8.90 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Groß | GW7: 5, GW8: 0, GW9: 2, GW10: 10, GW11: 4 | £7.8m | £6.3m | £2.5m | 8.90 |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | £7.8m | £5.4m | £3.4m | 7.49 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Iwobi | GW7: 11, GW8: 3, GW9: 6, GW10: 2, GW11: 1 | £7.8m | £5.4m | £3.4m | 7.49 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Virgil | GW7: 4, GW8: 9, GW9: 1, GW10: 4, GW11: 6 | £5.5m | £6.4m | £0.1m | 6.43 |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | £7.8m | £7.5m | £1.3m | 6.02 |
| Cherki | GW7: 0, GW8: 0, GW9: 1, GW10: 9, GW11: 1 | Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | £7.8m | £7.5m | £1.3m | 6.02 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | £7.2m | £6.6m | £1.6m | 5.37 |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | Jacquet | GW7: 3, GW8: 8, GW9: 2, GW10: 4, GW11: 6 | £4.1m | £5.1m | £0.0m | 5.01 |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | £7.4m | £6.6m | £1.8m | 4.85 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
