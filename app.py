"""Minimal Streamlit chat UI for the analytics agent."""

from __future__ import annotations

import streamlit as st

from agent.semantic_agent import SemanticAgent
from agent.text_to_sql_agent import AgentAnswer
from ui.theme import apply_page_style, render_mode_badge


def _format_result_table(answer: AgentAnswer) -> str:
    """Render query rows as a compact markdown table."""
    if not answer.rows:
        return "_No rows returned._"

    header = " | ".join(answer.columns)
    separator = " | ".join("---" for _ in answer.columns)
    body_lines = [
        " | ".join(str(value) for value in row) for row in answer.rows[:50]
    ]
    return "\n".join([header, separator, *body_lines])


def main() -> None:
    """Run a plain chat interface over the warehouse agent."""
    st.set_page_config(page_title="Chat — semantic layer", page_icon=None, layout="centered")
    apply_page_style()
    render_mode_badge()

    if "agent" not in st.session_state:
        st.session_state.agent = SemanticAgent()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    agent: SemanticAgent = st.session_state.agent

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_question = st.chat_input("Ask AI", width="stretch")
    if user_question is None:
        return

    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner(""):
            try:
                answer = agent.ask(user_question)
            except Exception as error:
                error_text = f"Could not answer that: {error}"
                st.markdown(error_text)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_text}
                )
                return

            result_markdown = _format_result_table(answer)
            st.markdown(result_markdown)
            st.markdown("**SQL**")
            st.code(answer.sql, language="sql")

            assistant_content = f"{result_markdown}\n\n```sql\n{answer.sql}\n```"
            st.session_state.messages.append(
                {"role": "assistant", "content": assistant_content}
            )


if __name__ == "__main__":
    main()
