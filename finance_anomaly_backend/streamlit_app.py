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

def save_user_transactions(user_id, data):
    txns = _load_json(TXNS_FILE)
    txns[user_id] = data
    _save_json(txns, TXNS_FILE)

def create_user(name, email):
    users = _load_json(USERS_FILE)
    for uid, udata in users.items():
        if udata.get("email") == email: return uid, udata
    uid = str(uuid.uuid4())
    users[uid] = {"name": name, "email": email}
    _save_json(users, USERS_FILE)
    return uid, users[uid]

st.set_page_config(page_title="Vortex Finance", page_icon="🔮", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: radial-gradient(circle at 20% 20%, #1e1e2e 0%, #11111b 50%, #09090b 100%); }
div[data-testid="stMetric"] { background: rgba(255, 255, 255, 0.03); padding: 24px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.08); transition: all 0.3s; }
.stButton>button { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; border-radius: 10px; font-weight: 600; border: none; }
.stButton>button:hover { filter: brightness(1.2); }
</style>
""", unsafe_allow_html=True)

if "user_id" not in st.session_state: st.session_state.user_id = None
if "threshold" not in st.session_state: st.session_state.threshold = 70

with st.sidebar:
    st.markdown("<h1 style='color: #6366f1; text-align: center'>VORTEX</h1>", unsafe_allow_html=True)
    page = st.radio("Navigate", ["🏠 Dashboard", "📤 Upload", "🧠 Analyze", "📋 History"])
    
    if st.session_state.user_id:
        st.write(f"Logged in as **{st.session_state.user_name}**")
        if st.button("Log Out"):
            st.session_state.user_id = None
            st.rerun()
    else:
        with st.expander("👤 Login"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            if st.button("Login") and name and email:
                uid, udata = create_user(name, email)
                st.session_state.user_id = uid
                st.session_state.user_name = udata["name"]
                st.rerun()

if page == "🏠 Dashboard":
    st.title("Vortex Finance Intelligence")
    if st.session_state.user_id:
        txns = get_user_transactions(st.session_state.user_id)
        if txns:
            df = pd.DataFrame(txns)
            c1, c2, c3 = st.columns(3)
            c1.metric("Transactions", len(df))
            c2.metric("Total Spend", f"₹{df['amount'].sum():,.0f}")
            c3.metric("Anomalies", df.get('is_anomaly', pd.Series([False]*len(df))).sum())

elif page == "📤 Upload":
    st.title("Upload Statement")
    if not st.session_state.user_id: st.warning("Login required"); st.stop()
    
    file = st.file_uploader("Upload CSV", type=["csv"])
    if file and st.button("Process"):
        content = file.getvalue()
        df = parse_csv(content)
        df = categorize_dataframe(df)
        save_user_transactions(st.session_state.user_id, df.to_dict("records"))
        st.success(f"Saved {len(df)} transactions")

elif page == "🧠 Analyze":
    st.title("Run AI Analysis")
    if not st.session_state.user_id: st.warning("Login required"); st.stop()
    
    threshold = st.slider("Risk Threshold", 0, 100, st.session_state.threshold)
    if st.button("Analyze"):
        txns = get_user_transactions(st.session_state.user_id)
        if not txns: st.error("No data")
        else:
            df = pd.DataFrame(txns)
            if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])
            df_feat = engineer_features(df)
            base = compute_baseline(df_feat)
            df_res = detect_anomalies(df_feat, base, st.session_state.user_id, threshold)
            
            save_df = df_res.copy()
            if 'date' in save_df.columns: save_df['date'] = save_df['date'].dt.strftime("%Y-%m-%d %H:%M:%S")
            save_user_transactions(st.session_state.user_id, save_df.to_dict("records"))
            
            expls = generate_explanations(df_res, base)
            st.success(f"Found {df_res['is_anomaly'].sum()} anomalies")
            for e in expls:
                st.write(f"- Txn {e.transaction_id} Risk: {e.risk_score}")
                for msg in e.explanations: st.write("  -", msg)

elif page == "📋 History":
    st.title("Transaction History")
    if not st.session_state.user_id: st.warning("Login required"); st.stop()
    
    txns = get_user_transactions(st.session_state.user_id)
    if txns:
        df = pd.DataFrame(txns)
        st.dataframe(df)
    else:
        st.info("Empty")
