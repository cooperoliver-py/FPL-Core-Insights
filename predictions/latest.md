# FPL predictions: 2026-2027, GW10

Last generated: 2026-10-31 20:12 UTC

Data commit: `533adbcaf9e3cb3f7dda7ae25b4182a64351399d`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW9: 6/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, CRY, EVE, FUL, LIV, NEW, TOT are deferred.

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
| De Cuyper | BHA | Defender | GW5: 6, GW6: 15, GW7: 6, GW8: 1, GW9: 9 | 37 | 7.40 | 5 |
| Evanilson | BOU | Forward | GW5: 2, GW6: 7, GW7: 12, GW8: 6, GW9: 9 | 36 | 7.20 | 5 |
| Haaland | MCI | Forward | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | 35 | 7.00 | 5 |
| Verbruggen | BHA | Goalkeeper | GW5: 6, GW6: 9, GW7: 6, GW8: 2, GW9: 11 | 34 | 6.80 | 5 |
| Vuskovic | BHA | Defender | GW5: 8, GW6: 8, GW7: 11, GW8: 1, GW9: 6 | 34 | 6.80 | 5 |
| Ayari | BHA | Midfielder | GW5: 3, GW6: 3, GW7: 13, GW8: 2, GW9: 10 | 31 | 6.20 | 5 |
| Hill | BOU | Defender | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | 30 | 6.00 | 5 |
| N.Jackson | AVL | Forward | GW5: 6, GW6: 9, GW7: 2, GW8: 13 | 30 | 7.50 | 4 |
| Manzambi | AVL | Midfielder | GW5: 13, GW6: 5, GW7: 11, GW8: 1 | 30 | 7.50 | 4 |
| Rudoni | COV | Midfielder | GW5: 5, GW6: 7, GW7: 6, GW8: 2, GW9: 9 | 29 | 5.80 | 5 |
| Konsa | ARS | Defender | GW5: 1, GW6: 4, GW7: 9, GW8: 14 | 28 | 7.00 | 4 |
| Gabriel | ARS | Defender | GW5: 1, GW6: 2, GW7: 8, GW8: 17 | 28 | 7.00 | 4 |
| Neto | CHE | Midfielder | GW5: 2, GW6: 5, GW7: 15, GW8: 3, GW9: 3 | 28 | 5.60 | 5 |
| Groß | BHA | Midfielder | GW5: 14, GW6: 6, GW7: 5, GW8: 0, GW9: 2 | 27 | 5.40 | 5 |
| Silva | BOU | Defender | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | 27 | 5.40 | 5 |
| Thiago | BRE | Forward | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | 27 | 5.40 | 5 |
| Kostoulas | BHA | Forward | GW5: 10, GW6: 1, GW7: 12, GW8: 2, GW9: 2 | 27 | 5.40 | 5 |
| Ajer | BRE | Defender | GW5: 7, GW6: 6, GW7: 3, GW8: 2, GW9: 8 | 26 | 5.20 | 5 |
| Tavernier | BOU | Midfielder | GW5: 2, GW6: 1, GW7: 10, GW8: 10, GW9: 3 | 26 | 5.20 | 5 |
| Boscagli | BHA | Defender | GW5: 6, GW6: 5, GW7: 10, GW8: -1, GW9: 6 | 26 | 5.20 | 5 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW10 player forecasts

