# FPL predictions: 2026-2027, GW10

Last generated: 2026-10-31 14:41 UTC

Data commit: `70f70217917038a4d934693b3e36fdaa4de6b9d0`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW9: 0/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, BHA, BOU, BRE, CHE, COV, CRY, EVE, FUL, HUL, IPS, LEE, LIV, MCI, MUN, NEW, NFO, SUN, TOT are deferred.

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

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top 20 players over the last 5 Gameweeks

Ranked by recorded FPL points in GW5–GW9. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | GW5: 6, GW6: 6, GW7: 13, GW8: 8 | 33 | 8.25 | 4 |
| N.Jackson | AVL | Forward | GW5: 6, GW6: 9, GW7: 2, GW8: 13 | 30 | 7.50 | 4 |
| Manzambi | AVL | Midfielder | GW5: 13, GW6: 5, GW7: 11, GW8: 1 | 30 | 7.50 | 4 |
| Konsa | ARS | Defender | GW5: 1, GW6: 4, GW7: 9, GW8: 14 | 28 | 7.00 | 4 |
| Gabriel | ARS | Defender | GW5: 1, GW6: 2, GW7: 8, GW8: 17 | 28 | 7.00 | 4 |
| De Cuyper | BHA | Defender | GW5: 6, GW6: 15, GW7: 6, GW8: 1 | 28 | 7.00 | 4 |
| Vuskovic | BHA | Defender | GW5: 8, GW6: 8, GW7: 11, GW8: 1 | 28 | 7.00 | 4 |
| Evanilson | BOU | Forward | GW5: 2, GW6: 7, GW7: 12, GW8: 6 | 27 | 6.75 | 4 |
| Isak | LIV | Forward | GW5: 8, GW6: 0, GW7: 9, GW8: 9 | 26 | 6.50 | 4 |
| Henderson | CHE | Midfielder | GW5: 2, GW6: 18, GW7: 3, GW8: 2 | 25 | 6.25 | 4 |
| Groß | BHA | Midfielder | GW5: 14, GW6: 6, GW7: 5, GW8: 0 | 25 | 6.25 | 4 |
| Neto | CHE | Midfielder | GW5: 2, GW6: 5, GW7: 15, GW8: 3 | 25 | 6.25 | 4 |
| Kostoulas | BHA | Forward | GW5: 10, GW6: 1, GW7: 12, GW8: 2 | 25 | 6.25 | 4 |
| Bassey | FUL | Defender | GW5: 6, GW6: 2, GW7: 8, GW8: 8 | 24 | 6.00 | 4 |
| Trafford | LEE | Goalkeeper | GW5: 10, GW6: 2, GW7: 2, GW8: 10 | 24 | 6.00 | 4 |
| Hill | BOU | Defender | GW5: 4, GW6: 2, GW7: 7, GW8: 11 | 24 | 6.00 | 4 |
| McGinn | AVL | Midfielder | GW5: 6, GW6: 10, GW7: 1, GW8: 6 | 23 | 5.75 | 4 |
| Iwobi | FUL | Midfielder | GW5: 5, GW6: 4, GW7: 11, GW8: 3 | 23 | 5.75 | 4 |
| Tavernier | BOU | Midfielder | GW5: 2, GW6: 1, GW7: 10, GW8: 10 | 23 | 5.75 | 4 |
| Verbruggen | BHA | Goalkeeper | GW5: 6, GW6: 9, GW7: 6, GW8: 2 | 23 | 5.75 | 4 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW10 player forecasts

