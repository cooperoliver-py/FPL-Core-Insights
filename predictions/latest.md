# FPL predictions: 2026-2027, GW11

Last generated: 2026-11-08 20:42 UTC

Data commit: `78510456b04837e388977f780a6a21962d3ebaf8`

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
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | 5.81 | 5.69 | 5.03 | 5.03 | 5.66 | 21.88 | 3.08 | high | 5-GW avg pts 8.80; mins 87; xGI 0.62; current GWs 10; fixture Elo diff +192 |
| Haaland | GW6: 6, GW7: 13, GW8: 8, GW9: 2, GW10: 2 | MCI | Forward | 5.77 | 4.29 | 5.77 | 5.32 | 5.67 | 21.37 | 1.35 | high | 5-GW avg pts 6.20; mins 88; xGI 0.60; current GWs 10; fixture Elo diff +102 |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | 5.72 | 5.18 | 5.81 | 5.15 | 3.60 | 20.80 | 2.54 | high | 5-GW avg pts 4.60; mins 89; xGI 0.39; current GWs 10; fixture Elo diff -30 |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | 5.58 | 5.23 | 5.58 | 6.26 | 6.72 | 23.16 | 2.86 | high | 5-GW avg pts 8.20; mins 90; xGI 0.20; current GWs 10; fixture Elo diff +205 |
| De Cuyper | GW6: 15, GW7: 6, GW8: 1, GW9: 9, GW10: 6 | BHA | Defender | 4.92 | 3.43 | 3.43 | 3.83 | 3.78 | 15.70 | 2.91 | high | 5-GW avg pts 7.40; mins 80; xGI 0.35; current GWs 10; fixture Elo diff +68 |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | 4.79 | 4.38 | 4.91 | 4.36 | 4.69 | 18.53 | 2.01 | high | 5-GW avg pts 5.60; mins 67; xGI 0.32; current GWs 10; fixture Elo diff +94 |
| Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | BHA | Defender | 4.76 | 3.54 | 3.39 | 4.10 | 4.35 | 16.14 | 3.10 | high | 5-GW avg pts 7.60; mins 90; xGI 0.19; current GWs 10; fixture Elo diff +68 |
| Doku | GW6: 12, GW7: 6, GW8: 2, GW9: 2, GW10: 2 | MCI | Midfielder | 4.75 | 3.88 | 4.75 | 4.50 | 4.71 | 18.03 | 2.40 | high | 5-GW avg pts 4.80; mins 76; xGI 0.40; current GWs 10; fixture Elo diff +102 |
| Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | BOU | Forward | 4.69 | 4.28 | 4.34 | 5.21 | 3.21 | 17.58 | 2.70 | high | 5-GW avg pts 8.60; mins 83; xGI 0.82; current GWs 10; fixture Elo diff +57 |
| Tonali | GW6: 7, GW7: 4, GW8: 5, GW9: 3, GW10: 1 | TOT | Midfielder | 4.55 | 4.01 | 3.81 | 2.51 | 4.48 | 15.66 | 2.95 | high | 5-GW avg pts 4.00; mins 90; xGI 0.18; current GWs 10; fixture Elo diff +20 |
| Verbruggen | GW6: 9, GW7: 6, GW8: 2, GW9: 11, GW10: 6 | BHA | Goalkeeper | 4.49 | 3.18 | 3.11 | 3.45 | 3.57 | 14.40 | 3.13 | high | 5-GW avg pts 6.80; mins 90; xGI 0.00; current GWs 10; fixture Elo diff +68 |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | MCI | Midfielder | 4.45 | 3.54 | 4.45 | 4.29 | 4.43 | 16.86 | 2.13 | high | 5-GW avg pts 4.00; mins 52; xGI 0.30; current GWs 10; fixture Elo diff +102 |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | 4.43 | 4.39 | 3.89 | 2.47 | 4.64 | 16.00 | 3.20 | high | 5-GW avg pts 6.60; mins 90; xGI 0.26; current GWs 10; fixture Elo diff +20 |
| B.Fernandes | GW6: 1, GW7: 1, GW8: 0, GW9: 2, GW10: 10 | MUN | Midfielder | 4.38 | 4.56 | 4.40 | 5.11 | 4.76 | 18.44 | 1.59 | high | 5-GW avg pts 2.80; mins 72; xGI 0.39; current GWs 10; fixture Elo diff +105 |
| Groß | GW6: 6, GW7: 5, GW8: 0, GW9: 2, GW10: 10 | BHA | Midfielder | 4.38 | 3.81 | 3.69 | 4.03 | 4.04 | 16.00 | 2.54 | high | 5-GW avg pts 4.60; mins 86; xGI 0.52; current GWs 10; fixture Elo diff +68 |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | 4.37 | 4.84 | 5.51 | 4.70 | 5.32 | 19.62 | 2.52 | high | 5-GW avg pts 2.20; mins 72; xGI 0.38; current GWs 10; fixture Elo diff +59 |
| Gomez | GW6: 5, GW7: 8, GW8: 2, GW9: 3, GW10: 9 | BHA | Midfielder | 4.36 | 3.77 | 3.45 | 3.82 | 4.20 | 15.71 | 3.14 | high | 5-GW avg pts 5.40; mins 88; xGI 0.19; current GWs 10; fixture Elo diff +68 |
| Ndiaye | GW6: 1, GW7: 5, GW8: 5, GW9: 2, GW10: 2 | MCI | Midfielder | 4.32 | 3.15 | 4.32 | 4.00 | 4.09 | 15.86 | 2.73 | high | 5-GW avg pts 3.00; mins 76; xGI 0.38; current GWs 10; fixture Elo diff +102 |
| Tavernier | GW6: 1, GW7: 10, GW8: 10, GW9: 3, GW10: 3 | BOU | Midfielder | 4.32 | 3.97 | 4.19 | 4.68 | 2.99 | 16.31 | 2.43 | high | 5-GW avg pts 5.40; mins 83; xGI 0.61; current GWs 10; fixture Elo diff +57 |
| Kudus | GW6: 3, GW7: 6, GW8: 3, GW9: 7, GW10: 2 | TOT | Midfielder | 4.30 | 3.73 | 4.08 | 3.08 | 3.99 | 15.47 | 2.34 | high | 5-GW avg pts 4.20; mins 82; xGI 0.32; current GWs 10; fixture Elo diff +20 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.3m**. Current squad selling value: **£98.7m**. Total available funds: **£99.0m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | £8.1m | 23.16 | GW11, GW12, GW13, GW14, GW15 | GW14, GW15 | — |
| Murillo | GW6: 2, GW7: 2, GW8: 1, GW9: 3, GW10: 4 | NFO | Defender | £5.5m | 17.28 | GW12, GW13, GW14, GW15 | — | — |
| Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | LEE | Defender | £5.1m | 16.23 | GW12, GW14 | — | GW12 |
| Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | BHA | Defender | £5.2m | 16.14 | GW11, GW14, GW15 | — | — |
| Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | TOT | Defender | £5.0m | 16.00 | GW11, GW12, GW13, GW15 | — | — |
| N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | AVL | Forward | £7.1m | 21.88 | GW11, GW12, GW13, GW14, GW15 | GW11, GW12 | — |
| Haaland | GW6: 6, GW7: 13, GW8: 8, GW9: 2, GW10: 2 | MCI | Forward | £15.8m | 21.37 | GW11, GW12, GW13, GW14, GW15 | — | GW11, GW13, GW14, GW15 |
| Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | BOU | Forward | £6.5m | 17.58 | GW11, GW12, GW13, GW14 | — | — |
| Kinsky | GW6: 3, GW7: 2, GW8: 9, GW9: 6, GW10: 2 | TOT | Goalkeeper | £4.4m | 13.87 | GW11, GW13, GW15 | — | — |
| Trafford | GW6: 2, GW7: 2, GW8: 10, GW9: 2, GW10: 10 | LEE | Goalkeeper | £5.0m | 13.11 | GW12, GW14 | — | — |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | £8.2m | 20.80 | GW11, GW12, GW13, GW14 | GW13 | — |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 19.62 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Mac Allister | GW6: 2, GW7: 1, GW8: 3, GW9: 1, GW10: 8 | LIV | Midfielder | £5.4m | 16.42 | GW12, GW13, GW15 | — | — |
| Gomez | GW6: 5, GW7: 8, GW8: 2, GW9: 3, GW10: 9 | BHA | Midfielder | £5.0m | 15.71 | GW11, GW14, GW15 | — | — |
| Tonali | GW6: 7, GW7: 4, GW8: 5, GW9: 3, GW10: 1 | TOT | Midfielder | £5.3m | 15.66 | GW11, GW13, GW15 | — | — |

