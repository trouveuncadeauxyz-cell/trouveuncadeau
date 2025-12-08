"""Interface Streamlit pour TrouveUnCadeau.xyz

Moteur de recommandation de cadeaux intelligents pour QuÃ©bec
Client frontal utilisant FastAPI backend
"""

import streamlit as st
import requests
import json
from datetime import datetime
import pandas as pd

# === IMPORTS CONFORMITE ===
from compliance_integration import (
    inject_compliance_styles,
    render_affiliate_banner,
    render_footer_links,
    render_sidebar_legal
)

# Configuration de la page
st.set_page_config(
    page_title="TrouveUnCadeau - Moteur de recommandation",
    page_icon="ðŸŽ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === STYLES CONFORMITE ===
inject_compliance_styles()

# Style CSS personnalisÃ©
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

# En-tÃªte principal
st.title("ðŸŽ TrouveUnCadeau.xyz")

# === BANNER AFFILIATION ===
render_affiliate_banner()
st.markdown("""
### Moteur de recommandation de cadeaux intelligents pour QuÃ©bec

Trouvez le cadeau parfait grÃ¢ce Ã  l'IA! DÃ©crivez votre budget, l'Ã¢ge du destinataire,
l'occasion, et ses intÃ©rÃªts pour obtenir des recommandations personnalisÃ©es.
""")

st.divider()

# Barre latÃ©rale
with st.sidebar:
    st.header("âš™ï¸ ParamÃ©trage")
    st.markdown("---")
    
    budget = st.slider(
        "Budget (CAD)",
        min_value=10.0,
        max_value=500.0,
        value=50.0,
        step=5.0,
        help="DÃ©finissez votre budget maximal en dollars canadiens"
    )
    
    recipient_age = st.number_input(
        "Ã‚ge du destinataire",
        min_value=1,
        max_value=120,
        value=25,
        help="L'Ã¢ge approximatif de la personne qui recevra le cadeau"
    )
    
    occasions = ["Anniversaire", "NoÃ«l", "FÃªte", "Remerciment", "Autre"]
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

    # === LIENS LEGAUX SIDEBAR ===
    render_sidebar_legal()

# Formulaire principal
col1, col2 = st.columns([3, 1])

with col1:
    interests = st.text_area(
        "ðŸ’¡ IntÃ©rÃªts et passions du destinataire",
        placeholder="Ex: Musique, photographie, cuisine, sport, lecture, technologie, voyage...",
        height=100,
        help="DÃ©crivez les intÃ©rÃªts de la personne pour obtenir des recommandations plus pertinentes"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    generate_button = st.button(
        "ðŸŒŸ GÃ©nÃ©rer\nrecommandations",
        use_container_width=True
    )

st.divider()

# Section des rÃ©sultats
if generate_button or st.session_state.recommendations:
    if generate_button:
        with st.spinner("ðŸ¤– TrouveUnCadeau analyse vos prÃ©fÃ©rences..."):
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
                st.error("âŒ Impossible de se connecter au service backend.\nAssurez-vous que le serveur FastAPI est lancÃ© sur http://localhost:8000")
            except Exception as e:
                st.error(f"âŒ Erreur lors de la gÃ©nÃ©ration des recommandations: {str(e)}")
    
    if st.session_state.recommendations:
        data = st.session_state.recommendations
        
        if data.get('status') == 'success' and data.get('recommendations'):
            st.success(f"âœ… {data['count']} recommandation(s) gÃ©nÃ©rÃ©e(s) pour vous!")
            
            recommendations = data.get('recommendations', [])
            
            for idx, rec in enumerate(recommendations, 1):
                with st.container():
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.subheader(f"ðŸŽ‰ Recommandation {idx}")
                        st.markdown(f"**Produit:** {rec.get('name', 'N/A')}")
                        st.markdown(f"**Description:** {rec.get('description', 'N/A')}")
                        st.markdown(f"**Prix:** {rec.get('price', 'N/A')}")
                        st.markdown(f"**CatÃ©gorie:** {rec.get('category', 'N/A')}")
                    
                    with col2:
                        if rec.get('affiliate_url'):
                            st.markdown(
                                f"[Voir sur Amazon ðŸ›ï¸]({rec['affiliate_url']})",
                                unsafe_allow_html=True
                            )
                        if rec.get('store_url'):
                            st.markdown(
                                f"[Aller au magasin]({rec['store_url']})",
                                unsafe_allow_html=True
                            )
                    
                    st.markdown("---")
        elif data.get('status') == 'warning':
            st.warning(f"âš ï¸ {data.get('message', 'Aucun rÃ©sultat')}")
        else:
            st.error(f"âŒ Erreur: {data.get('message', 'Erreur inconnue')}")

# Section secondaire: Consulter les produits disponibles
st.markdown("---")
if st.checkbox("ðŸ“„ Afficher tous les produits disponibles"):
    with st.spinner("ðŸ“… Chargement des produits..."):
        try:
            response = requests.get(
                f"{BACKEND_URL}/api/products",
                params={"limit": 100},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get('products'):
                st.info(f"ðŸ“‘ {data['count']} produits disponibles dans notre base de donnÃ©es")
                
                products_df = pd.DataFrame(data['products'])
                st.dataframe(products_df, use_container_width=True)
            else:
                st.info("ðŸ“„ Aucun produit disponible")
        except Exception as e:
            st.error(f"âŒ Erreur de chargement: {str(e)}")

# === FOOTER LEGAL CONFORMITE ===
render_footer_links()
