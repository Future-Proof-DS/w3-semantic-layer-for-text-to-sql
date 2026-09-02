"""Ingest raw Olist CSVs into a DuckDB warehouse."""

from pathlib import Path

import duckdb

DATA_DIRECTORY = Path(__file__).parent / "data"
DATABASE_PATH = DATA_DIRECTORY / "olist.duckdb"

# CSV stem -> short table name used by the semantic layer
CSV_TO_TABLE: dict[str, str] = {
    "olist_customers_dataset": "customers",
    "olist_geolocation_dataset": "geolocation",
    "olist_orders_dataset": "orders",
    "olist_order_items_dataset": "order_items",
    "olist_order_payments_dataset": "order_payments",
    "olist_order_reviews_dataset": "order_reviews",
    "olist_products_dataset": "products",
    "olist_sellers_dataset": "sellers",
    "product_category_name_translation": "product_category_name_translation",
}


def create_olist_database() -> Path:
    """Create DuckDB file and load each Olist CSV under its semantic-layer name."""
    if DATABASE_PATH.exists():
        DATABASE_PATH.unlink()

    connection = duckdb.connect(str(DATABASE_PATH))

    for csv_stem, table_name in CSV_TO_TABLE.items():
        csv_path = DATA_DIRECTORY / f"{csv_stem}.csv"
        connection.execute(
            f"""
            CREATE TABLE {table_name} AS
            SELECT * FROM read_csv_auto(?, header=true)
            """,
            [str(csv_path)],
        )

    connection.close()
    return DATABASE_PATH


if __name__ == "__main__":
    created_database_path = create_olist_database()
    print(f"Created {created_database_path}")
