# FPL predictions: 2026-2027, GW7

Last generated: 2026-10-10 20:16 UTC

Data commit: `75bee1dd774ba2257e05922f79e393c15652b4de`

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
| Silva | BOU | Defender | 5.31 | 4.19 | 4.94 | 5.08 | 4.90 | 19.53 | 3.91 | high | 5-GW avg pts 2.20; mins 90; xGI 0.34; current GWs 6; fixture Elo diff +90 |
| Gabriel | ARS | Defender | 4.75 | 5.33 | 4.51 | 6.30 | 4.59 | 20.31 | 2.54 | high | 5-GW avg pts 4.40; mins 90; xGI 0.13; current GWs 6; fixture Elo diff +283 |
| Anderson | MCI | Midfielder | 4.73 | 3.58 | 3.88 | 4.11 | 4.14 | 16.41 | 2.60 | high | 5-GW avg pts 3.00; mins 83; xGI 0.16; current GWs 5; fixture Elo diff +163 |
| Iwobi | FUL | Midfielder | 4.71 | 4.30 | 3.01 | 3.47 | 2.94 | 15.18 | 2.81 | high | 5-GW avg pts 3.20; mins 81; xGI 0.35; current GWs 6; fixture Elo diff +28 |
| Palmer | CHE | Midfielder | 4.66 | 4.83 | 4.26 | 4.62 | 4.87 | 18.58 | 1.92 | high | 5-GW avg pts 4.60; mins 89; xGI 0.34; current GWs 6; fixture Elo diff +25 |
| B.Fernandes | MUN | Midfielder | 4.59 | 4.34 | 4.23 | 4.24 | 4.12 | 17.33 | 1.46 | high | 5-GW avg pts 6.40; mins 88; xGI 0.73; current GWs 6; fixture Elo diff +49 |
| Saka | ARS | Midfielder | 4.58 | 4.90 | 4.43 | 6.28 | 4.55 | 19.66 | 2.05 | high | 5-GW avg pts 5.00; mins 88; xGI 0.77; current GWs 6; fixture Elo diff +283 |
| Havertz | ARS | Forward | 4.45 | 4.97 | 4.35 | 5.10 | 4.38 | 18.61 | 2.45 | high | 5-GW avg pts 3.00; mins 82; xGI 0.41; current GWs 6; fixture Elo diff +283 |
| Guéhi | MCI | Defender | 4.45 | 3.31 | 3.73 | 3.89 | 4.04 | 15.56 | 2.59 | high | 5-GW avg pts 6.00; mins 90; xGI 0.27; current GWs 5; fixture Elo diff +163 |
| Gibbs-White | NFO | Midfielder | 4.40 | 6.16 | 4.81 | 4.53 | 4.72 | 19.79 | 2.47 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -55 |
| Semenyo | MCI | Midfielder | 4.38 | 2.34 | 2.78 | 2.44 | 2.87 | 12.14 | 1.45 | high | 5-GW avg pts 6.60; mins 90; xGI 0.30; current GWs 5; fixture Elo diff +163 |
| Rúben | MCI | Defender | 4.36 | 3.09 | 3.54 | 3.96 | 3.98 | 15.14 | 2.75 | high | 5-GW avg pts 3.40; mins 90; xGI 0.21; current GWs 5; fixture Elo diff +163 |
| Groß | BHA | Midfielder | 4.33 | 3.57 | 3.46 | 4.31 | 5.57 | 16.66 | 2.82 | high | 5-GW avg pts 10.20; mins 90; xGI 0.51; current GWs 6; fixture Elo diff +31 |
| Thiago | BRE | Forward | 4.28 | 5.30 | 4.71 | 4.41 | 4.66 | 18.69 | 2.40 | high | 5-GW avg pts 2.80; mins 90; xGI 0.48; current GWs 6; fixture Elo diff +54 |
| Hill | BOU | Defender | 4.26 | 3.47 | 3.86 | 4.25 | 3.93 | 15.81 | 2.87 | high | 5-GW avg pts 2.60; mins 90; xGI 0.16; current GWs 6; fixture Elo diff +90 |
| Dewsbury-Hall | EVE | Midfielder | 4.03 | 3.20 | 3.96 | 4.94 | 3.96 | 15.91 | 2.41 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff -43 |
| King | FUL | Midfielder | 4.02 | 3.59 | 2.76 | 3.14 | 2.68 | 13.27 | 2.37 | high | 5-GW avg pts 3.80; mins 82; xGI 0.41; current GWs 6; fixture Elo diff +28 |
| Gvardiol | MCI | Defender | 3.99 | 3.17 | 3.44 | 3.55 | 3.76 | 14.34 | 2.52 | high | 5-GW avg pts 7.40; mins 87; xGI 0.19; current GWs 5; fixture Elo diff +163 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.6m**. Current squad selling value: **£98.7m**. Total available funds: **£99.3m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.1m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 20.31 | GW7, GW8, GW9, GW10, GW11 | GW10 | GW8 |
| Silva | BOU | Defender | £5.0m | 19.53 | GW7, GW8, GW9, GW10, GW11 | — | GW7, GW9 |
| Hill | BOU | Defender | £5.5m | 15.81 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Davis | IPS | Defender | £4.0m | 12.39 | GW9 | — | — |
| Giles | HUL | Defender | £4.0m | 11.60 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 24.60 | GW7, GW8, GW9, GW10, GW11 | GW7, GW9, GW11 | GW10 |
| Thiago | BRE | Forward | £7.8m | 18.69 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Havertz | ARS | Forward | £7.6m | 18.61 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Raya | ARS | Goalkeeper | £6.1m | 15.61 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Bentley | COV | Goalkeeper | £4.0m | 0.65 | Bench | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 19.79 | GW7, GW8, GW9, GW10, GW11 | GW8 | — |
| Stach | LEE | Midfielder | £6.0m | 17.25 | GW8, GW10, GW11 | — | — |
| Groß | BHA | Midfielder | £5.9m | 16.66 | GW7, GW10, GW11 | — | GW11 |
| Anderson | MCI | Midfielder | £6.3m | 16.41 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 15.18 | GW7, GW8 | — | — |

