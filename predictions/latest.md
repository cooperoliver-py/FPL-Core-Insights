# FPL predictions: 2026-2027, GW8

Last generated: 2026-10-23 13:44 UTC

Data commit: `4fb8198cb647f8ff72f012c7c497864a61428976`

## Data freshness

All scheduled Premier League fixtures before GW8 are complete.

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

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top 20 players over the last 5 Gameweeks

Ranked by recorded FPL points in GW3–GW7. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Vuskovic | BHA | Defender | GW3: 12, GW4: 6, GW5: 8, GW6: 8, GW7: 11 | 45 | 9.00 | 5 |
| Groß | BHA | Midfielder | GW3: 1, GW4: 17, GW5: 14, GW6: 6, GW7: 5 | 43 | 8.60 | 5 |
| Haaland | MCI | Forward | GW3: 9, GW4: 9, GW5: 6, GW6: 6, GW7: 13 | 43 | 8.60 | 5 |
| De Cuyper | BHA | Defender | GW3: 4, GW4: 11, GW5: 6, GW6: 15, GW7: 6 | 42 | 8.40 | 5 |
| Bogle | LEE | Defender | GW3: 14, GW4: 15, GW5: 5, GW6: 1, GW7: 2 | 37 | 7.40 | 5 |
| Kostoulas | BHA | Forward | GW3: 2, GW4: 10, GW5: 10, GW6: 1, GW7: 12 | 35 | 7.00 | 5 |
| Isak | LIV | Forward | GW3: 13, GW4: 2, GW5: 8, GW6: 0, GW7: 9 | 32 | 6.40 | 5 |
| Verbruggen | BHA | Goalkeeper | GW3: 3, GW4: 8, GW5: 6, GW6: 9, GW7: 6 | 32 | 6.40 | 5 |
| Tavernier | BOU | Midfielder | GW3: 10, GW4: 8, GW5: 2, GW6: 1, GW7: 10 | 31 | 6.20 | 5 |
| Raya | ARS | Goalkeeper | GW3: 3, GW4: 14, GW5: 1, GW6: 3, GW7: 9 | 30 | 6.00 | 5 |
| Semenyo | MCI | Midfielder | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | 30 | 6.00 | 5 |
| Belloumi | HUL | Midfielder | GW3: 5, GW4: 13, GW5: 4, GW6: 6, GW7: 2 | 30 | 6.00 | 5 |
| Manzambi | AVL | Midfielder | GW3: 0, GW4: 1, GW5: 13, GW6: 5, GW7: 11 | 30 | 6.00 | 5 |
| Boscagli | BHA | Defender | GW3: 2, GW4: 6, GW5: 6, GW6: 5, GW7: 10 | 29 | 5.80 | 5 |
| Van Hecke | TOT | Defender | GW3: 8, GW4: 8, GW5: 6, GW6: 3, GW7: 4 | 29 | 5.80 | 5 |
| Ayari | BHA | Midfielder | GW3: 2, GW4: 8, GW5: 3, GW6: 3, GW7: 13 | 29 | 5.80 | 5 |
| Tarkowski | EVE | Defender | GW3: 3, GW4: 8, GW5: 14, GW6: 3, GW7: 0 | 28 | 5.60 | 5 |
| A.Becker | LIV | Goalkeeper | GW3: 8, GW4: 9, GW5: 8, GW6: 1, GW7: 2 | 28 | 5.60 | 5 |
| Rice | ARS | Midfielder | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | 28 | 5.60 | 5 |
| F.Kadıoğlu | BHA | Defender | GW3: 2, GW4: 6, GW5: 5, GW6: 9, GW7: 6 | 28 | 5.60 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW8 player forecasts

