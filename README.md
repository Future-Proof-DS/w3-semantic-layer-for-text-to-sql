# Semantic Layer Text-to-SQL

Local DuckDB demo: a Streamlit chat backed by a semantic-aware Text-to-SQL agent on the [Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) dataset.

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

Edit `.env` and set `ANTHROPIC_API_KEY`.

## Run the chat UI

```powershell
.\scripts\run_chat.ps1
```

Opens at http://localhost:8501. Business definitions come from `configs/semantic_layer.yaml`.

## Eval harness (CLI)

```powershell
.\scripts\run_eval.ps1
```

Or:

```powershell
python -m evals.eval_runner
```

## Layout

```
app.py                        # Streamlit chat
scripts/                      # Launchers (chat + eval)
agent/
  semantic_agent.py           # Semantic-layer agent
  text_to_sql_agent.py        # Shared Text-to-SQL engine
configs/semantic_layer.yaml   # Tables, measures, relationships, golden queries
evals/                        # Gold questions + harness
data/                         # Olist CSVs + olist.duckdb
setup_db.py                   # CSV → DuckDB
main.py                       # One-shot CLI ask
```
