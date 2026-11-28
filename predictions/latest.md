# FPL predictions: 2026-2027, GW13

Last generated: 2026-11-28 08:18 UTC

Data commit: `76c3f4312baa4244020eee878429db4de8919488`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW12: 1/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, BHA, BOU, BRE, COV, CRY, EVE, FUL, HUL, IPS, LEE, LIV, MCI, MUN, NEW, SUN, TOT are deferred.

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
| 9 | 1.100 | 1.908 | 0.760 | 5.25 | 1.78 | 62 | 47 |
| 10 | 1.148 | 2.067 | 0.759 | 4.80 | 1.83 | 70 | 55 |
| 11 | 1.277 | 2.327 | 0.718 | 2.90 | 1.91 | 45 | 35 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top 20 players over the last 5 Gameweeks

Ranked by recorded FPL points in GW8–GW12. Average is total divided by recorded Gameweeks, including zero-point weeks. Missing Gameweeks are not treated as zero. Injured and excluded players are included.

| Player | Club | Pos | GW points (oldest to newest) | Total | Average | GWs recorded |
| --- | --- | --- | --- | --- | --- | --- |
| McBurnie | HUL | Forward | GW8: 8, GW9: 12, GW10: 2, GW11: 13 | 35 | 8.75 | 4 |
| Hill | BOU | Defender | GW8: 11, GW9: 6, GW10: 4, GW11: 14 | 35 | 8.75 | 4 |
| Wirtz | LIV | Midfielder | GW8: 6, GW9: 2, GW10: 13, GW11: 14 | 35 | 8.75 | 4 |
| N.Jackson | AVL | Forward | GW8: 13, GW9: 9, GW10: 11, GW11: 2 | 35 | 8.75 | 4 |
| Konsa | ARS | Defender | GW8: 14, GW9: 10, GW10: 8, GW11: 1 | 33 | 8.25 | 4 |
| Gabriel | ARS | Defender | GW8: 17, GW9: 6, GW10: 8, GW11: 1 | 32 | 8.00 | 4 |
| Van Hecke | TOT | Defender | GW8: 7, GW9: 15, GW10: 4, GW11: 6 | 32 | 8.00 | 4 |
| Evanilson | BOU | Forward | GW8: 6, GW9: 9, GW10: 9, GW11: 6 | 30 | 7.50 | 4 |
| Roefs | SUN | Goalkeeper | GW8: 9, GW9: 1, GW10: 9, GW11: 11 | 30 | 7.50 | 4 |
| Barry | EVE | Forward | GW8: 2, GW9: 9, GW10: 16, GW11: 2 | 29 | 7.25 | 4 |
| Araujo | LIV | Defender | GW8: 10, GW9: 4, GW10: 7, GW11: 6 | 27 | 6.75 | 4 |
| Silva | BOU | Defender | GW8: 8, GW9: 8, GW10: 3, GW11: 8 | 27 | 6.75 | 4 |
| E.Le Fée | SUN | Midfielder | GW8: 3, GW9: 8, GW10: 11, GW11: 3 | 25 | 6.25 | 4 |
| O'Nien | SUN | Defender | GW8: 9, GW9: 4, GW10: 5, GW11: 6 | 24 | 6.00 | 4 |
| Tavernier | BOU | Midfielder | GW8: 10, GW9: 3, GW10: 3, GW11: 8 | 24 | 6.00 | 4 |
| Isak | LIV | Forward | GW8: 9, GW9: 2, GW10: 8, GW11: 5 | 24 | 6.00 | 4 |
| Gibbs-White | NFO | Midfielder | GW8: 2, GW9: 2, GW10: 5, GW11: 2, GW12: 13 | 24 | 4.80 | 5 |
| Kluivert | BOU | Midfielder | GW8: 6, GW9: 6, GW10: 3, GW11: 9 | 24 | 6.00 | 4 |
| Trafford | LEE | Goalkeeper | GW8: 10, GW9: 2, GW10: 10, GW11: 2 | 24 | 6.00 | 4 |
| Kinsky | TOT | Goalkeeper | GW8: 9, GW9: 6, GW10: 2, GW11: 7 | 24 | 6.00 | 4 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW13 player forecasts

