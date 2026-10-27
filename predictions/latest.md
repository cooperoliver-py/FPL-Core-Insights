# FPL predictions: 2026-2027, GW9

Last generated: 2026-10-27 05:25 UTC

Data commit: `8c890d37c2fabfe5548f18c2bb347c3cfc96e091`

## Data freshness

All scheduled Premier League fixtures before GW9 are complete.

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

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top 20 players over the last 5 Gameweeks

Ranked by recorded FPL points in GW4–GW8. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Groß | BHA | Midfielder | GW4: 17, GW5: 14, GW6: 6, GW7: 5, GW8: 0 | 42 | 8.40 | 5 |
| Haaland | MCI | Forward | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | 42 | 8.40 | 5 |
| De Cuyper | BHA | Defender | GW4: 11, GW5: 6, GW6: 15, GW7: 6, GW8: 1 | 39 | 7.80 | 5 |
| Gabriel | ARS | Defender | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | 37 | 7.40 | 5 |
| Kostoulas | BHA | Forward | GW4: 10, GW5: 10, GW6: 1, GW7: 12, GW8: 2 | 35 | 7.00 | 5 |
| Raya | ARS | Goalkeeper | GW4: 14, GW5: 1, GW6: 3, GW7: 9, GW8: 7 | 34 | 6.80 | 5 |
| Konsa | ARS | Defender | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | 34 | 6.80 | 5 |
| Vuskovic | BHA | Defender | GW4: 6, GW5: 8, GW6: 8, GW7: 11, GW8: 1 | 34 | 6.80 | 5 |
| Evanilson | BOU | Forward | GW4: 5, GW5: 2, GW6: 7, GW7: 12, GW8: 6 | 32 | 6.40 | 5 |
| Tavernier | BOU | Midfielder | GW4: 8, GW5: 2, GW6: 1, GW7: 10, GW8: 10 | 31 | 6.20 | 5 |
| Verbruggen | BHA | Goalkeeper | GW4: 8, GW5: 6, GW6: 9, GW7: 6, GW8: 2 | 31 | 6.20 | 5 |
| Manzambi | AVL | Midfielder | GW4: 1, GW5: 13, GW6: 5, GW7: 11, GW8: 1 | 31 | 6.20 | 5 |
| Bassey | FUL | Defender | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | 30 | 6.00 | 5 |
| N.Jackson | AVL | Forward | GW4: 0, GW5: 6, GW6: 9, GW7: 2, GW8: 13 | 30 | 6.00 | 5 |
| Virgil | LIV | Defender | GW4: 8, GW5: 8, GW6: 0, GW7: 4, GW8: 9 | 29 | 5.80 | 5 |
| McGinn | AVL | Midfielder | GW4: 6, GW5: 6, GW6: 10, GW7: 1, GW8: 6 | 29 | 5.80 | 5 |
| Ayari | BHA | Midfielder | GW4: 8, GW5: 3, GW6: 3, GW7: 13, GW8: 2 | 29 | 5.80 | 5 |
| Muharemović | LEE | Defender | GW4: 7, GW5: 6, GW6: 2, GW7: 5, GW8: 9 | 29 | 5.80 | 5 |
| Belloumi | HUL | Midfielder | GW4: 13, GW5: 4, GW6: 6, GW7: 2, GW8: 4 | 29 | 5.80 | 5 |
| Jacquet | LIV | Defender | GW4: 9, GW5: 6, GW6: 3, GW7: 3, GW8: 8 | 29 | 5.80 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW9 player forecasts

