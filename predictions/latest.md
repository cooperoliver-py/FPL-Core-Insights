# FPL predictions: 2026-2027, GW1

Data commit: `087ae45c2b58dcbf0542cacff1e59e913e73e577`

Forecasts use only the canonical 2025/26 `By Gameweek` player data, strictly lagged 3/5-GW form, and target Premier League fixtures. Five-GW weights are [1.0, 0.9, 0.8, 0.7, 0.6]; price and availability are held constant.

## Held-out evaluation (historical GWs 31-38)

| Method | MAE | RMSE | Spearman |
| --- | --- | --- | --- |
| HistGradientBoosting | 0.971 | 1.916 | 0.696 |
| Rolling points (5 GW) | 1.033 | 2.129 | 0.683 |
| Lagged FPL ep_next | 1.008 | 2.116 | 0.671 |

## GW1 confidence

GW1 confidence is deliberately capped below `high`: returning players carry 2025/26 history by `player_code`, while new players are marked cold starts. Blank current Elo uses 2025/26 club Elo; promoted clubs use the prior league-low Elo and are explicitly flagged.

## Top GW1 player forecasts

| Player | Club | Pos | GW1 | GW2 | GW3 | GW4 | GW5 | 5GW score | 5GW value | Confidence | Raw drivers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B.Fernandes | MUN | Midfielder | 5.76 | 6.29 | 5.61 | 3.72 | 5.47 | 21.78 | 1.82 | medium | 5-GW avg pts 7.20; mins 90; xGI 0.62; fixture Elo diff +131 |
| Haaland | MCI | Forward | 5.17 | 5.00 | 5.86 | 4.86 | 5.57 | 21.10 | 1.36 | medium | 5-GW avg pts 5.40; mins 54; xGI 0.52; fixture Elo diff +172 |
| Saka | ARS | Midfielder | 5.16 | 4.06 | 4.88 | 4.38 | 4.23 | 18.33 | 1.93 | medium | 5-GW avg pts 4.80; mins 45; xGI 0.40; fixture Elo diff +265 |
| Bruno G. | ARS | Midfielder | 5.04 | 3.52 | 4.31 | 4.38 | 4.02 | 17.13 | 2.45 | medium | 5-GW avg pts 3.80; mins 82; xGI 0.35; fixture Elo diff +265 |
| Szoboszlai | LIV | Midfielder | 4.78 | 5.05 | 5.11 | 4.79 | 3.64 | 18.95 | 2.71 | medium | 5-GW avg pts 5.40; mins 90; xGI 0.45; fixture Elo diff +109 |
| Xhaka | SUN | Midfielder | 4.70 | 2.95 | 2.81 | 2.42 | 2.50 | 12.79 | 2.33 | medium | 5-GW avg pts 3.60; mins 90; xGI 0.28; fixture Elo diff -134 |
| Thiago | BRE | Forward | 4.70 | 4.31 | 4.80 | 3.76 | 5.23 | 18.19 | 2.27 | medium | 5-GW avg pts 2.60; mins 90; xGI 0.31; fixture Elo diff +34 |
| Watkins | AVL | Forward | 4.56 | 3.24 | 5.28 | 5.23 | 4.59 | 18.12 | 2.27 | medium | 5-GW avg pts 8.00; mins 76; xGI 0.67; fixture Elo diff +87 |
| Gabriel | ARS | Defender | 4.40 | 2.68 | 3.72 | 3.39 | 3.09 | 14.01 | 1.75 | medium | 5-GW avg pts 6.40; mins 81; xGI 0.20; fixture Elo diff +265 |
| Havertz | ARS | Forward | 4.28 | 3.35 | 4.03 | 3.57 | 3.47 | 15.09 | 2.01 | medium | 5-GW avg pts 3.40; mins 35; xGI 0.27; fixture Elo diff +265 |
| Tarkowski | EVE | Defender | 4.22 | 2.80 | 3.01 | 3.59 | 4.76 | 14.51 | 2.42 | medium | 5-GW avg pts 4.80; mins 90; xGI 0.22; fixture Elo diff -4 |
| Maguire | MUN | Defender | 4.21 | 4.10 | 3.02 | 2.41 | 2.93 | 13.76 | 2.75 | medium | 5-GW avg pts 5.40; mins 90; xGI 0.12; fixture Elo diff +131 |
| Palmer | CHE | Midfielder | 4.19 | 5.06 | 2.32 | 4.77 | 4.70 | 16.76 | 1.76 | medium | 5-GW avg pts 2.40; mins 72; xGI 0.34; fixture Elo diff -13 |
| Gibbs-White | NFO | Midfielder | 4.15 | 3.57 | 4.22 | 3.57 | 4.29 | 15.80 | 1.98 | medium | 5-GW avg pts 6.60; mins 58; xGI 0.44; fixture Elo diff +8 |
| Mbeumo | MUN | Midfielder | 4.15 | 5.03 | 4.10 | 4.19 | 4.10 | 17.34 | 2.17 | medium | 5-GW avg pts 4.40; mins 63; xGI 0.89; fixture Elo diff +131 |
| E.Le Fée | SUN | Midfielder | 4.09 | 3.32 | 3.11 | 2.04 | 2.33 | 12.39 | 2.07 | medium | 5-GW avg pts 5.40; mins 90; xGI 0.47; fixture Elo diff -134 |
| Ndiaye | EVE | Midfielder | 4.05 | 2.70 | 2.91 | 3.60 | 4.02 | 13.73 | 2.29 | medium | 5-GW avg pts 2.00; mins 90; xGI 0.34; fixture Elo diff -4 |
| Brobbey | SUN | Forward | 4.01 | 3.75 | 3.33 | 2.60 | 2.72 | 13.49 | 2.25 | medium | 5-GW avg pts 3.40; mins 77; xGI 0.34; fixture Elo diff -134 |
| Semenyo | MCI | Midfielder | 4.01 | 3.89 | 4.86 | 3.42 | 4.55 | 16.53 | 1.94 | medium | 5-GW avg pts 4.20; mins 73; xGI 0.20; fixture Elo diff +172 |
| Mainoo | MUN | Midfielder | 3.93 | 3.91 | 3.23 | 2.72 | 3.14 | 13.82 | 2.51 | medium | 5-GW avg pts 4.80; mins 90; xGI 0.13; fixture Elo diff +131 |

