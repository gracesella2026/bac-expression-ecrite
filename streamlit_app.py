# -*- coding: utf-8 -*-
"""Entraînement à l'expression écrite du bac de FLE.

L'application est un fichier HTML autonome, sans base de données et sans appel
réseau. Streamlit ne fait que l'afficher : tout le travail de l'élève reste dans
son navigateur, et la remise passe par Google Classroom.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

FICHIER = Path(__file__).parent / "static" / "expression-ecrite-eleves.html"
LIEN_PLEIN_ECRAN = "app/static/expression-ecrite-eleves.html"

st.set_page_config(
    page_title="Expression écrite — bac de FLE",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# On efface le bandeau et les marges de Streamlit, et on étire le cadre de
# l'application sur toute la hauteur de l'écran : l'élève ne voit que l'exercice.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu {display: none;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
      iframe[title="streamlit.components.v1.html"] {height: 100vh !important; width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def page() -> str:
    """Le fichier pèse environ 3 Mo (les 60 photos sont dedans) : on le lit une fois."""
    return FICHIER.read_text(encoding="utf-8")


if not FICHIER.exists():
    st.error(
        "Fichier introuvable : static/expression-ecrite-eleves.html\n\n"
        "Vérifiez que le fichier a bien été envoyé sur GitHub."
    )
else:
    components.html(page(), height=1400, scrolling=True)
    st.caption(
        "Si l'affichage est trop étroit, ouvrez l'application en plein écran : "
        f"[expression-ecrite-eleves.html]({LIEN_PLEIN_ECRAN})"
    )
