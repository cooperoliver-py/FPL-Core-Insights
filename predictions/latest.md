# FPL predictions: 2026-2027, GW9

Last generated: 2026-10-28 10:59 UTC

Data commit: `80912e962a4a95fc8738af82a45fda1ca203bc39`

## Data freshness

All scheduled Premier League fixtures before GW9 are complete.

The model learns from 2025/26 and completed, checked current-season Gameweeks. An equal-weight blend balances the original features with recent participation, longer-window per-90 rates, set-piece roles and observed workload across league, cup, European and friendly matches. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; prices remain fixed. Dated suspensions expire and later injury-return forecasts use a conservative historical recovery rate.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.852 | 1.848 | 0.752 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.022 and Spearman is 0.369.

The predicted top 20 averaged 4.78 actual points versus 1.69 for the selectable pool.

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
| Haaland | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | MCI | Forward | 6.11 | 6.43 | 7.11 | 3.55 | 7.00 | 24.27 | 1.54 | high | 5-GW avg pts 8.40; mins 88; xGI 0.78; current GWs 8; fixture Elo diff +103 |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | 5.61 | 7.43 | 5.63 | 5.22 | 5.63 | 23.83 | 3.02 | high | 5-GW avg pts 7.40; mins 90; xGI 0.24; current GWs 8; fixture Elo diff +246 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | 4.80 | 3.86 | 4.32 | 4.97 | 5.48 | 18.50 | 2.34 | high | 5-GW avg pts 2.80; mins 72; xGI 0.59; current GWs 8; fixture Elo diff +13 |
| Thiago | GW4: 1, GW5: 5, GW6: 4, GW7: 4, GW8: 5 | BRE | Forward | 4.65 | 4.39 | 4.66 | 3.84 | 2.69 | 16.62 | 2.13 | high | 5-GW avg pts 3.80; mins 90; xGI 0.53; current GWs 8; fixture Elo diff -53 |
| Mbeumo | GW4: 2, GW5: 2, GW6: 8, GW7: 8, GW8: 2 | MUN | Midfielder | 4.59 | 4.47 | 4.44 | 4.60 | 4.51 | 18.09 | 2.29 | high | 5-GW avg pts 4.40; mins 90; xGI 0.48; current GWs 8; fixture Elo diff +48 |
| Doku | GW4: 0, GW5: 1, GW6: 12, GW7: 6, GW8: 2 | MCI | Midfielder | 4.57 | 4.23 | 4.63 | 2.94 | 4.62 | 16.91 | 2.26 | high | 5-GW avg pts 4.20; mins 43; xGI 0.35; current GWs 8; fixture Elo diff +103 |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | 4.55 | 5.58 | 5.67 | 5.31 | 5.67 | 21.21 | 2.65 | high | 5-GW avg pts 4.40; mins 89; xGI 0.24; current GWs 8; fixture Elo diff +16 |
| Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | BOU | Defender | 4.39 | 4.91 | 4.24 | 4.23 | 3.83 | 17.46 | 3.17 | high | 5-GW avg pts 5.20; mins 90; xGI 0.04; current GWs 8; fixture Elo diff +89 |
| Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | BOU | Defender | 4.31 | 4.60 | 4.27 | 4.03 | 3.93 | 17.05 | 3.41 | high | 5-GW avg pts 4.40; mins 90; xGI 0.27; current GWs 8; fixture Elo diff +89 |
| Tavernier | GW4: 8, GW5: 2, GW6: 1, GW7: 10, GW8: 10 | BOU | Midfielder | 4.16 | 4.76 | 4.18 | 4.05 | 3.93 | 16.99 | 2.65 | high | 5-GW avg pts 6.20; mins 78; xGI 0.62; current GWs 8; fixture Elo diff +89 |
| N.Jackson | GW4: 0, GW5: 6, GW6: 9, GW7: 2, GW8: 13 | AVL | Forward | 4.12 | 3.56 | 4.77 | 4.65 | 4.12 | 16.88 | 2.48 | high | 5-GW avg pts 6.00; mins 79; xGI 0.38; current GWs 8; fixture Elo diff +139 |
| Cherki | GW4: 1, GW5: 8, GW6: 10, GW7: 0, GW8: 0 | MCI | Midfielder | 4.12 | 3.86 | 4.22 | 3.07 | 4.18 | 15.62 | 1.95 | high | 5-GW avg pts 3.80; mins 53; xGI 0.30; current GWs 8; fixture Elo diff +103 |
| Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | TOT | Defender | 4.11 | 4.00 | 4.96 | 4.15 | 4.06 | 17.03 | 3.47 | high | 5-GW avg pts 5.60; mins 90; xGI 0.19; current GWs 8; fixture Elo diff +19 |
| Xhaka | GW4: 1, GW5: 2, GW6: 2, GW7: 2, GW8: 3 | SUN | Midfielder | 4.09 | 3.40 | 3.08 | 4.13 | 2.94 | 14.26 | 2.64 | high | 5-GW avg pts 2.00; mins 90; xGI 0.21; current GWs 8; fixture Elo diff -84 |
| Evanilson | GW4: 5, GW5: 2, GW6: 7, GW7: 12, GW8: 6 | BOU | Forward | 4.09 | 4.94 | 4.10 | 3.92 | 3.77 | 16.83 | 2.71 | high | 5-GW avg pts 6.40; mins 87; xGI 0.62; current GWs 8; fixture Elo diff +89 |
| Tonali | GW4: 3, GW5: 2, GW6: 7, GW7: 4, GW8: 5 | TOT | Midfielder | 4.08 | 3.93 | 4.56 | 4.09 | 4.06 | 16.56 | 3.12 | high | 5-GW avg pts 4.20; mins 89; xGI 0.28; current GWs 8; fixture Elo diff +19 |
| Rayan | GW4: 2, GW5: 2, GW6: 2, GW7: 3, GW8: 10 | BOU | Midfielder | 4.06 | 4.32 | 4.09 | 3.97 | 3.85 | 16.31 | 2.59 | high | 5-GW avg pts 3.80; mins 87; xGI 0.50; current GWs 8; fixture Elo diff +89 |
| Kamara | GW4: 2, GW5: 6, GW6: 4, GW7: 5, GW8: 4 | AVL | Midfielder | 4.04 | 3.42 | 4.27 | 4.12 | 4.03 | 15.83 | 3.17 | high | 5-GW avg pts 4.20; mins 89; xGI 0.06; current GWs 8; fixture Elo diff +139 |
| Enciso | GW4: 2, GW5: 2, GW6: 2, GW7: 2, GW8: 10 | IPS | Midfielder | 4.03 | 2.97 | 3.13 | 2.94 | 3.94 | 13.62 | 2.48 | high | 5-GW avg pts 3.60; mins 79; xGI 0.36; current GWs 8; fixture Elo diff -113 |
| Kudus | GW4: 1, GW5: 4, GW6: 3, GW7: 6, GW8: 3 | TOT | Midfielder | 3.94 | 3.68 | 4.03 | 3.77 | 3.95 | 15.48 | 2.38 | high | 5-GW avg pts 3.40; mins 62; xGI 0.16; current GWs 8; fixture Elo diff +19 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.0m**. Current squad selling value: **£97.9m**. Total available funds: **£98.9m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £7.9m | 23.83 | GW9, GW10, GW11, GW12, GW13 | GW10 | GW9, GW12 |
| Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | BOU | Defender | £5.5m | 17.46 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | BOU | Defender | £5.0m | 17.05 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | TOT | Defender | £4.9m | 17.03 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Muharemović | GW4: 7, GW5: 6, GW6: 2, GW7: 5, GW8: 9 | LEE | Defender | £5.1m | 14.88 | GW10, GW12 | — | — |
| Haaland | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | MCI | Forward | £15.8m | 24.27 | GW9, GW10, GW11, GW13 | GW9, GW11, GW13 | GW10 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | £9.1m | 18.53 | GW10, GW11, GW12, GW13 | — | — |
| Evanilson | GW4: 5, GW5: 2, GW6: 7, GW7: 12, GW8: 6 | BOU | Forward | £6.2m | 16.83 | GW9, GW10 | — | — |
| Suzuki | GW4: 2, GW5: 2, GW6: 2, GW7: 8, GW8: 4 | AVL | Goalkeeper | £5.0m | 15.08 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Bentley | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | COV | Goalkeeper | £4.0m | 0.82 | Bench | — | — |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | £8.0m | 21.21 | GW9, GW10, GW11, GW12, GW13 | GW12 | GW11, GW13 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | £7.9m | 18.50 | GW9, GW11, GW12, GW13 | — | — |
| Tonali | GW4: 3, GW5: 2, GW6: 7, GW7: 4, GW8: 5 | TOT | Midfielder | £5.3m | 16.56 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Kamara | GW4: 2, GW5: 6, GW6: 4, GW7: 5, GW8: 4 | AVL | Midfielder | £5.0m | 15.83 | GW9, GW11, GW12, GW13 | — | — |
| Hughes | GW4: 1, GW5: 0, GW6: 0, GW7: 1, GW8: 0 | CRY | Midfielder | £4.3m | 2.58 | Bench | — | — |

