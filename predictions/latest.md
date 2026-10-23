# FPL predictions: 2026-2027, GW9

Last generated: 2026-10-23 20:03 UTC

Data commit: `37c0fe4bd10642509c962052e506f6126928cfab`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW8: 0/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, BHA, BOU, BRE, CHE, COV, CRY, EVE, FUL, HUL, IPS, LEE, LIV, MCI, MUN, NEW, NFO, SUN, TOT are deferred.

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
| De Cuyper | BHA | Defender | GW4: 11, GW5: 6, GW6: 15, GW7: 6 | 38 | 9.50 | 4 |
| Haaland | MCI | Forward | GW4: 9, GW5: 6, GW6: 6, GW7: 13 | 34 | 8.50 | 4 |
| Vuskovic | BHA | Defender | GW4: 6, GW5: 8, GW6: 8, GW7: 11 | 33 | 8.25 | 4 |
| Kostoulas | BHA | Forward | GW4: 10, GW5: 10, GW6: 1, GW7: 12 | 33 | 8.25 | 4 |
| Manzambi | AVL | Midfielder | GW4: 1, GW5: 13, GW6: 5, GW7: 11 | 30 | 7.50 | 4 |
| Verbruggen | BHA | Goalkeeper | GW4: 8, GW5: 6, GW6: 9, GW7: 6 | 29 | 7.25 | 4 |
| Raya | ARS | Goalkeeper | GW4: 14, GW5: 1, GW6: 3, GW7: 9 | 27 | 6.75 | 4 |
| Boscagli | BHA | Defender | GW4: 6, GW5: 6, GW6: 5, GW7: 10 | 27 | 6.75 | 4 |
| Ayari | BHA | Midfielder | GW4: 8, GW5: 3, GW6: 3, GW7: 13 | 27 | 6.75 | 4 |
| F.Kadıoğlu | BHA | Defender | GW4: 6, GW5: 5, GW6: 9, GW7: 6 | 26 | 6.50 | 4 |
| Evanilson | BOU | Forward | GW4: 5, GW5: 2, GW6: 7, GW7: 12 | 26 | 6.50 | 4 |
| João Pedro | CHE | Forward | GW4: 12, GW5: 0, GW6: 12, GW7: 2 | 26 | 6.50 | 4 |
| Tarkowski | EVE | Defender | GW4: 8, GW5: 14, GW6: 3, GW7: 0 | 25 | 6.25 | 4 |
| Schade | BRE | Midfielder | GW4: 15, GW5: 9, GW6: 1, GW7: 0 | 25 | 6.25 | 4 |
| Belloumi | HUL | Midfielder | GW4: 13, GW5: 4, GW6: 6, GW7: 2 | 25 | 6.25 | 4 |
| Neto | CHE | Midfielder | GW4: 2, GW5: 2, GW6: 5, GW7: 15 | 24 | 6.00 | 4 |
| Semenyo | MCI | Midfielder | GW4: 3, GW5: 17, GW6: 3, GW7: 1 | 24 | 6.00 | 4 |
| Gomez | BHA | Midfielder | GW4: 3, GW5: 8, GW6: 5, GW7: 8 | 24 | 6.00 | 4 |
| Henderson | CHE | Midfielder | GW4: 0, GW5: 2, GW6: 18, GW7: 3 | 23 | 5.75 | 4 |

Last 5 GW points are recorded current-season FPL totals, oldest to newest. Zero-point weeks are included. Double Gameweeks combine multiple matches; fewer entries mean fewer completed Gameweeks are available.

## Top GW9 player forecasts

