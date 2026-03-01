import json
import os
import uuid
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from app.services.parser import parse_csv, parse_pdf
from app.services.categorizer import categorize_dataframe
from app.services.feature_engineering import engineer_features
from app.services.baseline import compute_baseline
from app.services.anomaly_engine import detect_anomalies
from app.services.explanation_engine import generate_explanations

# ── Local Simple DB ───────────────────────────────────────────────────────────
DB_DIR = pathlib.Path("local_db")
DB_DIR.mkdir(exist_ok=True)
USERS_FILE = DB_DIR / "users.json"
TXNS_FILE = DB_DIR / "transactions.json"

def _load_json(file_path):
    if file_path.exists():
        with open(file_path, "r") as f:
            try: return json.load(f)
            except: return {}
    return {}

def _save_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f)

def get_user_transactions(user_id):
    return _load_json(TXNS_FILE).get(user_id, [])