| Player | Last 5 GW points | Club | Pos | GW8 | GW9 | GW10 | GW11 | GW12 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | 5.90 | 5.60 | 5.64 | 5.36 | 5.90 | 22.74 | 1.93 | high | 5-GW avg pts 1.60; mins 90; xGI 0.26; current GWs 7; fixture Elo diff +41 |
| Isak | GW3: 13, GW4: 2, GW5: 8, GW6: 0, GW7: 9 | LIV | Forward | 5.70 | 4.18 | 4.85 | 5.73 | 4.85 | 20.26 | 2.25 | high | 5-GW avg pts 6.40; mins 62; xGI 0.38; current GWs 7; fixture Elo diff +25 |
| Iwobi | GW3: 2, GW4: 3, GW5: 5, GW6: 4, GW7: 11 | FUL | Midfielder | 5.63 | 3.68 | 4.52 | 3.48 | 3.98 | 17.37 | 3.22 | high | 5-GW avg pts 5.00; mins 81; xGI 0.51; current GWs 7; fixture Elo diff -39 |
| Thiago | GW3: 2, GW4: 1, GW5: 5, GW6: 4, GW7: 4 | BRE | Forward | 5.46 | 4.96 | 4.43 | 4.87 | 3.93 | 19.24 | 2.47 | high | 5-GW avg pts 3.20; mins 90; xGI 0.46; current GWs 7; fixture Elo diff +53 |
| Gabriel | GW3: 2, GW4: 9, GW5: 1, GW6: 2, GW7: 8 | ARS | Defender | 5.43 | 4.87 | 5.78 | 5.09 | 4.23 | 20.54 | 2.60 | high | 5-GW avg pts 4.40; mins 90; xGI 0.19; current GWs 7; fixture Elo diff +253 |
| Rice | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | ARS | Midfielder | 5.20 | 4.68 | 5.75 | 4.83 | 4.40 | 20.03 | 2.74 | high | 5-GW avg pts 5.60; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +253 |
| Palmer | GW3: 1, GW4: 5, GW5: 2, GW6: 8, GW7: 2 | CHE | Midfielder | 5.16 | 4.63 | 5.13 | 5.15 | 5.01 | 20.04 | 2.04 | high | 5-GW avg pts 3.60; mins 89; xGI 0.22; current GWs 7; fixture Elo diff +21 |
| João Pedro | GW3: 1, GW4: 12, GW5: 0, GW6: 12, GW7: 2 | CHE | Forward | 5.14 | 4.42 | 4.69 | 5.14 | 4.59 | 19.22 | 2.43 | high | 5-GW avg pts 5.40; mins 68; xGI 0.28; current GWs 7; fixture Elo diff +21 |
| Gibbs-White | GW3: 3, GW4: 8, GW5: 2, GW6: 2, GW7: 0 | NFO | Midfielder | 5.09 | 3.73 | 3.44 | 3.50 | 4.06 | 16.09 | 2.04 | high | 5-GW avg pts 3.00; mins 72; xGI 0.50; current GWs 7; fixture Elo diff -8 |
| Wirtz | GW3: 3, GW4: 3, GW5: 6, GW6: 2, GW7: 5 | LIV | Midfielder | 4.97 | 3.32 | 4.56 | 4.85 | 4.56 | 17.74 | 2.46 | high | 5-GW avg pts 3.80; mins 81; xGI 0.24; current GWs 7; fixture Elo diff +25 |
| Barcola | GW3: 1, GW4: 3, GW5: 3, GW6: 2, GW7: 4 | LIV | Midfielder | 4.90 | 3.26 | 4.86 | 4.77 | 4.86 | 17.97 | 2.25 | high | 5-GW avg pts 2.60; mins 69; xGI 0.24; current GWs 5; fixture Elo diff +25 |
| Rogers | GW3: 6, GW4: 8, GW5: 2, GW6: 9, GW7: 2 | CHE | Midfielder | 4.88 | 4.11 | 4.58 | 4.87 | 4.55 | 18.39 | 2.30 | high | 5-GW avg pts 5.40; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +21 |
| N.Williams | GW3: 7, GW4: 2, GW5: 2, GW6: 1, GW7: 3 | NFO | Defender | 4.84 | 3.61 | 2.87 | 3.29 | 3.88 | 15.02 | 3.00 | high | 5-GW avg pts 3.00; mins 90; xGI 0.25; current GWs 7; fixture Elo diff -8 |
| Mbeumo | GW3: 8, GW4: 2, GW5: 2, GW6: 8, GW7: 8 | MUN | Midfielder | 4.68 | 4.47 | 4.59 | 4.41 | 4.68 | 18.27 | 2.31 | high | 5-GW avg pts 5.60; mins 90; xGI 0.43; current GWs 7; fixture Elo diff +41 |
| Bassey | GW3: 1, GW4: 6, GW5: 6, GW6: 2, GW7: 8 | FUL | Defender | 4.60 | 2.72 | 3.48 | 2.49 | 3.14 | 13.46 | 2.99 | high | 5-GW avg pts 4.60; mins 90; xGI 0.07; current GWs 7; fixture Elo diff -39 |
| McAtee | GW3: 2, GW4: 3, GW5: 2, GW6: 4, GW7: 2 | NFO | Midfielder | 4.48 | 3.61 | 2.82 | 3.20 | 3.71 | 14.45 | 2.63 | high | 5-GW avg pts 2.60; mins 85; xGI 0.26; current GWs 7; fixture Elo diff -8 |
| Murillo | GW3: 8, GW4: 6, GW5: 4, GW6: 2, GW7: 2 | NFO | Defender | 4.44 | 3.77 | 2.87 | 3.41 | 3.92 | 14.86 | 2.70 | high | 5-GW avg pts 4.40; mins 90; xGI 0.20; current GWs 7; fixture Elo diff -8 |
| Haaland | GW3: 9, GW4: 9, GW5: 6, GW6: 6, GW7: 13 | MCI | Forward | 4.41 | 5.20 | 5.32 | 5.85 | 3.38 | 19.48 | 1.24 | high | 5-GW avg pts 8.60; mins 88; xGI 1.01; current GWs 7; fixture Elo diff +78 |
| Ødegaard | GW3: 10, GW4: 3, GW5: 2, GW6: 1, GW7: 3 | ARS | Midfielder | 4.29 | 3.92 | 4.25 | 3.96 | 3.69 | 16.20 | 2.38 | high | 5-GW avg pts 3.80; mins 82; xGI 0.61; current GWs 7; fixture Elo diff +253 |
| Ajer | GW3: 2, GW4: 1, GW5: 7, GW6: 6, GW7: 3 | BRE | Defender | 4.28 | 3.60 | 3.39 | 3.59 | 2.96 | 14.52 | 3.23 | high | 5-GW avg pts 3.80; mins 90; xGI 0.09; current GWs 7; fixture Elo diff +53 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£98.9m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW3: 2, GW4: 9, GW5: 1, GW6: 2, GW7: 8 | ARS | Defender | £7.9m | 20.54 | GW8, GW9, GW10, GW11, GW12 | GW10 | — |
| Van Hecke | GW3: 8, GW4: 8, GW5: 6, GW6: 3, GW7: 4 | TOT | Defender | £4.9m | 17.00 | GW9, GW10, GW11, GW12 | — | GW11 |
| Richards | GW3: 1, GW4: 2, GW5: 8, GW6: 4, GW7: 2 | CRY | Defender | £4.9m | 15.87 | GW8, GW9, GW11, GW12 | — | — |
| Muharemović | GW3: 4, GW4: 7, GW5: 6, GW6: 2, GW7: 5 | LEE | Defender | £5.0m | 15.79 | GW8, GW10, GW12 | — | — |
| O'Shea | GW3: 3, GW4: 1, GW5: 2, GW6: 11, GW7: 3 | IPS | Defender | £4.0m | 13.91 | GW9 | — | — |
| Isak | GW3: 13, GW4: 2, GW5: 8, GW6: 0, GW7: 9 | LIV | Forward | £9.0m | 20.26 | GW8, GW9, GW10, GW11, GW12 | GW11 | GW8 |
| Thiago | GW3: 2, GW4: 1, GW5: 5, GW6: 4, GW7: 4 | BRE | Forward | £7.8m | 19.24 | GW8, GW9, GW10, GW11 | — | GW9 |
| João Pedro | GW3: 1, GW4: 12, GW5: 0, GW6: 12, GW7: 2 | CHE | Forward | £7.9m | 19.22 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Raya | GW3: 3, GW4: 14, GW5: 1, GW6: 3, GW7: 9 | ARS | Goalkeeper | £6.1m | 15.13 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Zetterer | GW3: 0, GW4: 0, GW5: 0, GW6: 0, GW7: 0 | LEE | Goalkeeper | £4.0m | 0.44 | Bench | — | — |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | £11.8m | 22.74 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW12 | — |
| Rice | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | ARS | Midfielder | £7.3m | 20.03 | GW8, GW9, GW10, GW11, GW12 | — | GW10 |
| Barcola | GW3: 1, GW4: 3, GW5: 3, GW6: 2, GW7: 4 | LIV | Midfielder | £8.0m | 17.97 | GW8, GW10, GW11, GW12 | — | GW12 |
| Iwobi | GW3: 2, GW4: 3, GW5: 5, GW6: 4, GW7: 11 | FUL | Midfielder | £5.4m | 17.37 | GW8, GW10 | — | — |
| Kamara | GW3: 3, GW4: 2, GW5: 6, GW6: 4, GW7: 5 | AVL | Midfielder | £5.0m | 14.81 | GW9, GW11, GW12 | — | — |

