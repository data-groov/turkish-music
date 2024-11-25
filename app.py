import streamlit as st
from sqlalchemy import create_engine, text

st.title("Test Base de Données")

try:
    engine = create_engine(st.secrets["postgres"]["url"])
    with engine.connect() as conn:
        # Simple test
        result = conn.execute(text("SELECT NOW()")).scalar()
        st.success(f"Connexion OK - Heure serveur : {result}")
except Exception as e:
    st.error(f"Erreur: {str(e)}")