| Player | Last 5 GW points | Club | Pos | GW10 | GW11 | GW12 | GW13 | GW14 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | 6.66 | 5.17 | 4.77 | 5.17 | 5.86 | 22.27 | 2.78 | high | 5-GW avg pts 7.40; mins 90; xGI 0.24; current GWs 8; fixture Elo diff +273 |
| Haaland | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | MCI | Forward | 6.52 | 7.14 | 3.56 | 7.03 | 5.79 | 24.19 | 1.53 | high | 5-GW avg pts 8.40; mins 88; xGI 0.78; current GWs 8; fixture Elo diff +104 |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | 5.52 | 5.54 | 5.56 | 5.54 | 4.57 | 21.58 | 2.66 | high | 5-GW avg pts 4.40; mins 89; xGI 0.24; current GWs 8; fixture Elo diff +17 |
| Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | BOU | Defender | 4.94 | 4.35 | 4.16 | 3.94 | 5.03 | 17.95 | 3.59 | high | 5-GW avg pts 4.40; mins 90; xGI 0.27; current GWs 8; fixture Elo diff +142 |
| Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | BOU | Defender | 4.89 | 4.13 | 4.25 | 3.59 | 4.78 | 17.39 | 3.16 | high | 5-GW avg pts 5.20; mins 90; xGI 0.04; current GWs 8; fixture Elo diff +142 |
| Evanilson | GW4: 5, GW5: 2, GW6: 7, GW7: 12, GW8: 6 | BOU | Forward | 4.85 | 4.01 | 3.83 | 3.69 | 5.06 | 17.15 | 2.72 | high | 5-GW avg pts 6.40; mins 87; xGI 0.62; current GWs 8; fixture Elo diff +142 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | 4.85 | 5.27 | 4.85 | 5.81 | 4.64 | 20.32 | 2.23 | high | 5-GW avg pts 5.60; mins 65; xGI 0.41; current GWs 8; fixture Elo diff +93 |
| Konsa | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | ARS | Defender | 4.74 | 3.76 | 3.62 | 3.76 | 4.42 | 16.30 | 3.47 | high | 5-GW avg pts 6.80; mins 90; xGI 0.13; current GWs 8; fixture Elo diff +273 |
| Garner | GW4: 4, GW5: 3, GW6: 4, GW7: 2, GW8: 3 | EVE | Midfielder | 4.72 | 3.66 | 3.22 | 3.21 | 4.06 | 15.28 | 2.55 | high | 5-GW avg pts 3.20; mins 90; xGI 0.15; current GWs 8; fixture Elo diff -25 |
| Tavernier | GW4: 8, GW5: 2, GW6: 1, GW7: 10, GW8: 10 | BOU | Midfielder | 4.61 | 4.11 | 4.03 | 3.87 | 4.79 | 17.12 | 2.63 | high | 5-GW avg pts 6.20; mins 78; xGI 0.62; current GWs 8; fixture Elo diff +142 |
| Thiago | GW4: 1, GW5: 5, GW6: 4, GW7: 4, GW8: 5 | BRE | Forward | 4.60 | 4.82 | 4.03 | 2.98 | 3.19 | 16.16 | 2.07 | high | 5-GW avg pts 3.80; mins 90; xGI 0.53; current GWs 8; fixture Elo diff -83 |
| Barry | GW4: 2, GW5: 6, GW6: 6, GW7: 2, GW8: 2 | EVE | Forward | 4.51 | 3.85 | 3.39 | 3.39 | 4.05 | 15.49 | 2.77 | high | 5-GW avg pts 3.60; mins 89; xGI 0.57; current GWs 8; fixture Elo diff -25 |
| Mbeumo | GW4: 2, GW5: 2, GW6: 8, GW7: 8, GW8: 2 | MUN | Midfielder | 4.49 | 4.44 | 4.53 | 4.46 | 5.35 | 18.45 | 2.33 | high | 5-GW avg pts 4.40; mins 90; xGI 0.48; current GWs 8; fixture Elo diff +82 |
| Dewsbury-Hall | GW4: 2, GW5: 3, GW6: 13, GW7: 2, GW8: 2 | EVE | Midfielder | 4.43 | 3.53 | 3.22 | 3.18 | 3.86 | 14.72 | 2.23 | high | 5-GW avg pts 4.40; mins 89; xGI 0.32; current GWs 8; fixture Elo diff -25 |
| Virgil | GW4: 8, GW5: 8, GW6: 0, GW7: 4, GW8: 9 | LIV | Defender | 4.37 | 4.04 | 4.37 | 4.77 | 3.95 | 17.21 | 2.69 | high | 5-GW avg pts 5.80; mins 90; xGI 0.02; current GWs 8; fixture Elo diff +93 |
| Ødegaard | GW4: 3, GW5: 2, GW6: 1, GW7: 3, GW8: 3 | ARS | Midfielder | 4.33 | 3.72 | 3.48 | 3.72 | 4.28 | 15.64 | 2.33 | high | 5-GW avg pts 2.40; mins 85; xGI 0.42; current GWs 8; fixture Elo diff +273 |
| Tarkowski | GW4: 8, GW5: 14, GW6: 3, GW7: 0, GW8: 2 | EVE | Defender | 4.32 | 3.39 | 2.86 | 2.88 | 3.55 | 13.81 | 2.23 | high | 5-GW avg pts 5.40; mins 90; xGI 0.02; current GWs 8; fixture Elo diff -25 |
| Rúben | GW4: 6, GW5: 1, GW6: 6, GW7: 1, GW8: 1 | MCI | Defender | 4.29 | 4.34 | 2.73 | 4.23 | 3.67 | 15.54 | 2.82 | high | 5-GW avg pts 3.00; mins 90; xGI 0.11; current GWs 8; fixture Elo diff +104 |
| Rayan | GW4: 2, GW5: 2, GW6: 2, GW7: 3, GW8: 10 | BOU | Midfielder | 4.22 | 4.19 | 4.16 | 3.79 | 4.31 | 16.56 | 2.63 | high | 5-GW avg pts 3.80; mins 87; xGI 0.50; current GWs 8; fixture Elo diff +142 |
| Pickford | GW4: 6, GW5: 8, GW6: 1, GW7: 2, GW8: 1 | EVE | Goalkeeper | 4.20 | 3.29 | 2.77 | 2.80 | 3.49 | 13.44 | 2.44 | high | 5-GW avg pts 3.60; mins 90; xGI 0.00; current GWs 8; fixture Elo diff -25 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.0m**. Current squad selling value: **£98.0m**. Total available funds: **£99.0m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £8.0m | 22.27 | GW10, GW11, GW12, GW13, GW14 | GW10, GW14 | — |
| Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | BOU | Defender | £5.0m | 17.95 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | BOU | Defender | £5.5m | 17.39 | GW10, GW11, GW12, GW14 | — | — |
| Konsa | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | ARS | Defender | £4.7m | 16.30 | GW10, GW13, GW14 | — | — |
| Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | TOT | Defender | £4.9m | 16.08 | GW10, GW11, GW12, GW13 | — | — |
| Haaland | GW4: 9, GW5: 6, GW6: 6, GW7: 13, GW8: 8 | MCI | Forward | £15.8m | 24.19 | GW10, GW11, GW13, GW14 | GW11, GW13 | GW10, GW14 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | £9.1m | 20.32 | GW10, GW11, GW12, GW13, GW14 | — | GW12, GW13 |
| Barry | GW4: 2, GW5: 6, GW6: 6, GW7: 2, GW8: 2 | EVE | Forward | £5.6m | 15.49 | GW10, GW14 | — | — |
| Petrović | GW4: 1, GW5: 2, GW6: 0, GW7: 6, GW8: 7 | BOU | Goalkeeper | £4.5m | 14.05 | GW10, GW14 | — | — |
| Kinsky | GW4: 7, GW5: 2, GW6: 3, GW7: 2, GW8: 9 | TOT | Goalkeeper | £4.4m | 13.36 | GW11, GW12, GW13 | — | — |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | £8.1m | 21.58 | GW10, GW11, GW12, GW13, GW14 | GW12 | GW11 |
| Mbeumo | GW4: 2, GW5: 2, GW6: 8, GW7: 8, GW8: 2 | MUN | Midfielder | £7.9m | 18.45 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Tonali | GW4: 3, GW5: 2, GW6: 7, GW7: 4, GW8: 5 | TOT | Midfielder | £5.3m | 15.70 | GW11, GW12, GW13 | — | — |
| Kamara | GW4: 2, GW5: 6, GW6: 4, GW7: 5, GW8: 4 | AVL | Midfielder | £5.0m | 15.55 | GW11, GW12, GW13 | — | — |
| Ampadu | GW4: 7, GW5: 5, GW6: 1, GW7: 1, GW8: 2 | LEE | Midfielder | £5.3m | 15.18 | GW12, GW14 | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £8.0m | 22.27 | GW10, GW11, GW12, GW13, GW14 | GW10, GW14 | GW11, GW12 |
| Bassey | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | FUL | Defender | £4.5m | 13.32 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Egan | GW4: 2, GW5: 1, GW6: 1, GW7: 4, GW8: 4 | HUL | Defender | £4.1m | 10.86 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | EVE | Defender | £5.5m | 4.48 | Bench | — | — |
| Furlong | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | IPS | Defender | £3.9m | 0.71 | Bench | — | — |
| Thiago | GW4: 1, GW5: 5, GW6: 4, GW7: 4, GW8: 5 | BRE | Forward | £7.8m | 16.16 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Havertz | GW4: 1, GW5: 2, GW6: 2, GW7: 2, GW8: 1 | ARS | Forward | £7.4m | 12.50 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Mheuka | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | CHE | Forward | £4.5m | 0.42 | Bench | — | — |
| Horníček | GW4: 1, GW5: 3, GW6: 0, GW7: 2, GW8: 8 | NEW | Goalkeeper | £5.0m | 12.22 | GW10, GW11, GW12, GW14 | — | — |
| Leno | GW4: 9, GW5: 3, GW6: 2, GW7: 6, GW8: 8 | FUL | Goalkeeper | £4.5m | 11.87 | GW13 | — | — |
| Rogers | GW4: 8, GW5: 2, GW6: 9, GW7: 2, GW8: 1 | CHE | Midfielder | £8.1m | 21.58 | GW10, GW11, GW12, GW13, GW14 | GW11, GW12, GW13 | GW10 |
| Gibbs-White | GW4: 8, GW5: 2, GW6: 2, GW7: 0, GW8: 2 | NFO | Midfielder | £7.9m | 17.46 | GW10, GW11, GW12, GW13, GW14 | — | GW13, GW14 |
| Cherki | GW4: 1, GW5: 8, GW6: 10, GW7: 0, GW8: 0 | MCI | Midfielder | £8.0m | 15.78 | GW10, GW11, GW12, GW13, GW14 | — | — |
| B.Fernandes | GW4: 2, GW5: 2, GW6: 1, GW7: 1, GW8: 0 | MUN | Midfielder | £11.7m | 11.48 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | ARS | Midfielder | £7.4m | 8.96 | GW10, GW11, GW12, GW13, GW14 | — | — |

