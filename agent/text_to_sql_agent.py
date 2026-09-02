"""Conversational Text-to-SQL agent over the local Olist DuckDB warehouse."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

import duckdb
from anthropic import Anthropic

from agent.context import load_schema_text, load_semantic_layer_text
from agent.paths import DATABASE_PATH, SEMANTIC_LAYER_PATH

SYSTEM_PROMPT_PREAMBLE = """
You are an analytics agent for the Olist e-commerce DuckDB warehouse.
Answer the user's question by writing a single DuckDB SQL query.

Rules:
- Use only the tables and columns listed in the schema below.
- Return ONLY the SQL query. No markdown fences, no commentary.
- Prefer explicit JOINs on keys. Avoid SELECT *.
- If the question is ambiguous, choose the simplest reasonable interpretation.
""".strip()


@dataclass
class AgentAnswer:
    """SQL plus the rows returned from DuckDB."""

    question: str
    sql: str
    columns: list[str]
    rows: list[tuple]
    is_semantic_layer_connected: bool


class AnalyticsAgent:
    """Ask a question in plain English, get SQL + query results."""

    def __init__(
        self,
        database_path: Path = DATABASE_PATH,
        semantic_layer_path: Path = SEMANTIC_LAYER_PATH,
        model_name: str = "claude-sonnet-4-5",
        use_semantic_layer: bool = False,
    ) -> None:
        self.database_path = database_path
        self.semantic_layer_path = semantic_layer_path
        self.model_name = model_name
        self.use_semantic_layer = use_semantic_layer
        self.schema_text = load_schema_text(database_path)
        # Everything is loaded and ready; the live wire-in decides whether it
        # enters the prompt.
        self.semantic_layer_text = load_semantic_layer_text(semantic_layer_path)
        self.client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    def build_system_prompt(self) -> tuple[str, bool]:
        """Assemble the system prompt. Returns prompt and whether semantic layer is connected."""
        prompt_parts: list[str] = [
            SYSTEM_PROMPT_PREAMBLE,
            "SCHEMA:\n" + self.schema_text,
        ]

        is_semantic_layer_connected = self.use_semantic_layer

        if self.use_semantic_layer:
            prompt_parts.append(
                "SEMANTIC LAYER (business definitions & join rules):\n"
                + self.semantic_layer_text
            )

        return "\n\n".join(prompt_parts), is_semantic_layer_connected

    def generate_sql(self, question: str) -> tuple[str, bool]:
        """Ask the model for SQL. Returns (sql, is_semantic_layer_connected)."""
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. Export it before starting the app."
            )

        system_prompt, is_semantic_layer_connected = self.build_system_prompt()
        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=1024,
            temperature=0,
            system=system_prompt,
            messages=[{"role": "user", "content": question}],
        )
        raw_text = response.content[0].text
        return _extract_sql(raw_text), is_semantic_layer_connected

    def ask(self, question: str) -> AgentAnswer:
        """Generate SQL, run it on DuckDB, and return the answer payload."""
        generated_sql, is_semantic_layer_connected = self.generate_sql(question)
        columns, rows = self._execute_sql(generated_sql)

        return AgentAnswer(
            question=question,
            sql=generated_sql,
            columns=columns,
            rows=rows,
            is_semantic_layer_connected=is_semantic_layer_connected,
        )

    def _execute_sql(self, sql: str) -> tuple[list[str], list[tuple]]:
        """Run read-only SQL against the local warehouse."""
        connection = duckdb.connect(str(self.database_path), read_only=True)
        cursor = connection.execute(sql)
        columns = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
        connection.close()
        return columns, rows


def _extract_sql(raw_text: str) -> str:
    """Pull SQL out of optional markdown fences the model sometimes adds."""
    fenced_match = re.search(r"```(?:sql)?\s*(.*?)```", raw_text, re.DOTALL | re.IGNORECASE)
    if fenced_match:
        return fenced_match.group(1).strip().rstrip(";")

    return raw_text.strip().rstrip(";")
