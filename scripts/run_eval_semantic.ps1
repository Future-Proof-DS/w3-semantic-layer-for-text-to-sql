Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot\..

.\.venv\Scripts\python.exe -m evals.eval_runner --mode semantic