| Player | Last 5 GW points | Club | Pos | GW9 | GW10 | GW11 | GW12 | GW13 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | MCI | Forward | 6.31 | 6.57 | 7.24 | 3.60 | 7.13 | 24.81 | 1.58 | high | 5-GW avg pts 8.40; mins 88; xGI 0.78; current GWs 8; fixture Elo diff +103 |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | 5.21 | 6.94 | 5.28 | 4.99 | 5.28 | 22.35 | 2.83 | high | 5-GW avg pts 7.40; mins 90; xGI 0.24; current GWs 8; fixture Elo diff +246 |
| Thiago | GW4: 1, GW5: 5, GW6: 4, GW7: 4, GW8: 5 | BRE | Forward | 4.72 | 4.48 | 4.77 | 3.94 | 2.91 | 17.07 | 2.19 | high | 5-GW avg pts 3.80; mins 90; xGI 0.53; current GWs 8; fixture Elo diff -53 |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | 4.60 | 5.44 | 5.55 | 5.49 | 5.55 | 21.11 | 2.64 | high | 5-GW avg pts 4.40; mins 89; xGI 0.24; current GWs 8; fixture Elo diff +16 |
| Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | BOU | Defender | 4.60 | 5.08 | 4.45 | 4.43 | 3.91 | 18.19 | 3.31 | high | 5-GW avg pts 5.20; mins 90; xGI 0.04; current GWs 8; fixture Elo diff +89 |
| Mbeumo | GW4: 2, GW5: 2, GW6: 8, GW7: 8, GW8: 2 | MUN | Midfielder | 4.55 | 4.63 | 4.51 | 4.64 | 4.54 | 18.29 | 2.32 | high | 5-GW avg pts 4.40; mins 90; xGI 0.48; current GWs 8; fixture Elo diff +48 |
| Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | BOU | Defender | 4.51 | 5.03 | 4.58 | 4.25 | 4.17 | 18.18 | 3.64 | high | 5-GW avg pts 4.40; mins 90; xGI 0.27; current GWs 8; fixture Elo diff +89 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | 4.47 | 3.56 | 3.97 | 4.66 | 5.51 | 17.42 | 2.21 | high | 5-GW avg pts 2.80; mins 72; xGI 0.59; current GWs 8; fixture Elo diff +13 |
| Doku | GW4: 0, GW5: 1, GW6: 12, GW7: 6, GW8: 2 | MCI | Midfielder | 4.33 | 4.09 | 4.38 | 3.15 | 4.47 | 16.41 | 2.19 | high | 5-GW avg pts 4.20; mins 43; xGI 0.35; current GWs 8; fixture Elo diff +103 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | 4.30 | 4.97 | 5.42 | 4.97 | 6.00 | 20.18 | 2.24 | high | 5-GW avg pts 5.60; mins 65; xGI 0.41; current GWs 8; fixture Elo diff +46 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | ARS | Midfielder | 4.24 | 5.50 | 4.34 | 3.94 | 4.34 | 18.02 | 2.44 | high | 5-GW avg pts 5.20; mins 86; xGI 0.32; current GWs 8; fixture Elo diff +246 |
| Tavernier | GW4: 8, GW5: 2, GW6: 1, GW7: 10, GW8: 10 | BOU | Midfielder | 4.24 | 4.61 | 4.20 | 4.03 | 3.96 | 16.94 | 2.65 | high | 5-GW avg pts 6.20; mins 78; xGI 0.62; current GWs 8; fixture Elo diff +89 |
| Rayan | GW4: 2, GW5: 2, GW6: 2, GW7: 3, GW8: 10 | BOU | Midfielder | 4.22 | 4.30 | 4.36 | 4.34 | 3.98 | 17.01 | 2.70 | high | 5-GW avg pts 3.80; mins 87; xGI 0.50; current GWs 8; fixture Elo diff +89 |
| N.Jackson | GW4: 0, GW5: 6, GW6: 9, GW7: 2, GW8: 13 | AVL | Forward | 4.20 | 3.54 | 4.82 | 4.70 | 4.09 | 16.99 | 2.54 | high | 5-GW avg pts 6.00; mins 79; xGI 0.38; current GWs 8; fixture Elo diff +139 |
| Evanilson | GW4: 5, GW5: 2, GW6: 7, GW7: 12, GW8: 6 | BOU | Forward | 4.19 | 4.88 | 4.15 | 3.95 | 3.83 | 16.97 | 2.74 | high | 5-GW avg pts 6.40; mins 87; xGI 0.62; current GWs 8; fixture Elo diff +89 |
| Cherki | GW4: 1, GW5: 8, GW6: 10, GW7: 0, GW8: 0 | MCI | Midfielder | 4.18 | 3.97 | 4.20 | 3.30 | 4.17 | 15.92 | 1.99 | high | 5-GW avg pts 3.80; mins 53; xGI 0.30; current GWs 8; fixture Elo diff +103 |
| Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | TOT | Defender | 4.17 | 4.00 | 4.77 | 4.14 | 4.13 | 16.96 | 3.46 | high | 5-GW avg pts 5.60; mins 90; xGI 0.19; current GWs 8; fixture Elo diff +19 |
| Xhaka | GW4: 1, GW5: 2, GW6: 2, GW7: 2, GW8: 3 | SUN | Midfielder | 4.06 | 3.35 | 3.10 | 4.03 | 2.93 | 14.14 | 2.62 | high | 5-GW avg pts 2.00; mins 90; xGI 0.21; current GWs 8; fixture Elo diff -84 |
| Tonali | GW4: 3, GW5: 2, GW6: 7, GW7: 4, GW8: 5 | TOT | Midfielder | 4.00 | 3.89 | 4.62 | 4.07 | 4.00 | 16.44 | 3.10 | high | 5-GW avg pts 4.20; mins 89; xGI 0.28; current GWs 8; fixture Elo diff +19 |
| Truffert | GW4: 3, GW5: 2, GW6: -1, GW7: 6, GW8: 10 | BOU | Defender | 3.97 | 4.14 | 3.92 | 3.73 | 3.62 | 15.61 | 2.89 | high | 5-GW avg pts 4.00; mins 89; xGI 0.20; current GWs 8; fixture Elo diff +89 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.0m**. Current squad selling value: **£97.9m**. Total available funds: **£98.9m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £7.9m | 22.35 | GW9, GW10, GW11, GW12, GW13 | GW10 | GW9, GW12 |
| Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | BOU | Defender | £5.5m | 18.19 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | BOU | Defender | £5.0m | 18.18 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | TOT | Defender | £4.9m | 16.96 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Konsa | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | ARS | Defender | £4.7m | 15.96 | GW10 | — | — |
| Haaland | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | MCI | Forward | £15.7m | 24.81 | GW9, GW10, GW11, GW13 | GW9, GW11, GW13 | GW10 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | £9.0m | 20.18 | GW9, GW10, GW11, GW12, GW13 | — | GW13 |
| N.Jackson | GW4: 0, GW5: 6, GW6: 9, GW7: 2, GW8: 13 | AVL | Forward | £6.7m | 16.99 | GW9, GW11, GW12, GW13 | — | — |
| Petrović | GW4: 1, GW5: 2, GW6: 0, GW7: 6, GW8: 7 | BOU | Goalkeeper | £4.5m | 14.12 | GW9, GW10 | — | — |
| Kinsky | GW4: 7, GW5: 2, GW6: 3, GW7: 2, GW8: 9 | TOT | Goalkeeper | £4.4m | 13.85 | GW11, GW12, GW13 | — | — |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | £8.0m | 21.11 | GW9, GW10, GW11, GW12, GW13 | GW12 | GW11 |
| Mbeumo | GW4: 2, GW5: 2, GW6: 8, GW7: 8, GW8: 2 | MUN | Midfielder | £7.9m | 18.29 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Tonali | GW4: 3, GW5: 2, GW6: 7, GW7: 4, GW8: 5 | TOT | Midfielder | £5.3m | 16.44 | GW9, GW11, GW12, GW13 | — | — |
| Ampadu | GW4: 7, GW5: 5, GW6: 1, GW7: 1, GW8: 2 | LEE | Midfielder | £5.3m | 14.58 | GW10, GW12 | — | — |
| Reed | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | FUL | Midfielder | £4.3m | 0.58 | Bench | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £7.9m | 22.35 | GW9, GW10, GW11, GW12, GW13 | GW9, GW10 | GW11, GW12 |
| Bassey | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | FUL | Defender | £4.5m | 12.60 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Egan | GW4: 2, GW5: 1, GW6: 1, GW7: 4, GW8: 4 | HUL | Defender | £4.1m | 11.90 | GW9, GW11, GW12, GW13 | — | — |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | EVE | Defender | £5.5m | 8.74 | GW10 | — | — |
| Furlong | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | IPS | Defender | £3.9m | 0.71 | Bench | — | — |
| Thiago | GW4: 1, GW5: 5, GW6: 4, GW7: 4, GW8: 5 | BRE | Forward | £7.8m | 17.07 | GW9, GW10, GW11, GW12, GW13 | — | GW9 |
| Havertz | GW4: 1, GW5: 2, GW6: 2, GW7: 2, GW8: 1 | ARS | Forward | £7.5m | 12.88 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Mheuka | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | CHE | Forward | £4.5m | 0.42 | Bench | — | — |
| Horníček | GW4: 1, GW5: 3, GW6: 0, GW7: 2, GW8: 8 | NEW | Goalkeeper | £5.0m | 12.17 | GW9, GW10, GW11, GW12 | — | — |
| Leno | GW4: 9, GW5: 3, GW6: 2, GW7: 6, GW8: 8 | FUL | Goalkeeper | £4.5m | 10.95 | GW13 | — | — |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | £8.0m | 21.11 | GW9, GW10, GW11, GW12, GW13 | GW11, GW12, GW13 | — |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | ARS | Midfielder | £7.4m | 18.02 | GW9, GW10, GW11, GW12, GW13 | — | GW10 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | £7.9m | 17.42 | GW9, GW10, GW11, GW12, GW13 | — | GW13 |
| Cherki | GW4: 1, GW5: 8, GW6: 10, GW7: 0, GW8: 0 | MCI | Midfielder | £8.0m | 15.92 | GW9, GW10, GW11, GW12, GW13 | — | — |
| B.Fernandes | GW4: 2, GW5: 2, GW6: 1, GW7: 1, GW8: 0 | MUN | Midfielder | £11.7m | 11.70 | GW9, GW10, GW11, GW12, GW13 | — | — |

