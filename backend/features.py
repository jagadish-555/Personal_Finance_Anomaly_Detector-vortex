
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def engineer_features(df: pd.DataFrame):

    df = df.copy()
    df.sort_values("Date", inplace=True)
    df.reset_index(drop=True, inplace=True)

    df["day_of_week"] = df["Date"].dt.dayofweek
    df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

    le = LabelEncoder()
    df["category_encoded"] = le.fit_transform(df["Category"])

    df["abs_amount"] = df["Amount"].abs()

    df["rolling_7_day_avg"] = (
        df.set_index("Date")["abs_amount"]
        .rolling("7D", min_periods=1)
        .mean()
        .values
    )

    df["rolling_7_day_std"] = (
        df.set_index("Date")["abs_amount"]
        .rolling("7D", min_periods=1)
        .std()
        .fillna(0)
        .values
    )

    freq = []
    for i, row in df.iterrows():
        current_date = row["Date"]
        three_days_ago = current_date - pd.Timedelta(days=3)
        count = ((df["Date"] >= three_days_ago) & (df["Date"] <= current_date)).sum()
        freq.append(count)
    df["transaction_frequency_last_3_days"] = freq

    amount_mean = df["abs_amount"].mean()
    amount_std = df["abs_amount"].std()
    if amount_std == 0:
        df["amount_normalized"] = 0.0
    else:
        df["amount_normalized"] = (df["abs_amount"] - amount_mean) / amount_std

    feature_columns = [
        "amount_normalized",
        "day_of_week",
        "is_weekend",
        "category_encoded",
        "rolling_7_day_avg",
        "rolling_7_day_std",
        "transaction_frequency_last_3_days",
    ]

    feature_matrix = df[feature_columns].values.astype(np.float64)
    feature_matrix = np.nan_to_num(feature_matrix, nan=0.0)

    return df, feature_matrix, feature_columns
