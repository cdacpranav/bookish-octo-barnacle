import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="🕉️ Ujjain Sacred Journey — Travel Planner",
    page_icon="🕉️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide Streamlit chrome for full-screen HTML experience ────
st.markdown(
    """
    <style>
        /* Hide header, footer, and menu */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stAppDeployButton {display: none;}

        /* Remove default padding so HTML fills the viewport */
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            max-width: 100% !important;
        }

        /* Make the iframe container fill the screen */
        iframe {
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Load and render the HTML ─────────────────────────────────
html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# Render full-page — height set tall enough to avoid inner scroll
components.html(html_content, height=12000, scrolling=True)
