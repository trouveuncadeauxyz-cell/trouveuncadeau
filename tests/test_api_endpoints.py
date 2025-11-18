"""Tests pour les endpoints API de TrouveUnCadeau.xyz

Tests automatisés pour valider tous les endpoints REST API.
"""

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
import os

# Configuration client de test
client = TestClient(app)


class TestHealthEndpoints:
    """Tests pour les endpoints de santé"""
    
    def test_root_health(self):
        """Test endpoint /health"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
    
    def test_api_health(self):
        """Test endpoint /api/health"""
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json()["status"] == "operational"


class TestProductsEndpoints:
    """Tests pour les endpoints de produits"""
    
    def test_get_products_default(self):
        """Test récupération produits avec paramètres par défaut"""
        response = client.get("/api/products")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "count" in data
        assert "products" in data
        assert isinstance(data["products"], list)
    
    def test_get_products_with_limit(self):
        """Test récupération produits avec limite"""
        response = client.get("/api/products?limit=5")
        assert response.status_code == 200
        data = response.json()
        assert len(data["products"]) <= 5
    
    def test_get_products_with_category(self):
        """Test filtrage par catégorie"""
        response = client.get("/api/products?category=tech")
        assert response.status_code == 200


class TestRecommendationsEndpoints:
    """Tests pour les endpoints de recommandations"""
    
    def test_get_recommendations(self):
        """Test génération de recommandations"""
        payload = {
            "budget": 50.0,
            "recipient_age": 25,
            "occasion": "anniversaire",
            "interests": "technologie",
            "count": 5
        }
        response = client.post("/api/recommendations", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "recommendations" in data
    
    def test_get_quick_recommendations(self):
        """Test recommandations rapides"""
        response = client.get("/api/recommendations/quick?query=cadeau&count=3")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "recommendations" in data


class TestSearchEndpoints:
    """Tests pour les endpoints de recherche"""
    
    def test_search_products(self):
        """Test recherche de produits"""
        response = client.get("/api/search?query=cadeau")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "items" in data
    
    def test_search_with_filters(self):
        """Test recherche avec filtres de prix"""
        response = client.get("/api/search?query=tech&price_min=10&price_max=100")
        assert response.status_code == 200
    
    def test_search_suggestions(self):
        """Test suggestions de recherche"""
        response = client.get("/api/search/suggestions?query=cad&limit=5")
        assert response.status_code == 200
        data = response.json()
        assert "suggestions" in data
        assert len(data["suggestions"]) <= 5


class TestCategoriesEndpoint:
    """Tests pour l'endpoint des catégories"""
    
    def test_get_categories(self):
        """Test récupération des catégories"""
        response = client.get("/api/products/categories")
        assert response.status_code == 200
        data = response.json()
        assert "categories" in data
        assert isinstance(data["categories"], list)


class TestRateLimiting:
    """Tests pour le rate limiting"""
    
    def test_rate_limit_not_exceeded(self):
        """Test que les requêtes normales passent"""
        for _ in range(5):
            response = client.get("/health")
            assert response.status_code == 200


class TestErrorHandling:
    """Tests pour la gestion d'erreurs"""
    
    def test_invalid_endpoint(self):
        """Test endpoint inexistant"""
        response = client.get("/api/invalid")
        assert response.status_code == 404
    
    def test_invalid_recommendation_params(self):
        """Test paramètres invalides pour recommendations"""
        payload = {"budget": -10}  # Budget négatif invalide
        response = client.post("/api/recommendations", json=payload)
        # Devrait retourner une erreur de validation
        assert response.status_code in [400, 422]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
