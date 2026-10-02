# FPL predictions: 2026-2027, GW6

Last generated: 2026-10-02 14:56 UTC

Data commit: `c0671578c2db7ab6e2a2df71d54707db5b75b804`

## Data freshness

All scheduled Premier League fixtures before GW6 are complete.

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

## Top GW6 player forecasts

| Player | Club | Pos | GW6 | GW7 | GW8 | GW9 | GW10 | 5GW score | 5GW value | History coverage | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 5.82 | 5.51 | 5.57 | 5.29 | 5.38 | 22.17 | 1.86 | high | 5-GW avg pts 6.20; mins 90; xGI 0.78; current GWs 5; fixture Elo diff +76 |
| Gibbs-White | NFO | Midfielder | 5.57 | 4.60 | 6.74 | 5.24 | 4.96 | 21.74 | 2.72 | high | 5-GW avg pts 5.60; mins 90; xGI 0.60; current GWs 5; fixture Elo diff -41 |
| Gabriel | ARS | Defender | 5.54 | 5.01 | 5.54 | 4.64 | 6.80 | 21.81 | 2.73 | high | 5-GW avg pts 5.00; mins 90; xGI 0.14; current GWs 5; fixture Elo diff +291 |
| Haaland | MCI | Forward | 5.30 | 7.86 | 5.35 | 6.11 | 6.01 | 24.53 | 1.57 | high | 5-GW avg pts 7.80; mins 90; xGI 0.99; current GWs 5; fixture Elo diff +144 |
| Pickford | EVE | Goalkeeper | 5.17 | 3.50 | 2.72 | 3.47 | 5.57 | 16.27 | 2.96 | high | 5-GW avg pts 5.00; mins 90; xGI 0.00; current GWs 5; fixture Elo diff +18 |
| Dewsbury-Hall | EVE | Midfielder | 5.14 | 4.22 | 3.28 | 4.15 | 5.19 | 17.59 | 2.67 | high | 5-GW avg pts 4.00; mins 90; xGI 0.36; current GWs 5; fixture Elo diff +18 |
| Tarkowski | EVE | Defender | 4.92 | 3.90 | 2.73 | 3.75 | 5.22 | 16.37 | 2.64 | high | 5-GW avg pts 8.60; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Cunha | MUN | Midfielder | 4.63 | 4.23 | 4.61 | 4.15 | 4.46 | 17.70 | 2.24 | high | 5-GW avg pts 5.20; mins 81; xGI 0.29; current GWs 5; fixture Elo diff +76 |
| Branthwaite | EVE | Defender | 4.59 | 3.88 | 2.70 | 3.75 | 4.93 | 15.83 | 2.88 | high | 5-GW avg pts 5.40; mins 90; xGI 0.04; current GWs 5; fixture Elo diff +18 |
| Mbeumo | MUN | Midfielder | 4.57 | 4.40 | 4.67 | 4.40 | 4.58 | 18.10 | 2.29 | high | 5-GW avg pts 5.00; mins 90; xGI 0.77; current GWs 5; fixture Elo diff +76 |
| Saka | ARS | Midfielder | 4.52 | 4.35 | 4.52 | 4.23 | 6.12 | 18.68 | 1.97 | high | 5-GW avg pts 6.40; mins 83; xGI 0.84; current GWs 5; fixture Elo diff +291 |
| Barry | EVE | Forward | 4.44 | 4.03 | 2.39 | 3.78 | 4.50 | 15.32 | 2.69 | high | 5-GW avg pts 4.00; mins 83; xGI 0.73; current GWs 5; fixture Elo diff +18 |
| Rogers | CHE | Midfielder | 4.43 | 4.25 | 4.40 | 4.16 | 4.25 | 17.24 | 2.24 | high | 5-GW avg pts 5.80; mins 87; xGI 0.59; current GWs 5; fixture Elo diff +10 |
| Thiago | BRE | Forward | 4.43 | 4.77 | 5.54 | 5.21 | 4.75 | 19.66 | 2.52 | high | 5-GW avg pts 2.00; mins 88; xGI 0.66; current GWs 5; fixture Elo diff +31 |
| Botman | NEW | Defender | 4.41 | 3.33 | 3.71 | 3.86 | 3.72 | 15.31 | 3.06 | high | 5-GW avg pts 3.00; mins 90; xGI 0.05; current GWs 5; fixture Elo diff +37 |
| Murillo | NFO | Defender | 4.36 | 3.05 | 4.47 | 3.71 | 3.21 | 15.21 | 2.77 | high | 5-GW avg pts 4.60; mins 90; xGI 0.16; current GWs 5; fixture Elo diff -41 |
| Groß | BHA | Midfielder | 4.31 | 4.56 | 3.77 | 3.63 | 4.47 | 16.65 | 2.87 | high | 5-GW avg pts 9.40; mins 90; xGI 0.53; current GWs 5; fixture Elo diff -10 |
| Iwobi | FUL | Midfielder | 4.30 | 4.68 | 4.16 | 2.97 | 3.22 | 15.86 | 2.94 | high | 5-GW avg pts 2.80; mins 82; xGI 0.32; current GWs 5; fixture Elo diff +95 |
| Barnes | NEW | Midfielder | 4.30 | 3.49 | 4.11 | 4.04 | 4.24 | 16.10 | 2.64 | high | 5-GW avg pts 5.60; mins 90; xGI 0.22; current GWs 5; fixture Elo diff +37 |
| Armstrong | EVE | Midfielder | 4.30 | 3.26 | 2.57 | 3.23 | 4.27 | 14.11 | 2.82 | high | 5-GW avg pts 3.20; mins 89; xGI 0.14; current GWs 5; fixture Elo diff +18 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.
History coverage measures available rows, not calibrated prediction certainty. Missing match records do not prove that a player rested.

