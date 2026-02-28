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