| Player | Last 5 GW points | Club | Pos | GW13 | GW14 | GW15 | GW16 | GW17 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wirtz | GW7: 5, GW8: 6, GW9: 2, GW10: 13, GW11: 14 | LIV | Midfielder | 6.21 | 4.92 | 5.58 | 5.79 | 6.26 | 22.91 | 3.02 | high | 5-GW avg pts 8.00; mins 83; xGI 0.55; current GWs 11; fixture Elo diff +176 |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | 5.86 | 4.56 | 5.25 | 5.47 | 5.30 | 21.18 | 2.25 | high | 5-GW avg pts 6.60; mins 84; xGI 0.58; current GWs 11; fixture Elo diff +176 |
| Haaland | GW7: 13, GW8: 8, GW9: 2, GW10: 2, GW11: 2 | MCI | Forward | 5.39 | 5.00 | 5.30 | 6.19 | 5.00 | 21.46 | 1.37 | high | 5-GW avg pts 5.40; mins 90; xGI 0.73; current GWs 11; fixture Elo diff +204 |
| Rudoni | GW7: 6, GW8: 2, GW9: 9, GW10: 2, GW11: 10 | COV | Midfielder | 5.37 | 3.65 | 3.76 | 3.64 | 3.83 | 16.51 | 3.30 | high | 5-GW avg pts 5.80; mins 88; xGI 0.29; current GWs 11; fixture Elo diff -174 |
| Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | MCI | Midfielder | 4.75 | 4.31 | 4.58 | 5.30 | 4.31 | 18.59 | 2.48 | high | 5-GW avg pts 2.80; mins 87; xGI 0.40; current GWs 11; fixture Elo diff +204 |
| Gibbs-White | GW8: 2, GW9: 2, GW10: 5, GW11: 2, GW12: 13 | NFO | Midfielder | 4.72 | 4.10 | 4.37 | 4.63 | 3.70 | 17.37 | 2.23 | high | 5-GW avg pts 4.80; mins 90; xGI 0.59; current GWs 12; fixture Elo diff +56 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | 4.71 | 4.71 | 4.81 | 3.42 | 4.72 | 18.02 | 2.47 | high | 5-GW avg pts 7.40; mins 84; xGI 0.57; current GWs 11; fixture Elo diff +142 |
| Barcola | GW7: 4, GW8: 6, GW9: 1, GW10: 5, GW11: 5 | LIV | Midfielder | 4.63 | 3.47 | 4.55 | 4.50 | 4.20 | 17.07 | 2.11 | high | 5-GW avg pts 4.20; mins 79; xGI 0.63; current GWs 9; fixture Elo diff +176 |
| Ødegaard | GW7: 3, GW8: 3, GW9: 3, GW10: 11, GW11: 5 | ARS | Midfielder | 4.56 | 5.11 | 4.61 | 4.46 | 4.95 | 18.94 | 2.83 | high | 5-GW avg pts 5.00; mins 89; xGI 0.39; current GWs 11; fixture Elo diff +223 |
| Rogers | GW8: 1, GW9: 9, GW10: 2, GW11: 5, GW12: 2 | CHE | Midfielder | 4.50 | 3.85 | 2.82 | 3.99 | 4.36 | 15.64 | 1.88 | high | 5-GW avg pts 3.80; mins 90; xGI 0.32; current GWs 12; fixture Elo diff -22 |
| Palmer | GW8: -1, GW9: 8, GW10: 2, GW11: 2, GW12: 2 | CHE | Midfielder | 4.48 | 3.95 | 3.18 | 4.23 | 4.70 | 16.37 | 1.69 | high | 5-GW avg pts 2.60; mins 88; xGI 0.30; current GWs 12; fixture Elo diff -22 |
| Virgil | GW7: 4, GW8: 9, GW9: 1, GW10: 4, GW11: 6 | LIV | Defender | 4.39 | 3.50 | 4.32 | 4.36 | 4.14 | 16.54 | 2.58 | high | 5-GW avg pts 4.80; mins 90; xGI 0.13; current GWs 11; fixture Elo diff +176 |
| Araujo | GW7: 1, GW8: 10, GW9: 4, GW10: 7, GW11: 6 | LIV | Defender | 4.34 | 3.56 | 4.26 | 4.35 | 4.12 | 16.47 | 3.00 | high | 5-GW avg pts 5.60; mins 78; xGI 0.26; current GWs 11; fixture Elo diff +176 |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | 4.31 | 4.94 | 5.05 | 4.95 | 4.88 | 19.19 | 2.37 | high | 5-GW avg pts 8.00; mins 90; xGI 0.20; current GWs 11; fixture Elo diff +223 |
| Anderson | GW7: 1, GW8: 1, GW9: 4, GW10: 2, GW11: 10 | MCI | Midfielder | 4.30 | 3.72 | 3.89 | 4.41 | 3.72 | 16.07 | 2.59 | high | 5-GW avg pts 3.60; mins 75; xGI 0.26; current GWs 11; fixture Elo diff +204 |
| Enciso | GW7: 2, GW8: 10, GW9: 8, GW10: 1, GW11: 2 | IPS | Midfielder | 4.26 | 3.29 | 3.29 | 3.01 | 3.29 | 13.93 | 2.53 | high | 5-GW avg pts 4.60; mins 86; xGI 0.31; current GWs 11; fixture Elo diff -155 |
| Jacquet | GW7: 3, GW8: 8, GW9: 2, GW10: 4, GW11: 6 | LIV | Defender | 4.25 | 3.49 | 4.18 | 4.21 | 3.91 | 16.03 | 3.14 | high | 5-GW avg pts 4.60; mins 90; xGI 0.08; current GWs 11; fixture Elo diff +176 |
| Tavernier | GW7: 10, GW8: 10, GW9: 3, GW10: 3, GW11: 8 | BOU | Midfielder | 4.24 | 5.20 | 3.29 | 5.18 | 4.28 | 17.75 | 2.61 | high | 5-GW avg pts 6.80; mins 87; xGI 0.79; current GWs 11; fixture Elo diff +96 |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | ARS | Forward | 4.19 | 4.62 | 4.37 | 4.35 | 4.57 | 17.64 | 2.38 | high | 5-GW avg pts 3.80; mins 64; xGI 0.28; current GWs 11; fixture Elo diff +223 |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | 4.18 | 2.91 | 4.35 | 2.90 | 3.69 | 14.51 | 2.79 | high | 5-GW avg pts 7.20; mins 90; xGI 0.28; current GWs 11; fixture Elo diff -61 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£1.3m**. Current squad selling value: **£97.9m**. Total available funds: **£99.2m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£1.7m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | £8.1m | 19.19 | GW13, GW14, GW15, GW16, GW17 | — | — |
| Konsa | GW7: 9, GW8: 14, GW9: 10, GW10: 8, GW11: 1 | ARS | Defender | £4.9m | 17.09 | GW13, GW14, GW15, GW17 | — | — |
| De Cuyper | GW7: 6, GW8: 1, GW9: 9, GW10: 6, GW11: 1 | BHA | Defender | £5.6m | 17.07 | GW15, GW16, GW17 | — | — |
| Silva | GW7: 8, GW8: 8, GW9: 8, GW10: 3, GW11: 8 | BOU | Defender | £5.1m | 15.81 | GW14, GW16 | — | — |
| Van Hecke | GW7: 4, GW8: 7, GW9: 15, GW10: 4, GW11: 6 | TOT | Defender | £5.2m | 14.51 | GW13, GW15 | — | — |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | £9.4m | 21.18 | GW13, GW14, GW15, GW16, GW17 | — | GW13, GW15, GW17 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | £7.3m | 18.02 | GW13, GW14, GW15, GW17 | — | — |
| Evanilson | GW7: 12, GW8: 6, GW9: 9, GW10: 9, GW11: 6 | BOU | Forward | £6.6m | 17.30 | GW13, GW14, GW16 | GW14 | — |
| A.Becker | GW7: 2, GW8: 6, GW9: 2, GW10: 4, GW11: 7 | LIV | Goalkeeper | £5.5m | 14.95 | GW13, GW15, GW16, GW17 | — | — |
| Trafford | GW7: 2, GW8: 10, GW9: 2, GW10: 10, GW11: 2 | LEE | Goalkeeper | £5.1m | 12.29 | GW14 | — | — |
| Wirtz | GW7: 5, GW8: 6, GW9: 2, GW10: 13, GW11: 14 | LIV | Midfielder | £7.6m | 22.91 | GW13, GW14, GW15, GW16, GW17 | GW13, GW15, GW16, GW17 | — |
| Ødegaard | GW7: 3, GW8: 3, GW9: 3, GW10: 11, GW11: 5 | ARS | Midfielder | £6.7m | 18.94 | GW13, GW14, GW15, GW16, GW17 | — | — |
| Groß | GW7: 5, GW8: 0, GW9: 2, GW10: 10, GW11: 4 | BHA | Midfielder | £6.4m | 18.73 | GW14, GW15, GW16, GW17 | — | GW16 |
| Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | MCI | Midfielder | £7.5m | 18.59 | GW13, GW15, GW16, GW17 | — | — |
| Tavernier | GW7: 10, GW8: 10, GW9: 3, GW10: 3, GW11: 8 | BOU | Midfielder | £6.8m | 17.75 | GW13, GW14, GW16, GW17 | — | GW14 |

