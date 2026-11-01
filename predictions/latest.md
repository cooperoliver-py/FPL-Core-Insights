# FPL predictions: 2026-2027, GW10

Last generated: 2026-11-01 06:39 UTC

Data commit: `aaff6e3af1735de0bb03ce7873056ef6ad0c0db0`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW9: 8/10 fixtures finished. Completed clubs contribute current-season form; ARS, EVE, LIV, NEW are deferred.

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
| N.Jackson | AVL | Forward | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | 39 | 7.80 | 5 |
| De Cuyper | BHA | Defender | GW5: 6, GW6: 15, GW7: 6, GW8: 1, GW9: 9 | 37 | 7.40 | 5 |
| Manzambi | AVL | Midfielder | GW5: 13, GW6: 5, GW7: 11, GW8: 1, GW9: 7 | 37 | 7.40 | 5 |
| Evanilson | BOU | Forward | GW5: 2, GW6: 7, GW7: 12, GW8: 6, GW9: 9 | 36 | 7.20 | 5 |
| Haaland | MCI | Forward | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | 35 | 7.00 | 5 |
| Van Hecke | TOT | Defender | GW5: 6, GW6: 3, GW7: 4, GW8: 7, GW9: 15 | 35 | 7.00 | 5 |
| Verbruggen | BHA | Goalkeeper | GW5: 6, GW6: 9, GW7: 6, GW8: 2, GW9: 11 | 34 | 6.80 | 5 |
| Vuskovic | BHA | Defender | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | 34 | 6.80 | 5 |
| Ayari | BHA | Midfielder | GW5: 3, GW6: 3, GW7: 13, GW8: 2, GW9: 10 | 31 | 6.20 | 5 |
| Hill | BOU | Defender | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | 30 | 6.00 | 5 |
| Iwobi | FUL | Midfielder | GW5: 5, GW6: 4, GW7: 11, GW8: 3, GW9: 6 | 29 | 5.80 | 5 |
| Rudoni | COV | Midfielder | GW5: 5, GW6: 7, GW7: 6, GW8: 2, GW9: 9 | 29 | 5.80 | 5 |
| Konsa | ARS | Defender | GW5: 1, GW6: 4, GW7: 9, GW8: 14 | 28 | 7.00 | 4 |
| Gabriel | ARS | Defender | GW5: 1, GW6: 2, GW7: 8, GW8: 17 | 28 | 7.00 | 4 |
| Neto | CHE | Midfielder | GW5: 2, GW6: 5, GW7: 15, GW8: 3, GW9: 3 | 28 | 5.60 | 5 |
| Groß | BHA | Midfielder | GW5: 14, GW6: 6, GW7: 5, GW8: 0, GW9: 2 | 27 | 5.40 | 5 |
| Silva | BOU | Defender | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | 27 | 5.40 | 5 |
| Thiago | BRE | Forward | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | 27 | 5.40 | 5 |
| Kostoulas | BHA | Forward | GW5: 10, GW6: 1, GW7: 12, GW8: 2, GW9: 2 | 27 | 5.40 | 5 |
| Ajer | BRE | Defender | GW5: 7, GW6: 6, GW7: 3, GW8: 2, GW9: 8 | 26 | 5.20 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW10 player forecasts

