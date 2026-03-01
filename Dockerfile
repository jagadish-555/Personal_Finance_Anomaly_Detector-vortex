# Dockerfile for Vortex Finance — FastAPI backend only (Render)
# Streamlit frontend is deployed separately on Streamlit Cloud
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY finance_anomaly_backend/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY finance_anomaly_backend/ /app/

# Render provides a dynamic $PORT — FastAPI listens on it
EXPOSE 8000

# Run FastAPI on Render's dynamic PORT (defaults to 8000 locally)
CMD ["sh", "-c", "python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