| Player | Last 5 GW points | Club | Pos | GW10 | GW11 | GW12 | GW13 | GW14 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | 6.66 | 5.17 | 4.77 | 5.17 | 5.86 | 22.27 | 2.78 | high | 5-GW avg pts 7.40; mins 90; xGI 0.24; current GWs 8; fixture Elo diff +273 |
| Haaland | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | MCI | Forward | 6.32 | 6.79 | 3.41 | 6.78 | 5.69 | 23.32 | 1.48 | high | 5-GW avg pts 7.00; mins 88; xGI 0.75; current GWs 9; fixture Elo diff +104 |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 8 | CHE | Midfielder | 5.39 | 5.41 | 5.38 | 5.41 | 4.30 | 20.93 | 2.58 | high | 5-GW avg pts 4.40; mins 89; xGI 0.33; current GWs 9; fixture Elo diff +17 |
| Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | BOU | Defender | 5.06 | 4.36 | 4.43 | 3.83 | 5.00 | 18.21 | 3.31 | high | 5-GW avg pts 6.00; mins 90; xGI 0.04; current GWs 9; fixture Elo diff +142 |
| Evanilson | GW5: 2, GW6: 7, GW7: 12, GW8: 6, GW9: 9 | BOU | Forward | 5.01 | 3.93 | 3.76 | 3.69 | 5.22 | 17.27 | 2.74 | high | 5-GW avg pts 7.20; mins 84; xGI 0.68; current GWs 9; fixture Elo diff +142 |
| Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | BOU | Defender | 4.89 | 4.08 | 4.03 | 3.45 | 4.81 | 17.08 | 3.42 | high | 5-GW avg pts 5.40; mins 90; xGI 0.11; current GWs 9; fixture Elo diff +142 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | 4.85 | 5.27 | 4.85 | 5.81 | 4.64 | 20.32 | 2.23 | high | 5-GW avg pts 5.60; mins 65; xGI 0.41; current GWs 8; fixture Elo diff +93 |
| Palmer | GW5: 2, GW6: 8, GW7: 2, GW8: -1, GW9: 8 | CHE | Midfielder | 4.75 | 4.68 | 4.84 | 4.68 | 3.89 | 18.44 | 1.88 | high | 5-GW avg pts 3.80; mins 87; xGI 0.34; current GWs 9; fixture Elo diff +17 |
| Konsa | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | ARS | Defender | 4.74 | 3.76 | 3.62 | 3.76 | 4.42 | 16.30 | 3.47 | high | 5-GW avg pts 6.80; mins 90; xGI 0.13; current GWs 8; fixture Elo diff +273 |
| Garner | GW4: 4, GW5: 3, GW6: 4, GW7: 2, GW8: 3 | EVE | Midfielder | 4.72 | 3.66 | 3.22 | 3.21 | 4.06 | 15.28 | 2.55 | high | 5-GW avg pts 3.20; mins 90; xGI 0.15; current GWs 8; fixture Elo diff -25 |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | 4.63 | 5.02 | 3.95 | 2.91 | 3.11 | 16.22 | 2.08 | high | 5-GW avg pts 5.40; mins 90; xGI 0.56; current GWs 9; fixture Elo diff -83 |
| Tavernier | GW5: 2, GW6: 1, GW7: 10, GW8: 10, GW9: 3 | BOU | Midfielder | 4.61 | 4.12 | 4.00 | 3.90 | 4.68 | 17.06 | 2.62 | high | 5-GW avg pts 5.20; mins 80; xGI 0.51; current GWs 9; fixture Elo diff +142 |
| B.Fernandes | GW5: 2, GW6: 1, GW7: 1, GW8: 0, GW9: 2 | MUN | Midfielder | 4.51 | 4.37 | 4.47 | 4.33 | 5.02 | 18.06 | 1.54 | high | 5-GW avg pts 1.20; mins 72; xGI 0.24; current GWs 9; fixture Elo diff +82 |
| Barry | GW4: 2, GW5: 6, GW6: 6, GW7: 2, GW8: 2 | EVE | Forward | 4.51 | 3.85 | 3.39 | 3.39 | 4.05 | 15.49 | 2.77 | high | 5-GW avg pts 3.60; mins 89; xGI 0.57; current GWs 8; fixture Elo diff -25 |
| Rayan | GW5: 2, GW6: 2, GW7: 3, GW8: 10, GW9: 3 | BOU | Midfielder | 4.47 | 4.22 | 4.29 | 3.86 | 4.46 | 17.08 | 2.71 | high | 5-GW avg pts 4.00; mins 88; xGI 0.44; current GWs 9; fixture Elo diff +142 |
| Mbeumo | GW5: 2, GW6: 8, GW7: 8, GW8: 2, GW9: 1 | MUN | Midfielder | 4.46 | 4.29 | 4.48 | 4.31 | 5.44 | 18.19 | 2.30 | high | 5-GW avg pts 4.20; mins 90; xGI 0.43; current GWs 9; fixture Elo diff +82 |
| Dewsbury-Hall | GW4: 2, GW5: 3, GW6: 13, GW7: 2, GW8: 2 | EVE | Midfielder | 4.43 | 3.53 | 3.22 | 3.18 | 3.86 | 14.72 | 2.23 | high | 5-GW avg pts 4.40; mins 89; xGI 0.32; current GWs 8; fixture Elo diff -25 |
| Virgil | GW4: 8, GW5: 8, GW6: 0, GW7: 4, GW8: 9 | LIV | Defender | 4.37 | 4.04 | 4.37 | 4.77 | 3.95 | 17.21 | 2.69 | high | 5-GW avg pts 5.80; mins 90; xGI 0.02; current GWs 8; fixture Elo diff +93 |
| Ødegaard | GW4: 3, GW5: 2, GW6: 1, GW7: 3, GW8: 3 | ARS | Midfielder | 4.33 | 3.72 | 3.48 | 3.72 | 4.28 | 15.64 | 2.33 | high | 5-GW avg pts 2.40; mins 85; xGI 0.42; current GWs 8; fixture Elo diff +273 |
| Tarkowski | GW4: 8, GW5: 14, GW6: 3, GW7: 0, GW8: 2 | EVE | Defender | 4.32 | 3.39 | 2.86 | 2.88 | 3.55 | 13.81 | 2.23 | high | 5-GW avg pts 5.40; mins 90; xGI 0.02; current GWs 8; fixture Elo diff -25 |

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
| Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | BOU | Defender | £5.5m | 18.21 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | BOU | Defender | £5.0m | 17.08 | GW10, GW11, GW12, GW14 | — | — |
| Konsa | GW4: 6, GW5: 1, GW6: 4, GW7: 9, GW8: 14 | ARS | Defender | £4.7m | 16.30 | GW10, GW13, GW14 | — | — |
| Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | TOT | Defender | £4.9m | 16.02 | GW10, GW11, GW12, GW13 | — | — |
| Haaland | GW5: 6, GW6: 6, GW7: 13, GW8: 8, GW9: 2 | MCI | Forward | £15.8m | 23.32 | GW10, GW11, GW13, GW14 | GW11, GW13 | GW10, GW14 |
| Isak | GW4: 2, GW5: 8, GW6: 0, GW7: 9, GW8: 9 | LIV | Forward | £9.1m | 20.32 | GW10, GW11, GW12, GW13, GW14 | — | GW12, GW13 |
| Barry | GW4: 2, GW5: 6, GW6: 6, GW7: 2, GW8: 2 | EVE | Forward | £5.6m | 15.49 | GW10, GW14 | — | — |
| Petrović | GW5: 2, GW6: 0, GW7: 6, GW8: 7, GW9: 6 | BOU | Goalkeeper | £4.5m | 13.99 | GW10, GW14 | — | — |
| Kinsky | GW4: 7, GW5: 2, GW6: 3, GW7: 2, GW8: 9 | TOT | Goalkeeper | £4.4m | 13.59 | GW11, GW12, GW13 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 8 | CHE | Midfielder | £8.1m | 20.93 | GW10, GW11, GW12, GW13, GW14 | GW12 | GW11 |
| Mbeumo | GW5: 2, GW6: 8, GW7: 8, GW8: 2, GW9: 1 | MUN | Midfielder | £7.9m | 18.19 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Tonali | GW4: 3, GW5: 2, GW6: 7, GW7: 4, GW8: 5 | TOT | Midfielder | £5.3m | 15.68 | GW11, GW12, GW13 | — | — |
| Kamara | GW4: 2, GW5: 6, GW6: 4, GW7: 5, GW8: 4 | AVL | Midfielder | £5.0m | 15.42 | GW11, GW12, GW13 | — | — |
| Ampadu | GW5: 5, GW6: 1, GW7: 1, GW8: 2, GW9: 3 | LEE | Midfielder | £5.3m | 14.62 | GW12, GW14 | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW4: 9, GW5: 1, GW6: 2, GW7: 8, GW8: 17 | ARS | Defender | £8.0m | 22.27 | GW10, GW11, GW12, GW13, GW14 | GW10, GW14 | GW11 |
| Bassey | GW4: 6, GW5: 6, GW6: 2, GW7: 8, GW8: 8 | FUL | Defender | £4.5m | 13.32 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Egan | GW5: 1, GW6: 1, GW7: 4, GW8: 4, GW9: 1 | HUL | Defender | £4.1m | 8.48 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | EVE | Defender | £5.5m | 4.48 | Bench | — | — |
| Furlong | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | IPS | Defender | £3.9m | 0.56 | Bench | — | — |
| Thiago | GW5: 5, GW6: 4, GW7: 4, GW8: 5, GW9: 9 | BRE | Forward | £7.8m | 16.22 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Havertz | GW4: 1, GW5: 2, GW6: 2, GW7: 2, GW8: 1 | ARS | Forward | £7.4m | 12.50 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Mheuka | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | CHE | Forward | £4.5m | 0.38 | Bench | — | — |
| Horníček | GW4: 1, GW5: 3, GW6: 0, GW7: 2, GW8: 8 | NEW | Goalkeeper | £5.0m | 12.24 | GW10, GW11, GW12, GW14 | — | — |
| Leno | GW4: 9, GW5: 3, GW6: 2, GW7: 6, GW8: 8 | FUL | Goalkeeper | £4.5m | 11.87 | GW13 | — | — |
| Rogers | GW5: 2, GW6: 9, GW7: 2, GW8: 1, GW9: 8 | CHE | Midfielder | £8.1m | 20.93 | GW10, GW11, GW12, GW13, GW14 | GW11, GW12, GW13 | GW10 |
| B.Fernandes | GW5: 2, GW6: 1, GW7: 1, GW8: 0, GW9: 2 | MUN | Midfielder | £11.7m | 18.06 | GW10, GW11, GW12, GW13, GW14 | — | GW14 |
| Gibbs-White | GW5: 2, GW6: 2, GW7: 0, GW8: 2, GW9: 2 | NFO | Midfielder | £7.9m | 17.77 | GW10, GW11, GW12, GW13, GW14 | — | GW12, GW13 |
| Cherki | GW5: 8, GW6: 10, GW7: 0, GW8: 0, GW9: 1 | MCI | Midfielder | £8.0m | 16.16 | GW10, GW11, GW12, GW13, GW14 | — | — |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | ARS | Midfielder | £7.4m | 8.96 | GW10, GW11, GW12, GW13, GW14 | — | — |

