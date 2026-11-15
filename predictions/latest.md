# FPL predictions: 2026-2027, GW11

Last generated: 2026-11-15 21:10 UTC

Data commit: `5d073f8afa20d4f5dd57256add6bdbb0da4ef891`

## Data freshness

All scheduled Premier League fixtures before GW11 are complete.

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

Ranked by recorded FPL points in GW6–GW10. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Konsa | ARS | Defender | GW6: 4, GW7: 9, GW8: 14, GW9: 10, GW10: 8 | 45 | 9.00 | 5 |
| N.Jackson | AVL | Forward | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | 44 | 8.80 | 5 |
| Evanilson | BOU | Forward | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | 43 | 8.60 | 5 |
| Gabriel | ARS | Defender | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | 41 | 8.20 | 5 |
| Vuskovic | BHA | Defender | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | 38 | 7.60 | 5 |
| De Cuyper | BHA | Defender | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | 37 | 7.40 | 5 |
| Barry | EVE | Forward | GW6: 6, GW7: 2, GW8: 2, GW9: 9, GW10: 16 | 35 | 7.00 | 5 |
| Verbruggen | BHA | Goalkeeper | GW6: 9, GW7: 6, GW8: 2, GW9: 11, GW10: 6 | 34 | 6.80 | 5 |
| Van Hecke | TOT | Defender | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | 33 | 6.60 | 5 |
| Haaland | MCI | Forward | GW6: 6, GW7: 13, GW8: 8, GW9: 2, GW10: 2 | 31 | 6.20 | 5 |
| Ayari | BHA | Midfielder | GW6: 3, GW7: 13, GW8: 2, GW9: 10, GW10: 3 | 31 | 6.20 | 5 |
| Raya | ARS | Goalkeeper | GW6: 3, GW7: 9, GW8: 7, GW9: 5, GW10: 6 | 30 | 6.00 | 5 |
| Rice | ARS | Midfielder | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | 30 | 6.00 | 5 |
| Dewsbury-Hall | EVE | Midfielder | GW6: 13, GW7: 2, GW8: 2, GW9: 4, GW10: 9 | 30 | 6.00 | 5 |
| Hill | BOU | Defender | GW6: 2, GW7: 7, GW8: 11, GW9: 6, GW10: 4 | 30 | 6.00 | 5 |
| Muharemović | LEE | Defender | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | 29 | 5.80 | 5 |
| Isak | LIV | Forward | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | 28 | 5.60 | 5 |
| Calafiori | ARS | Defender | GW6: 9, GW7: 6, GW8: 1, GW9: 6, GW10: 6 | 28 | 5.60 | 5 |
| E.Le Fée | SUN | Midfielder | GW6: 2, GW7: 4, GW8: 3, GW9: 8, GW10: 11 | 28 | 5.60 | 5 |
| Wirtz | LIV | Midfielder | GW6: 2, GW7: 5, GW8: 6, GW9: 2, GW10: 13 | 28 | 5.60 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW11 player forecasts