Squad cost: £99.0m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £7.9m | 23.83 | GW9, GW10, GW11, GW12, GW13 | GW9, GW10 | GW11, GW12, GW13 |
| Bassey | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | FUL | Defender | £4.5m | 12.91 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Egan | GW4: 2, GW5: 1, GW6: 1, GW7: 4, GW8: 4 | HUL | Defender | £4.1m | 12.52 | GW9, GW11, GW12, GW13 | — | — |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | EVE | Defender | £5.5m | 8.97 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Furlong | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | IPS | Defender | £3.9m | 0.71 | Bench | — | — |
| Thiago | GW4: 1, GW5: 5, GW6: 4, GW7: 4, GW8: 5 | BRE | Forward | £7.8m | 16.62 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Havertz | GW4: 1, GW5: 2, GW6: 2, GW7: 2, GW8: 1 | ARS | Forward | £7.5m | 12.75 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Mheuka | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | CHE | Forward | £4.5m | 0.44 | Bench | — | — |
| Horníček | GW4: 1, GW5: 3, GW6: 0, GW7: 2, GW8: 8 | NEW | Goalkeeper | £5.0m | 12.09 | GW9, GW10, GW12 | — | — |
| Leno | GW4: 9, GW5: 3, GW6: 2, GW7: 6, GW8: 8 | FUL | Goalkeeper | £4.5m | 11.61 | GW11, GW13 | — | — |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | £8.0m | 21.21 | GW9, GW10, GW11, GW12, GW13 | GW11, GW12, GW13 | GW10 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | £7.9m | 18.50 | GW9, GW10, GW11, GW12, GW13 | — | GW9 |
| Cherki | GW4: 1, GW5: 8, GW6: 10, GW7: 0, GW8: 0 | MCI | Midfielder | £8.0m | 15.62 | GW9, GW10, GW11, GW12, GW13 | — | — |
| B.Fernandes | GW4: 2, GW5: 2, GW6: 1, GW7: 1, GW8: 0 | MUN | Midfielder | £11.7m | 12.02 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | ARS | Midfielder | £7.4m | 8.31 | GW10 | — | — |