| Player | Last 5 GW points | Club | Pos | GW9 | GW10 | GW11 | GW12 | GW13 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | 5.60 | 5.64 | 5.36 | 5.90 | 5.60 | 22.45 | 1.90 | high | 5-GW avg pts 1.60; mins 90; xGI 0.26; current GWs 7; fixture Elo diff +48 |
| Haaland | GW3: 9, GW4: 9, GW5: 6, GW6: 6, GW7: 13 | MCI | Forward | 5.20 | 5.32 | 5.85 | 3.38 | 5.85 | 20.55 | 1.31 | high | 5-GW avg pts 8.60; mins 88; xGI 1.01; current GWs 7; fixture Elo diff +103 |
| Thiago | GW3: 2, GW4: 1, GW5: 5, GW6: 4, GW7: 4 | BRE | Forward | 4.96 | 4.43 | 4.87 | 3.93 | 2.93 | 17.35 | 2.22 | high | 5-GW avg pts 3.20; mins 90; xGI 0.46; current GWs 7; fixture Elo diff -53 |
| Gabriel | GW3: 2, GW4: 9, GW5: 1, GW6: 2, GW7: 8 | ARS | Defender | 4.87 | 5.78 | 5.09 | 4.23 | 5.09 | 20.17 | 2.55 | high | 5-GW avg pts 4.40; mins 90; xGI 0.19; current GWs 7; fixture Elo diff +246 |
| Doku | GW3: 0, GW4: 0, GW5: 1, GW6: 12, GW7: 6 | MCI | Midfielder | 4.76 | 4.45 | 4.81 | 3.46 | 4.81 | 17.92 | 2.39 | high | 5-GW avg pts 3.80; mins 25; xGI 0.24; current GWs 7; fixture Elo diff +103 |
| Rice | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | ARS | Midfielder | 4.68 | 5.75 | 4.83 | 4.40 | 4.83 | 19.69 | 2.70 | high | 5-GW avg pts 5.60; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +246 |
| Palmer | GW3: 1, GW4: 5, GW5: 2, GW6: 8, GW7: 2 | CHE | Midfielder | 4.63 | 5.13 | 5.15 | 5.01 | 5.15 | 19.96 | 2.04 | high | 5-GW avg pts 3.60; mins 89; xGI 0.22; current GWs 7; fixture Elo diff +16 |
| Mbeumo | GW3: 8, GW4: 2, GW5: 2, GW6: 8, GW7: 8 | MUN | Midfielder | 4.47 | 4.59 | 4.41 | 4.68 | 4.47 | 18.09 | 2.29 | high | 5-GW avg pts 5.60; mins 90; xGI 0.43; current GWs 7; fixture Elo diff +48 |
| João Pedro | GW3: 1, GW4: 12, GW5: 0, GW6: 12, GW7: 2 | CHE | Forward | 4.42 | 4.69 | 5.14 | 4.59 | 5.14 | 19.05 | 2.41 | high | 5-GW avg pts 5.40; mins 68; xGI 0.28; current GWs 7; fixture Elo diff +16 |
| Van Hecke | GW3: 8, GW4: 8, GW5: 6, GW6: 3, GW7: 4 | TOT | Defender | 4.42 | 4.05 | 5.42 | 4.21 | 4.19 | 17.87 | 3.65 | high | 5-GW avg pts 5.80; mins 90; xGI 0.20; current GWs 7; fixture Elo diff +19 |
| E.Le Fée | GW3: 8, GW4: 0, GW5: 5, GW6: 2, GW7: 4 | SUN | Midfielder | 4.36 | 3.55 | 3.26 | 3.83 | 3.26 | 14.80 | 2.60 | high | 5-GW avg pts 3.80; mins 88; xGI 0.62; current GWs 7; fixture Elo diff -84 |
| O'Shea | GW3: 3, GW4: 1, GW5: 2, GW6: 11, GW7: 3 | IPS | Defender | 4.19 | 3.41 | 2.86 | 3.23 | 3.93 | 14.16 | 3.54 | high | 5-GW avg pts 4.00; mins 90; xGI 0.07; current GWs 7; fixture Elo diff -113 |
| Isak | GW3: 13, GW4: 2, GW5: 8, GW6: 0, GW7: 9 | LIV | Forward | 4.18 | 4.85 | 5.73 | 4.85 | 5.99 | 20.12 | 2.24 | high | 5-GW avg pts 6.40; mins 62; xGI 0.38; current GWs 7; fixture Elo diff +46 |
| Rogers | GW3: 6, GW4: 8, GW5: 2, GW6: 9, GW7: 2 | CHE | Midfielder | 4.11 | 4.58 | 4.87 | 4.55 | 4.80 | 18.20 | 2.27 | high | 5-GW avg pts 5.40; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +16 |
| Botman | GW3: 1, GW4: 2, GW5: 4, GW6: 8, GW7: 3 | NEW | Defender | 4.07 | 3.85 | 2.67 | 3.62 | 3.40 | 14.25 | 2.85 | high | 5-GW avg pts 3.60; mins 90; xGI 0.08; current GWs 7; fixture Elo diff -50 |
| Richards | GW3: 1, GW4: 2, GW5: 8, GW6: 4, GW7: 2 | CRY | Defender | 4.07 | 3.28 | 4.37 | 4.45 | 3.54 | 15.75 | 3.21 | high | 5-GW avg pts 3.40; mins 90; xGI 0.04; current GWs 7; fixture Elo diff +61 |
| Khalaili | GW3: 3, GW4: 7, GW5: 6, GW6: 2, GW7: 0 | CRY | Defender | 4.05 | 3.46 | 4.24 | 4.32 | 3.71 | 15.81 | 3.16 | high | 5-GW avg pts 3.60; mins 90; xGI 0.32; current GWs 7; fixture Elo diff +61 |
| N.Jackson | GW3: 2, GW4: 0, GW5: 6, GW6: 9, GW7: 2 | AVL | Forward | 4.05 | 3.96 | 4.35 | 4.21 | 4.01 | 16.45 | 2.49 | high | 5-GW avg pts 3.80; mins 79; xGI 0.44; current GWs 7; fixture Elo diff +139 |
| Calafiori | GW3: 2, GW4: 6, GW5: 1, GW6: 9, GW7: 6 | ARS | Defender | 4.05 | 4.29 | 4.10 | 3.46 | 4.10 | 16.06 | 2.68 | high | 5-GW avg pts 4.80; mins 83; xGI 0.30; current GWs 7; fixture Elo diff +246 |
| Tavernier | GW3: 10, GW4: 8, GW5: 2, GW6: 1, GW7: 10 | BOU | Midfielder | 4.04 | 4.04 | 4.07 | 3.89 | 3.91 | 16.00 | 2.58 | high | 5-GW avg pts 6.20; mins 79; xGI 0.65; current GWs 7; fixture Elo diff +89 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£98.9m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW3: 2, GW4: 9, GW5: 1, GW6: 2, GW7: 8 | ARS | Defender | £7.9m | 20.17 | GW9, GW10, GW11, GW12, GW13 | GW10 | GW9 |
| Van Hecke | GW3: 8, GW4: 8, GW5: 6, GW6: 3, GW7: 4 | TOT | Defender | £4.9m | 17.87 | GW9, GW10, GW11, GW12, GW13 | — | GW11 |
| Silva | GW3: 1, GW4: 3, GW5: 3, GW6: 0, GW7: 8 | BOU | Defender | £5.0m | 16.39 | GW9, GW10, GW11 | — | — |
| Richards | GW3: 1, GW4: 2, GW5: 8, GW6: 4, GW7: 2 | CRY | Defender | £4.9m | 15.75 | GW9, GW11, GW12 | — | — |
| O'Shea | GW3: 3, GW4: 1, GW5: 2, GW6: 11, GW7: 3 | IPS | Defender | £4.0m | 14.16 | GW9, GW13 | — | — |
| Isak | GW3: 13, GW4: 2, GW5: 8, GW6: 0, GW7: 9 | LIV | Forward | £9.0m | 20.12 | GW9, GW10, GW11, GW12, GW13 | GW11, GW13 | — |
| João Pedro | GW3: 1, GW4: 12, GW5: 0, GW6: 12, GW7: 2 | CHE | Forward | £7.9m | 19.05 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Kusi-Asare | GW3: 0, GW4: 0, GW5: 0, GW6: 0, GW7: 0 | FUL | Forward | £4.4m | 0.33 | Bench | — | — |
| Suzuki | GW3: 10, GW4: 2, GW5: 2, GW6: 2, GW7: 8 | AVL | Goalkeeper | £5.0m | 13.81 | GW9, GW11, GW12, GW13 | — | — |
| Petrović | GW3: 1, GW4: 1, GW5: 2, GW6: 0, GW7: 6 | BOU | Goalkeeper | £4.5m | 12.98 | GW10 | — | — |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | £11.8m | 22.45 | GW9, GW10, GW11, GW12, GW13 | GW9, GW12 | GW13 |
| Palmer | GW3: 1, GW4: 5, GW5: 2, GW6: 8, GW7: 2 | CHE | Midfielder | £9.8m | 19.96 | GW9, GW10, GW11, GW12, GW13 | — | GW12 |
| Rice | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | ARS | Midfielder | £7.3m | 19.69 | GW9, GW10, GW11, GW12, GW13 | — | GW10 |
| Wirtz | GW3: 3, GW4: 3, GW5: 6, GW6: 2, GW7: 5 | LIV | Midfielder | £7.2m | 17.68 | GW10, GW11, GW12, GW13 | — | — |
| Iwobi | GW3: 2, GW4: 3, GW5: 5, GW6: 4, GW7: 11 | FUL | Midfielder | £5.4m | 16.15 | GW10, GW12, GW13 | — | — |

