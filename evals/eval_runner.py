"""Evaluation harness: run gold questions through the agent and score pass/fail."""

from __future__ import annotations

import json
from pathlib import Path

from agent.semantic_agent import SemanticAgent
from evals.row_compare import normalize_rows

GOLD_QUESTIONS_PATH = Path(__file__).parent / "gold_questions.json"


def run_evaluation() -> int:
    """Score the semantic agent against all gold questions. Returns exit code."""
    gold_questions = json.loads(GOLD_QUESTIONS_PATH.read_text(encoding="utf-8"))
    agent = SemanticAgent()
    pass_count = 0

    print(f"Eval harness — semantic layer ({len(gold_questions)} questions)\n")

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
            passed = False
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
    """Run the harness."""
    raise SystemExit(run_evaluation())


if __name__ == "__main__":
    main()
