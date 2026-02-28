"""
utils.py
--------
CSV parsing, cleaning, and keyword-based transaction categorization.
"""

import pandas as pd
from io import BytesIO


# --------------- Keyword → Category Mapping ---------------

CATEGORY_KEYWORDS = {
    "Food": ["swiggy", "zomato", "food", "restaurant", "dominos", "pizza", "burger", "cafe", "dining"],
    "Transport": ["uber", "ola", "rapido", "metro", "fuel", "petrol", "diesel", "parking", "cab"],
    "Shopping": ["amazon", "flipkart", "myntra", "ajio", "shopping", "mall", "store"],
    "Housing": ["rent", "maintenance", "society", "electricity", "water", "gas bill"],
    "Entertainment": ["netflix", "spotify", "hotstar", "movie", "theatre", "gaming", "steam"],
    "Bills": ["recharge", "airtel", "jio", "vi", "broadband", "wifi", "insurance", "emi"],
}


def categorize(description: str) -> str:
    """
    Map a transaction description to a category using keyword matching.
    Returns 'Others' if no keyword matches.
    """
    desc_lower = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in desc_lower:
                return category
    return "Others"


# --------------- CSV Parsing & Cleaning ---------------

def parse_csv(file_bytes: bytes) -> pd.DataFrame:
    """
    Read raw CSV bytes, clean the data, and add a 'Category' column.

    Expected CSV columns: Date, Description, Amount
    Optional column: Type (Debit/Credit)

    Returns a cleaned DataFrame sorted by Date ascending.
    """
    df = pd.read_csv(BytesIO(file_bytes))

    # --- Normalise column names (strip whitespace, title-case) ---
    df.columns = df.columns.str.strip().str.title()

    # --- Validate required columns ---
    required = {"Date", "Description", "Amount"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {missing}")

    # --- Parse dates ---
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=False, errors="coerce")

    # --- Drop rows where Date or Amount is missing ---
    df.dropna(subset=["Date", "Amount"], inplace=True)

    # --- Ensure Amount is numeric ---
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df.dropna(subset=["Amount"], inplace=True)

    # --- Sort by date ---
    df.sort_values("Date", inplace=True)
    df.reset_index(drop=True, inplace=True)

    # --- Add category column ---
    df["Category"] = df["Description"].astype(str).apply(categorize)

    return df
