# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-11 06:14 UTC

Data commit: `7a279fb621de381f8f78ee01c897efac220b4d9a`

## Data freshness

**⚠️ Some relevant Premier League fixtures are not complete.**

- GW6: 6/10 fixtures finished. Completed clubs contribute current-season form; COV, CRY, EVE, HUL, LIV, MCI, NEW, NFO are deferred.

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

XI + captain is measured before autosubs; archived exclusions are omitted from forecast-skill metrics. These frozen forecasts may come from earlier model versions.

## Top GW7 player forecasts

| Player | Club | Pos | GW7 | GW8 | GW9 | GW10 | GW11 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Haaland | MCI | Forward | 7.51 | 5.16 | 5.93 | 5.71 | 6.18 | 24.60 | 1.58 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +163 |
| Cherki | MCI | Midfielder | 5.49 | 4.09 | 4.23 | 4.11 | 4.23 | 17.97 | 2.30 | high | 5-GW avg pts 6.80; mins 60; xGI 0.45; current GWs 5; fixture Elo diff +163 |
| Silva | BOU | Defender | 5.30 | 4.19 | 4.96 | 5.12 | 4.97 | 19.60 | 3.92 | high | 5-GW avg pts 2.20; mins 90; xGI 0.32; current GWs 6; fixture Elo diff +90 |
| Palmer | CHE | Midfielder | 5.30 | 5.56 | 4.98 | 5.18 | 5.59 | 21.26 | 2.19 | high | 5-GW avg pts 4.60; mins 89; xGI 0.34; current GWs 6; fixture Elo diff +25 |
| B.Fernandes | MUN | Midfielder | 5.19 | 5.51 | 5.02 | 5.20 | 4.80 | 20.68 | 1.74 | high | 5-GW avg pts 6.00; mins 90; xGI 0.74; current GWs 6; fixture Elo diff +49 |
| Iwobi | FUL | Midfielder | 5.12 | 4.78 | 3.50 | 3.95 | 3.42 | 17.04 | 3.16 | high | 5-GW avg pts 3.20; mins 81; xGI 0.35; current GWs 6; fixture Elo diff +28 |
| Thiago | BRE | Forward | 5.00 | 5.63 | 5.44 | 4.91 | 5.39 | 21.08 | 2.70 | high | 5-GW avg pts 2.80; mins 90; xGI 0.48; current GWs 6; fixture Elo diff +54 |
| Mbeumo | MUN | Midfielder | 4.79 | 4.99 | 4.63 | 4.81 | 4.64 | 19.13 | 2.42 | high | 5-GW avg pts 6.20; mins 90; xGI 0.70; current GWs 6; fixture Elo diff +49 |
| Anderson | MCI | Midfielder | 4.73 | 3.58 | 3.88 | 4.11 | 4.14 | 16.41 | 2.60 | high | 5-GW avg pts 3.00; mins 83; xGI 0.16; current GWs 5; fixture Elo diff +163 |
| Gabriel | ARS | Defender | 4.64 | 5.22 | 4.40 | 6.15 | 4.48 | 19.85 | 2.51 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +283 |
| Saka | ARS | Midfielder | 4.58 | 4.90 | 4.43 | 6.28 | 4.55 | 19.66 | 2.05 | high | 5-GW avg pts 5.00; mins 88; xGI 0.79; current GWs 6; fixture Elo diff +283 |
| Guéhi | MCI | Defender | 4.45 | 3.31 | 3.73 | 3.89 | 4.04 | 15.56 | 2.59 | high | 5-GW avg pts 6.00; mins 90; xGI 0.27; current GWs 5; fixture Elo diff +163 |
| Groß | BHA | Midfielder | 4.42 | 3.70 | 3.64 | 4.38 | 5.69 | 17.15 | 2.86 | high | 5-GW avg pts 10.20; mins 90; xGI 0.56; current GWs 6; fixture Elo diff +31 |
| Gibbs-White | NFO | Midfielder | 4.40 | 6.16 | 4.81 | 4.53 | 4.72 | 19.79 | 2.47 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -55 |
| Havertz | ARS | Forward | 4.39 | 4.91 | 4.30 | 4.98 | 4.33 | 18.34 | 2.44 | high | 5-GW avg pts 3.00; mins 82; xGI 0.38; current GWs 6; fixture Elo diff +283 |
| Semenyo | MCI | Midfielder | 4.38 | 2.34 | 2.78 | 2.44 | 2.87 | 12.14 | 1.45 | high | 5-GW avg pts 6.60; mins 90; xGI 0.30; current GWs 5; fixture Elo diff +163 |
| Rúben | MCI | Defender | 4.36 | 3.09 | 3.54 | 3.96 | 3.98 | 15.14 | 2.75 | high | 5-GW avg pts 3.40; mins 90; xGI 0.21; current GWs 5; fixture Elo diff +163 |
| Cunha | MUN | Midfielder | 4.33 | 4.71 | 4.21 | 4.48 | 4.13 | 17.55 | 2.22 | high | 5-GW avg pts 6.80; mins 84; xGI 0.26; current GWs 6; fixture Elo diff +49 |
| Van Hecke | TOT | Defender | 4.29 | 3.36 | 3.83 | 3.86 | 4.36 | 15.69 | 3.20 | high | 5-GW avg pts 5.20; mins 90; xGI 0.22; current GWs 6; fixture Elo diff +31 |
| Hill | BOU | Defender | 4.26 | 3.57 | 3.96 | 4.27 | 4.04 | 16.04 | 2.92 | high | 5-GW avg pts 2.60; mins 90; xGI 0.16; current GWs 6; fixture Elo diff +90 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.6m**. Current squad selling value: **£98.5m**. Total available funds: **£99.1m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.85 | GW7, GW8, GW9, GW10, GW11 | GW10 | — |
| Silva | BOU | Defender | £5.0m | 19.60 | GW7, GW8, GW9, GW10, GW11 | — | GW7 |
| Van Hecke | TOT | Defender | £4.9m | 15.69 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Diop | IPS | Defender | £4.0m | 13.03 | GW9 | — | — |
| Davis | IPS | Defender | £4.0m | 12.93 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 24.60 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW11 | GW10 |
| Thiago | BRE | Forward | £7.8m | 21.08 | GW7, GW8, GW9, GW10, GW11 | — | GW8, GW9 |
| Havertz | ARS | Forward | £7.5m | 18.34 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Raya | ARS | Goalkeeper | £6.1m | 15.61 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Matthews | CRY | Goalkeeper | £4.0m | 0.33 | Bench | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 19.79 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 19.13 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Groß | BHA | Midfielder | £6.0m | 17.15 | GW7, GW10, GW11 | — | GW11 |
| Iwobi | FUL | Midfielder | £5.4m | 17.04 | GW7, GW8, GW10 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 14.94 | GW8, GW11 | — | — |