Squad cost: £97.8m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW7: 8, GW8: 17, GW9: 6, GW10: 8, GW11: 1 | ARS | Defender | £8.1m | 19.19 | GW13, GW14, GW15, GW16, GW17 | GW14 | — |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | FUL | Defender | £4.5m | 13.80 | GW13, GW14, GW15, GW16, GW17 | — | — |
| Branthwaite | GW7: 1, GW8: 0, GW9: 9, GW10: 3, GW11: 2 | EVE | Defender | £5.5m | 13.69 | GW13, GW14, GW15, GW16, GW17 | — | — |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | IPS | Defender | £3.9m | 8.73 | Bench | — | — |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | HUL | Defender | £4.0m | 6.30 | Bench | — | — |
| Isak | GW7: 9, GW8: 9, GW9: 2, GW10: 8, GW11: 5 | LIV | Forward | £9.4m | 21.18 | GW13, GW14, GW15, GW16, GW17 | — | GW13, GW15, GW16, GW17 |
| N.Jackson | GW7: 2, GW8: 13, GW9: 9, GW10: 11, GW11: 2 | AVL | Forward | £7.3m | 18.02 | GW13, GW14, GW15, GW16, GW17 | — | — |
| Havertz | GW7: 2, GW8: 1, GW9: 9, GW10: 2, GW11: 5 | ARS | Forward | £7.4m | 17.64 | GW13, GW14, GW15, GW16, GW17 | — | — |
| Leno | GW7: 6, GW8: 8, GW9: 2, GW10: 3, GW11: 2 | FUL | Goalkeeper | £4.5m | 13.11 | GW13, GW16, GW17 | — | — |
| Horníček | GW7: 2, GW8: 8, GW9: 3, GW10: 3, GW11: 1 | NEW | Goalkeeper | £5.0m | 12.77 | GW14, GW15 | — | — |
| Wirtz | GW7: 5, GW8: 6, GW9: 2, GW10: 13, GW11: 14 | LIV | Midfielder | £7.6m | 22.91 | GW13, GW14, GW15, GW16, GW17 | GW13, GW15, GW16, GW17 | GW14 |
| Rice | GW7: 9, GW8: 3, GW9: 8, GW10: 3, GW11: 3 | ARS | Midfielder | £7.5m | 17.42 | GW13, GW14, GW15, GW16, GW17 | — | — |
| Gibbs-White | GW8: 2, GW9: 2, GW10: 5, GW11: 2, GW12: 13 | NFO | Midfielder | £7.8m | 17.37 | GW13, GW14, GW15, GW16, GW17 | — | — |
| Rogers | GW8: 1, GW9: 9, GW10: 2, GW11: 5, GW12: 2 | CHE | Midfielder | £8.3m | 15.64 | GW13, GW14, GW16, GW17 | — | — |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | MUN | Midfielder | £7.8m | 13.53 | GW15 | — | — |

