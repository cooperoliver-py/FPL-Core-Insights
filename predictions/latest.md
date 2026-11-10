# FPL predictions: 2026-2027, GW11

Last generated: 2026-11-10 16:34 UTC

Data commit: `c271f215e965990990a6c0c9d299f87da2d40626`

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
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | 6.66 | 5.31 | 5.09 | 5.31 | 5.55 | 22.56 | 3.58 | high | 5-GW avg pts 4.60; mins 86; xGI 0.52; current GWs 10; fixture Elo diff +68 |
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | 6.08 | 6.12 | 4.80 | 4.80 | 6.16 | 22.49 | 3.17 | high | 5-GW avg pts 8.80; mins 87; xGI 0.62; current GWs 10; fixture Elo diff +192 |
| Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | BOU | Forward | 5.83 | 5.46 | 5.28 | 6.89 | 3.83 | 22.08 | 3.40 | high | 5-GW avg pts 8.60; mins 83; xGI 0.82; current GWs 10; fixture Elo diff +57 |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | 5.77 | 5.72 | 5.81 | 7.11 | 6.08 | 24.18 | 2.08 | high | 5-GW avg pts 2.80; mins 72; xGI 0.45; current GWs 10; fixture Elo diff +105 |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | 5.71 | 4.31 | 4.55 | 2.63 | 5.05 | 18.09 | 3.55 | high | 5-GW avg pts 6.60; mins 90; xGI 0.26; current GWs 10; fixture Elo diff +20 |
| De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | BHA | Defender | 5.56 | 3.97 | 3.68 | 4.16 | 4.29 | 17.57 | 3.19 | high | 5-GW avg pts 7.40; mins 80; xGI 0.34; current GWs 10; fixture Elo diff +68 |
| Haaland | GW6: 6, GW7: 13, GW8: 8, GW9: 2, GW10: 2 | MCI | Forward | 5.55 | 3.95 | 5.55 | 4.97 | 5.28 | 20.19 | 1.28 | high | 5-GW avg pts 6.20; mins 88; xGI 0.60; current GWs 10; fixture Elo diff +102 |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | 5.35 | 5.05 | 5.35 | 4.75 | 3.39 | 19.53 | 2.38 | high | 5-GW avg pts 4.60; mins 89; xGI 0.32; current GWs 10; fixture Elo diff -30 |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | 5.15 | 4.98 | 5.63 | 4.66 | 5.31 | 20.58 | 2.54 | high | 5-GW avg pts 3.60; mins 82; xGI 0.39; current GWs 8; fixture Elo diff +94 |
| Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | BHA | Defender | 5.02 | 4.07 | 3.56 | 4.45 | 4.64 | 17.43 | 3.29 | high | 5-GW avg pts 7.60; mins 90; xGI 0.19; current GWs 10; fixture Elo diff +68 |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | 5.00 | 4.99 | 5.45 | 4.73 | 4.99 | 20.16 | 2.17 | high | 5-GW avg pts 5.60; mins 67; xGI 0.31; current GWs 10; fixture Elo diff +94 |
| Doku | GW6: 12, GW7: 6, GW8: 2, GW9: 2, GW10: 2 | MCI | Midfielder | 4.89 | 3.39 | 4.89 | 4.48 | 4.69 | 17.81 | 2.37 | high | 5-GW avg pts 4.80; mins 76; xGI 0.40; current GWs 10; fixture Elo diff +102 |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | MCI | Midfielder | 4.86 | 3.42 | 4.86 | 4.18 | 4.78 | 17.61 | 2.23 | high | 5-GW avg pts 4.00; mins 52; xGI 0.30; current GWs 10; fixture Elo diff +102 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | 4.69 | 5.09 | 4.71 | 5.63 | 5.01 | 19.98 | 2.53 | high | 5-GW avg pts 4.20; mins 88; xGI 0.41; current GWs 10; fixture Elo diff +105 |
| Tavernier | GW6: 1, GW7: 10, GW8: 10, GW9: 3, GW10: 3 | BOU | Midfielder | 4.67 | 4.36 | 4.39 | 5.01 | 2.73 | 17.24 | 2.57 | high | 5-GW avg pts 5.40; mins 83; xGI 0.61; current GWs 10; fixture Elo diff +57 |
| Verbruggen | GW6: 9, GW7: 6, GW8: 2, GW9: 11, GW10: 6 | BHA | Goalkeeper | 4.65 | 3.93 | 3.61 | 3.90 | 4.00 | 16.20 | 3.52 | high | 5-GW avg pts 6.80; mins 90; xGI 0.00; current GWs 10; fixture Elo diff +68 |
| Wirtz | GW6: 2, GW7: 5, GW8: 6, GW9: 2, GW10: 13 | LIV | Midfielder | 4.57 | 4.61 | 4.90 | 4.42 | 4.43 | 18.39 | 2.55 | high | 5-GW avg pts 5.60; mins 78; xGI 0.33; current GWs 10; fixture Elo diff +94 |
| Ndiaye | GW6: 1, GW7: 5, GW8: 5, GW9: 2, GW10: 2 | MCI | Midfielder | 4.55 | 3.01 | 4.55 | 3.77 | 4.29 | 16.11 | 2.78 | high | 5-GW avg pts 3.00; mins 76; xGI 0.38; current GWs 10; fixture Elo diff +102 |
| Kudus | GW6: 3, GW7: 6, GW8: 3, GW9: 7, GW10: 2 | TOT | Midfielder | 4.55 | 4.14 | 4.18 | 2.66 | 4.25 | 16.03 | 2.43 | high | 5-GW avg pts 4.20; mins 82; xGI 0.32; current GWs 10; fixture Elo diff +20 |
| Palmer | GW6: 8, GW7: 2, GW8: -1, GW9: 8, GW10: 2 | CHE | Midfielder | 4.54 | 4.38 | 4.54 | 3.95 | 2.87 | 16.60 | 1.69 | high | 5-GW avg pts 3.80; mins 87; xGI 0.33; current GWs 10; fixture Elo diff -30 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.3m**. Current squad selling value: **£98.7m**. Total available funds: **£99.0m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | £5.1m | 18.09 | GW11, GW12, GW13, GW15 | — | — |
| De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | BHA | Defender | £5.5m | 17.57 | GW11, GW13, GW14, GW15 | — | — |
| Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | LEE | Defender | £5.1m | 17.04 | GW12, GW14 | — | GW12 |
| Maatsen | GW6: 0, GW7: 0, GW8: 2, GW9: 2, GW10: 0 | AVL | Defender | £4.4m | 15.63 | GW11, GW13, GW15 | — | — |
| Bogle | GW6: 1, GW7: 2, GW8: 5, GW9: 1, GW10: 7 | LEE | Defender | £4.8m | 15.57 | GW12, GW14 | — | — |
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | £7.1m | 22.49 | GW11, GW12, GW13, GW14, GW15 | GW12, GW15 | GW11 |
| Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | BOU | Forward | £6.5m | 22.08 | GW11, GW12, GW13, GW14 | — | GW14 |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 20.16 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Verbruggen | GW6: 9, GW7: 6, GW8: 2, GW9: 11, GW10: 6 | BHA | Goalkeeper | £4.6m | 16.20 | GW11, GW12, GW14, GW15 | — | — |
| Sels | GW6: 2, GW7: 2, GW8: 2, GW9: 1, GW10: 2 | NFO | Goalkeeper | £5.0m | 13.30 | GW13 | — | — |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | £11.6m | 24.18 | GW11, GW12, GW13, GW14, GW15 | GW14 | GW13, GW15 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | £6.3m | 22.56 | GW11, GW12, GW13, GW14, GW15 | GW11 | — |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 20.70 | GW12, GW13, GW14, GW15 | GW13 | — |
| Barcola | GW6: 2, GW7: 4, GW8: 6, GW9: 1, GW10: 5 | LIV | Midfielder | £8.1m | 20.58 | GW11, GW13, GW15 | — | — |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | £7.9m | 19.98 | GW11, GW12, GW14, GW15 | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | £8.1m | 16.08 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Bassey | GW6: 2, GW7: 8, GW8: 8, GW9: 1, GW10: 2 | FUL | Defender | £4.5m | 12.55 | GW12, GW13, GW14, GW15 | — | — |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | EVE | Defender | £5.5m | 12.26 | GW11, GW12, GW14, GW15 | — | — |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | HUL | Defender | £4.1m | 10.67 | GW11, GW13 | — | — |
| Furlong | GW6: 0, GW7: 0, GW8: 0, GW9: 0, GW10: 0 | IPS | Defender | £3.9m | 0.57 | Bench | — | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.3m | 20.16 | GW11, GW12, GW13, GW14, GW15 | — | GW11, GW13 |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | ARS | Forward | £7.4m | 12.25 | GW11, GW12, GW13, GW15 | — | — |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | BRE | Forward | £7.8m | 4.63 | GW14 | — | — |
| Horníček | GW6: 0, GW7: 2, GW8: 8, GW9: 3, GW10: 3 | NEW | Goalkeeper | £5.0m | 12.53 | GW14, GW15 | — | — |
| Leno | GW6: 2, GW7: 6, GW8: 8, GW9: 2, GW10: 3 | FUL | Goalkeeper | £4.5m | 12.32 | GW11, GW12, GW13 | — | — |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 20.70 | GW11, GW12, GW13, GW14, GW15 | GW12, GW13, GW15 | GW14 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | £7.9m | 19.98 | GW11, GW12, GW13, GW14, GW15 | GW14 | GW12, GW15 |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | £8.2m | 19.53 | GW11, GW12, GW13, GW14, GW15 | GW11 | — |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | MCI | Midfielder | £7.9m | 17.61 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | ARS | Midfielder | £7.5m | 14.38 | GW11, GW12, GW13, GW14, GW15 | — | — |

Squad cost: £99.4m.

## One-transfer recommendation

**Thiago → N.Jackson** (projected weighted XI+captain gain 12.14).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | £7.8m | £7.1m | £1.0m | 12.14 |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | £7.4m | £7.1m | £0.6m | 12.11 |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | £7.8m | £6.5m | £1.6m | 11.18 |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | £7.4m | £6.5m | £1.2m | 11.15 |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.4m | £6.3m | £1.4m | 9.90 |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | £7.8m | £6.3m | £1.8m | 6.67 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | £5.5m | £5.1m | £0.7m | 6.05 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | £5.5m | £5.5m | £0.3m | 5.38 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | £5.5m | £5.1m | £0.7m | 5.32 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | £5.5m | £5.3m | £0.5m | 5.03 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
