# 🚀 TrouveUnCadeau.xyz - Guide de Déploiement Production

## 📋 Vue d'ensemble

Guide complet pour déployer TrouveUnCadeau.xyz sur DigitalOcean avec Docker Compose.

### Architecture

- **Backend**: FastAPI (Python 3.13) - Port 8000
- **Frontend**: Streamlit (Python 3.13) - Port 8501
- **Reverse Proxy**: Nginx - Ports 80/443
- **Orchestration**: Docker Compose
- **Workflow**: n8n (déjà configuré sur le serveur)

---

## 🔧 Prérequis

### Sur le serveur DigitalOcean

```bash
# Docker et Docker Compose installés
docker --version
docker-compose --version

# Git installé
git --version

# Certbot pour Let's Encrypt SSL
sudo apt install certbot python3-certbot-nginx
```

### Variables d'environnement requises

Copiez `.env.example` vers `.env` et remplissez:

```bash
cp .env.example .env
nano .env
```

**Variables essentielles:**

```env
# Airtable Configuration
AIRTABLE_API_KEY=your_airtable_api_key
AIRTABLE_BASE_ID=your_base_id
AIRTABLE_TABLE_ID=your_table_id

# AI APIs
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
PERPLEXITY_API_KEY=your_perplexity_key

# Amazon Affiliate
AMAZON_AFFILIATE_TAG=your_tag

# n8n Webhook
N8N_WEBHOOK_URL=https://n8n.trouveuncadeau.xyz/webhook/your_webhook_id

# Application
ENVIRONMENT=production
LOG_LEVEL=INFO
```

---

## 📦 Étape 1: Cloner le Repository

```bash
# SSH vers votre droplet DigitalOcean
ssh root@trouveuncadeau.xyz

# Créer le dossier d'application
mkdir -p /opt/trouveuncadeau
cd /opt/trouveuncadeau

# Cloner le repository
git clone https://github.com/trouveuncadeauxyz-cell/trouveuncadeau.git .
```

---

## 🔐 Étape 2: Configuration SSL

### Obtenir les certificats Let's Encrypt

```bash
# Arrêter nginx temporairement si en cours d'exécution
sudo systemctl stop nginx

# Obtenir les certificats
sudo certbot certonly --standalone -d trouveuncadeau.xyz -d www.trouveuncadeau.xyz

# Les certificats seront dans:
# /etc/letsencrypt/live/trouveuncadeau.xyz/fullchain.pem
# /etc/letsencrypt/live/trouveuncadeau.xyz/privkey.pem
```

### Renouvellement automatique

```bash
# Ajouter un cron job pour le renouvellement
sudo crontab -e

# Ajouter cette ligne (renouvelle tous les lundis à 2h30)
30 2 * * 1 certbot renew --quiet && docker-compose -f /opt/trouveuncadeau/docker-compose.yml restart nginx
```

---

## 🐳 Étape 3: Configuration Docker

### Créer le fichier .env

```bash
cd /opt/trouveuncadeau
cp .env.example .env
nano .env
# Remplir toutes les variables d'environnement
```

### Vérifier la configuration Docker Compose

```bash
# Valider le fichier docker-compose.yml
docker-compose config
```

---

## 🚀 Étape 4: Déploiement

### Build et démarrage des conteneurs

```bash
cd /opt/trouveuncadeau

# Build les images
docker-compose build --no-cache

# Démarrer tous les services
docker-compose up -d

# Vérifier le statut
docker-compose ps
```

### Vérifier les logs

```bash
# Tous les services
docker-compose logs -f

# Service spécifique
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f nginx
```

---

## ✅ Étape 5: Vérification

### Health checks

```bash
# Backend health
curl https://trouveuncadeau.xyz/health

# API test
curl https://trouveuncadeau.xyz/api/health
```

### Accès aux services

- **Frontend**: https://trouveuncadeau.xyz
- **API Backend**: https://trouveuncadeau.xyz/api/
- **n8n**: https://n8n.trouveuncadeau.xyz

---

## 🔄 Mises à jour

### Déployer une nouvelle version

