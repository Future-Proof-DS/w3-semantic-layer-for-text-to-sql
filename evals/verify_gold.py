"""Verify every gold_sql result matches expected_rows."""

from __future__ import annotations

import json
from pathlib import Path

import duckdb

from evals.row_compare import normalize_rows

GOLD_PATH = Path(__file__).parent / "gold_questions.json"
DATABASE_PATH = Path(__file__).resolve().parent.parent / "data" / "olist.duckdb"


def verify_gold_questions() -> None:
    """Execute each gold query and compare to the stored expected rows."""
    questions = json.loads(GOLD_PATH.read_text(encoding="utf-8"))
    connection = duckdb.connect(str(DATABASE_PATH), read_only=True)
    failure_count = 0

    for question in questions:
        actual_rows = normalize_rows(connection.execute(question["gold_sql"]).fetchall())
        expected_rows = normalize_rows(
            [tuple(row) for row in question["expected_rows"]]
        )

        if actual_rows != expected_rows:
            failure_count += 1
            print(f"FAIL {question['id']}: expected {expected_rows}, got {actual_rows}")
        else:
            print(f"PASS {question['id']}")

    connection.close()

    if failure_count:
        raise SystemExit(f"{failure_count} gold question(s) failed verification")

    print(f"All {len(questions)} gold questions verified against DuckDB.")


if __name__ == "__main__":
    verify_gold_questions()
