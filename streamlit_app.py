# -*- coding: utf-8 -*-
"""Entraînement à l'expression écrite du bac de FLE.

L'application est un fichier HTML autonome, sans compte, sans base de données
et sans appel réseau. Streamlit ne fait que l'afficher : le travail de l'élève
reste dans son navigateur, et la remise passe par Google Classroom.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

RACINE = Path(__file__).parent

st.set_page_config(
    page_title="Expression écrite — bac de FLE",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# On efface le bandeau et les marges de Streamlit, et on étire l'application
# sur toute la hauteur de l'écran : l'élève ne voit que l'exercice.
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


def trouver_application():
    """Le plus gros fichier .html du dépôt, où qu'il soit et quel que soit son nom."""
    candidats = [p for p in RACINE.rglob("*.html") if p.is_file() and ".git" not in p.parts]
    return max(candidats, key=lambda p: p.stat().st_size) if candidats else None


@st.cache_data(show_spinner=False)
def page(chemin: str, taille: int) -> str:
    """Le fichier pèse environ 3 Mo (les 60 photos sont dedans) : on le lit une fois."""
    return Path(chemin).read_text(encoding="utf-8")


application = trouver_application()

if application is None:
    st.error("Aucun fichier .html n'a été trouvé dans le dépôt.")
    presents = sorted(
        p.relative_to(RACINE).as_posix()
        for p in RACINE.rglob("*")
        if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
    )
    st.write("Voici ce que contient réellement le dépôt :")
    st.code("\n".join(presents) or "(aucun fichier)")
else:
    components.html(page(str(application), application.stat().st_size),
                    height=1400, scrolling=True)