Squad cost: £99.0m.

## Your current squad

| Player | Last 5 GW points | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | GW3: 2, GW4: 9, GW5: 1, GW6: 2, GW7: 8 | ARS | Defender | £7.9m | 20.17 | GW9, GW10, GW11, GW12, GW13 | GW10 | GW11 |
| Branthwaite | GW3: 3, GW4: 6, GW5: 8, GW6: 3, GW7: 1 | EVE | Defender | £5.5m | 14.90 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Bassey | GW3: 1, GW4: 6, GW5: 6, GW6: 2, GW7: 8 | FUL | Defender | £4.5m | 12.23 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Egan | GW3: 6, GW4: 2, GW5: 1, GW6: 1, GW7: 4 | HUL | Defender | £4.1m | 11.36 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Furlong | GW3: 0, GW4: 0, GW5: 0, GW6: 0, GW7: 0 | IPS | Defender | £3.9m | 0.75 | Bench | — | — |
| Thiago | GW3: 2, GW4: 1, GW5: 5, GW6: 4, GW7: 4 | BRE | Forward | £7.8m | 17.35 | GW9, GW10, GW11, GW12, GW13 | — | GW9 |
| Havertz | GW3: 8, GW4: 1, GW5: 2, GW6: 2, GW7: 2 | ARS | Forward | £7.5m | 15.96 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Mheuka | GW3: 0, GW4: 0, GW5: 0, GW6: 0, GW7: 0 | CHE | Forward | £4.5m | 0.41 | Bench | — | — |
| Leno | GW3: 1, GW4: 9, GW5: 3, GW6: 2, GW7: 6 | FUL | Goalkeeper | £4.5m | 11.47 | GW10, GW11, GW12, GW13 | — | — |
| Horníček | GW3: 2, GW4: 1, GW5: 3, GW6: 0, GW7: 2 | NEW | Goalkeeper | £5.0m | 11.44 | GW9 | — | — |
| B.Fernandes | GW3: 2, GW4: 2, GW5: 2, GW6: 1, GW7: 1 | MUN | Midfielder | £11.8m | 22.45 | GW9, GW10, GW11, GW12, GW13 | GW9, GW11, GW12, GW13 | GW10 |
| Rogers | GW3: 6, GW4: 8, GW5: 2, GW6: 9, GW7: 2 | CHE | Midfielder | £8.0m | 18.20 | GW9, GW10, GW11, GW12, GW13 | — | GW12 |
| Gibbs-White | GW3: 3, GW4: 8, GW5: 2, GW6: 2, GW7: 0 | NFO | Midfielder | £7.9m | 15.57 | GW9, GW10, GW11, GW12, GW13 | — | GW13 |
| Cherki | GW3: 3, GW4: 1, GW5: 8, GW6: 10, GW7: 0 | MCI | Midfielder | £8.0m | 12.36 | GW9, GW10, GW11, GW12, GW13 | — | — |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | MCI | Midfielder | £8.3m | 0.00 | Bench | — | — |

