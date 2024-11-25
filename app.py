import streamlit as st
from sqlalchemy import create_engine, text

st.title("Test Base de Données")

try:
    engine = create_engine(st.secrets["postgres"]["url"])
    with engine.connect() as conn:
        # Test insertion
        conn.execute(text("INSERT INTO label (nom, pays) VALUES ('Test Label', 'France')"))
        conn.commit()
        
        # Vérification
        result = conn.execute(text("SELECT COUNT(*) FROM label")).scalar()
        st.success(f"Connexion OK - {result} labels trouvés")
except Exception as e:
    st.error(f"Erreur: {str(e)}")