Squad cost: £98.6m.

## One-transfer recommendation

**Mbeumo → Groß** (projected weighted XI+captain gain 3.92).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | Groß | GW7: 5, GW8: 0, GW9: 2, GW10: 10, GW11: 4 | £7.8m | £6.4m | £2.7m | 3.92 |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | Doku | GW7: 6, GW8: 2, GW9: 2, GW10: 2, GW11: 2 | £7.8m | £7.5m | £1.6m | 3.65 |
| Branthwaite | GW7: 1, GW8: 0, GW9: 9, GW10: 3, GW11: 2 | De Cuyper | GW7: 6, GW8: 1, GW9: 9, GW10: 6, GW11: 1 | £5.5m | £5.6m | £1.2m | 3.38 |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | Silva | GW7: 8, GW8: 8, GW9: 8, GW10: 3, GW11: 8 | £4.0m | £5.1m | £0.2m | 3.37 |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | Silva | GW7: 8, GW8: 8, GW9: 8, GW10: 3, GW11: 8 | £3.9m | £5.1m | £0.1m | 3.37 |
| Bassey | GW7: 8, GW8: 8, GW9: 1, GW10: 2, GW11: 1 | De Cuyper | GW7: 6, GW8: 1, GW9: 9, GW10: 6, GW11: 1 | £4.5m | £5.6m | £0.2m | 3.27 |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | Jacquet | GW7: 3, GW8: 8, GW9: 2, GW10: 4, GW11: 6 | £4.0m | £5.1m | £0.2m | 3.27 |
| Furlong | GW7: 0, GW8: 0, GW9: 0, GW10: 0, GW11: 1 | Jacquet | GW7: 3, GW8: 8, GW9: 2, GW10: 4, GW11: 6 | £3.9m | £5.1m | £0.1m | 3.27 |
| Mbeumo | GW7: 8, GW8: 2, GW9: 1, GW10: 2, GW11: 1 | Tavernier | GW7: 10, GW8: 10, GW9: 3, GW10: 3, GW11: 8 | £7.8m | £6.8m | £2.3m | 3.05 |
| Egan | GW7: 4, GW8: 4, GW9: 1, GW10: 2, GW11: 0 | Kerkez | GW7: 2, GW8: 6, GW9: 1, GW10: 2, GW11: 6 | £4.0m | £5.2m | £0.1m | 3.03 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, or recursive future form.
