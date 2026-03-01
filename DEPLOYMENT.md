# Vortex Finance Deployment Guide (Non-Streamlit)

This project is containerized using Docker to be deployed on platforms like **Render**, **Railway**, or **AWS/GCP**.

## 🚀 Deployment Options

### 1. Render / Railway (Easiest)
Both Render and Railway support `Dockerfile` deployments. 
1. Push this project to your GitHub.
2. Connect your repo to [Render](https://render.com) or [Railway](https://railway.app).
3. The platform will automatically detect the `Dockerfile` and build the image.
4. **Ports to Expose**: 
   - Port `8501` for the Streamlit UI.
   - Port `8000` for the FastAPI backend.

### 2. Manual Docker Deployment
If you have a VPS (DigitalOcean, Linode):
```bash
# Build the image
docker build -t vortex-finance .

# Run the container
docker run -p 8501:8501 -p 8000:8000 vortex-finance
```

## 🛠️ Configuration Note
Ensure `streamlit_app.py` points to your deployed backend URL.
Current setting: `API_BASE = "http://localhost:8000"` (works if both run in the same container).

## 📁 Files Created
- `Dockerfile`: Multi-process container setup (FastAPI + Streamlit).
- `start.sh`: Shell script to launch both services on startup.
