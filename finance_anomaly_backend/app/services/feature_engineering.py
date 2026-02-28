import numpy as np
import pandas as pd


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.sort_values("date").reset_index(drop=True)

    df["abs_amount"] = df["amount"].abs()
    df["log_amount"] = np.log1p(df["abs_amount"])
