# FPL predictions: 2026-2027, GW9

Last generated: 2026-10-25 13:19 UTC

Data commit: `8f223d5d4cb023f79021d568f7e25ac94b423c5d`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW8: 5/10 fixtures finished. Completed clubs contribute current-season form; BHA, BOU, BRE, CRY, HUL, LEE, LIV, MUN, NEW, SUN are deferred.

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

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top 20 players over the last 5 Gameweeks

Ranked by recorded FPL points in GW4–GW8. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Groß | BHA | Midfielder | GW4: 17, GW5: 14, GW6: 6, GW7: 5 | 42 | 10.50 | 4 |
| Haaland | MCI | Forward | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | 42 | 8.40 | 5 |
| De Cuyper | BHA | Defender | GW4: 11, GW5: 6, GW6: 15, GW7: 6 | 38 | 9.50 | 4 |
| Gabriel | ARS | Defender | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | 37 | 7.40 | 5 |
| Raya | ARS | Goalkeeper | GW4: 14, GW5: 1, GW6: 3, GW7: 9, GW8: 7 | 34 | 6.80 | 5 |
| Konsa | ARS | Defender | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | 34 | 6.80 | 5 |
| Vuskovic | BHA | Defender | GW4: 6, GW5: 8, GW6: 8, GW7: 11 | 33 | 8.25 | 4 |
| Kostoulas | BHA | Forward | GW4: 10, GW5: 10, GW6: 1, GW7: 12 | 33 | 8.25 | 4 |
| Manzambi | AVL | Midfielder | GW4: 1, GW5: 13, GW6: 5, GW7: 11, GW8: 1 | 31 | 6.20 | 5 |
| Bassey | FUL | Defender | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | 30 | 6.00 | 5 |
| N.Jackson | AVL | Forward | GW4: 0, GW5: 6, GW6: 9, GW7: 2, GW8: 13 | 30 | 6.00 | 5 |
| McGinn | AVL | Midfielder | GW4: 6, GW5: 6, GW6: 10, GW7: 1, GW8: 6 | 29 | 5.80 | 5 |
| Verbruggen | BHA | Goalkeeper | GW4: 8, GW5: 6, GW6: 9, GW7: 6 | 29 | 7.25 | 4 |
| Leno | FUL | Goalkeeper | GW4: 9, GW5: 3, GW6: 2, GW7: 6, GW8: 8 | 28 | 5.60 | 5 |
| Van Hecke | TOT | Defender | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | 28 | 5.60 | 5 |
| Tarkowski | EVE | Defender | GW4: 8, GW5: 14, GW6: 3, GW7: 0, GW8: 2 | 27 | 5.40 | 5 |
| Boscagli | BHA | Defender | GW4: 6, GW5: 6, GW6: 5, GW7: 10 | 27 | 6.75 | 4 |
| Neto | CHE | Midfielder | GW4: 2, GW5: 2, GW6: 5, GW7: 15, GW8: 3 | 27 | 5.40 | 5 |
| Affengruber | FUL | Defender | GW4: 8, GW5: 4, GW6: 3, GW7: 6, GW8: 6 | 27 | 5.40 | 5 |
| Ayari | BHA | Midfielder | GW4: 8, GW5: 3, GW6: 3, GW7: 13 | 27 | 6.75 | 4 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW9 player forecasts