## Your budget

Bank: **£0.0m**. Current squad selling value: **£99.3m**. Total available funds: **£99.3m**.

A transfer can spend your bank plus the outgoing player's selling price. Keeping a player does not require buying them back at their current price.

The squad comparison below is affordable with **£0.0m** left in the bank. It may require multiple transfers; use the one-transfer recommendation for your next move.

## ML-optimal squad within your budget

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.81 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW6, GW8 |
| Silva | BOU | Defender | £5.0m | 18.65 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Truffert | BOU | Defender | £5.4m | 16.35 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Muharemović | LEE | Defender | £5.0m | 14.79 | GW8, GW10 | — | — |
| Davis | IPS | Defender | £4.0m | 13.79 | GW9 | — | — |
| Haaland | MCI | Forward | £15.6m | 24.53 | GW6, GW7, GW8, GW9, GW10 | GW7, GW9 | GW10 |
| Thiago | BRE | Forward | £7.8m | 19.66 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Barry | EVE | Forward | £5.7m | 15.32 | GW6, GW7, GW9, GW10 | — | — |
| Pickford | EVE | Goalkeeper | £5.5m | 16.27 | GW6, GW9, GW10 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.94 | GW7, GW8 | — | — |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.74 | GW6, GW7, GW8, GW9, GW10 | GW6, GW8 | GW9 |
| Cherki | MCI | Midfielder | £7.8m | 18.24 | GW6, GW7, GW8, GW9, GW10 | — | GW7 |
| Dewsbury-Hall | EVE | Midfielder | £6.6m | 17.59 | GW6, GW7, GW9, GW10 | — | — |
| Iwobi | FUL | Midfielder | £5.4m | 15.86 | GW6, GW7, GW8 | — | — |
| Janelt | BRE | Midfielder | £5.0m | 14.71 | GW8 | — | — |

Squad cost: £99.3m.

## Your current squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gabriel | ARS | Defender | £8.0m | 21.81 | GW6, GW7, GW8, GW9, GW10 | GW10 | GW7 |
| Branthwaite | EVE | Defender | £5.5m | 15.83 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Bassey | FUL | Defender | £4.5m | 14.25 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Egan | HUL | Defender | £4.1m | 12.23 | GW6, GW7, GW8, GW9 | — | — |
| Furlong | IPS | Defender | £3.9m | 0.73 | Bench | — | — |
| Thiago | BRE | Forward | £7.8m | 19.66 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Havertz | ARS | Forward | £7.6m | 11.42 | GW6, GW8, GW10 | — | — |
| Mheuka | CHE | Forward | £4.5m | 0.34 | Bench | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 13.94 | GW7, GW8 | — | — |
| Horníček | NEW | Goalkeeper | £5.0m | 13.00 | GW6, GW9, GW10 | — | — |
| B.Fernandes | MUN | Midfielder | £11.9m | 22.17 | GW6, GW7, GW8, GW9, GW10 | GW6, GW7, GW9 | GW8, GW10 |
| Gibbs-White | NFO | Midfielder | £8.0m | 21.74 | GW6, GW7, GW8, GW9, GW10 | GW8 | GW6, GW9 |
| Mbeumo | MUN | Midfielder | £7.9m | 18.10 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Rogers | CHE | Midfielder | £7.7m | 17.24 | GW6, GW7, GW8, GW9, GW10 | — | — |
| Semenyo | MCI | Midfielder | £8.4m | 12.22 | GW7, GW9, GW10 | — | — |

Squad cost: £99.3m.

## One-transfer recommendation

**Semenyo → Cherki** (projected weighted XI+captain gain 5.63).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Semenyo | Cherki | £8.4m | £7.8m | £0.6m | 5.63 |
| Semenyo | Cunha | £8.4m | £7.9m | £0.5m | 4.91 |
| Semenyo | Dewsbury-Hall | £8.4m | £6.6m | £1.8m | 4.80 |
| Semenyo | Groß | £8.4m | £5.8m | £2.6m | 3.87 |
| Havertz | Gonzalo | £7.6m | £6.0m | £1.6m | 3.74 |
| Havertz | Barry | £7.6m | £5.7m | £1.9m | 3.52 |
| Havertz | Wissa | £7.6m | £6.2m | £1.4m | 3.46 |
| Havertz | Evanilson | £7.6m | £6.0m | £1.6m | 3.40 |
| Semenyo | Schade | £8.4m | £6.2m | £2.2m | 3.33 |
| Semenyo | Barnes | £8.4m | £6.1m | £2.3m | 3.32 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
