Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot\..

.\.venv\Scripts\python.exe -m streamlit run app.py `
    --server.port 8501 `
    --server.headless true `
    --browser.gatherUsageStats false
