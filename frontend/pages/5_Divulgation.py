"""
TrouveUnCadeau.xyz - Page Divulgation d'Affiliation
====================================================
Conformité: Ad Standards Canada, CASL, FTC Guidelines

À placer dans: pages/5_Divulgation.py (ou 5_📋_Divulgation.py pour emoji)
"""

import streamlit as st
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Divulgation d'Affiliation | TrouveUnCadeau.xyz",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Informations de l'entreprise
COMPANY_INFO = {
    "name": "TrouveUnCadeau.xyz",
    "email": "contact@trouveuncadeau.xyz",
    "address": "Saguenay-Lac-Saint-Jean, Québec, Canada",
}

# Programmes d'affiliation actifs
AFFILIATE_PROGRAMS = [
    {
        "name": "Amazon Associates",
        "commission": "1-10% selon catégorie",
        "cookie": "24 heures",
        "description": "Programme principal pour produits diversifiés"
    },
    {
        "name": "Etsy (via Awin)",
        "commission": "4%",
        "cookie": "30 jours",
        "description": "Produits artisanaux et faits main"
    },
    {
        "name": "eBay Partner Network",
        "commission": "1-4%",
        "cookie": "24 heures",
        "description": "Produits variés et enchères"
    },
    {
        "name": "Indigo/Chapters",
        "commission": "5%",
        "cookie": "7 jours",
        "description": "Livres et articles lifestyle"
    },
    {
        "name": "Bookshop.org",
        "commission": "10%",
        "cookie": "30 jours",
        "description": "Livres - Soutient les librairies indépendantes"
    },
]

# ============================================================================
# STYLES CSS
# ============================================================================

st.markdown("""
<style>
/* Style général */
.main-title {
    color: #2d6a4f;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.subtitle {
    color: #6c757d;
    font-size: 1rem;
    margin-bottom: 2rem;
}

/* Sections */
.disclosure-section {
    background: #ffffff;
    border: 1px solid #e9ecef;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 2px solid #95d5b2;
}

.section-icon {
    font-size: 1.5rem;
}

.section-title {
    color: #2d6a4f;
    font-size: 1.3rem;
    font-weight: 600;
    margin: 0;
}

/* Cartes programmes */
.program-card {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 8px;
    padding: 16px;
    margin: 12px 0;
    border-left: 4px solid #40916c;
}

.program-name {
    font-weight: 600;
    color: #1b4332;
    font-size: 1.1rem;
    margin-bottom: 8px;
}

.program-details {
    display: flex;
    gap: 20px;
    font-size: 0.9rem;
    color: #495057;
    margin-bottom: 8px;
}

.program-description {
    font-size: 0.85rem;
    color: #6c757d;
    font-style: italic;
}

/* Liste */
.commitment-list {
    list-style: none;
    padding: 0;
}

.commitment-list li {
    padding: 10px 0 10px 35px;
    position: relative;
    border-bottom: 1px solid #f1f3f4;
}

.commitment-list li:before {
    content: "✓";
    position: absolute;
    left: 0;
    color: #40916c;
    font-weight: bold;
    font-size: 1.2rem;
}

.commitment-list li:last-child {
    border-bottom: none;
}

/* Footer */
.legal-footer {
    background: #f8f9fa;
    border-top: 1px solid #dee2e6;
    padding: 24px;
    margin-top: 40px;
    border-radius: 0 0 12px 12px;
    text-align: center;
}

.legal-footer p {
    margin: 8px 0;
    font-size: 0.9rem;
    color: #6c757d;
}

.legal-footer a {
    color: #0056b3;
    text-decoration: none;
}

.legal-footer a:hover {
    text-decoration: underline;
}

/* Highlight box */
.highlight-box {
    background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
    border-radius: 8px;
    padding: 16px 20px;
    margin: 16px 0;
    border-left: 4px solid #28a745;
}

.highlight-box strong {
    color: #155724;
}
</style>
""", unsafe_allow_html=True)


# ============================================================================
# CONTENU DE LA PAGE
# ============================================================================

