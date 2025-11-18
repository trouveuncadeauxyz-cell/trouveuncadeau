"""Pydantic models (schemas) for request/response validation

Définit les structures de données utilisées par l'API FastAPI
pour valider les entrées et sorties.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


# ============ PRODUITS ============

class ProductBase(BaseModel):
    """Modèle de base pour les produits"""
    name: str = Field(..., min_length=1, max_length=200, description="Nom du produit")
    description: Optional[str] = Field(None, max_length=1000, description="Description détaillée")
    price: float = Field(..., gt=0, description="Prix en CAD")
    category: str = Field("gifts", max_length=100, description="Catégorie du produit")
    url: Optional[str] = Field(None, description="URL du produit")
    affiliate_url: Optional[str] = Field(None, description="URL affiliée Amazon")
    tags: Optional[str] = Field(None, description="Tags pour recherche")


class Product(ProductBase):
    """Modèle complet d'un produit avec métadonnées"""
    id: str = Field(..., description="ID unique Airtable")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ProductsResponse(BaseModel):
    """Réponse pour l'endpoint GET /api/products"""
    status: str = Field("success", description="Statut de la requête")
    count: int = Field(..., ge=0, description="Nombre de produits")
    products: List[Product] = Field(default_factory=list, description="Liste des produits")


# ============ RECOMMANDATIONS ============

class RecommendationRequest(BaseModel):
    """Requête pour générer des recommandations"""
    budget: float = Field(50.0, ge=10.0, le=5000.0, description="Budget maximal en CAD")
    recipient_age: int = Field(25, ge=1, le=120, description="Âge du destinataire")
    occasion: str = Field("anniversaire", max_length=100, description="Type d'occasion")
    interests: Optional[str] = Field(None, max_length=500, description="Intérêts du destinataire")
    count: int = Field(5, ge=1, le=10, description="Nombre de recommandations")


class RecommendationItem(BaseModel):
    """Un article dans les recommandations"""
    name: str = Field(..., description="Nom du produit recommandé")
    price: str = Field(..., description="Prix en CAD")
    description: Optional[str] = Field(None, description="Description")
    category: Optional[str] = Field(None, description="Catégorie")
    affiliate_url: Optional[str] = Field(None, description="Lien affilié Amazon")
    match_score: Optional[float] = Field(None, ge=0.0, le=100.0, description="Score de correspondance (%)")
    reasoning: Optional[str] = Field(None, description="Pourquoi cette recommandation")

    class Config:
        from_attributes = True


class RecommendationsResponse(BaseModel):
    """Réponse pour l'endpoint POST /api/recommendations"""
    status: str = Field("success", description="Statut (success/warning/error)")
    count: int = Field(0, ge=0, description="Nombre de recommandations")
    message: Optional[str] = Field(None, description="Message d'information")
    recommendations: List[RecommendationItem] = Field(default_factory=list, description="Liste des recommandations")
    model: Optional[str] = Field(None, description="Modèle IA utilisé")
    processing_time_ms: Optional[float] = Field(None, ge=0, description="Temps de traitement en ms")


# ============ SANTE ============

class HealthStatus(BaseModel):
    """Status de santé du service"""
    status: str = Field("healthy", description="État du service")
    timestamp: datetime = Field(..., description="Timestamp de la vérification")
    version: str = Field("1.0.0", description="Version du service")


class ServiceHealth(BaseModel):
    """Status complet avec détails des services"""
    status: str = Field("operational", description="État opérationnel")
    timestamp: datetime = Field(..., description="Timestamp")
    services: Dict[str, str] = Field(default_factory=dict, description="État de chaque service")
    uptime_seconds: Optional[float] = Field(None, description="Temps depuis le démarrage")


# ============ ERREURS ============

class ErrorResponse(BaseModel):
    """Réponse d'erreur standard"""
    status: str = Field("error", description="Statut d'erreur")
    message: str = Field(..., description="Message d'erreur")
    detail: Optional[str] = Field(None, description="Détails supplémentaires")
    error_code: Optional[str] = Field(None, description="Code d'erreur")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp de l'erreur")


class ValidationError(BaseModel):
    """Erreur de validation"""
    field: str = Field(..., description="Champ en erreur")
    message: str = Field(..., description="Message d'erreur")
    type: str = Field(..., description="Type d'erreur")


class ValidationErrorResponse(ErrorResponse):
    """Réponse d'erreur de validation"""
    errors: List[ValidationError] = Field(default_factory=list, description="Liste des erreurs")


# ============ PAGINATION ============

class PaginationParams(BaseModel):
    """Paramètres de pagination"""
    skip: int = Field(0, ge=0, description="Nombre d'éléments à sauter")
    limit: int = Field(100, ge=1, le=1000, description="Nombre d'éléments à retourner")
    sort_by: Optional[str] = Field(None, description="Champ pour le tri")
    sort_order: str = Field("asc", pattern="^(asc|desc)$", description="Ordre de tri")


class PaginatedResponse(BaseModel):
    """Réponse paginée générique"""
    status: str = Field("success", description="Statut")
    total: int = Field(..., ge=0, description="Total d'éléments")
    skip: int = Field(0, ge=0, description="Eléments sauts")
    limit: int = Field(100, ge=1, description="Limite")
    items: List[Dict[str, Any]] = Field(default_factory=list, description="Eléments")
    has_more: bool = Field(False, description="Y a-t-il plus d'éléments?")


# ============ CONFIG & METADATA ============

class APIInfo(BaseModel):
    """Information sur l'API"""
    title: str = Field("TrouveUnCadeau API", description="Titre")
    version: str = Field("1.0.0", description="Version")
    description: str = Field("Moteur de recommandation de cadeaux", description="Description")
    docs_url: str = Field("/api/docs", description="URL documentation")
    openapi_url: str = Field("/api/openapi.json", description="URL OpenAPI spec")