Squad cost: £98.3m.

## One-transfer recommendation

**Branthwaite → Silva** (projected weighted XI+captain gain 9.54).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Silva | GW4: 3, GW5: 3, GW6: 0, GW7: 8, GW8: 8 | £5.5m | £5.0m | £1.5m | 9.54 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Mbeumo | GW4: 2, GW5: 2, GW6: 8, GW7: 8, GW8: 2 | £7.4m | £7.9m | £0.5m | 9.49 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Hill | GW4: 2, GW5: 4, GW6: 2, GW7: 7, GW8: 11 | £5.5m | £5.5m | £1.0m | 8.97 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Virgil | GW4: 8, GW5: 8, GW6: 0, GW7: 4, GW8: 9 | £5.5m | £6.4m | £0.1m | 8.80 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Tavernier | GW4: 8, GW5: 2, GW6: 1, GW7: 10, GW8: 10 | £7.4m | £6.5m | £1.9m | 8.16 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Barcola | GW4: 3, GW5: 3, GW6: 2, GW7: 4, GW8: 6 | £7.4m | £8.1m | £0.3m | 7.74 |
| Furlong | GW4: 0, GW5: 0, GW6: 0, GW7: 0, GW8: 0 | Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | £3.9m | £4.9m | £0.0m | 7.67 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | £5.5m | £4.9m | £1.6m | 7.67 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Rayan | GW4: 2, GW5: 2, GW6: 2, GW7: 3, GW8: 10 | £7.4m | £6.3m | £2.1m | 7.59 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | De Cuyper | GW4: 11, GW5: 6, GW6: 15, GW7: 6, GW8: 1 | £5.5m | £5.3m | £1.2m | 7.58 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
