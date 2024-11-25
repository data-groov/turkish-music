import streamlit as st
from sqlalchemy import create_engine, text

st.title("Test Base de Données")

try:
    engine = create_engine(st.secrets["postgres"]["url"])
    with engine.connect() as conn:
        # Liste des tables
        tables = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)).fetchall()
        
        st.success("Connexion OK")
        st.write("Tables disponibles:", [table[0] for table in tables])
except Exception as e:
    st.error(f"Erreur: {str(e)}")