Squad cost: £99.4m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW6: 2, GW7: 8, GW8: 17, GW9: 6, GW10: 8 | ARS | Defender | £8.1m | 23.16 | GW11, GW12, GW13, GW14, GW15 | GW12, GW14, GW15 | GW11, GW13 |
| Bassey | GW6: 2, GW7: 8, GW8: 8, GW9: 1, GW10: 2 | FUL | Defender | £4.5m | 12.81 | GW12, GW13, GW14, GW15 | — | — |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | EVE | Defender | £5.5m | 11.84 | GW11, GW12, GW14 | — | — |
| Egan | GW6: 1, GW7: 4, GW8: 4, GW9: 1, GW10: 2 | HUL | Defender | £4.1m | 11.18 | GW11, GW13, GW15 | — | — |
| Furlong | GW6: 0, GW7: 0, GW8: 0, GW9: 0, GW10: 0 | IPS | Defender | £3.9m | 0.54 | Bench | — | — |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | LIV | Forward | £9.2m | 18.53 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | ARS | Forward | £7.4m | 13.44 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | BRE | Forward | £7.8m | 3.76 | Bench | — | — |
| Horníček | GW6: 0, GW7: 2, GW8: 8, GW9: 3, GW10: 3 | NEW | Goalkeeper | £5.0m | 12.47 | GW11, GW12, GW14, GW15 | — | — |
| Leno | GW6: 2, GW7: 6, GW8: 8, GW9: 2, GW10: 3 | FUL | Goalkeeper | £4.5m | 11.83 | GW13 | — | — |
| Rogers | GW6: 9, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | CHE | Midfielder | £8.2m | 20.80 | GW11, GW12, GW13, GW14, GW15 | GW11, GW13 | GW12, GW14 |
| Gibbs-White | GW6: 2, GW7: 0, GW8: 2, GW9: 2, GW10: 5 | NFO | Midfielder | £7.8m | 19.62 | GW11, GW12, GW13, GW14, GW15 | — | GW15 |
| Mbeumo | GW6: 8, GW7: 8, GW8: 2, GW9: 1, GW10: 2 | MUN | Midfielder | £7.9m | 17.17 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Cherki | GW6: 10, GW7: 0, GW8: 0, GW9: 1, GW10: 9 | MCI | Midfielder | £7.9m | 16.86 | GW11, GW12, GW13, GW14, GW15 | — | — |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | ARS | Midfielder | £7.5m | 13.64 | GW11, GW12, GW13, GW14, GW15 | — | — |