| Player | Last 5 GW points | Club | Pos | GW11 | GW12 | GW13 | GW14 | GW15 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | 6.76 | 5.01 | 4.81 | 5.04 | 5.26 | 21.81 | 3.46 | high | 5-GW avg pts 4.60; mins 86; xGI 0.52; current GWs 10; fixture Elo diff +68 |
| De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | BHA | Defender | 5.97 | 3.80 | 3.72 | 4.20 | 4.19 | 17.83 | 3.24 | high | 5-GW avg pts 7.40; mins 80; xGI 0.34; current GWs 10; fixture Elo diff +68 |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | 5.74 | 4.30 | 4.53 | 2.65 | 5.09 | 18.14 | 3.56 | high | 5-GW avg pts 6.60; mins 90; xGI 0.26; current GWs 10; fixture Elo diff +20 |
| Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | BOU | Forward | 5.63 | 5.37 | 5.11 | 6.91 | 3.67 | 21.59 | 3.32 | high | 5-GW avg pts 8.60; mins 83; xGI 0.82; current GWs 10; fixture Elo diff +57 |
| Haaland | GW6: 6, GW7: 13, GW8: 8, GW9: 2, GW10: 2 | MCI | Forward | 5.60 | 4.01 | 5.60 | 5.19 | 5.37 | 20.55 | 1.30 | high | 5-GW avg pts 6.20; mins 88; xGI 0.60; current GWs 10; fixture Elo diff +102 |
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | 5.56 | 6.00 | 4.28 | 4.28 | 5.93 | 20.93 | 2.95 | high | 5-GW avg pts 8.80; mins 87; xGI 0.62; current GWs 10; fixture Elo diff +192 |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | 5.28 | 5.16 | 5.32 | 6.61 | 5.56 | 22.15 | 1.91 | high | 5-GW avg pts 2.80; mins 72; xGI 0.45; current GWs 10; fixture Elo diff +105 |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | 5.26 | 5.11 | 5.26 | 4.68 | 3.42 | 19.39 | 2.36 | high | 5-GW avg pts 4.60; mins 89; xGI 0.32; current GWs 10; fixture Elo diff -30 |
| Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | BHA | Defender | 5.15 | 3.98 | 3.61 | 4.41 | 4.47 | 17.39 | 3.28 | high | 5-GW avg pts 7.60; mins 90; xGI 0.19; current GWs 10; fixture Elo diff +68 |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | 4.96 | 4.88 | 5.42 | 4.53 | 5.10 | 19.92 | 2.46 | high | 5-GW avg pts 3.60; mins 82; xGI 0.39; current GWs 8; fixture Elo diff +94 |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | 4.88 | 4.83 | 5.39 | 4.56 | 4.91 | 19.68 | 2.12 | high | 5-GW avg pts 5.60; mins 67; xGI 0.31; current GWs 10; fixture Elo diff +94 |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | MCI | Midfielder | 4.78 | 3.38 | 4.78 | 4.17 | 4.67 | 17.36 | 2.20 | high | 5-GW avg pts 4.00; mins 52; xGI 0.30; current GWs 10; fixture Elo diff +102 |
| Doku | GW6: 12, GW7: 6, GW8: 2, GW9: 2, GW10: 2 | MCI | Midfielder | 4.66 | 3.15 | 4.66 | 4.23 | 4.42 | 16.83 | 2.24 | high | 5-GW avg pts 4.80; mins 76; xGI 0.40; current GWs 10; fixture Elo diff +102 |
| Tavernier | GW6: 1, GW7: 10, GW8: 10, GW9: 3, GW10: 3 | BOU | Midfielder | 4.56 | 4.34 | 4.31 | 5.08 | 2.63 | 17.05 | 2.55 | high | 5-GW avg pts 5.40; mins 83; xGI 0.61; current GWs 10; fixture Elo diff +57 |
| Palmer | GW6: 8, GW7: 2, GW8: -1, GW9: 8, GW10: 2 | CHE | Midfielder | 4.55 | 4.40 | 4.55 | 3.98 | 2.87 | 16.65 | 1.70 | high | 5-GW avg pts 3.80; mins 87; xGI 0.33; current GWs 10; fixture Elo diff -30 |
| Kudus | GW6: 3, GW7: 6, GW8: 3, GW9: 7, GW10: 2 | TOT | Midfielder | 4.55 | 4.16 | 4.18 | 2.66 | 4.27 | 16.06 | 2.43 | high | 5-GW avg pts 4.20; mins 82; xGI 0.32; current GWs 10; fixture Elo diff +20 |
| Verbruggen | GW6: 9, GW7: 6, GW8: 2, GW9: 11, GW10: 6 | BHA | Goalkeeper | 4.52 | 3.62 | 3.36 | 3.67 | 3.71 | 15.26 | 3.25 | high | 5-GW avg pts 6.80; mins 90; xGI 0.00; current GWs 10; fixture Elo diff +68 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | 4.50 | 4.88 | 4.52 | 5.58 | 4.79 | 19.28 | 2.44 | high | 5-GW avg pts 4.20; mins 88; xGI 0.41; current GWs 10; fixture Elo diff +105 |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | 4.45 | 5.10 | 6.35 | 5.15 | 5.24 | 20.86 | 2.67 | high | 5-GW avg pts 2.20; mins 72; xGI 0.38; current GWs 10; fixture Elo diff +59 |
| Tonali | GW6: 7, GW7: 4, GW8: 5, GW9: 3, GW10: 1 | TOT | Midfielder | 4.42 | 3.88 | 4.02 | 2.79 | 4.24 | 15.63 | 2.95 | high | 5-GW avg pts 4.00; mins 90; xGI 0.18; current GWs 10; fixture Elo diff +20 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.3m**. Current squad selling value: **£98.7m**. Total available funds: **£99.0m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£1.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | £5.1m | 18.14 | GW11, GW12, GW13, GW15 | — | — |
| De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | BHA | Defender | £5.5m | 17.83 | GW11, GW13, GW15 | — | GW11 |
| Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | BHA | Defender | £5.3m | 17.39 | GW11, GW13, GW14, GW15 | — | — |
| Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | LEE | Defender | £5.1m | 17.24 | GW12, GW14 | — | GW12 |
| Bogle | GW6: 1, GW7: 2, GW8: 5, GW9: 1, GW10: 7 | LEE | Defender | £4.8m | 16.10 | GW12, GW14 | — | — |
| Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | BOU | Forward | £6.5m | 21.59 | GW11, GW12, GW13, GW14 | GW14 | — |
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | £7.1m | 20.93 | GW11, GW12, GW15 | GW12, GW15 | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 19.68 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Donnarumma | GW6: 9, GW7: 1, GW8: 1, GW9: 2, GW10: 1 | MCI | Goalkeeper | £5.4m | 15.21 | GW11, GW13, GW14, GW15 | — | — |
| Roefs | GW6: 1, GW7: 2, GW8: 9, GW9: 1, GW10: 9 | SUN | Goalkeeper | £4.8m | 13.10 | GW12 | — | — |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | £11.6m | 22.15 | GW11, GW12, GW13, GW14, GW15 | — | GW14, GW15 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | £6.3m | 21.81 | GW11, GW12, GW13, GW14, GW15 | GW11 | — |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 20.86 | GW11, GW12, GW13, GW14, GW15 | GW13 | — |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | £8.1m | 19.92 | GW11, GW12, GW13, GW14, GW15 | — | GW13 |
| Iwobi | GW6: 4, GW7: 11, GW8: 3, GW9: 6, GW10: 2 | FUL | Midfielder | £5.4m | 18.07 | GW13, GW14, GW15 | — | — |

