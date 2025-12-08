import streamlit as st

def show():
    st.title("📜 Conditions d'Utilisation")
    st.markdown("*Dernière mise à jour : 8 décembre 2024*")
    
    st.markdown("---")
    
    st.header("1. Acceptation des Conditions")
    st.markdown("""
    En accédant et en utilisant TrouveUnCadeau.xyz, vous acceptez d'être lié par ces conditions d'utilisation. 
    Si vous n'acceptez pas ces conditions, veuillez ne pas utiliser notre service.
    """)
    
    st.header("2. Description du Service")
    st.markdown("""
    TrouveUnCadeau.xyz est une plateforme de recommandation de cadeaux alimentée par l'intelligence artificielle qui :
    
    - Fournit des suggestions de cadeaux personnalisées
    - Redirige vers des sites marchands partenaires
    - Génère des revenus via des commissions d'affiliation
    - Offre des fonctionnalités sociales de partage de listes
    """)
    
    st.header("3. Compte Utilisateur")
    st.markdown("""
    ### 3.1 Création de Compte
    - Vous devez fournir des informations exactes et à jour
    - Vous êtes responsable de la confidentialité de votre mot de passe
    - Vous devez avoir au moins 13 ans pour créer un compte
    
    ### 3.2 Responsabilités
    - Vous êtes responsable de toutes les activités effectuées via votre compte
    - Vous devez nous informer immédiatement de toute utilisation non autorisée
    - Nous nous réservons le droit de suspendre ou supprimer tout compte en cas d'utilisation abusive
    """)
    
    st.header("4. Utilisation Acceptable")
    st.markdown("""
    Vous vous engagez à NE PAS :
    
    - Utiliser le service à des fins illégales
    - Tenter d'accéder à des zones non autorisées du système
    - Perturber ou interférer avec le fonctionnement du service
    - Collecter des informations sur d'autres utilisateurs
    - Utiliser des robots, scrapers ou autres moyens automatisés sans autorisation
    - Publier du contenu offensant, illégal ou inapproprié
    - Usurper l'identité d'une autre personne
    """)
    
    st.header("5. Liens d'Affiliation")
    st.markdown("""
    ### 5.1 Divulgation
    TrouveUnCadeau.xyz participe à des programmes d'affiliation. Lorsque vous cliquez sur certains liens 
    et effectuez un achat, nous pouvons recevoir une commission sans frais supplémentaires pour vous.
    
    ### 5.2 Indépendance
    - Nos recommandations sont basées sur la pertinence pour vos besoins
    - Nous maintenons notre indépendance éditoriale
    - Les commissions d'affiliation n'influencent pas nos recommandations
    
    ### 5.3 Prix
    Les prix affichés sont fournis à titre indicatif et peuvent varier. Vérifiez toujours le prix 
    final sur le site marchand avant d'effectuer un achat.
    """)
    
    st.header("6. Propriété Intellectuelle")
    st.markdown("""
    ### 6.1 Contenu de TrouveUnCadeau.xyz
    - Tous les contenus (textes, logos, designs, code) sont notre propriété ou celle de nos partenaires
    - Vous ne pouvez pas reproduire, distribuer ou exploiter nos contenus sans autorisation
    
    ### 6.2 Contenu Utilisateur
    - Vous conservez la propriété du contenu que vous créez (listes, commentaires)
    - Vous nous accordez une licence pour utiliser ce contenu dans le cadre du service
    - Vous garantissez avoir les droits sur le contenu que vous publiez
    """)
    
    st.header("7. Limitation de Responsabilité")
    st.markdown("""
    ### 7.1 Service "Tel Quel"
    Le service est fourni "tel quel" sans garantie d'aucune sorte. Nous ne garantissons pas :
    - La disponibilité continue du service
    - L'exactitude des informations fournies
    - La qualité des produits recommandés
    
    ### 7.2 Achats Tiers
    - Nous ne sommes pas responsables des transactions effectuées sur des sites tiers
    - Les litiges concernant des achats doivent être résolus directement avec le marchand
    - Vérifiez toujours les politiques de retour et garanties du marchand
    
    ### 7.3 Limitation de Dommages
    Dans la mesure permise par la loi, nous ne serons pas responsables des dommages indirects, 
    accessoires ou consécutifs résultant de l'utilisation de notre service.
    """)
    
    st.header("8. Modifications du Service")
    st.markdown("""
    Nous nous réservons le droit de :
    
    - Modifier ou interrompre le service à tout moment
    - Changer les tarifs (si applicable)
    - Modifier ces conditions d'utilisation
    
    Les modifications importantes vous seront notifiées par courriel ou via la plateforme.
    """)
    
    st.header("9. Résiliation")
    st.markdown("""
    ### 9.1 Par Vous
    Vous pouvez supprimer votre compte à tout moment depuis les paramètres.
    
    ### 9.2 Par Nous
    Nous pouvons suspendre ou résilier votre compte si :
    - Vous violez ces conditions d'utilisation
    - Votre compte reste inactif pendant une période prolongée
    - Nous devons nous conformer à une obligation légale
    
    ### 9.3 Effets de la Résiliation
    - Accès au service révoqué
    - Suppression de vos données selon notre politique de confidentialité
    - Perte de l'accès à vos listes et favoris
    """)
    
    st.header("10. Loi Applicable")
    st.markdown("""
    Ces conditions sont régies par les lois de la province de Québec, Canada. 
    Tout litige sera soumis à la juridiction exclusive des tribunaux de Québec.
    """)
    
    st.header("11. Dispositions Diverses")
    st.markdown("""
    ### 11.1 Intégralité de l'Accord
    Ces conditions constituent l'intégralité de l'accord entre vous et TrouveUnCadeau.xyz.
    
    ### 11.2 Divisibilité
    Si une disposition est jugée invalide, les autres dispositions restent en vigueur.
    
    ### 11.3 Renonciation
    Le fait de ne pas exercer un droit ne constitue pas une renonciation à ce droit.
    """)
    
    st.header("12. Contact")
    st.markdown("""
    Pour toute question concernant ces conditions d'utilisation :
    
    📧 **Email** : legal@trouveuncadeau.xyz  
    🌐 **Site web** : https://trouveuncadeau.xyz  
    📍 **Adresse** : [À compléter avec adresse légale]
    """)
    
    st.markdown("---")
    st.info("💡 En continuant à utiliser TrouveUnCadeau.xyz, vous acceptez ces conditions d'utilisation dans leur intégralité.")

if __name__ == "__main__":
    show()
