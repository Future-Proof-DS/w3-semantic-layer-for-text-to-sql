"""Evaluation harness: run gold questions through the agent and score pass/fail."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from agent.env import load_project_env
from agent.semantic_agent import SemanticAgent
from agent.text_to_sql_agent import AnalyticsAgent
from evals.row_compare import normalize_rows

GOLD_QUESTIONS_PATH = Path(__file__).parent / "gold_questions.json"

MODE_LABELS: dict[str, str] = {
    "schema": "schema only",
    "semantic": "semantic layer",
}


def _build_agent(mode: str) -> AnalyticsAgent:
    """Return the agent for schema-only or semantic-layer scoring."""
    if mode == "schema":
        return AnalyticsAgent(use_semantic_layer=False)
    if mode == "semantic":
        return SemanticAgent()
    raise ValueError(f"Unknown mode: {mode}")


def run_evaluation(mode: str = "semantic") -> int:
    """Score an agent against all gold questions. Returns exit code."""
    gold_questions = json.loads(GOLD_QUESTIONS_PATH.read_text(encoding="utf-8"))
    agent = _build_agent(mode)
    mode_label = MODE_LABELS[mode]
    pass_count = 0

    print(f"Eval harness — {mode_label} ({len(gold_questions)} questions)\n")

    for question in gold_questions:
        question_id = question["id"]
        try:
            answer = agent.ask(question["question"])
            actual_rows = normalize_rows(answer.rows)
            expected_rows = normalize_rows(
                [tuple(row) for row in question["expected_rows"]]
            )
            passed = actual_rows == expected_rows
        except Exception as error:
            print(f"FAIL {question_id}: {error}")
            continue

        if passed:
            pass_count += 1
            print(f"PASS {question_id}")
        else:
            print(
                f"FAIL {question_id}: expected {expected_rows}, got {actual_rows}"
            )

    total_count = len(gold_questions)
    score_percent = round(100 * pass_count / total_count)
    print(f"\nScore: {pass_count}/{total_count} ({score_percent}%)")

    return 0


def main() -> None:
    """Parse CLI args and run the harness."""
    load_project_env()

    parser = argparse.ArgumentParser(
        description="Score Text-to-SQL agent on gold questions"
    )
    parser.add_argument(
        "--mode",
        choices=["schema", "semantic"],
        default="semantic",
        help="schema = no semantic layer, semantic = SemanticAgent (default)",
    )
    args = parser.parse_args()
    raise SystemExit(run_evaluation(args.mode))


if __name__ == "__main__":
    main()