Squad cost: £99.2m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 20.31 | GW7, GW8, GW9, GW10, GW11 | GW10 | GW7, GW8 |
| Branthwaite | EVE | Defender | £5.5m | 14.99 | GW7, GW9, GW10, GW11 | — | — |
| Bassey | FUL | Defender | £4.5m | 12.63 | GW7, GW8, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 12.55 | GW8, GW9, GW11 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.62 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 18.69 | GW7, GW8, GW9, GW10, GW11 | — | GW9, GW11 |
| Havertz | ARS | Forward | £7.6m | 18.61 | GW7, GW8, GW9, GW10, GW11 | — | GW10 |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 12.29 | GW7, GW8, GW10, GW11 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 11.11 | GW9 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 19.79 | GW7, GW8, GW9, GW10, GW11 | GW8, GW9, GW11 | — |
| Cherki | MCI | Midfielder | £7.8m | 17.97 | GW7, GW8, GW9, GW10, GW11 | GW7 | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 17.33 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Rogers | CHE | Midfielder | £7.8m | 15.82 | GW7, GW8, GW9, GW10, GW11 | — | — |
| Mbeumo | MUN | Midfielder | £7.9m | 15.14 | GW7, GW8, GW9, GW10, GW11 | — | — |

Squad cost: £98.8m.

## One-transfer recommendation

**Bassey → Silva** (projected weighted XI+captain gain 5.89).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Bassey | Silva | £4.5m | £5.0m | £0.1m | 5.89 |
| Branthwaite | Silva | £5.5m | £5.0m | £1.1m | 4.49 |
| Horníček | Pickford | £5.0m | £5.5m | £0.1m | 2.39 |
| B.Fernandes | Saka | £11.9m | £9.6m | £2.9m | 2.33 |
| Mbeumo | Stach | £7.9m | £6.0m | £2.5m | 2.12 |
| Mbeumo | Groß | £7.9m | £5.9m | £2.6m | 2.03 |
| Horníček | Donnarumma | £5.0m | £5.5m | £0.1m | 1.64 |
| Rogers | Stach | £7.7m | £6.0m | £2.3m | 1.43 |
| Rogers | Groß | £7.7m | £5.9m | £2.4m | 1.35 |
| B.Fernandes | Palmer | £11.9m | £9.7m | £2.8m | 1.34 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
