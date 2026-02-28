
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(feature_matrix: np.ndarray, df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42,
    )

    model.fit(feature_matrix)

    predictions = model.predict(feature_matrix)
    scores = model.decision_function(feature_matrix)

    df["anomaly_flag"] = (predictions == -1).astype(int)
    df["anomaly_score"] = scores

    df["anomaly_reason"] = ""
    for i, row in df.iterrows():
        if row["anomaly_flag"] == 1:
            reasons = []
            if row.get("rolling_7_day_avg", 0) > 0:
                ratio = row["abs_amount"] / row["rolling_7_day_avg"]
                if ratio > 2:
                    reasons.append(f"Spending {ratio:.1f}x above weekly avg")
            if row.get("rolling_7_day_std", 0) > 0:
                deviation = (row["abs_amount"] - row["rolling_7_day_avg"]) / row["rolling_7_day_std"]
                if deviation > 2:
                    reasons.append(f"High deviation from rolling mean ({deviation:.1f}σ)")
            if row.get("transaction_frequency_last_3_days", 0) > 5:
                reasons.append("Abnormal transaction frequency")
            if row.get("category_encoded", -1) != -1:
                cat_counts = df["Category"].value_counts(normalize=True)
                cat = row["Category"]
                if cat in cat_counts and cat_counts[cat] < 0.05:
                    reasons.append(f"Rare category: {cat}")
            if not reasons:
                reasons.append("Unusual spending pattern detected")
            df.at[i, "anomaly_reason"] = "; ".join(reasons)

    return df


def generate_summary(df: pd.DataFrame) -> dict:

    debit_mask = df["Amount"] < 0
    total_spending = float(df.loc[debit_mask, "Amount"].sum())
    total_income = float(df.loc[~debit_mask, "Amount"].sum())

    category_breakdown = (
        df.loc[debit_mask]
        .groupby("Category")["Amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
        .to_dict()
    )

    anomaly_count = int(df["anomaly_flag"].sum())

    top_anomalies = (
        df[df["anomaly_flag"] == 1]
        .nsmallest(5, "anomaly_score")[["Date", "Description", "Amount", "Category", "anomaly_score", "anomaly_reason"]]
        .to_dict(orient="records")
    )

    for item in top_anomalies:
        if pd.notna(item.get("Date")):
            item["Date"] = str(item["Date"])

    return {
        "total_spending": abs(total_spending),
        "total_income": total_income,
        "category_breakdown": category_breakdown,
        "anomaly_count": anomaly_count,
        "total_transactions": len(df),
        "top_anomalies": top_anomalies,
    }