def main():
    # Titre principal
    st.markdown('<h1 class="main-title">📋 Divulgation d\'Affiliation</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">Dernière mise à jour: {datetime.now().strftime("%d %B %Y")}</p>', unsafe_allow_html=True)
    
    # -------------------------------------------------------------------------
    # Section 1: Engagement de transparence
    # -------------------------------------------------------------------------
    st.markdown("""
    <div class="disclosure-section">
        <div class="section-header">
            <span class="section-icon">🎯</span>
            <h2 class="section-title">Notre Engagement de Transparence</h2>
        </div>
        <p>
            <strong>TrouveUnCadeau.xyz</strong> est un service gratuit de recommandation de cadeaux 
            propulsé par l'intelligence artificielle. Pour maintenir ce service accessible à tous, 
            nous participons à plusieurs programmes d'affiliation.
        </p>
        <div class="highlight-box">
            <strong>Ce que cela signifie pour vous:</strong> Lorsque vous cliquez sur certains liens 
            de notre site et effectuez un achat, nous pouvons recevoir une petite commission de la 
            part du détaillant. <em>Cela n'entraîne aucun coût supplémentaire pour vous.</em>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # -------------------------------------------------------------------------
    # Section 2: Programmes d'affiliation
    # -------------------------------------------------------------------------
    st.markdown("""
    <div class="disclosure-section">
        <div class="section-header">
            <span class="section-icon">🤝</span>
            <h2 class="section-title">Nos Partenaires Affiliés</h2>
        </div>
        <p>Nous participons actuellement aux programmes d'affiliation suivants:</p>
    """, unsafe_allow_html=True)
    
    for program in AFFILIATE_PROGRAMS:
        st.markdown(f"""
        <div class="program-card">
            <div class="program-name">{program['name']}</div>
            <div class="program-details">
                <span>💰 Commission: {program['commission']}</span>
                <span>🍪 Cookie: {program['cookie']}</span>
            </div>
            <div class="program-description">{program['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # -------------------------------------------------------------------------
    # Section 3: Politique éditoriale
    # -------------------------------------------------------------------------
    st.markdown("""
    <div class="disclosure-section">
        <div class="section-header">
            <span class="section-icon">✍️</span>
            <h2 class="section-title">Notre Politique Éditoriale</h2>
        </div>
        <p>Notre intégrité éditoriale est primordiale. Voici nos engagements:</p>
        <ul class="commitment-list">
            <li><strong>Indépendance:</strong> Les commissions d'affiliation n'influencent pas nos recommandations. 
                Notre IA recommande les produits les plus adaptés à vos besoins, qu'ils soient affiliés ou non.</li>
            <li><strong>Honnêteté:</strong> Nous ne recommandons que des produits que nous estimons utiles et de qualité.</li>
            <li><strong>Transparence:</strong> Tous les liens affiliés sont clairement identifiés sur notre site.</li>
            <li><strong>Objectivité:</strong> Nos algorithmes sont conçus pour prioriser la pertinence, pas les commissions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # -------------------------------------------------------------------------
    # Section 4: Utilisation des revenus
    # -------------------------------------------------------------------------
    st.markdown("""
    <div class="disclosure-section">
        <div class="section-header">
            <span class="section-icon">💰</span>
            <h2 class="section-title">Utilisation des Revenus</h2>
        </div>
        <p>Les revenus générés par les programmes d'affiliation nous permettent de:</p>
        <ul class="commitment-list">
            <li>Maintenir notre infrastructure technique (serveurs, API d'IA)</li>
            <li>Développer de nouvelles fonctionnalités</li>
            <li>Garder le service entièrement gratuit pour nos utilisateurs</li>
            <li>Améliorer continuellement la qualité de nos recommandations</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # -------------------------------------------------------------------------
    # Section 5: Conformité réglementaire
    # -------------------------------------------------------------------------
    st.markdown("""
    <div class="disclosure-section">
        <div class="section-header">
            <span class="section-icon">⚖️</span>
            <h2 class="section-title">Conformité Réglementaire</h2>
        </div>
        <p>Cette divulgation est conforme aux exigences de:</p>
        <ul class="commitment-list">
            <li><strong>Ad Standards Canada</strong> - Lignes directrices sur le marketing d'influence (2025)</li>
            <li><strong>CASL</strong> - Loi canadienne anti-pourriel (identification de l'expéditeur)</li>
            <li><strong>Loi sur la concurrence</strong> - Bureau de la concurrence du Canada</li>
            <li><strong>FTC Guidelines</strong> - Pour nos visiteurs américains (16 CFR Part 255)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # -------------------------------------------------------------------------
    # Section 6: Contact
    # -------------------------------------------------------------------------
    st.markdown(f"""
    <div class="disclosure-section">
        <div class="section-header">
            <span class="section-icon">📬</span>
            <h2 class="section-title">Nous Contacter</h2>
        </div>
        <p>Si vous avez des questions concernant notre politique d'affiliation:</p>
        <p>
            <strong>Email:</strong> <a href="mailto:{COMPANY_INFO['email']}">{COMPANY_INFO['email']}</a><br>
            <strong>Adresse:</strong> {COMPANY_INFO['address']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # -------------------------------------------------------------------------
    # Footer légal
    # -------------------------------------------------------------------------
    current_year = datetime.now().year
    st.markdown(f"""
    <div class="legal-footer">
        <p>
            <a href="/Confidentialite">Politique de confidentialité</a> |
            <a href="/Conditions">Conditions d'utilisation</a> |
            <a href="mailto:{COMPANY_INFO['email']}">Contact</a>
        </p>
        <p>© {current_year} {COMPANY_INFO['name']} | {COMPANY_INFO['address']}</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
