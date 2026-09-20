"""Shared Streamlit theme for the chat UI."""

ACCENT_COLOR = "#e2b84b"
PAGE_BACKGROUND = "#ffffff"
SURFACE_COLOR = "#f0f0f0"
TEXT_COLOR = "#000000"
MUTED_TEXT_COLOR = "#6b6b6b"
BORDER_COLOR = "#e5e5e5"
CODE_BACKGROUND = "#f5f5f5"
CHAT_CONTENT_MAX_WIDTH = "736px"
CHAT_INPUT_RADIUS = "28px"

PAGE_STYLE = f"""
<style>
    html, body, .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > section,
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    [data-testid="stHeader"],
    section.main,
    .block-container,
    .main .block-container,
    [data-testid="stBottom"],
    [data-testid="stBottom"] > div,
    [data-testid="stBottomBlockContainer"] {{
        background-color: {PAGE_BACKGROUND} !important;
        background-image: none !important;
        color: {TEXT_COLOR} !important;
        border: none !important;
        border-top: none !important;
        box-shadow: none !important;
        outline: none !important;
    }}

    [data-testid="stToolbar"] {{
        display: none !important;
    }}

    [data-testid="stHeader"] {{
        height: 0 !important;
        min-height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        border: none !important;
        overflow: visible !important;
    }}

    .block-container,
    [data-testid="stMainBlockContainer"] .block-container {{
        padding-top: 2.5rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: {CHAT_CONTENT_MAX_WIDTH} !important;
        overflow: visible !important;
    }}

    [data-testid="stBottom"] {{
        position: sticky !important;
        border-top: none !important;
        box-shadow: none !important;
        background: {PAGE_BACKGROUND} !important;
    }}

    [data-testid="stBottom"]::before,
    [data-testid="stBottom"]::after,
    [data-testid="stBottom"] > div::before,
    [data-testid="stBottom"] > div::after {{
        content: none !important;
        display: none !important;
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
    }}

    [data-testid="stBottomBlockContainer"] {{
        max-width: {CHAT_CONTENT_MAX_WIDTH} !important;
        width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 0.75rem !important;
        padding-bottom: 1.25rem !important;
        border-top: none !important;
        box-shadow: none !important;
        background: {PAGE_BACKGROUND} !important;
    }}

    [data-testid="stBottomBlockContainer"] [data-testid="stVerticalBlock"],
    [data-testid="stBottomBlockContainer"] [data-testid="stVerticalBlock"] > div,
    [data-testid="stBottomBlockContainer"] [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stBottomBlockContainer"] [data-testid="element-container"],
    [data-testid="stBottomBlockContainer"] .stElementContainer,
    [data-testid="stBottomBlockContainer"] .stChatInput,
    [data-testid="stBottomBlockContainer"] [data-testid="stChatInput"],
    [data-testid="stBottomBlockContainer"] [data-testid="stChatInput"] > div {{
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        border: none !important;
        border-top: none !important;
        box-shadow: none !important;
    }}

    [data-testid="stChatMessage"] {{
        background-color: {PAGE_BACKGROUND} !important;
        border: none !important;
        overflow: visible !important;
        padding-top: 0.25rem;
    }}

    [data-testid="stChatMessage"]:first-of-type {{
        margin-top: 0.5rem;
    }}

    [data-testid="chatAvatarIcon-user"],
    [data-testid="chatAvatarIcon-assistant"] {{
        overflow: visible !important;
    }}

    [data-testid="stChatMessageContent"] {{
        background-color: {PAGE_BACKGROUND} !important;
        color: {TEXT_COLOR} !important;
    }}

    div[data-testid="stChatInput"] > div,
    div[class*="e1p9v2yr1"] {{
        background-color: {SURFACE_COLOR} !important;
        border: none !important;
        border-color: transparent !important;
        border-radius: {CHAT_INPUT_RADIUS} !important;
        box-shadow: none !important;
        padding-top: 0.55rem !important;
        padding-bottom: 0.55rem !important;
        padding-left: 1rem !important;
        padding-right: 0.75rem !important;
    }}

    div[data-testid="stChatInput"] > div:focus-within,
    div[class*="e1p9v2yr1"]:focus-within {{
        border: none !important;
        border-color: transparent !important;
        box-shadow: none !important;
    }}

    div[data-testid="stChatInput"] textarea,
    [data-testid="stChatInputTextArea"] {{
        background-color: transparent !important;
        color: {TEXT_COLOR} !important;
        -webkit-text-fill-color: {TEXT_COLOR} !important;
        caret-color: {TEXT_COLOR} !important;
    }}

    div[data-testid="stChatInput"] textarea::placeholder,
    [data-testid="stChatInputTextArea"]::placeholder {{
        color: {MUTED_TEXT_COLOR} !important;
        opacity: 1 !important;
    }}

    div[data-testid="stChatInput"] button {{
        background-color: transparent !important;
        color: {TEXT_COLOR} !important;
        border: none !important;
    }}

    .stMarkdown, .stMarkdown p, label {{
        color: {TEXT_COLOR} !important;
    }}

    .stMarkdown code {{
        background-color: {CODE_BACKGROUND} !important;
        color: {TEXT_COLOR} !important;
        border: 1px solid {BORDER_COLOR};
        padding: 0.1rem 0.35rem;
        border-radius: 4px;
    }}

    pre, code, .stCode, .stCodeBlock, [data-testid="stCode"], [data-testid="stCodeBlock"] {{
        background-color: {PAGE_BACKGROUND} !important;
        color: {TEXT_COLOR} !important;
        border: 1px solid {BORDER_COLOR} !important;
    }}

    .result-value {{
        font-size: 1.75rem;
        font-weight: 700;
        color: {TEXT_COLOR};
        margin: 0.25rem 0 1rem 0;
    }}

    .result-label {{
        font-size: 0.8rem;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        color: {MUTED_TEXT_COLOR};
        margin-bottom: 0.15rem;
    }}

    .mode-badge {{
        position: fixed;
        top: 1rem;
        left: 1rem;
        z-index: 999;
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        font-size: 0.8rem;
        line-height: 1;
        color: {TEXT_COLOR};
        pointer-events: none;
        user-select: none;
    }}

    .mode-badge__dot {{
        width: 0.45rem;
        height: 0.45rem;
        border-radius: 50%;
        background-color: {ACCENT_COLOR};
        flex-shrink: 0;
    }}

    /* Keep the fixed badge out of the chat document flow */
    .stElementContainer:has(.mode-badge),
    [data-testid="stHtml"]:has(.mode-badge),
    div:has(> .mode-badge) {{
        height: 0 !important;
        min-height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        border: none !important;
        overflow: visible !important;
    }}
</style>
"""


def apply_page_style() -> None:
    """Inject shared chat styles into the Streamlit document head area."""
    import streamlit as st

    st.html(PAGE_STYLE)


def render_mode_badge() -> None:
    """Show a quiet top-left chip for the semantic layer."""
    import streamlit as st

    st.html(
        '<div class="mode-badge">'
        '<span class="mode-badge__dot"></span>'
        "Semantic layer"
        "</div>"
    )
