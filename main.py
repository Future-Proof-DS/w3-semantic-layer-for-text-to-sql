"""CLI helper for one-off questions against the analytics agent."""

import argparse

from agent.text_to_sql_agent import AnalyticsAgent


def main() -> None:
    """Ask one question from the terminal."""
    parser = argparse.ArgumentParser(description="Olist analytics agent CLI")
    parser.add_argument("--question", required=True, help="Natural-language question")
    args = parser.parse_args()

    agent = AnalyticsAgent()
    answer = agent.ask(args.question)
    print(answer.sql)
    print(answer.columns)
    for row in answer.rows:
        print(row)
    print(
        "semantic_layer:"
        + ("connected" if answer.is_semantic_layer_connected else "disconnected")
    )


if __name__ == "__main__":
    main()