Squad cost: £98.2m.

## One-transfer recommendation

**Branthwaite → Hill** (projected weighted XI+captain gain 7.19).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | £5.5m | £5.5m | £1.0m | 7.19 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | £5.5m | £5.0m | £1.5m | 7.18 |
| B.Fernandes | GW4: 2, GW5: 2, GW6: 1, GW7: 1, GW8: 0 | Mbeumo | GW4: 2, GW5: 2, GW6: 8, GW7: 8, GW8: 2 | £11.7m | £7.9m | £4.8m | 6.59 |
| Egan | GW4: 2, GW5: 1, GW6: 1, GW7: 4, GW8: 4 | Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | £4.1m | £5.0m | £0.1m | 6.02 |
| Furlong | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | £3.9m | £4.9m | £0.0m | 5.97 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | £5.5m | £4.9m | £1.6m | 5.97 |
| Bassey | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | £4.5m | £5.5m | £0.0m | 5.58 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Virgil | GW4: 8, GW5: 8, GW6: 0, GW7: 4, GW8: 9 | £5.5m | £6.4m | £0.1m | 5.58 |
| Bassey | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | £4.5m | £5.0m | £0.5m | 5.57 |
| B.Fernandes | GW4: 2, GW5: 2, GW6: 1, GW7: 1, GW8: 0 | Rayan | GW4: 2, GW5: 2, GW6: 2, GW7: 3, GW8: 10 | £11.7m | £6.3m | £6.4m | 5.31 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
