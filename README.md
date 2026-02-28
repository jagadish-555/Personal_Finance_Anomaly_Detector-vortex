# 💳 Personal Finance Anomaly Detector

> Turning transaction data into actionable financial intelligence.


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

### 3️Hybrid Anomaly Detection
- Z-score deviation
- Rolling average comparison
- New merchant detection
- Frequency spike detection
- Isolation Forest (optional)

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

# __System Architecture__

Bank Statement  
↓  
Parsing & Normalization  
↓  
Categorization  
↓  
Feature Engineering  
↓  
Anomaly Detection Engine  
↓  
Risk Scoring  
↓  
Dashboard & Alerts  


---

# __Objective__

Move personal finance from:

**Passive transaction viewing**

to

**Proactive behavioral financial monitoring**