Squad cost: £99.1m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £7.9m | 19.85 | GW7, GW8, GW9, GW10, GW11 | GW10 | — |
| Branthwaite | EVE | Defender | £5.5m | 14.99 | GW7, GW9, GW10, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 13.28 | GW7, GW8, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 12.55 | GW8, GW9, GW11 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.72 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 21.08 | GW7, GW8, GW9, GW10, GW11 | GW9, GW11 | GW8 |
| Havertz | ARS | Forward | £7.5m | 18.34 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.88 | GW7, GW8, GW10, GW11 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.11 | GW9 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 20.68 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9, GW10, GW11 |
| Gibbs-White | NFO | Midfielder | £8.0m | 19.79 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Mbeumo | MUN | Midfielder | £7.9m | 19.13 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Cherki | MCI | Midfielder | £7.8m | 17.97 | GW7, GW8, GW9, GW10, GW11 | GW7 | — |
| Rogers | CHE | Midfielder | £7.8m | 17.08 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £98.6m.

## One-transfer recommendation

**Bassey → Silva** (projected weighted XI+captain gain 5.17).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Bassey | Silva | £4.5m | £5.0m | £0.1m | 5.17 |
| Branthwaite | Silva | £5.5m | £5.0m | £1.1m | 4.35 |
| Horníček | Pickford | £5.0m | £5.5m | £0.1m | 2.24 |
| Furlong | Ajer | £3.9m | £4.5m | £0.0m | 1.37 |
| Horníček | Donnarumma | £5.0m | £5.5m | £0.1m | 1.31 |
| Bassey | Van Hecke | £4.5m | £4.9m | £0.2m | 1.27 |
| Egan | Ajer | £4.1m | £4.5m | £0.2m | 1.06 |
| Horníček | Suzuki | £5.0m | £5.0m | £0.6m | 1.02 |
| Horníček | Tzolakis | £5.0m | £4.7m | £0.9m | 1.00 |
| Horníček | Verbruggen | £5.0m | £4.5m | £1.1m | 0.96 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