Squad cost: £98.2m.

## One-transfer recommendation

**Rice → Mbeumo** (projected weighted XI+captain gain 9.01).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Mbeumo | GW4: 2, GW5: 2, GW6: 8, GW7: 8, GW8: 2 | £7.4m | £7.9m | £0.5m | 9.01 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | £5.5m | £5.5m | £1.0m | 8.49 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | £5.5m | £5.0m | £1.5m | 8.08 |
| Furlong | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | £3.9m | £4.9m | £0.0m | 8.05 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | £5.5m | £4.9m | £1.6m | 8.05 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Tavernier | GW4: 8, GW5: 2, GW6: 1, GW7: 10, GW8: 10 | £7.4m | £6.4m | £2.0m | 7.91 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Doku | GW4: 0, GW5: 1, GW6: 12, GW7: 6, GW8: 2 | £7.4m | £7.5m | £0.9m | 7.83 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Tonali | GW4: 3, GW5: 2, GW6: 7, GW7: 4, GW8: 5 | £7.4m | £5.3m | £3.1m | 7.48 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Rayan | GW4: 2, GW5: 2, GW6: 2, GW7: 3, GW8: 10 | £7.4m | £6.3m | £2.1m | 7.23 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Gakpo | GW4: 1, GW5: 3, GW6: 0, GW7: 0, GW8: 3 | £7.4m | £7.1m | £1.3m | 6.95 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