Squad cost: £98.3m.

## One-transfer recommendation

**Branthwaite → Hill** (projected weighted XI+captain gain 10.21).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Hill | GW5: 4, GW6: 2, GW7: 7, GW8: 11, GW9: 6 | £5.5m | £5.5m | £1.0m | 10.21 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Mbeumo | GW5: 2, GW6: 8, GW7: 8, GW8: 2, GW9: 1 | £7.4m | £7.9m | £0.5m | 9.23 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Virgil | GW4: 8, GW5: 8, GW6: 0, GW7: 4, GW8: 9 | £5.5m | £6.4m | £0.1m | 9.21 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | £5.5m | £5.0m | £1.5m | 9.08 |
| Egan | GW5: 1, GW6: 1, GW7: 4, GW8: 4, GW9: 1 | Silva | GW5: 3, GW6: 0, GW7: 8, GW8: 8, GW9: 8 | £4.1m | £5.0m | £0.1m | 8.60 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Rayan | GW5: 2, GW6: 2, GW7: 3, GW8: 10, GW9: 3 | £7.4m | £6.3m | £2.1m | 8.12 |
| Rice | GW4: 6, GW5: 1, GW6: 7, GW7: 9, GW8: 3 | Tavernier | GW5: 2, GW6: 1, GW7: 10, GW8: 10, GW9: 3 | £7.4m | £6.5m | £1.9m | 8.10 |
| Furlong | GW5: 0, GW6: 0, GW7: 0, GW8: 0, GW9: 0 | Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | £3.9m | £4.9m | £0.0m | 8.02 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Van Hecke | GW4: 8, GW5: 6, GW6: 3, GW7: 4, GW8: 7 | £5.5m | £4.9m | £1.6m | 8.02 |
| Branthwaite | GW4: 6, GW5: 8, GW6: 3, GW7: 1, GW8: 0 | Jacquet | GW4: 9, GW5: 6, GW6: 3, GW7: 3, GW8: 8 | £5.5m | £5.1m | £1.4m | 7.81 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