Squad cost: £99.2m.

## One-transfer recommendation

**Semenyo → Rice** (projected weighted XI+captain gain 9.40).

| Out | Last 5 GW points (out) | In | Last 5 GW points (in) | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Rice | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | £8.3m | £7.3m | £1.2m | 9.40 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Mbeumo | GW3: 8, GW4: 2, GW5: 2, GW6: 8, GW7: 8 | £8.3m | £7.9m | £0.6m | 7.80 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Barcola | GW3: 1, GW4: 3, GW5: 3, GW6: 2, GW7: 4 | £8.3m | £8.0m | £0.5m | 7.64 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Doku | GW3: 0, GW4: 0, GW5: 1, GW6: 12, GW7: 6 | £8.3m | £7.5m | £1.0m | 7.63 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Wirtz | GW3: 3, GW4: 3, GW5: 6, GW6: 2, GW7: 5 | £8.3m | £7.2m | £1.3m | 7.40 |
| Cherki | GW3: 3, GW4: 1, GW5: 8, GW6: 10, GW7: 0 | Rice | GW3: 5, GW4: 6, GW5: 1, GW6: 7, GW7: 9 | £7.9m | £7.3m | £0.8m | 7.32 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Groß | GW3: 1, GW4: 17, GW5: 14, GW6: 6, GW7: 5 | £8.3m | £6.2m | £2.3m | 5.87 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Iwobi | GW3: 2, GW4: 3, GW5: 5, GW6: 4, GW7: 11 | £8.3m | £5.4m | £3.1m | 5.87 |
| Cherki | GW3: 3, GW4: 1, GW5: 8, GW6: 10, GW7: 0 | Mbeumo | GW3: 8, GW4: 2, GW5: 2, GW6: 8, GW7: 8 | £7.9m | £7.9m | £0.2m | 5.72 |
| Semenyo | GW3: 6, GW4: 3, GW5: 17, GW6: 3, GW7: 1 | Tavernier | GW3: 10, GW4: 8, GW5: 2, GW6: 1, GW7: 10 | £8.3m | £6.2m | £2.3m | 5.72 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