Raw drivers are descriptive inputs, not SHAP or causal attributions.

## Recommended £100m squad

| Player | Club | Position | Cost | Weighted score | Starts | Captains | Vice-captains |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Virgil | LIV | Defender | £6.5m | 15.73 | GW1, GW2, GW3, GW4 | — | — |
| Muñoz | CRY | Defender | £5.5m | 14.19 | GW1, GW3, GW4, GW5 | — | — |
| Maguire | MUN | Defender | £5.0m | 13.76 | GW1, GW2 | — | — |
| Botman | NEW | Defender | £5.0m | 13.64 | GW2, GW5 | — | — |
| Mitchell | CRY | Defender | £4.5m | 13.61 | GW3, GW4, GW5 | — | — |
| Thiago | BRE | Forward | £8.0m | 18.19 | GW1, GW2, GW3, GW4, GW5 | — | GW5 |
| Watkins | AVL | Forward | £8.0m | 18.12 | GW1, GW2, GW3, GW4, GW5 | GW4 | GW3 |
| Mheuka | CHE | Forward | £4.5m | 2.14 | Bench | — | — |
| Pope | NEW | Goalkeeper | £5.0m | 12.36 | GW2, GW4, GW5 | — | — |
| Leno | FUL | Goalkeeper | £4.5m | 11.87 | GW1, GW3 | — | — |
| B.Fernandes | MUN | Midfielder | £12.0m | 21.78 | GW1, GW2, GW3, GW4, GW5 | GW1, GW2, GW3, GW5 | — |
| Szoboszlai | LIV | Midfielder | £7.0m | 18.95 | GW1, GW2, GW3, GW4, GW5 | — | GW2, GW4 |
| Saka | ARS | Midfielder | £9.5m | 18.33 | GW1, GW2, GW3, GW4, GW5 | — | GW1 |
| Mbeumo | MUN | Midfielder | £8.0m | 17.34 | GW1, GW2, GW3, GW4, GW5 | — | — |
| Bruno G. | ARS | Midfielder | £7.0m | 17.13 | GW1, GW2, GW3, GW4, GW5 | — | — |

Squad cost: £100.0m.

## Limits

Predictions are estimates, not guarantees. The model does not use chips, transfer hits, price-change forecasts, recursive future form, or a UI.