| Player | Last 5 GW points | Club | Pos | GW10 | GW11 | GW12 | GW13 | GW14 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | 6.66 | 5.17 | 4.77 | 5.17 | 5.86 | 22.27 | 2.78 | high | 5-GW avg pts 7.40; mins 90; xGI 0.24; current GWs 8; fixture Elo diff +273 |
| Haaland | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | MCI | Forward | 6.36 | 6.97 | 3.56 | 6.96 | 5.70 | 23.77 | 1.50 | high | 5-GW avg pts 7.00; mins 88; xGI 0.71; current GWs 9; fixture Elo diff +104 |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | 5.45 | 5.50 | 5.44 | 5.50 | 4.28 | 21.17 | 2.61 | high | 5-GW avg pts 4.60; mins 89; xGI 0.33; current GWs 9; fixture Elo diff +17 |
| Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | BOU | Defender | 5.22 | 4.52 | 4.50 | 3.94 | 5.22 | 18.77 | 3.41 | high | 5-GW avg pts 6.00; mins 90; xGI 0.04; current GWs 9; fixture Elo diff +142 |
| Evanilson | GW5: 2, GW6: 7, GW7: 12, GW8: 6, GW9: 9 | BOU | Forward | 5.01 | 3.98 | 3.77 | 3.74 | 5.22 | 17.36 | 2.71 | high | 5-GW avg pts 7.20; mins 84; xGI 0.68; current GWs 9; fixture Elo diff +142 |
| Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | BOU | Defender | 4.98 | 4.31 | 4.12 | 3.67 | 4.96 | 17.70 | 3.54 | high | 5-GW avg pts 5.40; mins 90; xGI 0.11; current GWs 9; fixture Elo diff +142 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | 4.85 | 5.27 | 4.85 | 5.81 | 4.64 | 20.32 | 2.21 | high | 5-GW avg pts 5.60; mins 65; xGI 0.41; current GWs 8; fixture Elo diff +93 |
| Konsa | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | ARS | Defender | 4.74 | 3.76 | 3.62 | 3.76 | 4.42 | 16.30 | 3.47 | high | 5-GW avg pts 6.80; mins 90; xGI 0.13; current GWs 8; fixture Elo diff +273 |
| Garner | GW4: 4, GW5: 3, GW6: 4, GW7: 2, GW8: 3 | EVE | Midfielder | 4.72 | 3.66 | 3.22 | 3.18 | 4.06 | 15.26 | 2.54 | high | 5-GW avg pts 3.20; mins 90; xGI 0.15; current GWs 8; fixture Elo diff -25 |
| Palmer | GW5: 2, GW6: 8, GW7: 2, GW8: -1, GW9: 8 | CHE | Midfielder | 4.63 | 4.76 | 4.71 | 4.76 | 3.80 | 18.28 | 1.87 | high | 5-GW avg pts 3.80; mins 87; xGI 0.37; current GWs 9; fixture Elo diff +17 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | 4.63 | 5.07 | 3.98 | 2.96 | 3.17 | 16.34 | 2.10 | high | 5-GW avg pts 5.40; mins 90; xGI 0.56; current GWs 9; fixture Elo diff -83 |
| Tavernier | GW5: 2, GW6: 1, GW7: 10, GW8: 10, GW9: 3 | BOU | Midfielder | 4.61 | 4.20 | 4.00 | 3.98 | 4.68 | 17.18 | 2.60 | high | 5-GW avg pts 5.20; mins 80; xGI 0.51; current GWs 9; fixture Elo diff +142 |
| Rayan | GW5: 2, GW6: 2, GW7: 3, GW8: 10, GW9: 3 | BOU | Midfielder | 4.56 | 4.41 | 4.38 | 4.05 | 4.57 | 17.60 | 2.79 | high | 5-GW avg pts 4.00; mins 88; xGI 0.44; current GWs 9; fixture Elo diff +142 |
| Barry | GW4: 2, GW5: 6, GW6: 6, GW7: 2, GW8: 2 | EVE | Forward | 4.51 | 3.85 | 3.39 | 3.35 | 4.05 | 15.47 | 2.76 | high | 5-GW avg pts 3.60; mins 89; xGI 0.57; current GWs 8; fixture Elo diff -25 |
| Mbeumo | GW5: 2, GW6: 8, GW7: 8, GW8: 2, GW9: 1 | MUN | Midfielder | 4.50 | 4.33 | 4.52 | 4.35 | 5.48 | 18.34 | 2.32 | high | 5-GW avg pts 4.20; mins 90; xGI 0.43; current GWs 9; fixture Elo diff +82 |
| B.Fernandes | GW5: 2, GW6: 1, GW7: 1, GW8: 0, GW9: 2 | MUN | Midfielder | 4.49 | 4.43 | 4.51 | 4.41 | 5.16 | 18.27 | 1.56 | high | 5-GW avg pts 1.20; mins 72; xGI 0.23; current GWs 9; fixture Elo diff +82 |
| Dewsbury-Hall | GW4: 2, GW5: 3, GW6: 13, GW7: 2, GW8: 2 | EVE | Midfielder | 4.43 | 3.53 | 3.22 | 3.14 | 3.86 | 14.70 | 2.23 | high | 5-GW avg pts 4.40; mins 89; xGI 0.32; current GWs 8; fixture Elo diff -25 |
| Virgil | GW4: 8, GW5: 8, GW6: 0, GW7: 4, GW8: 9 | LIV | Defender | 4.37 | 4.04 | 4.37 | 4.77 | 3.95 | 17.21 | 2.69 | high | 5-GW avg pts 5.80; mins 90; xGI 0.02; current GWs 8; fixture Elo diff +93 |
| Rúben | GW5: 1, GW6: 6, GW7: 1, GW8: 1, GW9: 2 | MCI | Defender | 4.34 | 4.47 | 2.88 | 4.45 | 3.69 | 16.00 | 2.91 | high | 5-GW avg pts 2.20; mins 90; xGI 0.11; current GWs 9; fixture Elo diff +104 |
| Ødegaard | GW4: 3, GW5: 2, GW6: 1, GW7: 3, GW8: 3 | ARS | Midfielder | 4.33 | 3.72 | 3.48 | 3.72 | 4.28 | 15.64 | 2.33 | high | 5-GW avg pts 2.40; mins 85; xGI 0.42; current GWs 8; fixture Elo diff +273 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.0m**. Current squad selling value: **£97.9m**. Total available funds: **£98.9m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £8.0m | 22.27 | GW10, GW11, GW12, GW13, GW14 | GW10, GW14 | — |
| Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | BOU | Defender | £5.5m | 18.77 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | BOU | Defender | £5.0m | 17.70 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Muharemović | GW5: 6, GW6: 2, GW7: 5, GW8: 9, GW9: 3 | LEE | Defender | £5.1m | 16.55 | GW10, GW12, GW14 | — | — |
| Konsa | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | ARS | Defender | £4.7m | 16.30 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Haaland | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | MCI | Forward | £15.8m | 23.77 | GW10, GW11, GW13, GW14 | GW11, GW13 | GW10, GW14 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | £9.2m | 20.32 | GW10, GW11, GW12, GW13, GW14 | — | GW13 |
| N.Jackson | GW5: 6, GW6: 9, GW7: 2, GW8: 13, GW9: 9 | AVL | Forward | £7.0m | 18.24 | GW10, GW11, GW12, GW13, GW14 | — | GW12 |
| Petrović | GW5: 2, GW6: 0, GW7: 6, GW8: 7, GW9: 6 | BOU | Goalkeeper | £4.5m | 14.37 | GW10, GW14 | — | — |
| Kinsky | GW5: 2, GW6: 3, GW7: 2, GW8: 9, GW9: 6 | TOT | Goalkeeper | £4.4m | 13.74 | GW11, GW12, GW13 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | £8.1m | 21.17 | GW10, GW11, GW12, GW13, GW14 | GW12 | GW11 |
| Gibbs-White | GW5: 2, GW6: 2, GW7: 0, GW8: 2, GW9: 2 | NFO | Midfielder | £7.9m | 18.16 | GW11, GW12, GW13, GW14 | — | — |
| Tonali | GW5: 2, GW6: 7, GW7: 4, GW8: 5, GW9: 3 | TOT | Midfielder | £5.3m | 16.37 | GW10, GW11, GW12, GW13 | — | — |
| Hughes | GW5: 0, GW6: 0, GW7: 1, GW8: 0, GW9: 1 | CRY | Midfielder | £4.3m | 3.23 | Bench | — | — |
| Reed | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | FUL | Midfielder | £4.3m | 0.65 | Bench | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £8.0m | 22.27 | GW10, GW11, GW12, GW13, GW14 | GW10, GW14 | GW11 |
| Bassey | GW5: 6, GW6: 2, GW7: 8, GW8: 8, GW9: 1 | FUL | Defender | £4.5m | 12.58 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Egan | GW5: 1, GW6: 1, GW7: 4, GW8: 4, GW9: 1 | HUL | Defender | £4.1m | 8.59 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | EVE | Defender | £5.5m | 4.48 | Bench | — | — |
| Furlong | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | IPS | Defender | £3.9m | 0.56 | Bench | — | — |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | £7.8m | 16.34 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Havertz | GW4: 1, GW5: 2, GW6: 2, GW7: 2, GW8: 1 | ARS | Forward | £7.4m | 12.50 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Mheuka | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Horníček | GW4: 1, GW5: 3, GW6: 0, GW7: 2, GW8: 8 | NEW | Goalkeeper | £5.0m | 12.18 | GW10, GW11, GW12, GW14 | — | — |
| Leno | GW5: 3, GW6: 2, GW7: 6, GW8: 8, GW9: 2 | FUL | Goalkeeper | £4.5m | 11.80 | GW13 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 9 | CHE | Midfielder | £8.1m | 21.17 | GW10, GW11, GW12, GW13, GW14 | GW11, GW12 | GW10, GW13 |
| B.Fernandes | GW5: 2, GW6: 1, GW7: 1, GW8: 0, GW9: 2 | MUN | Midfielder | £11.7m | 18.27 | GW10, GW11, GW12, GW13, GW14 | — | GW14 |
| Gibbs-White | GW5: 2, GW6: 2, GW7: 0, GW8: 2, GW9: 2 | NFO | Midfielder | £7.9m | 18.16 | GW10, GW11, GW12, GW13, GW14 | GW13 | GW12 |
| Cherki | GW5: 8, GW6: 10, GW7: 0, GW8: 0, GW9: 1 | MCI | Midfielder | £7.9m | 15.59 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | ARS | Midfielder | £7.4m | 8.96 | GW10, GW11, GW12, GW13, GW14 | — | — |