Squad cost: £99.0m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW3: 2, GW4: 9, GW5: 1, GW6: 2, GW7: 8 | ARS | Defender | £7.9m | 20.54 | GW8, GW9, GW10, GW11, GW12 | GW10 | GW11 |
| Branthwaite | GW3: 3, GW4: 6, GW5: 8, GW6: 3, GW7: 1 | EVE | Defender | £5.5m | 14.06 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Bassey | GW3: 1, GW4: 6, GW5: 6, GW6: 2, GW7: 8 | FUL | Defender | £4.5m | 13.46 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Egan | GW3: 6, GW4: 2, GW5: 1, GW6: 1, GW7: 4 | HUL | Defender | £4.1m | 10.91 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Furlong | GW3: 0, GW4: 0, GW5: 0, GW6: 0, GW7: 0 | IPS | Defender | £3.9m | 0.75 | Bench | — | — |
| Thiago | GW3: 2, GW4: 1, GW5: 5, GW6: 4, GW7: 4 | BRE | Forward | £7.8m | 19.24 | GW8, GW9, GW10, GW11, GW12 | — | GW8, GW9 |
| Havertz | GW3: 8, GW4: 1, GW5: 2, GW6: 2, GW7: 2 | ARS | Forward | £7.5m | 16.26 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Mheuka | GW3: 0, GW4: 0, GW5: 0, GW6: 0, GW7: 0 | CHE | Forward | £4.5m | 0.41 | Bench | — | — |
| Leno | GW3: 1, GW4: 9, GW5: 3, GW6: 2, GW7: 6 | FUL | Goalkeeper | £4.5m | 12.47 | GW8, GW10, GW11, GW12 | — | — |
| Horníček | GW3: 2, GW4: 1, GW5: 3, GW6: 0, GW7: 2 | NEW | Goalkeeper | £5.0m | 11.63 | GW9 | — | — |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | £11.8m | 22.74 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW11, GW12 | GW10 |
| Rogers | GW3: 6, GW4: 8, GW5: 2, GW6: 9, GW7: 2 | CHE | Midfielder | £8.0m | 18.39 | GW8, GW9, GW10, GW11, GW12 | — | GW12 |
| Gibbs-White | GW3: 3, GW4: 8, GW5: 2, GW6: 2, GW7: 0 | NFO | Midfielder | £7.9m | 16.09 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Cherki | GW3: 3, GW4: 1, GW5: 8, GW6: 10, GW7: 0 | MCI | Midfielder | £8.0m | 12.18 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | MCI | Midfielder | £8.3m | 0.00 | Bench | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Semenyo → Rice** (projected weighted XI+captain gain 10.06).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Rice | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | £8.3m | £7.3m | £1.2m | 10.06 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Mbeumo | GW3: 8, GW4: 2, GW5: 2, GW6: 8, GW7: 8 | £8.3m | £7.9m | £0.6m | 8.30 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Barcola | GW3: 1, GW4: 3, GW5: 3, GW6: 2, GW7: 4 | £8.3m | £8.0m | £0.5m | 8.01 |
| Cherki | GW3: 3, GW4: 1, GW5: 8, GW6: 10, GW7: 0 | Rice | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | £7.9m | £7.3m | £0.8m | 7.84 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Wirtz | GW3: 3, GW4: 3, GW5: 6, GW6: 2, GW7: 5 | £8.3m | £7.2m | £1.3m | 7.77 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Doku | GW3: 0, GW4: 0, GW5: 1, GW6: 12, GW7: 6 | £8.3m | £7.5m | £1.0m | 7.58 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Iwobi | GW3: 2, GW4: 3, GW5: 5, GW6: 4, GW7: 11 | £8.3m | £5.4m | £3.1m | 7.40 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Ødegaard | GW3: 10, GW4: 3, GW5: 2, GW6: 1, GW7: 3 | £8.3m | £6.8m | £1.7m | 6.23 |
| Cherki | GW3: 3, GW4: 1, GW5: 8, GW6: 10, GW7: 0 | Mbeumo | GW3: 8, GW4: 2, GW5: 2, GW6: 8, GW7: 8 | £7.9m | £7.9m | £0.2m | 6.09 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Stach | GW3: 2, GW4: 3, GW5: 5, GW6: 2, GW7: 2 | £8.3m | £6.0m | £2.5m | 5.87 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
