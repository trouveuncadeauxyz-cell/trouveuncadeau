"""
TrouveUnCadeau.xyz - Module d'Intégration Conformité
====================================================
Ce module fournit les fonctions à intégrer dans votre app.py principal.

INSTRUCTIONS D'INTÉGRATION:
1. Copiez ce fichier dans votre projet (à côté de app.py)
2. Importez les fonctions nécessaires dans app.py
3. Appelez les fonctions aux endroits appropriés

Exemple dans app.py:
    from compliance_integration import (
        inject_compliance_styles,
        render_affiliate_banner,
        render_footer_links,
        render_sidebar_legal
    )
"""

import streamlit as st
from datetime import datetime

# ============================================================================
# CONFIGURATION - À PERSONNALISER
# ============================================================================

SITE_CONFIG = {
    "name": "TrouveUnCadeau.xyz",
    "email": "contact@trouveuncadeau.xyz",
    "address": "Saguenay-Lac-Saint-Jean, Québec, Canada",
}


# ============================================================================
# STYLES CSS GLOBAUX
# ============================================================================

COMPLIANCE_STYLES = """
<style>
/* ===== Banner de divulgation d'affiliation ===== */
.affiliate-disclosure-banner {
    background: linear-gradient(135deg, #f0f9f4 0%, #d4edda 100%);
    border-left: 4px solid #28a745;
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    margin: 0 0 20px 0;
    font-size: 14px;
    color: #155724;
    display: flex;
    align-items: center;
    gap: 10px;
}

.affiliate-disclosure-banner.compact {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-left: 3px solid #6c757d;
    padding: 8px 12px;
    font-size: 12px;
    color: #6c757d;
}

.affiliate-disclosure-banner a {
    color: #0056b3;
    text-decoration: underline;
}

.affiliate-disclosure-banner .icon {
    font-size: 18px;
    flex-shrink: 0;
}

/* ===== Footer légal ===== */
.legal-footer-bar {
    background: #f8f9fa;
    border-top: 1px solid #e9ecef;
    padding: 16px 20px;
    margin-top: 40px;
    text-align: center;
    font-size: 13px;
    color: #6c757d;
}

.legal-footer-bar a {
    color: #0056b3;
    text-decoration: none;
    margin: 0 12px;
}

.legal-footer-bar a:hover {
    text-decoration: underline;
}

.legal-footer-bar .copyright {
    margin-top: 8px;
    font-size: 12px;
}

/* ===== Sidebar legal ===== */
.sidebar-legal-box {
    background: #f9f9f9;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 12px;
    margin-top: 20px;
    font-size: 11px;
    color: #6c757d;
}

.sidebar-legal-box a {
    color: #0056b3;
    text-decoration: none;
}

.sidebar-legal-box .title {
    font-weight: 600;
    color: #495057;
    margin-bottom: 8px;
}

/* ===== Product link indicator ===== */
.affiliate-link-indicator {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 11px;
    color: #6c757d;
    margin-left: 6px;
}

.affiliate-link-indicator::before {
    content: "🔗";
    font-size: 10px;
}
</style>
"""


def inject_compliance_styles():
    """
    Injecte les styles CSS de conformité.
    
    À appeler UNE SEULE FOIS au début de votre app, après st.set_page_config().
    
    Exemple:
        st.set_page_config(...)
        inject_compliance_styles()
    """
    st.markdown(COMPLIANCE_STYLES, unsafe_allow_html=True)


# ============================================================================
# COMPOSANTS DE DIVULGATION
# ============================================================================

def render_affiliate_banner(compact: bool = False):
    """
    Affiche le banner de divulgation d'affiliation.
    
    Args:
        compact: Si True, affiche une version plus petite et discrète
    
    À appeler:
        - En haut de la page principale de recommandations
        - Sur toute page affichant des liens affiliés
    
    Exemple:
        render_affiliate_banner()  # Version standard
        render_affiliate_banner(compact=True)  # Version compacte
    """
    if compact:
        st.markdown("""
        <div class="affiliate-disclosure-banner compact">
            <span class="icon">ℹ️</span>
            <span>Cet article contient des liens affiliés. 
            <a href="/Divulgation">En savoir plus</a></span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="affiliate-disclosure-banner">
            <span class="icon">💡</span>
            <span>
                <strong>Transparence:</strong> Ce contenu contient des liens affiliés. 
                En achetant via ces liens, vous nous aidez à maintenir ce service gratuit, 
                sans frais supplémentaires pour vous.
                <a href="/Divulgation">Voir notre politique complète →</a>
            </span>
        </div>
        """, unsafe_allow_html=True)


