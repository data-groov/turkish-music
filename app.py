import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("Test Base de Données")

try:
    engine = create_engine(st.secrets["postgres"]["url"])
    with engine.connect() as conn:
        result = conn.execute("SELECT COUNT(*) FROM release").fetchone()[0]
        st.success(f"Connexion OK - {result} releases trouvées")
except Exception as e:
    st.error(f"Erreur: {str(e)}")
