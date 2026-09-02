"""Semantic-aware Text-to-SQL entry point."""

from agent.text_to_sql_agent import AnalyticsAgent


class SemanticAgent(AnalyticsAgent):
    """Agent that loads business definitions from the semantic layer YAML."""

    def __init__(self, **kwargs) -> None:
        super().__init__(use_semantic_layer=True, **kwargs)
