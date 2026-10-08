@echo off
setlocal
cd /d "%~dp0.."

set WORKSHOP_AGENT_MODE=schema

.\.venv\Scripts\python.exe -m streamlit run app.py --server.port 8501 --server.headless true --browser.gatherUsageStats false
