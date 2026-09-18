"""Date-aware availability from snapshots known at the forecast origin."""

from __future__ import annotations

import re

import numpy as np
import pandas as pd


_RETURN_DATE = re.compile(
    r"\b(Expected back|Suspended until)\s+(\d{1,2})\s+([A-Za-z]{3})\b(?:\s+(\d{4})\b)?",
    re.IGNORECASE,
)
_MONTHS = {name: month for month, name in enumerate(
    "jan feb mar apr may jun jul aug sep oct nov dec".split(), 1
)}


def _dates(value, index: pd.Index) -> pd.Series:
    return pd.to_datetime(pd.Series(value, index=index), errors="coerce", utc=True, format="mixed")


def _return_date(news, anchor: pd.Timestamp) -> tuple[str, pd.Timestamp] | None:
    match = _RETURN_DATE.search(str(news))
    if match is None or pd.isna(anchor):
        return None
    kind, day, month, year = match.groups()
    month_number = _MONTHS.get(month.lower())
    if month_number is None:
        return None
    candidates = []
    for candidate_year in ([int(year)] if year else range(anchor.year - 1, anchor.year + 2)):
        try:
            candidates.append(pd.Timestamp(candidate_year, month_number, int(day), tz="UTC"))
        except ValueError:
            continue
    if not candidates:
        return None
    # ponytail: yearless dates use the nearest year; explicit source years remove ambiguity.
    date = min(candidates, key=lambda candidate: abs(candidate - anchor.normalize()))
    return kind.lower(), date


def availability_for_fixture(
    frame: pd.DataFrame,
    kickoff,
    as_of,
    *,
    injury_return_probability: float | None = None,
    is_next_round: bool = False,
) -> pd.Series:
    """Return availability factors without treating an expected return as confirmed fitness.

    Supply snapshots already known at ``as_of``. Historical frames containing
    ``availability_lag1`` use only the corresponding lagged news/status columns.
    Injury recovery needs a probability estimated from earlier observations;
    absent that evidence the current chance remains unchanged. The next round's
    explicit chance wins over a projected recovery. Suspension expiry restores
    eligibility, not a guarantee of starting or playing. Missing kickoff dates
    retain the snapshot factor; a known blank gameweek always returns zero.
    """
    if injury_return_probability is not None and not (
        np.isfinite(injury_return_probability) and 0 <= injury_return_probability <= 1
    ):
        raise ValueError("injury_return_probability must be between zero and one")
    suffix = "_lag1" if "availability_lag1" in frame else ""

    def column(name, default=np.nan):
        return frame.get(name + suffix, pd.Series(default, index=frame.index))

    status = column("status", "a").fillna("a").astype(str)
    if suffix:
        probability = pd.to_numeric(frame["availability_lag1"], errors="coerce").fillna(1.0)
    else:
        chance = pd.to_numeric(column("chance_of_playing_next_round"), errors="coerce")
        fallback = status.map({"a": 1.0, "d": 0.75, "i": 0.0, "u": 0.0, "s": 0.0, "n": 0.0})
        probability = (chance / 100).where(chance.notna(), fallback).fillna(0.5)
    probability = probability.clip(0, 1).astype(float)
    origins, kickoffs = _dates(as_of, frame.index), _dates(kickoff, frame.index)
    news_added_raw = column("news_added")
    news_added = _dates(news_added_raw, frame.index)
    for offset, (state, news, added, raw_added, origin, fixture) in enumerate(zip(
        status, column("news", ""), news_added, news_added_raw, origins, kickoffs
    )):
        if state not in {"i", "d", "s"} or pd.isna(origin) or pd.isna(fixture):
            continue
        if pd.notna(added) and added > origin:
            continue
        if pd.notna(raw_added) and str(raw_added).strip() and pd.isna(added):
            continue
        parsed = _return_date(news, added if pd.notna(added) else origin)
        if parsed is None:
            continue
        kind, return_date = parsed
        # A missed return date in an unchanged injury snapshot is not fresh evidence.
        if return_date < origin.normalize() or fixture.normalize() < return_date:
            continue
        if state == "s" and kind == "suspended until":
            probability.iloc[offset] = 1.0
        elif state in {"i", "d"} and kind == "expected back" and not is_next_round:
            if injury_return_probability is not None:
                probability.iloc[offset] = max(probability.iloc[offset], injury_return_probability)
    probability.loc[status.isin({"u", "n"})] = 0.0
    if "fixture_count" in frame:
        probability.loc[pd.to_numeric(frame["fixture_count"], errors="coerce").eq(0)] = 0.0
    return probability


def estimate_return_availability(history: pd.DataFrame, min_samples: int = 20) -> dict:
    """Estimate observed appearances after expected returns using earlier snapshots.

    The caller must restrict history to outcomes available before its prediction
    origin. ``kickoff_time`` is the target fixture date; news/status are post-GW
    snapshots and are therefore shifted here. No future outcome is inspected by
    ``availability_for_fixture`` itself. The sample count accompanies the prior
    so sparse evidence cannot silently become a confident recovery assumption.
    """
    required = {"kickoff_time", "minutes", "status", "news"}
    if not required.issubset(history):
        return {"probability": None, "samples": 0}
    identity = "player_code" if "player_code" in history else "id"
    if identity not in history:
        return {"probability": None, "samples": 0}
    rows = history.copy()
    rows["kickoff_time"] = _dates(rows["kickoff_time"], rows.index)
    rows = rows.dropna(subset=["kickoff_time"]).sort_values(
        [identity, "kickoff_time"]
    ).reset_index(drop=True)
    previous = rows.groupby(identity, sort=False).shift(1)
    previous["availability_lag1"] = 0.0
    for name in ("status", "news", "news_added"):
        if name in previous:
            previous[name + "_lag1"] = previous[name]
    if "fixture_count" in rows:
        previous["fixture_count"] = rows["fixture_count"]
    eligible = availability_for_fixture(
        previous, rows["kickoff_time"], previous["kickoff_time"], injury_return_probability=1.0
    ).eq(1.0) & previous["status"].isin({"i", "d"})
    minutes = pd.to_numeric(rows["minutes"], errors="coerce")
    outcomes = minutes.loc[eligible & minutes.notna()]
    return {
        "probability": float(outcomes.gt(0).mean()) if len(outcomes) >= min_samples else None,
        "samples": len(outcomes),
    }
