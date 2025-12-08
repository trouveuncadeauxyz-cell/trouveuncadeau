import streamlit as st

def show():
    st.title("🔒 Politique de Confidentialité")
    st.markdown("*Dernière mise à jour : 8 décembre 2024*")
    
    st.markdown("---")
    
    st.header("1. Collecte des Informations")
    st.markdown("""
    TrouveUnCadeau.xyz collecte les informations suivantes :
    
    - **Informations de compte** : nom, adresse courriel lors de l'inscription
    - **Données d'utilisation** : historique de recherches, préférences de cadeaux
    - **Informations techniques** : adresse IP, type de navigateur, pages visitées
    - **Cookies** : pour améliorer l'expérience utilisateur
    """)
    
    st.header("2. Utilisation des Informations")
    st.markdown("""
    Vos informations sont utilisées pour :
    
    - Fournir des recommandations de cadeaux personnalisées
    - Améliorer nos services et fonctionnalités
    - Communiquer avec vous au sujet de votre compte
    - Analyser l'utilisation de la plateforme
    - Respecter nos obligations légales
    """)
    
    st.header("3. Partage des Informations")
    st.markdown("""
    Nous ne vendons jamais vos informations personnelles. Nous pouvons partager vos données avec :
    
    - **Partenaires affiliés** : uniquement les informations nécessaires pour traiter vos clics
    - **Prestataires de services** : hébergement, analytiques (dans le respect du RGPD)
    - **Autorités légales** : si requis par la loi
    """)
    
    st.header("4. Protection des Données")
    st.markdown("""
    Nous mettons en œuvre des mesures de sécurité appropriées :
    
    - Chiffrement SSL/TLS pour toutes les communications
    - Accès restreint aux données personnelles
    - Surveillance régulière de nos systèmes
    - Conformité RGPD et lois canadiennes sur la protection des données
    """)
    
    st.header("5. Vos Droits")
    st.markdown("""
    Conformément au RGPD et aux lois canadiennes, vous avez le droit de :
    
    - **Accéder** à vos données personnelles
    - **Rectifier** des informations inexactes
    - **Supprimer** votre compte et vos données
    - **Exporter** vos données
    - **Vous opposer** au traitement de vos données
    - **Retirer votre consentement** à tout moment
    
    Pour exercer ces droits, contactez-nous à privacy@trouveuncadeau.xyz
    """)
    
    st.header("6. Cookies et Technologies Similaires")
    st.markdown("""
    Nous utilisons des cookies pour :
    
    - Maintenir votre session active
    - Mémoriser vos préférences
    - Analyser le trafic du site
    - Optimiser nos recommandations
    
    Vous pouvez gérer vos préférences de cookies dans les paramètres de votre navigateur.
    """)
    
    st.header("7. Conservation des Données")
    st.markdown("""
    Nous conservons vos données aussi longtemps que :
    
    - Votre compte est actif
    - Nécessaire pour vous fournir nos services
    - Requis par la loi
    
    Vous pouvez demander la suppression de vos données à tout moment.
    """)
    
    st.header("8. Modifications de cette Politique")
    st.markdown("""
    Nous pouvons mettre à jour cette politique de confidentialité. Les modifications importantes 
    vous seront notifiées par courriel ou via notre plateforme.
    """)
    
    st.header("9. Contact")
    st.markdown("""
    Pour toute question concernant cette politique de confidentialité :
    
    📧 **Email** : privacy@trouveuncadeau.xyz  
    🌐 **Site web** : https://trouveuncadeau.xyz  
    📍 **Adresse** : [À compléter avec adresse légale]
    """)
    
    st.markdown("---")
    st.info("💡 Votre vie privée est importante pour nous. Nous nous engageons à protéger vos données conformément aux normes les plus strictes.")

if __name__ == "__main__":
    show()
