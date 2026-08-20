# FPL predictions: 2026-2027, GW1

Last generated: 2026-08-20 09:45 UTC

Data commit: `087ae45c2b58dcbf0542cacff1e59e913e73e577`

Forecasts use only the canonical 2025/26 `By Gameweek` player data, strictly lagged 3/5-GW form, and target Premier League fixtures. Five-GW weights are [1.0, 0.9, 0.8, 0.7, 0.6]; price and availability are held constant.

## Held-out evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.966 | 1.912 | 0.695 |
| Rolling points (5 GW) | 1.033 | 2.129 | 0.683 |
| Lagged FPL ep_next | 1.008 | 2.116 | 0.671 |

## GW1 confidence

GW1 confidence is deliberately capped below `high`: returning players carry 2025/26 history by `player_code`, while new players are marked cold starts. Blank current Elo uses 2025/26 club Elo; promoted clubs use the prior league-low Elo and are explicitly flagged.

## Top GW1 player forecasts

| Player | Club | Pos | GW1 | GW2 | GW3 | GW4 | GW5 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 5.90 | 6.13 | 5.92 | 3.93 | 5.77 | 22.37 | 1.86 | medium | 5-GW avg pts 7.20; mins 90; xGI 0.62; fixture Elo diff +131 |
| Szoboszlai | LIV | Midfielder | 5.25 | 5.38 | 5.47 | 5.23 | 4.04 | 20.55 | 2.94 | medium | 5-GW avg pts 5.40; mins 90; xGI 0.45; fixture Elo diff +109 |
| Watkins | AVL | Forward | 4.74 | 3.09 | 5.22 | 5.21 | 4.78 | 18.21 | 2.28 | medium | 5-GW avg pts 8.00; mins 76; xGI 0.67; fixture Elo diff +87 |
| Saka | ARS | Midfielder | 4.70 | 3.67 | 4.61 | 4.36 | 4.06 | 17.18 | 1.81 | medium | 5-GW avg pts 4.80; mins 45; xGI 0.40; fixture Elo diff +265 |
| Bruno G. | ARS | Midfielder | 4.57 | 3.44 | 4.30 | 4.26 | 4.03 | 16.51 | 2.36 | medium | 5-GW avg pts 3.80; mins 82; xGI 0.35; fixture Elo diff +265 |
| Haaland | MCI | Forward | 4.50 | 4.42 | 5.04 | 4.01 | 4.95 | 18.29 | 1.18 | medium | 5-GW avg pts 5.40; mins 54; xGI 0.52; fixture Elo diff +172 |
| E.Le Fée | SUN | Midfielder | 4.31 | 3.39 | 3.27 | 2.10 | 2.33 | 12.84 | 2.14 | medium | 5-GW avg pts 5.40; mins 90; xGI 0.47; fixture Elo diff -134 |
| Xhaka | SUN | Midfielder | 4.28 | 3.08 | 3.07 | 2.54 | 2.59 | 12.85 | 2.34 | medium | 5-GW avg pts 3.60; mins 90; xGI 0.28; fixture Elo diff -134 |
| Thiago | BRE | Forward | 4.22 | 4.05 | 4.55 | 3.58 | 4.53 | 16.72 | 2.09 | medium | 5-GW avg pts 2.60; mins 90; xGI 0.31; fixture Elo diff +34 |
| Maguire | MUN | Defender | 4.19 | 4.17 | 3.21 | 2.57 | 3.21 | 14.24 | 2.85 | medium | 5-GW avg pts 5.40; mins 90; xGI 0.12; fixture Elo diff +131 |
| Gibbs-White | NFO | Midfielder | 4.17 | 3.53 | 4.21 | 3.53 | 4.37 | 15.82 | 1.98 | medium | 5-GW avg pts 6.60; mins 58; xGI 0.44; fixture Elo diff +8 |
| Gabriel | ARS | Defender | 4.14 | 2.61 | 3.75 | 3.46 | 3.19 | 13.83 | 1.73 | medium | 5-GW avg pts 6.40; mins 81; xGI 0.20; fixture Elo diff +265 |
| Mbeumo | MUN | Midfielder | 4.07 | 4.74 | 3.98 | 3.93 | 3.98 | 16.66 | 2.08 | medium | 5-GW avg pts 4.40; mins 63; xGI 0.89; fixture Elo diff +131 |
| Palmer | CHE | Midfielder | 4.06 | 4.51 | 1.97 | 4.44 | 4.40 | 15.44 | 1.63 | medium | 5-GW avg pts 2.40; mins 72; xGI 0.34; fixture Elo diff -13 |
| Tarkowski | EVE | Defender | 4.05 | 2.72 | 2.83 | 3.55 | 5.06 | 14.29 | 2.38 | medium | 5-GW avg pts 4.80; mins 90; xGI 0.22; fixture Elo diff -4 |
| Amad | MUN | Midfielder | 4.02 | 3.82 | 3.72 | 2.69 | 3.72 | 14.55 | 2.43 | medium | 5-GW avg pts 2.80; mins 69; xGI 0.41; fixture Elo diff +131 |
| Mainoo | MUN | Midfielder | 3.96 | 3.75 | 3.31 | 2.70 | 3.31 | 13.86 | 2.52 | medium | 5-GW avg pts 4.80; mins 90; xGI 0.13; fixture Elo diff +131 |
| Sarr | CRY | Midfielder | 3.95 | 2.84 | 3.95 | 3.82 | 3.93 | 14.70 | 2.26 | medium | 5-GW avg pts 4.40; mins 78; xGI 0.66; fixture Elo diff -6 |
| Havertz | ARS | Forward | 3.86 | 3.15 | 3.81 | 3.49 | 3.43 | 14.24 | 1.90 | medium | 5-GW avg pts 3.40; mins 35; xGI 0.27; fixture Elo diff +265 |
| Keane | EVE | Defender | 3.86 | 2.92 | 2.97 | 3.52 | 4.46 | 14.01 | 2.80 | medium | 5-GW avg pts 2.40; mins 90; xGI 0.12; fixture Elo diff -4 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## Recommended £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Danso | TOT | Defender | £5.0m | 14.82 | GW2, GW3, GW4 | — | — |
| Maguire | MUN | Defender | £5.0m | 14.24 | GW1, GW2, GW3 | — | — |
| Lacroix | CHE | Defender | £6.0m | 14.16 | GW1, GW2, GW4, GW5 | — | — |
| Botman | NEW | Defender | £5.0m | 14.15 | GW2, GW3, GW5 | — | GW5 |
| Keane | EVE | Defender | £5.0m | 14.01 | GW1, GW4, GW5 | — | — |
| Watkins | AVL | Forward | £8.0m | 18.21 | GW1, GW3, GW4, GW5 | — | GW4 |
| Thiago | BRE | Forward | £8.0m | 16.72 | GW1, GW2, GW3, GW4, GW5 | — | — |
| Neave | NEW | Forward | £4.5m | 3.07 | Bench | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 13.11 | GW2, GW4, GW5 | — | — |
| Kelleher | BRE | Goalkeeper | £5.0m | 12.80 | GW1, GW3 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 22.37 | GW1, GW2, GW3, GW4, GW5 | GW1, GW2, GW3, GW5 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 20.55 | GW1, GW2, GW3, GW4, GW5 | GW4 | GW1, GW2, GW3 |
| Saka | ARS | Midfielder | £9.5m | 17.18 | GW1, GW2, GW3, GW4, GW5 | — | — |
| Mbeumo | MUN | Midfielder | £8.0m | 16.66 | GW1, GW2, GW3, GW4, GW5 | — | — |
| Bruno G. | ARS | Midfielder | £7.0m | 16.51 | GW1, GW2, GW3, GW4, GW5 | — | — |

Squad cost: £100.0m.

## One-transfer recommendation

**Mitchell → Robinson** (projected weighted XI+captain gain 0.47).

| Out | In | Sell | Buy | Bank after | XI+captain gain |
| --- | --- | --- | --- | --- | --- |
| Mitchell | Robinson | £4.5m | £4.5m | £0.0m | 0.47 |
| Muñoz | Danso | £5.5m | £5.0m | £0.5m | 0.29 |
| Mitchell | Rodon | £4.5m | £4.5m | £0.0m | 0.22 |
| Mheuka | Scarlett | £4.5m | £4.5m | £0.0m | 0.00 |
| Mheuka | Walle Egeli | £4.5m | £4.5m | £0.0m | 0.00 |
| Mheuka | Furo | £4.5m | £4.5m | £0.0m | 0.00 |
| Mheuka | Neave | £4.5m | £4.5m | £0.0m | 0.00 |
| Mheuka | Kusi-Asare | £4.5m | £4.5m | £0.0m | 0.00 |
| Mitchell | Justin | £4.5m | £4.5m | £0.0m | -0.08 |
| Leno | Verbruggen | £4.5m | £4.5m | £0.0m | -0.10 |

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
