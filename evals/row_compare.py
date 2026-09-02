"""Normalize and compare DuckDB result rows for eval scoring."""


def normalize_cell(value: object) -> object:
    """Round floats so JSON and DuckDB compare cleanly."""
    if isinstance(value, float):
        return round(value, 2)
    return value


def normalize_rows(rows: list[tuple]) -> list[list[object]]:
    """Normalize every cell in a DuckDB result set."""
    return [
        [normalize_cell(cell) for cell in row]
        for row in rows
    ]