| Player | Last 5 GW points | Club | Pos | GW9 | GW10 | GW11 | GW12 | GW13 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | 5.64 | 5.68 | 5.41 | 5.94 | 5.64 | 22.63 | 1.93 | high | 5-GW avg pts 1.60; mins 90; xGI 0.26; current GWs 7; fixture Elo diff +48 |
| Haaland | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | MCI | Forward | 5.58 | 5.63 | 6.16 | 3.97 | 6.16 | 22.06 | 1.40 | high | 5-GW avg pts 8.40; mins 88; xGI 0.78; current GWs 8; fixture Elo diff +103 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | 5.57 | 4.11 | 4.89 | 5.93 | 6.59 | 21.28 | 2.69 | high | 5-GW avg pts 2.80; mins 72; xGI 0.59; current GWs 8; fixture Elo diff +13 |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | 5.16 | 6.14 | 5.26 | 5.10 | 5.26 | 21.62 | 2.74 | high | 5-GW avg pts 7.40; mins 90; xGI 0.24; current GWs 8; fixture Elo diff +246 |
| Thiago | GW3: 2, GW4: 1, GW5: 5, GW6: 4, GW7: 4 | BRE | Forward | 4.95 | 4.45 | 4.85 | 3.96 | 2.93 | 17.37 | 2.23 | high | 5-GW avg pts 3.20; mins 90; xGI 0.46; current GWs 7; fixture Elo diff -53 |
| Doku | GW4: 0, GW5: 1, GW6: 12, GW7: 6, GW8: 2 | MCI | Midfielder | 4.83 | 4.73 | 5.01 | 3.51 | 5.01 | 18.56 | 2.47 | high | 5-GW avg pts 4.20; mins 43; xGI 0.35; current GWs 8; fixture Elo diff +103 |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | 4.58 | 4.81 | 5.21 | 4.83 | 5.14 | 19.54 | 2.44 | high | 5-GW avg pts 4.40; mins 89; xGI 0.24; current GWs 8; fixture Elo diff +16 |
| Cherki | GW4: 1, GW5: 8, GW6: 10, GW7: 0, GW8: 0 | MCI | Midfielder | 4.50 | 3.94 | 4.54 | 3.38 | 4.54 | 16.77 | 2.10 | high | 5-GW avg pts 3.80; mins 53; xGI 0.30; current GWs 8; fixture Elo diff +103 |
| Mbeumo | GW3: 8, GW4: 2, GW5: 2, GW6: 8, GW7: 8 | MUN | Midfielder | 4.35 | 4.47 | 4.29 | 4.57 | 4.35 | 17.62 | 2.23 | high | 5-GW avg pts 5.60; mins 90; xGI 0.43; current GWs 7; fixture Elo diff +48 |
| E.Le Fée | GW3: 8, GW4: 0, GW5: 5, GW6: 2, GW7: 4 | SUN | Midfielder | 4.35 | 3.49 | 3.24 | 3.77 | 3.24 | 14.67 | 2.57 | high | 5-GW avg pts 3.80; mins 88; xGI 0.62; current GWs 7; fixture Elo diff -84 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | ARS | Midfielder | 4.32 | 5.70 | 4.41 | 3.99 | 4.41 | 18.42 | 2.49 | high | 5-GW avg pts 5.20; mins 86; xGI 0.32; current GWs 8; fixture Elo diff +246 |
| Palmer | GW4: 5, GW5: 2, GW6: 8, GW7: 2, GW8: -1 | CHE | Midfielder | 4.20 | 4.58 | 4.66 | 4.40 | 4.66 | 17.92 | 1.83 | high | 5-GW avg pts 3.20; mins 87; xGI 0.24; current GWs 8; fixture Elo diff +16 |
| Botman | GW3: 1, GW4: 2, GW5: 4, GW6: 8, GW7: 3 | NEW | Defender | 4.13 | 3.92 | 2.74 | 3.69 | 3.47 | 14.52 | 2.90 | high | 5-GW avg pts 3.60; mins 90; xGI 0.08; current GWs 7; fixture Elo diff -50 |
| Isak | GW3: 13, GW4: 2, GW5: 8, GW6: 0, GW7: 9 | LIV | Forward | 4.09 | 4.85 | 5.64 | 4.85 | 5.90 | 19.90 | 2.21 | high | 5-GW avg pts 6.40; mins 62; xGI 0.38; current GWs 7; fixture Elo diff +46 |
| O'Shea | GW4: 1, GW5: 2, GW6: 11, GW7: 3, GW8: 2 | IPS | Defender | 4.02 | 3.26 | 2.89 | 3.11 | 3.73 | 13.69 | 3.42 | high | 5-GW avg pts 3.80; mins 90; xGI 0.07; current GWs 8; fixture Elo diff -113 |
| Xhaka | GW3: 3, GW4: 1, GW5: 2, GW6: 2, GW7: 2 | SUN | Midfielder | 4.01 | 3.47 | 2.95 | 3.79 | 2.95 | 13.92 | 2.58 | high | 5-GW avg pts 2.00; mins 90; xGI 0.24; current GWs 7; fixture Elo diff -84 |
| Tavernier | GW3: 10, GW4: 8, GW5: 2, GW6: 1, GW7: 10 | BOU | Midfielder | 3.99 | 3.99 | 4.03 | 3.80 | 3.87 | 15.79 | 2.51 | high | 5-GW avg pts 6.20; mins 79; xGI 0.65; current GWs 7; fixture Elo diff +89 |
| Barry | GW4: 2, GW5: 6, GW6: 6, GW7: 2, GW8: 2 | EVE | Forward | 3.98 | 4.60 | 3.98 | 3.50 | 3.41 | 15.80 | 2.77 | high | 5-GW avg pts 3.60; mins 89; xGI 0.57; current GWs 8; fixture Elo diff -30 |
| Barnes | GW3: 12, GW4: 2, GW5: 9, GW6: 2, GW7: 2 | NEW | Midfielder | 3.97 | 3.93 | 2.60 | 3.75 | 3.35 | 14.22 | 2.33 | high | 5-GW avg pts 5.40; mins 90; xGI 0.39; current GWs 7; fixture Elo diff -50 |
| Janelt | GW3: 11, GW4: 4, GW5: 3, GW6: 3, GW7: -1 | BRE | Midfielder | 3.95 | 3.55 | 3.85 | 3.15 | 2.56 | 13.97 | 2.79 | high | 5-GW avg pts 4.00; mins 90; xGI 0.09; current GWs 7; fixture Elo diff -53 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£98.7m**. Total available funds: **£98.9m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £7.9m | 21.62 | GW9, GW10, GW11, GW12, GW13 | GW10 | — |
| Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | TOT | Defender | £4.9m | 15.78 | GW9, GW11, GW12, GW13 | — | — |
| Jacquet | GW3: 5, GW4: 9, GW5: 6, GW6: 3, GW7: 3 | LIV | Defender | £5.1m | 15.69 | GW10, GW11, GW12, GW13 | — | — |
| Muharemović | GW3: 4, GW4: 7, GW5: 6, GW6: 2, GW7: 5 | LEE | Defender | £5.0m | 14.94 | GW10, GW12 | — | — |
| O'Shea | GW4: 1, GW5: 2, GW6: 11, GW7: 3, GW8: 2 | IPS | Defender | £4.0m | 13.69 | GW9, GW13 | — | — |
| Isak | GW3: 13, GW4: 2, GW5: 8, GW6: 0, GW7: 9 | LIV | Forward | £9.0m | 19.90 | GW9, GW10, GW11, GW12, GW13 | GW11 | GW13 |
| Thiago | GW3: 2, GW4: 1, GW5: 5, GW6: 4, GW7: 4 | BRE | Forward | £7.8m | 17.37 | GW9, GW10, GW11, GW12 | — | — |
| J.Angulo | GW3: 0, GW4: 0, GW5: 0, GW6: 1, GW7: 0 | SUN | Forward | £4.5m | 1.04 | Bench | — | — |
| Kinsky | GW4: 7, GW5: 2, GW6: 3, GW7: 2, GW8: 9 | TOT | Goalkeeper | £4.4m | 13.83 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Phillips | GW3: 0, GW4: 0, GW5: 0, GW6: 0, GW7: 0 | HUL | Goalkeeper | £4.0m | 0.42 | Bench | — | — |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | £11.7m | 22.63 | GW9, GW10, GW11, GW12, GW13 | GW9, GW12 | GW11 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | £7.9m | 21.28 | GW9, GW10, GW11, GW12, GW13 | GW13 | GW9, GW12 |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | £8.0m | 19.54 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Doku | GW4: 0, GW5: 1, GW6: 12, GW7: 6, GW8: 2 | MCI | Midfielder | £7.5m | 18.56 | GW9, GW10, GW11, GW13 | — | — |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | ARS | Midfielder | £7.4m | 18.42 | GW9, GW10, GW11, GW12, GW13 | — | GW10 |

