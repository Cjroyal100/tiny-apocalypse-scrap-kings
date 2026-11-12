import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="Tiny Apocalypse: Scrap Kings", page_icon="⚙️", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>#MainMenu,footer,header{visibility:hidden}.block-container{padding:0!important;max-width:100%!important}[data-testid="stAppViewContainer"]{background:#0d120f}iframe{border:0!important;display:block}</style>""", unsafe_allow_html=True)
html_path=Path(__file__).parent/"game.html"
if not html_path.exists(): st.error("game.html is missing. Put it beside app.py in the repository root.")
else: components.html(html_path.read_text(encoding="utf-8"), height=900, scrolling=False)