Squad cost: £99.3m.

## One-transfer recommendation

**Thiago → N.Jackson** (projected weighted XI+captain gain 9.57).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | £7.8m | £7.1m | £1.0m | 9.57 |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | £7.4m | £7.1m | £0.6m | 8.94 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Murillo | GW6: 2, GW7: 2, GW8: 1, GW9: 3, GW10: 4 | £5.5m | £5.5m | £0.3m | 5.24 |
| Thiago | GW6: 4, GW7: 4, GW8: 5, GW9: 9, GW10: -2 | Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | £7.8m | £6.5m | £1.6m | 5.01 |
| Rice | GW6: 7, GW7: 9, GW8: 3, GW9: 8, GW10: 3 | Doku | GW6: 12, GW7: 6, GW8: 2, GW9: 2, GW10: 2 | £7.4m | £7.5m | £0.2m | 4.39 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Muharemović | GW6: 2, GW7: 5, GW8: 9, GW9: 3, GW10: 10 | £5.5m | £5.1m | £0.7m | 4.23 |
| Havertz | GW6: 2, GW7: 2, GW8: 1, GW9: 9, GW10: 2 | Evanilson | GW6: 7, GW7: 12, GW8: 6, GW9: 9, GW10: 9 | £7.4m | £6.5m | £1.2m | 4.15 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Vuskovic | GW6: 8, GW7: 11, GW8: 1, GW9: 6, GW10: 12 | £5.5m | £5.2m | £0.6m | 4.11 |
| Branthwaite | GW6: 3, GW7: 1, GW8: 0, GW9: 9, GW10: 3 | Van Hecke | GW6: 3, GW7: 4, GW8: 7, GW9: 15, GW10: 4 | £5.5m | £5.0m | £0.8m | 4.05 |
| Isak | GW6: 0, GW7: 9, GW8: 9, GW9: 2, GW10: 8 | N.Jackson | GW6: 9, GW7: 2, GW8: 13, GW9: 9, GW10: 11 | £9.2m | £7.1m | £2.4m | 3.85 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
