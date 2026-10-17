# FPL predictions: 2026-2027, GW8

Last generated: 2026-10-17 18:44 UTC

Data commit: `a16ede936aaca3ab4ec81f181136e9236195ccde`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW7: 4/10 fixtures finished. Completed clubs contribute current-season form; ARS, AVL, BHA, BOU, COV, CRY, LEE, MUN, NEW, NFO, SUN, TOT are deferred.

Incomplete Gameweeks are not scored in live performance reporting until the official data is finished and checked.

The model learns from 2025/26 and completed, checked current-season Gameweeks. An equal-weight blend balances the original features with recent participation, longer-window per-90 rates, set-piece roles and observed workload across league, cup, European and friendly matches. Five-GW forecast weights are [1.0, 0.9, 0.8, 0.7, 0.6]; prices remain fixed. Dated suspensions expire and later injury-return forecasts use a conservative historical recovery rate.

## Walk-forward evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.852 | 1.847 | 0.753 |
| Rolling points (5 GW) | 0.903 | 2.008 | 0.765 |
| Lagged FPL ep_next | 0.960 | 2.098 | 0.721 |

Evaluation covers 6,661 player-Gameweeks; 67.1% scored zero. Among 2,284 appearances, model MAE is 2.020 and Spearman is 0.370.

The predicted top 20 averaged 4.87 actual points versus 1.69 for the selectable pool.

## Live-season performance

| GW | MAE | RMSE | Spearman | Top 20 | Pool | XI + captain | FPL avg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.528 | 2.580 | 0.553 | 3.40 | 1.88 | 39 | 50 |
| 2 | 1.211 | 2.131 | 0.697 | 6.60 | 1.74 | 112 | 81 |
| 3 | 1.211 | 2.030 | 0.750 | 4.25 | 1.83 | 44 | 51 |
| 4 | 1.278 | 2.257 | 0.711 | 5.40 | 1.91 | 72 | 69 |
| 5 | 1.240 | 2.245 | 0.746 | 5.15 | 2.02 | 47 | 48 |
| 6 | 1.120 | 2.092 | 0.724 | 4.70 | 1.85 | 55 | 58 |

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW8 player forecasts

| Player | Club | Pos | GW8 | GW9 | GW10 | GW11 | GW12 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | 6.13 | 7.10 | 7.06 | 7.54 | 5.63 | 26.83 | 1.71 | high | 5-GW avg pts 8.60; mins 88; xGI 1.03; current GWs 7; fixture Elo diff +78 |
| Palmer | CHE | Midfielder | 6.04 | 5.37 | 5.96 | 6.06 | 6.10 | 23.54 | 2.43 | high | 5-GW avg pts 3.60; mins 89; xGI 0.22; current GWs 7; fixture Elo diff +21 |
| Iwobi | FUL | Midfielder | 5.33 | 3.51 | 4.27 | 3.46 | 4.10 | 16.80 | 3.11 | high | 5-GW avg pts 5.00; mins 81; xGI 0.52; current GWs 7; fixture Elo diff -39 |
| Isak | LIV | Forward | 5.18 | 4.42 | 4.97 | 5.11 | 5.03 | 19.73 | 2.19 | high | 5-GW avg pts 6.40; mins 62; xGI 0.37; current GWs 7; fixture Elo diff +25 |
| B.Fernandes | MUN | Midfielder | 5.04 | 4.68 | 4.88 | 4.70 | 4.99 | 19.43 | 1.65 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +41 |
| Gabriel | ARS | Defender | 5.03 | 4.56 | 5.64 | 4.74 | 3.88 | 19.28 | 2.44 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +253 |
| Calvert-Lewin | LEE | Forward | 5.00 | 3.73 | 4.24 | 3.89 | 4.89 | 17.41 | 2.90 | high | 5-GW avg pts 4.60; mins 84; xGI 0.59; current GWs 6; fixture Elo diff +22 |
| Thiago | BRE | Forward | 4.99 | 5.16 | 4.91 | 5.07 | 4.32 | 19.70 | 2.53 | high | 5-GW avg pts 3.20; mins 90; xGI 0.45; current GWs 7; fixture Elo diff +53 |
| João Pedro | CHE | Forward | 4.99 | 4.38 | 4.64 | 4.99 | 4.75 | 18.97 | 2.43 | high | 5-GW avg pts 5.40; mins 68; xGI 0.28; current GWs 7; fixture Elo diff +21 |
| Rogers | CHE | Midfielder | 4.89 | 4.22 | 4.89 | 4.96 | 4.89 | 19.01 | 2.41 | high | 5-GW avg pts 5.40; mins 88; xGI 0.24; current GWs 7; fixture Elo diff +21 |
| McAtee | NFO | Midfielder | 4.89 | 3.58 | 3.10 | 3.14 | 3.43 | 14.85 | 2.70 | high | 5-GW avg pts 2.60; mins 87; xGI 0.25; current GWs 6; fixture Elo diff -8 |
| Mbeumo | MUN | Midfielder | 4.88 | 4.30 | 4.72 | 4.52 | 4.65 | 18.48 | 2.37 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +41 |
| Rice | ARS | Midfielder | 4.66 | 4.13 | 4.86 | 4.20 | 3.90 | 17.55 | 2.40 | high | 5-GW avg pts 4.80; mins 87; xGI 0.15; current GWs 6; fixture Elo diff +253 |
| N.Williams | NFO | Defender | 4.60 | 3.30 | 2.72 | 3.26 | 3.39 | 14.07 | 2.81 | high | 5-GW avg pts 3.60; mins 90; xGI 0.29; current GWs 6; fixture Elo diff -8 |
| Cunha | MUN | Midfielder | 4.60 | 4.41 | 4.43 | 4.28 | 4.58 | 17.85 | 2.26 | high | 5-GW avg pts 6.80; mins 84; xGI 0.26; current GWs 6; fixture Elo diff +41 |
| Ajer | BRE | Defender | 4.58 | 3.64 | 3.38 | 3.64 | 3.13 | 14.98 | 3.33 | high | 5-GW avg pts 3.80; mins 90; xGI 0.09; current GWs 7; fixture Elo diff +53 |
| Muharemović | LEE | Defender | 4.56 | 3.68 | 4.58 | 3.77 | 5.19 | 17.30 | 3.46 | high | 5-GW avg pts 4.60; mins 90; xGI 0.09; current GWs 6; fixture Elo diff +22 |
| Bassey | FUL | Defender | 4.53 | 2.68 | 3.31 | 2.45 | 3.21 | 13.24 | 2.94 | high | 5-GW avg pts 4.60; mins 90; xGI 0.07; current GWs 7; fixture Elo diff -39 |
| Stach | LEE | Midfielder | 4.53 | 3.67 | 4.47 | 3.82 | 4.54 | 16.80 | 2.80 | high | 5-GW avg pts 3.20; mins 89; xGI 0.25; current GWs 6; fixture Elo diff +22 |
| Wirtz | LIV | Midfielder | 4.50 | 3.55 | 4.18 | 4.34 | 4.20 | 16.59 | 2.30 | high | 5-GW avg pts 3.80; mins 81; xGI 0.24; current GWs 7; fixture Elo diff +25 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.2m**. Current squad selling value: **£98.9m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Silva | BOU | Defender | £5.0m | 20.06 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Muharemović | LEE | Defender | £5.0m | 17.30 | GW8, GW10, GW12 | — | — |
| Hill | BOU | Defender | £5.5m | 17.10 | GW9, GW10, GW11 | — | — |
| Richards | CRY | Defender | £4.9m | 17.01 | GW8, GW9, GW11, GW12 | — | — |
| van Ewijk | COV | Defender | £3.9m | 9.73 | Bench | — | — |
| Haaland | MCI | Forward | £15.7m | 26.83 | GW8, GW9, GW10, GW11, GW12 | GW8, GW9, GW10, GW11 | GW12 |
| Thiago | BRE | Forward | £7.8m | 19.70 | GW8, GW9, GW10, GW11, GW12 | — | — |
| João Pedro | CHE | Forward | £7.8m | 18.97 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Donnarumma | MCI | Goalkeeper | £5.5m | 15.07 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Matthews | CRY | Goalkeeper | £4.0m | 0.39 | Bench | — | — |
| Palmer | CHE | Midfielder | £9.7m | 23.54 | GW8, GW9, GW10, GW11, GW12 | GW12 | GW8, GW9, GW10, GW11 |
| Rogers | CHE | Midfielder | £7.9m | 19.01 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Groß | BHA | Midfielder | £6.1m | 17.48 | GW9, GW10, GW11, GW12 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 16.80 | GW8, GW10 | — | — |
| Timber | CRY | Midfielder | £5.0m | 16.03 | GW8, GW9, GW11, GW12 | — | — |

