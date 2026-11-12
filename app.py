import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="TINY APOCALYPSE: SCRAP KINGS", page_icon="⚙️", layout="wide")
st.markdown("""
<style>
  .block-container {padding: .5rem .5rem 0 .5rem; max-width: 100%;}
  header, footer {visibility:hidden;}
  [data-testid="stToolbar"] {display:none;}
</style>
""", unsafe_allow_html=True)

html = Path(__file__).parent / "game.html"
components.html(html.read_text(encoding="utf-8"), height=900, scrolling=False)