```bash
cd /opt/trouveuncadeau

# Pull les derniers changements
git pull origin main

# Rebuild et redémarrer
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Vérifier les logs
docker-compose logs -f
```

---

## 🛠️ Maintenance

### Commandes utiles

```bash
# Redémarrer tous les services
docker-compose restart

# Redémarrer un service spécifique
docker-compose restart backend

# Voir les logs en temps réel
docker-compose logs -f --tail=100

# Nettoyer les images non utilisées
docker system prune -a

# Sauvegarder les logs
docker-compose logs > logs_$(date +%Y%m%d_%H%M%S).txt
```

### Monitoring

```bash
# Utilisation des ressources
docker stats

# Espace disque
df -h

# Mémoire
free -h
```

---

## 🐛 Troubleshooting

### Backend ne démarre pas

```bash
# Vérifier les variables d'environnement
docker-compose config | grep -A 20 backend

# Logs détaillés
docker-compose logs backend --tail=200

# Tester manuellement
docker-compose run --rm backend python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### Frontend Streamlit inaccessible

```bash
# Vérifier si le conteneur tourne
docker-compose ps frontend

# Logs
docker-compose logs frontend

# Tester la connexion backend
docker-compose exec frontend curl http://backend:8000/health
```

### Erreurs SSL

```bash
# Vérifier les certificats
sudo certbot certificates

# Renouveler manuellement
sudo certbot renew --force-renewal

# Redémarrer nginx
docker-compose restart nginx
```

### Base de données Airtable inaccessible

```bash
# Tester la connexion depuis le backend
docker-compose exec backend python -c "
import os
from pyairtable import Api
api = Api(os.getenv('AIRTABLE_API_KEY'))
print('Airtable connection OK')
"
```

---

## 📊 Performance

### Optimisations recommandées

1. **Cache Redis** (optionnel, à ajouter plus tard)
2. **CDN Cloudflare** pour les assets statiques
3. **Monitoring avec Prometheus/Grafana**
4. **Log aggregation avec ELK Stack**

### Limites actuelles

- Rate limiting: 30-200 req/min par endpoint
- Caching: 10-30 minutes TTL
- Timeout AI requests: 300 secondes

---

## 🔒 Sécurité

### Checklist de sécurité

- ✅ HTTPS obligatoire (HTTP → HTTPS redirect)
- ✅ HSTS headers activés
- ✅ X-Frame-Options: SAMEORIGIN
- ✅ X-Content-Type-Options: nosniff
- ✅ Variables d'environnement dans .env (pas dans le code)
- ✅ Rate limiting sur tous les endpoints
- ✅ Logs sanitisés (pas de données sensibles)

### Firewall

```bash
# UFW configuration
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP
sudo ufw allow 443/tcp   # HTTPS
sudo ufw enable
```

---

## 📞 Support

### En cas de problème

1. Vérifier les logs: `docker-compose logs -f`
2. Vérifier le statut: `docker-compose ps`
3. Consulter la documentation Notion
4. Vérifier les health checks

### Liens utiles

- **Repository**: https://github.com/trouveuncadeauxyz-cell/trouveuncadeau
- **n8n Workflow**: https://n8n.trouveuncadeau.xyz
- **Documentation Notion**: [Lien vers Notion]

---

## 📝 Checklist de déploiement

- [ ] Serveur DigitalOcean configuré
- [ ] Docker et Docker Compose installés
- [ ] Certificats SSL Let's Encrypt obtenus
- [ ] Repository cloné dans /opt/trouveuncadeau
- [ ] Fichier .env créé et rempli
- [ ] docker-compose.yml validé
- [ ] Build réussi sans erreurs
- [ ] Tous les conteneurs démarrent correctement
- [ ] Health checks passent
- [ ] Frontend accessible sur https://trouveuncadeau.xyz
- [ ] API backend répond
- [ ] n8n workflow connecté
- [ ] Tests de bout en bout réussis
- [ ] Monitoring configuré
- [ ] Backups planifiés

---

**Date de dernière mise à jour**: JOUR 8
**Version**: 1.0.0
**Prêt pour production**: ✅
