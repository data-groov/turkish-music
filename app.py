import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuration de la page
st.set_page_config(
    page_title="Analyse Musicale Turque",
    page_icon="🎵",
    layout="wide"
)

# Connexion à la base de données
@st.cache_resource
def init_connection():
    return create_engine(st.secrets["postgres"]["url"])

# Chargement des données
@st.cache_data
def load_genre_data():
    return pd.read_sql("""
        SELECT 
            EXTRACT(YEAR FROM r.date_sortie) as annee,
            c.genre,
            COUNT(*) as nombre_releases
        FROM release r
        JOIN release_version rv ON r.id_release = rv.id_release
        JOIN version v ON rv.id_version = v.id_version
        JOIN chanson c ON v.id_chanson = c.id_chanson
        WHERE c.genre IS NOT NULL
        GROUP BY annee, genre
        ORDER BY annee;
    """, init_connection())

# Interface utilisateur
st.title("🎵 Analyse de la Musique Turque (1960-1990)")

try:
    # Chargement des données
    df = load_genre_data()
    
    # Création du graphique
    fig = px.line(
        df,
        x="annee",
        y="nombre_releases",
        color="genre",
        title="Évolution des genres musicaux"
    )
    
    # Affichage du graphique
    st.plotly_chart(fig, use_container_width=True)
    
except Exception as e:
    st.error(f"Erreur de connexion à la base de données: {str(e)}")
    st.info("Vérifiez les paramètres de connexion dans secrets.toml")