Squad cost: £99.1m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £7.9m | 21.62 | GW9, GW10, GW11, GW12, GW13 | GW10 | GW11 |
| Bassey | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | FUL | Defender | £4.5m | 13.76 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Egan | GW3: 6, GW4: 2, GW5: 1, GW6: 1, GW7: 4 | HUL | Defender | £4.1m | 11.28 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | EVE | Defender | £5.5m | 9.80 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Furlong | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | IPS | Defender | £3.9m | 0.75 | Bench | — | — |
| Thiago | GW3: 2, GW4: 1, GW5: 5, GW6: 4, GW7: 4 | BRE | Forward | £7.8m | 17.37 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Havertz | GW4: 1, GW5: 2, GW6: 2, GW7: 2, GW8: 1 | ARS | Forward | £7.5m | 13.78 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Mheuka | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | CHE | Forward | £4.5m | 0.41 | Bench | — | — |
| Leno | GW4: 9, GW5: 3, GW6: 2, GW7: 6, GW8: 8 | FUL | Goalkeeper | £4.5m | 12.27 | GW10, GW11, GW12, GW13 | — | — |
| Horníček | GW3: 2, GW4: 1, GW5: 3, GW6: 0, GW7: 2 | NEW | Goalkeeper | £5.0m | 11.63 | GW9 | — | — |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | £11.7m | 22.63 | GW9, GW10, GW11, GW12, GW13 | GW9, GW11, GW12 | GW10, GW13 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | £7.9m | 21.28 | GW9, GW10, GW11, GW12, GW13 | GW13 | GW9, GW12 |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | £8.0m | 19.54 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Cherki | GW4: 1, GW5: 8, GW6: 10, GW7: 0, GW8: 0 | MCI | Midfielder | £8.0m | 16.77 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | MCI | Midfielder | £8.2m | 0.00 | Bench | — | — |

