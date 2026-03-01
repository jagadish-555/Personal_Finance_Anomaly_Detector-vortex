# Personal Finance Anomaly Detector

> Turning transaction data into actionable financial intelligence.


---

## Quick Start

```bash
# 1. Enter the backend directory and activate the virtual environment
cd finance_anomaly_backend
source .venv/bin/activate        # macOS/Linux
pip install -r requirements.txt  # first time only

# 2. Start the FastAPI backend (Terminal 1)
uvicorn app.main:app --reload --port 8000

# 3. Start the Streamlit frontend (Terminal 2)
streamlit run streamlit_app.py
```

- **Backend API:** http://localhost:8000/docs
- **Streamlit UI:** http://localhost:8501

---

## Project Structure

```
├── README.md                          ← You are here
├── Erdiagram.md                       ← Database ER diagram (Mermaid)
├── .gitignore
│
├── finance_anomaly_backend/           ← Main application
│   ├── requirements.txt               ← Python dependencies
│   ├── streamlit_app.py               ← Streamlit frontend (806 lines)
│   ├── finance_anomaly.db             ← SQLite database (auto-created)
│   │
│   └── app/                           ← FastAPI backend package
│       ├── main.py                    ← App entry point, routers, lifespan
│       ├── database.py                ← SQLAlchemy engine & session
│       ├── models.py                  ← ORM models (User, Transaction, UserBaseline)
│       ├── schemas.py                 ← Pydantic request/response schemas
│       │
│       ├── routes/
│       │   ├── upload.py              ← POST /upload (CSV/PDF parsing)
│       │   └── analyze.py             ← POST /analyze, GET /transactions
│       │
│       ├── services/
│       │   ├── parser.py              ← CSV & PDF bank statement parsing
│       │   ├── categorizer.py         ← Keyword-based transaction categorization
│       │   ├── feature_engineering.py ← Feature extraction for ML
│       │   ├── baseline.py            ← Per-user behavioral baseline
│       │   ├── anomaly_engine.py      ← Hybrid detection (statistical + Isolation Forest)
│       │   └── explanation_engine.py  ← Human-readable anomaly explanations
│       │
│       ├── utils/
│       │   └── helpers.py             ← Currency cleaning, merchant extraction, etc.
│       │
│       └── ml_models/                 ← Persisted per-user Isolation Forest models (.pkl)
│
└── notebooks/                         ← Research & demo notebooks
    ├── final_collab.ipynb             ← Standalone Colab prototype
    └── pipeline_demo.ipynb            ← Full backend pipeline walkthrough
```


---

# __Problem Statement__

With the rise of digital banking, users generate massive transaction data across bank accounts, UPI apps, and credit cards.

However, banks only provide **transaction lists**, not **behavioral insights**.

Users cannot easily detect:

- Abnormally high transactions  
- Sudden spending spikes  
- New or suspicious merchants  
- Long-term behavioral shifts  

There is no lightweight, user-centric system that intelligently analyzes personal financial behavior.


---

## __Problem Title__

Personal Finance Anomaly Detector


---

## __Problem Description__

Users receive raw transaction data but lack:

- Personalized anomaly detection  
- Intelligent categorization  
- Behavioral deviation alerts  
- Explainable financial insights  

The system must convert transaction data into **proactive financial awareness**.


---

## __Target Users__

Everyone Who does transaction through online mode or withdraw cash from ATM's


---

## __Existing Gaps__

- **Data without intelligence**
- No personalized anomaly detection
- No explainable alerts
- Reactive financial monitoring
- Fragmented financial data


---

# __Problem Understanding & Approach__


## __Root Cause Analysis__

The issue exists because:

- Transaction formats vary (CSV / PDF)
- “Unusual” is different for every user
- No personalized spending baseline exists
- Systems focus on fraud detection, not behavioral analysis

The real problem is:

> Lack of a personalized anomaly detection system.


---

## __Solution Strategy__

We follow a 3-layer approach:

### 1️Data Normalization
- Parse CSV & PDF
- Standardize columns
- Clean transaction descriptions

### 2️Intelligent Categorization
- Rule-based keyword matching
- Expandable ML classification

# 🔍 __Hybrid Anomaly Detection Framework__

Our system detects anomalies across multiple behavioral dimensions to provide **explainable financial intelligence**.


---

## 1️ __Amount-Based Anomalies__

Detects unusual transaction amounts relative to user history.

- **Z-Score Deviation**  
  Flags transactions significantly higher or lower than personal average.

- **Category-Based Deviation**  
  Compares transaction amount against category-specific historical mean.

- **Extreme Outlier Detection**  
  Identifies transactions far outside normal financial range.


---

## 2️ __Frequency-Based Anomalies__

Detects abnormal transaction bursts or activity spikes.

- **Transaction Burst Detection**  
  Multiple transactions within a short time window.

- **Daily/Weekly Spike Detection**  
  Sudden increase in transaction count compared to rolling average.

- **Rapid Repeat Merchant Activity**  
  Same merchant used multiple times within minutes.


---

## 3️ __Merchant-Based Anomalies__

Detects irregular merchant behavior.

- **New Merchant Detection**  
  First-time transaction with a merchant.

- **Rare Merchant Usage**  
  Merchant historically used very infrequently.

- **Merchant Category Mismatch**  
  Merchant category inconsistent with usual spending behavior.


---

## 4️ __Behavioral Shift Anomalies__

Detects long-term spending pattern changes.

- **Monthly Category Spike**  
  Significant increase compared to last 3-month average.

- **Budget Drift Detection**  
  Category spending exceeds normal proportion.

- **Income-to-Expense Ratio Shift**  
  Sudden imbalance in spending behavior.


---

## 5️ __Location-Based Anomalies__

Detects geographic irregularities.

- **New Location Detection**  
  First transaction from a new city or region.

- **Geo-Deviation Detection**  
  Transaction outside normal geographic radius.

- **Impossible Travel Detection**  
  Transactions occurring in distant cities within unrealistic time gaps.


---

## 6️ __Time-Based Anomalies__

Detects unusual transaction timing behavior.

- **Unusual Time of Day**  
  Transactions outside normal activity hours.

- **Weekend/Weekday Behavior Shift**  
  Spending inconsistent with historical weekday patterns.

- **Night-Time High-Value Transactions**  
  High-risk activity during late hours.


---

## 7️ __Transaction Pattern Anomalies__

Detects structured suspicious behavior.

- **Round Number Pattern Detection**  
  Repeated transactions of identical rounded amounts.

- **Split Transaction Pattern**  
  Large payment divided into multiple smaller transactions.

- **Micro-Transaction Clusters**  
  Multiple small deductions within short duration.


---

## 8️ __Machine Learning-Based Anomalies (Optional Enhancement)__

- **Isolation Forest Detection**  
  Detects multi-dimensional outliers in feature space.

- **Feature-Space Outlier Scoring**  
  Identifies abnormal patterns across combined behavioral features.

- **Composite Risk Score (0–100)**  
  Weighted anomaly scoring model.


---

# __Final Composite Risk Scoring__

Each anomaly dimension contributes to a final **Risk Score (0–100)**:

- Amount Deviation  
- Frequency Spike  
- Merchant Novelty  
- Behavioral Shift  
- Location Irregularity  
- Time-Based Risk  

Only transactions exceeding a defined threshold generate alerts to minimize false positives.


---

> The goal is not just anomaly detection —  
> but **multi-dimensional, explainable financial behavior intelligence.**

Focus: **Explainable AI**, not black-box alerts.


---

# __Proposed Solution__


## __Solution Overview__

A web-based system that:

- Imports bank statements
- Learns personal spending behavior
- Detects anomalies
- Assigns risk scores
- Visualizes irregularities


---

## __Core Idea__

Instead of showing a transaction list, the system:

