"""Interface Streamlit pour TrouveUnCadeau.xyz

Moteur de recommandation de cadeaux intelligents pour Québec
Client frontal utilisant FastAPI backend
"""

import streamlit as st
import requests
import json
from datetime import datetime
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="TrouveUnCadeau - Moteur de recommandation",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #00D9FF;
        color: #000;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem;
    }
    .stButton > button:hover {
        background-color: #00B8D4;
    }
</style>
""", unsafe_allow_html=True)

# Configuration de l'API backend
BACKEND_URL = "http://localhost:8000"

# Initialiser la session
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'products' not in st.session_state:
    st.session_state.products = None

# En-tête principal
st.title("🎁 TrouveUnCadeau.xyz")
st.markdown("""
### Moteur de recommandation de cadeaux intelligents pour Québec

Trouvez le cadeau parfait grâce à l'IA! Décrivez votre budget, l'âge du destinataire,
l'occasion, et ses intérêts pour obtenir des recommandations personnalisées.
""")

st.divider()

# Barre latérale
with st.sidebar:
    st.header("⚙️ Paramétrage")
    st.markdown("---")
    
    budget = st.slider(
        "Budget (CAD)",
        min_value=10.0,
        max_value=500.0,
        value=50.0,
        step=5.0,
        help="Définissez votre budget maximal en dollars canadiens"
    )
    
    recipient_age = st.number_input(
        "Âge du destinataire",
        min_value=1,
        max_value=120,
        value=25,
        help="L'âge approximatif de la personne qui recevra le cadeau"
    )
    
    occasions = ["Anniversaire", "Noël", "Fête", "Remerciment", "Autre"]
    occasion = st.selectbox(
        "Occasion",
        occasions,
        help="Choisissez l'occasion de ce cadeau"
    )
    
    st.markdown("---")
    
    count = st.slider(
        "Nombre de recommandations",
        min_value=1,
        max_value=10,
        value=5,
        help="Combien de suggestions voulez-vous?"
    )

# Formulaire principal
col1, col2 = st.columns([3, 1])

with col1:
    interests = st.text_area(
        "💡 Intérêts et passions du destinataire",
        placeholder="Ex: Musique, photographie, cuisine, sport, lecture, technologie, voyage...",
        height=100,
        help="Décrivez les intérêts de la personne pour obtenir des recommandations plus pertinentes"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    generate_button = st.button(
        "🌟 Générer\nrecommandations",
        use_container_width=True
    )

st.divider()

# Section des résultats
if generate_button or st.session_state.recommendations:
    if generate_button:
        with st.spinner("🤖 TrouveUnCadeau analyse vos préférences..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/api/recommendations",
                    params={
                        "budget": budget,
                        "recipient_age": recipient_age,
                        "occasion": occasion.lower(),
                        "interests": interests,
                        "count": count
                    },
                    timeout=30
                )
                response.raise_for_status()
                st.session_state.recommendations = response.json()
            except requests.exceptions.ConnectionError:
                st.error("❌ Impossible de se connecter au service backend.\nAssurez-vous que le serveur FastAPI est lancé sur http://localhost:8000")
            except Exception as e:
                st.error(f"❌ Erreur lors de la génération des recommandations: {str(e)}")
    
    if st.session_state.recommendations:
        data = st.session_state.recommendations
        
        if data.get('status') == 'success' and data.get('recommendations'):
            st.success(f"✅ {data['count']} recommandation(s) générée(s) pour vous!")
            
            recommendations = data.get('recommendations', [])
            
            for idx, rec in enumerate(recommendations, 1):
                with st.container():
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.subheader(f"🎉 Recommandation {idx}")
                        st.markdown(f"**Produit:** {rec.get('name', 'N/A')}")
                        st.markdown(f"**Description:** {rec.get('description', 'N/A')}")
                        st.markdown(f"**Prix:** {rec.get('price', 'N/A')}")
                        st.markdown(f"**Catégorie:** {rec.get('category', 'N/A')}")
                    
                    with col2:
                        if rec.get('affiliate_url'):
                            st.markdown(
                                f"[Voir sur Amazon 🛍️]({rec['affiliate_url']})",
                                unsafe_allow_html=True
                            )
                        if rec.get('store_url'):
                            st.markdown(
                                f"[Aller au magasin]({rec['store_url']})",
                                unsafe_allow_html=True
                            )
                    
                    st.markdown("---")
        elif data.get('status') == 'warning':
            st.warning(f"⚠️ {data.get('message', 'Aucun résultat')}")
        else:
            st.error(f"❌ Erreur: {data.get('message', 'Erreur inconnue')}")

# Section secondaire: Consulter les produits disponibles
st.markdown("---")
if st.checkbox("📄 Afficher tous les produits disponibles"):
    with st.spinner("📅 Chargement des produits..."):
        try:
            response = requests.get(
                f"{BACKEND_URL}/api/products",
                params={"limit": 100},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get('products'):
                st.info(f"📑 {data['count']} produits disponibles dans notre base de données")
                
                products_df = pd.DataFrame(data['products'])
                st.dataframe(products_df, use_container_width=True)
            else:
                st.info("📄 Aucun produit disponible")
        except Exception as e:
            st.error(f"❌ Erreur de chargement: {str(e)}")

# Pied de page
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; font-size: 0.9em;'>
    <p>TrouveUnCadeau.xyz &copy; 2024 | Moteur IA de recommandation de cadeaux pour Québec</p>
    <p>Alimenté par FastAPI, Streamlit, LangChain et Airtable</p>
</div>
""", unsafe_allow_html=True)
