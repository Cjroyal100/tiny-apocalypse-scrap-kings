import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tiny Apocalypse: Scrap Kings",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the game area clean and mobile-friendly.
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    [data-testid="stAppViewContainer"] {background: #0d120f;}
    [data-testid="stVerticalBlock"] {gap: 0 !important;}
    iframe {border: 0 !important;}
</style>
""", unsafe_allow_html=True)

game_file = Path(__file__).parent / "game.html"
if not game_file.exists():
    st.error("The game.html file is missing. Make sure it is in the same folder as app.py.")
else:
    html = game_file.read_text(encoding="utf-8")
    components.html(html, height=850, scrolling=False)