- Learns what is **normal**
- Detects deviations
- Generates **risk score (0–100)**
- Explains WHY a transaction is unusual

Example:

₹4,982 at SWIGGY  
3.2× higher than usual  
New merchant  
48% increase in food spending  

This transforms raw data into **financial intelligence**.


---

## __Key Features__

### Multi-Format Parsing
- CSV upload
- PDF parsing
- Data cleaning

### Automatic Categorization
- Merchant keyword detection
- ML-based classification (optional)

### Hybrid Anomaly Detection
- Statistical deviation
- Behavioral shift detection
- Frequency spike detection
- New merchant flagging

### Explainable Risk Scoring
- Composite anomaly score
- Clear reasoning for alerts

### Interactive Dashboard
- Spending timeline
- Category breakdown
- Highlighted anomalies
- Monthly comparisons

### Smart Notification System
- Threshold-based alerts
- Reduced false positives


---

---

# 4️⃣ System Architecture

## High-Level Flow

User → Frontend (Streamlit) → Backend (FastAPI) → Anomaly Engine → Database → Response → Dashboard

---

## Architecture Description

The system follows a modular, service-oriented backend architecture:

1. **Frontend (Streamlit)**  
   - Uploads bank statements (CSV/PDF)  
   - Displays anomaly results  
   - Visualizes spending trends and risk scores  

2. **Backend (FastAPI)**  
   - Handles API requests  
   - Validates data using Pydantic schemas  
   - Routes processing to appropriate services  

3. **Processing Layer**
   - Parsing & Normalization  
   - Categorization  
   - Feature Engineering  
   - Baseline Computation  
   - Hybrid Anomaly Engine  

4. **Database Layer (SQLite + SQLAlchemy)**
   - Stores Users  
   - Stores Transactions  
   - Stores Behavioral Baselines  

5. **ML Layer**
   - Isolation Forest (optional enhancement)  
   - Composite Risk Scoring Engine  
   - Explainability Engine  

---

# 5️⃣ Database Design

## ER Diagram

(Add ER diagram image here)

---

## ER Diagram Description

### 1️⃣ User
- user_id (PK)
- name
- email
- created_at

### 2️⃣ Transaction
- transaction_id (PK)
- user_id (FK)
- date
- amount
- category
- description
- location
- hour
- risk_score
- is_anomaly
- created_at

Relationship:
- One User → Many Transactions

### 3️⃣ UserBaseline
- baseline_id (PK)
- user_id (FK)
- avg_spend
- std_spend
- category_distribution
- active_hours_distribution

Relationship:
- One User → One Baseline

---

# 6️⃣ Dataset Selected

## Dataset Name
Custom User Bank Statements (CSV / PDF)

## Source
User-uploaded bank statements

## Data Type
- Structured CSV  
- Semi-structured PDF bank statements  

## Selection Reason

- Real-world financial data format  
- Enables personalized anomaly detection  
- Reflects real behavioral spending patterns  

## Preprocessing Steps

1. Column standardization  
2. Currency symbol cleaning  
3. Merchant extraction  
4. Date-time parsing  
5. Category keyword mapping  
6. Feature generation (amount deviation, hour, frequency, etc.)  

---

# 7️⃣ Model Selected

## Model Name
Hybrid Statistical + Isolation Forest Model

Using:
- Z-Score Based Deviation  
- Behavioral Shift Detection  
- Frequency Spike Detection  
- Optional: IsolationForest (Scikit-learn)  

## Selection Reasoning

- Financial data is user-specific  
- No labeled anomaly data available  
- Need unsupervised detection  
- Isolation Forest handles multi-dimensional outliers  

## Alternatives Considered

- One-Class SVM  
- Local Outlier Factor  
- Autoencoder (deep learning)  
- Pure statistical threshold model  

Hybrid approach chosen for:
- Interpretability  
- Lower computational cost  
- Reduced overfitting risk  

## Evaluation Metrics

- Precision  
- Recall  
- F1 Score  
- False Positive Rate  
- Risk Score Distribution Analysis  