Squad cost: £99.2m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.28 | GW8, GW9, GW10, GW11, GW12 | GW10 | GW8 |
| Branthwaite | EVE | Defender | £5.5m | 14.88 | GW9, GW10, GW11, GW12 | — | GW10 |
| Bassey | FUL | Defender | £4.5m | 13.24 | GW8, GW10, GW12 | — | — |
| Egan | HUL | Defender | £4.1m | 12.06 | GW8, GW9, GW11, GW12 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.77 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.70 | GW8, GW9, GW10, GW11, GW12 | GW9, GW11 | — |
| Havertz | ARS | Forward | £7.5m | 15.99 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.31 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.10 | GW8, GW10 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.45 | GW9, GW11, GW12 | — | — |
| B.Fernandes | MUN | Midfielder | £11.8m | 19.43 | GW8, GW9, GW10, GW11, GW12 | GW8, GW12 | GW9 |
| Rogers | CHE | Midfielder | £7.9m | 19.01 | GW8, GW9, GW10, GW11, GW12 | — | GW11, GW12 |
| Semenyo | MCI | Midfielder | £8.3m | 14.26 | GW8, GW9, GW10, GW11, GW12 | — | — |
| Cherki | MCI | Midfielder | £7.9m | 12.98 | GW8, GW9, GW10, GW11 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 12.91 | GW8, GW9, GW10, GW11, GW12 | — | — |

Squad cost: £99.1m.

## One-transfer recommendation

**B.Fernandes → Palmer** (projected weighted XI+captain gain 6.91).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| B.Fernandes | Palmer | £11.8m | £9.7m | £2.3m | 6.91 |
| Gibbs-White | Mbeumo | £8.0m | £7.8m | £0.4m | 5.57 |
| Cherki | Mbeumo | £7.8m | £7.8m | £0.2m | 5.39 |
| Gibbs-White | Groß | £8.0m | £6.1m | £2.1m | 5.06 |
| Branthwaite | Silva | £5.5m | £5.0m | £0.7m | 5.02 |
| Gibbs-White | Cunha | £8.0m | £7.9m | £0.3m | 4.94 |
| Cherki | Groß | £7.8m | £6.1m | £1.9m | 4.88 |
| Cherki | Cunha | £7.8m | £7.9m | £0.1m | 4.76 |
| Gibbs-White | Rice | £8.0m | £7.3m | £0.9m | 4.64 |
| Cherki | Rice | £7.8m | £7.3m | £0.7m | 4.47 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