Squad cost: £98.2m.

## One-transfer recommendation

**Branthwaite → Hill** (projected weighted XI+captain gain 10.77).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | £5.5m | £5.5m | £1.0m | 10.77 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | £5.5m | £5.0m | £1.5m | 9.70 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Mbeumo | GW5: 2, GW6: 8, GW7: 8, GW8: 2, GW9: 1 | £7.4m | £7.9m | £0.5m | 9.38 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Virgil | GW4: 8, GW5: 8, GW6: 0, GW7: 4, GW8: 9 | £5.5m | £6.4m | £0.1m | 9.21 |
| Egan | GW5: 1, GW6: 1, GW7: 4, GW8: 4, GW9: 1 | Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | £4.1m | £5.0m | £0.1m | 9.11 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Rayan | GW5: 2, GW6: 2, GW7: 3, GW8: 10, GW9: 3 | £7.4m | £6.3m | £2.1m | 8.64 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Muharemović | GW5: 6, GW6: 2, GW7: 5, GW8: 9, GW9: 3 | £5.5m | £5.1m | £1.4m | 8.54 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Van Hecke | GW5: 6, GW6: 3, GW7: 4, GW8: 7, GW9: 15 | £5.5m | £5.0m | £1.5m | 8.26 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Tavernier | GW5: 2, GW6: 1, GW7: 10, GW8: 10, GW9: 3 | £7.4m | £6.6m | £1.8m | 8.22 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Rúben | GW5: 1, GW6: 6, GW7: 1, GW8: 1, GW9: 2 | £5.5m | £5.5m | £1.0m | 8.00 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