---

# 8️⃣ Technology Stack

## Frontend
- Streamlit  
- Plotly  
- Pandas  

## Backend
- FastAPI  
- Uvicorn  
- Pydantic  
- SQLAlchemy  

## ML/AI
- Scikit-learn  
- Isolation Forest  
- NumPy  
- Custom Statistical Engine  

## Database
- SQLite (development)  
- PostgreSQL (scalable option)  

## Deployment
- Render / Railway / AWS (Future-ready)  
- Docker (optional containerization)  

---

# 9️⃣ API Documentation & Testing

## API Endpoints List

### POST /upload
- Upload CSV/PDF  
- Parse & store transactions  

### POST /analyze
- Run anomaly detection  
- Generate risk scores  

### GET /transactions
- Fetch transactions with anomaly flags  

### GET /summary
- Fetch spending analytics summary  

---



---

# 🔟 Module-wise Development & Deliverables

## Checkpoint 1: Research & Planning
- Literature review  
- Anomaly detection model comparison  
- ER diagram design  

## Checkpoint 2: Backend Development
- FastAPI setup  
- Database models  
- API routing  

## Checkpoint 3: Frontend Development
- Streamlit dashboard  
- Upload interface  
- Visualization panels  

## Checkpoint 4: Model Training
- Feature engineering  
- Baseline calculation  
- Statistical detection engine  

## Checkpoint 5: Model Integration
- API → ML pipeline integration  
- Risk scoring logic  
- Explainability generation  

## Checkpoint 6: Deployment
- Production-ready server  
- Database persistence  
- UI integration  

---

# 1️⃣1️⃣ End-to-End Workflow

1. User uploads bank statement  
2. Backend parses transactions  
3. Data is normalized & categorized  
4. User behavioral baseline computed  
5. Hybrid anomaly engine evaluates transactions  
6. Risk score assigned  
7. Dashboard visualizes flagged anomalies  

---

# 1️⃣2️⃣ Demo & Video

- Live Demo Link: https://jagadish-555-person-finance-anomaly-backendstreamlit-app-2zojc0.streamlit.app/
- Demo Video Link: https://drive.google.com/file/d/1AaEn7InrQLz1HQZGrHYMruzp6PNNFOjT/view?usp=sharing)
- GitHub Repository: https://github.com/jagadish-555/Personal_Finance_Anomaly_Detector-vortex 

---

# 1️⃣3️⃣ Hackathon Deliverables Summary

- Fully functional backend API  
- Interactive anomaly dashboard  
- Hybrid anomaly detection engine  
- Explainable AI layer  
- Database integration  
- Modular project architecture  

---

# 1️⃣4️⃣ Team Roles & Responsibilities

| Member Name | Role | Responsibilities |
|-------------|------|-----------------|
| Jagadish Ishwar Patil | ML & Backend  
| Aditya Sinha | Backend and Deploymenton |
| Milan Kumar |Frontend and Presentation |

---

# 1️⃣5️⃣ Future Scope & Scalability

## Short-Term
- Add Autoencoder-based anomaly detection  
- Improve merchant classification  
- Add dynamic contamination tuning  

## Long-Term
- Multi-bank integration  
- Real-time transaction monitoring  
- Mobile app integration  
- AI-based financial advisory system  

---

# 1️⃣6️⃣ Known Limitations

- Requires minimum transaction history for stable baseline  
- Location-based anomaly depends on data availability  
- PDF parsing may vary by bank format  
- No real-time bank API integration yet  

---

# 1️⃣7️⃣ Impact

- Improves personal financial awareness  
- Reduces unnoticed abnormal spending  
- Encourages proactive financial monitoring  
- Provides explainable AI insights instead of black-box alerts  

---

# 🎯 Final Positioning Statement

Personal Finance Anomaly Detector is not a fraud system.

It is a behavioral intelligence system for personal finance, designed to convert transaction logs into explainable, risk-scored financial insights.
