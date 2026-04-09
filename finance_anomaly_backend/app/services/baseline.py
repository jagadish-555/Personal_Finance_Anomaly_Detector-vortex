from datetime import datetime
from typing import Any, Optional

import numpy as np
import pandas as pd




def compute_baseline(df: pd.DataFrame) -> dict[str, Any]:
    """Compute a behavioural baseline from a user's transaction history.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain at least: date, abs_amount, category, merchant.

    Returns
    -------
    dict with keys:
        category_stats  — {category: {mean_amount, std_amount, frequency_per_week, count}}
        merchant_stats  — {merchant: {count, mean_amount}}
        weekly_avg_spend — float
        weekly_std_spend — float
    """
    df = df.copy()
    df = df.sort_values("date").reset_index(drop=True)


    category_stats: dict[str, dict] = {}
    if "category" in df.columns:
        total_weeks = _total_weeks(df)
        for cat, grp in df.groupby("category"):
            category_stats[str(cat)] = {
                "mean_amount": round(float(grp["abs_amount"].mean()), 2),
                "std_amount": round(float(grp["abs_amount"].std(ddof=0)), 2),
                "frequency_per_week": round(len(grp) / max(total_weeks, 1), 2),
                "count": int(len(grp)),
            }

    # ── Per-merchant stats ───────────────────────────────────────────────
    merchant_stats: dict[str, dict] = {}
    if "merchant" in df.columns:
        for merchant, grp in df.groupby("merchant"):
            merchant_stats[str(merchant)] = {
                "count": int(len(grp)),
                "mean_amount": round(float(grp["abs_amount"].mean()), 2),
            }

    # ── Weekly spend stats ───────────────────────────────────────────────
    weekly_spend = _weekly_spend(df)
    weekly_avg = round(float(weekly_spend.mean()), 2) if len(weekly_spend) else 0.0
    weekly_std = round(float(weekly_spend.std(ddof=0)), 2) if len(weekly_spend) > 1 else 0.0

    return {
        "category_stats": category_stats,
        "merchant_stats": merchant_stats,
        "weekly_avg_spend": weekly_avg,
        "weekly_std_spend": weekly_std,
    }


def _total_weeks(df: pd.DataFrame) -> float:
    if df.empty:
        return 1.0
    span = (df["date"].max() - df["date"].min()).days
    return max(span / 7.0, 1.0)


def _weekly_spend(df: pd.DataFrame) -> pd.Series:
    if df.empty:
        return pd.Series(dtype=float)
    weekly = df.set_index("date").resample("W")["abs_amount"].sum()
    return weekly
