"""Format warehouse schema and semantic-layer YAML for the LLM prompt."""

from __future__ import annotations

from pathlib import Path

import duckdb
import yaml

from agent.paths import CORE_TABLE_NAMES, DATABASE_PATH, SEMANTIC_LAYER_PATH


def load_schema_text(
    database_path: Path = DATABASE_PATH,
    table_names: list[str] | None = None,
) -> str:
    """Read column lists from DuckDB for the tables the agent may query."""
    selected_table_names = table_names or CORE_TABLE_NAMES
    connection = duckdb.connect(str(database_path), read_only=True)

    schema_blocks: list[str] = []
    for table_name in selected_table_names:
        columns = connection.execute(
            """
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = ?
            ORDER BY ordinal_position
            """,
            [table_name],
        ).fetchall()

        if not columns:
            continue

        column_lines = "\n".join(
            f"  - {column_name}: {data_type}" for column_name, data_type in columns
        )
        schema_blocks.append(f"TABLE {table_name}\n{column_lines}")

    connection.close()

    if not schema_blocks:
        raise FileNotFoundError(
            f"No core tables found in {database_path}. Run setup_db.py after placing CSVs in data/."
        )

    return "\n\n".join(schema_blocks)


def load_semantic_layer_text(config_path: Path = SEMANTIC_LAYER_PATH) -> str:
    """Render the bootcamp-style semantic layer YAML as plain text for the prompt."""
    with config_path.open(encoding="utf-8") as config_file:
        semantic_layer = yaml.safe_load(config_file)

    return yaml.safe_dump(semantic_layer, sort_keys=False)
