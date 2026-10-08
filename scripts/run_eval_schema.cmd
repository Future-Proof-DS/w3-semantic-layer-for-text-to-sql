@echo off
setlocal
cd /d "%~dp0.."

.\.venv\Scripts\python.exe -m evals.eval_runner --mode schema