Squad cost: £98.1m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | £8.1m | 16.25 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Bassey | GW6: 2, GW7: 8, GW8: 8, GW9: 1, GW10: 2 | FUL | Defender | £4.5m | 12.65 | GW12, GW13, GW14, GW15 | — | — |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | EVE | Defender | £5.5m | 12.17 | GW11, GW12, GW14, GW15 | — | — |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | HUL | Defender | £4.1m | 10.82 | GW11, GW13 | — | — |
| Furlong | GW6: 0, GW7: 0, GW8: 0, GW9: 0, GW10: 0 | IPS | Defender | £3.9m | 0.56 | Bench | — | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 19.68 | GW11, GW12, GW13, GW14, GW15 | — | GW11, GW13, GW15 |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | ARS | Forward | £7.4m | 12.28 | GW11, GW12, GW13, GW15 | — | — |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | BRE | Forward | £7.8m | 4.32 | GW14 | — | — |
| Horníček | GW6: 0, GW7: 2, GW8: 8, GW9: 3, GW10: 3 | NEW | Goalkeeper | £5.0m | 12.69 | GW12, GW14, GW15 | — | — |
| Leno | GW6: 2, GW7: 6, GW8: 8, GW9: 2, GW10: 3 | FUL | Goalkeeper | £4.5m | 12.37 | GW11, GW13 | — | — |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 20.86 | GW11, GW12, GW13, GW14, GW15 | GW13, GW15 | GW12, GW14 |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | £8.2m | 19.39 | GW11, GW12, GW13, GW14, GW15 | GW11, GW12 | — |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | £7.9m | 19.28 | GW11, GW12, GW13, GW14, GW15 | GW14 | — |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | MCI | Midfielder | £7.9m | 17.36 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | ARS | Midfielder | £7.5m | 14.34 | GW11, GW12, GW13, GW14, GW15 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Havertz → Evanilson** (projected weighted XI+captain gain 10.70).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | £7.4m | £6.5m | £1.2m | 10.70 |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | £7.8m | £6.5m | £1.6m | 10.70 |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | £7.4m | £7.1m | £0.6m | 10.02 |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | £7.8m | £7.1m | £1.0m | 10.02 |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.4m | £6.3m | £1.4m | 8.99 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | £5.5m | £5.1m | £0.7m | 6.28 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | £5.5m | £5.5m | £0.3m | 6.19 |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.8m | £6.3m | £1.8m | 5.96 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | £5.5m | £5.1m | £0.7m | 5.68 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | £5.5m | £5.3m | £0.5m | 5.04 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