Squad cost: £99.0m.

## One-transfer recommendation

**Semenyo → Doku** (projected weighted XI+captain gain 9.31).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Doku | GW4: 0, GW5: 1, GW6: 12, GW7: 6, GW8: 2 | £8.2m | £7.5m | £0.9m | 9.31 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | £8.2m | £7.4m | £1.0m | 9.16 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Barcola | GW3: 1, GW4: 3, GW5: 3, GW6: 2, GW7: 4 | £8.2m | £8.0m | £0.4m | 8.72 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Mbeumo | GW3: 8, GW4: 2, GW5: 2, GW6: 8, GW7: 8 | £8.2m | £7.9m | £0.5m | 8.37 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Wirtz | GW3: 3, GW4: 3, GW5: 6, GW6: 2, GW7: 5 | £8.2m | £7.2m | £1.2m | 8.34 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Groß | GW3: 1, GW4: 17, GW5: 14, GW6: 6, GW7: 5 | £8.2m | £6.2m | £2.2m | 6.81 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Neto | GW4: 2, GW5: 2, GW6: 5, GW7: 15, GW8: 3 | £8.2m | £6.6m | £1.8m | 6.65 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Ødegaard | GW4: 3, GW5: 2, GW6: 1, GW7: 3, GW8: 3 | £8.2m | £6.8m | £1.6m | 6.58 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Tavernier | GW3: 10, GW4: 8, GW5: 2, GW6: 1, GW7: 10 | £8.2m | £6.3m | £2.1m | 6.54 |
| Semenyo | GW4: 3, GW5: 17, GW6: 3, GW7: 1, GW8: 0 | Rayan | GW3: 2, GW4: 2, GW5: 2, GW6: 2, GW7: 3 | £8.2m | £6.3m | £2.1m | 6.35 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
