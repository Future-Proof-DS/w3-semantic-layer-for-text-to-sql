"""Shared paths and helpers for the Olist analytics agent."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIRECTORY = PROJECT_ROOT / "data"
DATABASE_PATH = DATA_DIRECTORY / "olist.duckdb"
SEMANTIC_LAYER_PATH = PROJECT_ROOT / "configs" / "semantic_layer.yaml"

# Tables the chat agent is allowed to see (keeps prompts small and on-story).
CORE_TABLE_NAMES: list[str] = [
    "orders",
    "customers",
    "order_items",
    "order_payments",
    "products",
    "sellers",
]