def render_footer_links():
    """
    Affiche les liens légaux en bas de page.
    
    À appeler à la fin de chaque page principale.
    
    Exemple:
        # ... votre contenu ...
        render_footer_links()
    """
    current_year = datetime.now().year
    st.markdown(f"""
    <div class="legal-footer-bar">
        <div>
            <a href="/Divulgation">📋 Divulgation d'affiliation</a>
            <a href="/Confidentialite">🔒 Confidentialité</a>
            <a href="/Conditions">📜 Conditions</a>
            <a href="mailto:{SITE_CONFIG['email']}">📬 Contact</a>
        </div>
        <div class="copyright">
            © {current_year} {SITE_CONFIG['name']} | {SITE_CONFIG['address']}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar_legal():
    """
    Affiche une mini-section légale dans la sidebar.
    
    À appeler dans le bloc with st.sidebar de votre app.
    
    Exemple:
        with st.sidebar:
            # ... vos éléments de sidebar ...
            render_sidebar_legal()
    """
    st.markdown("""
    <div class="sidebar-legal-box">
        <div class="title">📋 Informations légales</div>
        <div>
            Ce site participe à des programmes d'affiliation.<br>
            <a href="/Divulgation">Divulgation</a> | 
            <a href="/Confidentialite">Confidentialité</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_product_affiliate_indicator():
    """
    Retourne un indicateur à afficher à côté des liens produits.
    
    Exemple:
        st.markdown(f"[Acheter sur Amazon]({url}) {render_product_affiliate_indicator()}", 
                    unsafe_allow_html=True)
    """
    return '<span class="affiliate-link-indicator">Lien affilié</span>'


# ============================================================================
# FORMULAIRE NEWSLETTER CASL-CONFORME
# ============================================================================

def render_newsletter_form(on_submit_callback=None):
    """
    Affiche un formulaire d'inscription newsletter conforme CASL.
    
    Args:
        on_submit_callback: Fonction à appeler avec (email, consent) si le formulaire est soumis
    
    Returns:
        tuple: (email, consented) si soumis et valide, (None, None) sinon
    
    Exemple:
        def save_subscriber(email, consent):
            # Sauvegarder dans Airtable/n8n
            pass
        
        email, consent = render_newsletter_form(on_submit_callback=save_subscriber)
    """
    
    st.markdown("### 📬 Restez informé des meilleures idées cadeaux")
    
    with st.form("newsletter_signup_form", clear_on_submit=True):
        email = st.text_input(
            "Adresse email",
            placeholder="votre@email.com",
            help="Votre email ne sera jamais partagé avec des tiers."
        )
        
        # CASL: Case non cochée par défaut (consentement exprès)
        consent = st.checkbox(
            "J'accepte de recevoir des communications commerciales de TrouveUnCadeau.xyz. "
            "Je comprends que je peux me désabonner à tout moment en cliquant sur le lien "
            "de désabonnement présent dans chaque email.",
            value=False,
            help="Requis pour recevoir notre newsletter (conformité CASL)"
        )
        
        # Identification de l'expéditeur (requis par CASL)
        st.caption(f"""
        **Identification de l'expéditeur (CASL):**  
        {SITE_CONFIG['name']} | {SITE_CONFIG['address']} | {SITE_CONFIG['email']}  
        
        En vous inscrivant, vous acceptez notre [Politique de Confidentialité](/Confidentialite).
        """)
        
        submitted = st.form_submit_button("✉️ S'inscrire", use_container_width=True)
        
        if submitted:
            # Validation
            if not email or "@" not in email or "." not in email:
                st.error("❌ Veuillez entrer une adresse email valide.")
                return None, None
            
            if not consent:
                st.error("❌ Vous devez accepter de recevoir nos communications pour vous inscrire.")
                return None, None
            
            # Succès
            if on_submit_callback:
                on_submit_callback(email, consent)
            
            st.success("✅ Merci pour votre inscription! Vous recevrez bientôt nos meilleures idées cadeaux.")
            return email, consent
    
    return None, None


# ============================================================================
# UTILITAIRES
# ============================================================================

def get_affiliate_link_html(url: str, text: str, show_indicator: bool = True) -> str:
    """
    Génère le HTML pour un lien affilié avec indicateur optionnel.
    
    Args:
        url: URL du lien affilié
        text: Texte du lien
        show_indicator: Afficher l'indicateur "Lien affilié"
    
    Returns:
        str: HTML du lien
    
    Exemple:
        link_html = get_affiliate_link_html(
            "https://amazon.ca/dp/xxx?tag=trouveuncadea-20",
            "Voir sur Amazon",
            show_indicator=True
        )
        st.markdown(link_html, unsafe_allow_html=True)
    """
    indicator = render_product_affiliate_indicator() if show_indicator else ""
    return f'<a href="{url}" target="_blank" rel="noopener sponsored">{text}</a>{indicator}'


# ============================================================================
# EXEMPLE D'UTILISATION DANS APP.PY
# ============================================================================

INTEGRATION_EXAMPLE = '''
# ============================================================================
# EXEMPLE: Comment intégrer dans votre app.py existant
# ============================================================================

import streamlit as st
from compliance_integration import (
    inject_compliance_styles,
    render_affiliate_banner,
    render_footer_links,
    render_sidebar_legal
)

# Configuration de la page
st.set_page_config(
    page_title="TrouveUnCadeau.xyz - Trouvez le cadeau parfait",
    page_icon="🎁",
    layout="wide"
)

# IMPORTANT: Injecter les styles de conformité au début
inject_compliance_styles()

def main():
    # Sidebar
    with st.sidebar:
        st.title("🎁 TrouveUnCadeau")
        # ... vos éléments de navigation ...
        
        # Ajouter les liens légaux en bas de la sidebar
        render_sidebar_legal()
    
    # Contenu principal
    st.title("🎁 Trouvez le Cadeau Parfait")
    
    # Afficher le banner de divulgation
    render_affiliate_banner()
    
    # ... votre contenu de recommandation ...
    
    # Footer avec liens légaux
    render_footer_links()

if __name__ == "__main__":
    main()
'''

if __name__ == "__main__":
    # Démo
    st.set_page_config(page_title="Démo Conformité", page_icon="🧪", layout="wide")
    inject_compliance_styles()
    
    st.title("🧪 Démo - Module de Conformité")
    
    st.header("1. Banner de divulgation")
    render_affiliate_banner()
    render_affiliate_banner(compact=True)
    
    st.header("2. Footer légal")
    render_footer_links()
    
    st.header("3. Sidebar légal")
    with st.sidebar:
        st.title("Sidebar Démo")
        render_sidebar_legal()
    
    st.header("4. Formulaire Newsletter")
    render_newsletter_form()
    
    st.header("5. Code d'intégration")
    st.code(INTEGRATION_EXAMPLE, language="python")
