"""Naive Text-to-SQL entry point (schema only, no semantic layer)."""

from agent.text_to_sql_agent import AnalyticsAgent


class BaseAgent(AnalyticsAgent):
    """Schema-only agent for the baseline workshop score."""

    def __init__(self, **kwargs) -> None:
        super().__init__(use_semantic_layer=False, **kwargs)
