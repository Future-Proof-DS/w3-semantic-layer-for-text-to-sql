Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot\..

$env:WORKSHOP_AGENT_MODE = "semantic"

.\.venv\Scripts\python.exe -m streamlit run app.py `
    --server.port 8502 `
    --server.headless true `
    --browser.gatherUsageStats false
