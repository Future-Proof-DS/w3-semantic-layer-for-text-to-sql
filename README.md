# Workshop 3 — Semantic Layer for Text-to-SQL

Local DuckDB demo comparing a schema-only Text-to-SQL agent against a semantic-aware agent on the [Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) dataset.

A Streamlit chat is the agent face; the eval harness stays CLI.

## Dataset

Brazilian E-Commerce Public Dataset by Olist — ~100k orders from 2016–2018 across multiple marketplaces in Brazil. Real commercial data, anonymised (store/partner names replaced with Game of Thrones houses).

You can view an order from multiple angles: status, price, payment, freight, customer location, product attributes, and reviews. A geolocation file maps Brazilian zip prefixes to lat/lng.

**Olist** connects small businesses to marketplaces under one contract; sellers fulfill and ship via Olist logistics partners. After delivery (or the estimated date), customers get a satisfaction survey.

Notes that matter for analytics:
- An order can have multiple items.
- Items on the same order can come from different sellers.
- Payment value includes freight; product revenue should not confuse the two.
- Joining `order_payments` directly to `order_items` fans out rows and double-counts.

CSVs live in `data/`; `python setup_db.py` loads them into `data/olist.duckdb` under short table names (`orders`, `customers`, `order_items`, …).

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python setup_db.py
copy .env.example .env
```

Edit `.env` locally and set `ANTHROPIC_API_KEY`. The file is gitignored — never paste the key in the terminal during a demo.

## Run the chat UI

Two launcher scripts — schema-only (port **8501**) and semantic layer (port **8502**):

```powershell
.\scripts\run_chat_schema.ps1
.\scripts\run_chat_semantic.ps1
```

Browser titles: **Chat — schema only** and **Chat — semantic layer**.

## Eval harness (CLI)

```powershell
.\scripts\run_eval_schema.ps1
.\scripts\run_eval_semantic.ps1
```

Or directly:

```powershell
python -m evals.eval_runner --mode schema
python -m evals.eval_runner --mode semantic
```

Scoreboard stays in the terminal — not in the chat UI.

## Layout

```
app.py                        # Streamlit chat (mode via WORKSHOP_AGENT_MODE)
scripts/                      # Demo launchers (chat + eval)
agent/
  base_agent.py               # Schema-only agent
  semantic_agent.py           # Semantic-layer agent
  text_to_sql_agent.py        # Shared Text-to-SQL engine
configs/semantic_layer.yaml   # Tables, measures, relationships, golden queries
evals/                        # Gold questions + harness
data/                         # Olist CSVs + olist.duckdb
setup_db.py                   # CSV → DuckDB
main.py                       # One-shot CLI ask
```
