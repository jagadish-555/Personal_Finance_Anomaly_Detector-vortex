import numpy as np
import pandas as pd


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.sort_values("date").reset_index(drop=True)

    df["abs_amount"] = df["amount"].abs()
    df["log_amount"] = np.log1p(df["abs_amount"])

    # Time-based features
    df["hour_of_day"] = df["date"].dt.hour
    df["day_of_week"] = df["date"].dt.dayofweek
    df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)
    
    # Cyclical hour features
    df["hour_sin"] = np.sin(2 * np.pi * df["hour_of_day"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour_of_day"] / 24)

    # Time delta features
    df["days_since_last_transaction"] = (
        df["date"].diff().dt.total_seconds().div(86_400).fillna(0).round(2)
    )

    # Rolling statistics
    df = df.set_index("date").sort_index()
    df["rolling_7_day_spend"] = (
        df["abs_amount"]
        .rolling("7D", min_periods=1)
        .sum()
    )
    df["rolling_7_day_avg"] = (
        df["abs_amount"]
        .rolling("7D", min_periods=1)
        .mean()
    )
    df["amount_vs_7d_avg"] = df["abs_amount"] / (df["rolling_7_day_avg"] + 1)
    df = df.reset_index()

    # Frequency features
    if "merchant" in df.columns:
        merchant_counts = df["merchant"].value_counts()
        df["merchant_frequency"] = df["merchant"].map(merchant_counts).fillna(0).astype(int)
    else:
        df["merchant_frequency"] = 0

    category_counts = df["category"].value_counts()
    df["category_frequency"] = df["category"].map(category_counts).fillna(0).astype(int)

    # Category-specific Z-score
    df["category_mean"] = df.groupby("category")["abs_amount"].transform("mean")
    df["category_std"] = df.groupby("category")["abs_amount"].transform("std").fillna(0)
    df["amount_zscore"] = (df["abs_amount"] - df["category_mean"]) / (df["category_std"] + 1)

    return df


def get_feature_matrix(df: pd.DataFrame) -> np.ndarray:
    feature_cols = [
        "abs_amount",
        "log_amount",
        "hour_sin",
        "hour_cos",
        "days_since_last_transaction",
        "rolling_7_day_spend",
        "amount_vs_7d_avg",
        "amount_zscore",
        "merchant_frequency",
        "category_frequency",
    ]
    matrix = df[feature_cols].values.astype(np.float64)
    matrix = np.nan_to_num(matrix, nan=0.0, posinf=0.0, neginf=0.0)
    return matrix
