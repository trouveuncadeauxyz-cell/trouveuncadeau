"""Custom validators for request parameters and business logic."""

from typing import Optional, List
from pydantic import validator, root_validator

from .exceptions import ValidationError


class BudgetValidator:
    """Validator for budget-related parameters."""
    
    MIN_BUDGET = 10
    MAX_BUDGET = 10000
    
    @staticmethod
    def validate_budget(value: float) -> float:
        """Validate budget is within acceptable range."""
        if not isinstance(value, (int, float)):
            raise ValidationError(
                message="Le budget doit être un nombre",
                error_code="INVALID_BUDGET_TYPE"
            )
        
        if value < BudgetValidator.MIN_BUDGET:
            raise ValidationError(
                message=f"Le budget minimum est ${BudgetValidator.MIN_BUDGET}",
                error_code="BUDGET_TOO_LOW"
            )
        
        if value > BudgetValidator.MAX_BUDGET:
            raise ValidationError(
                message=f"Le budget maximum est ${BudgetValidator.MAX_BUDGET}",
                error_code="BUDGET_TOO_HIGH"
            )
        
        return round(float(value), 2)


class AgeValidator:
    """Validator for age-related parameters."""
    
    MIN_AGE = 1
    MAX_AGE = 120
    
    @staticmethod
    def validate_age(value: int) -> int:
        """Validate age is within acceptable range."""
        if not isinstance(value, int):
            raise ValidationError(
                message="L'âge doit être un nombre entier",
                error_code="INVALID_AGE_TYPE"
            )
        
        if value < AgeValidator.MIN_AGE:
            raise ValidationError(
                message=f"L'âge minimum est {AgeValidator.MIN_AGE}",
                error_code="AGE_TOO_LOW"
            )
        
        if value > AgeValidator.MAX_AGE:
            raise ValidationError(
                message=f"L'âge maximum est {AgeValidator.MAX_AGE}",
                error_code="AGE_TOO_HIGH"
            )
        
        return value


class OccasionValidator:
    """Validator for occasion-related parameters."""
    
    VALID_OCCASIONS = [
        "anniversaire",
        "noel",
        "fete_des_meres",
        "fete_des_peres",
        "saint_valentin",
        "graduation",
        "mariage",
        "depart_retraite",
        "bulle_confiance",
        "merci",
        "souhaite_remise",
        "autre"
    ]
    
    @staticmethod
    def validate_occasion(value: str) -> str:
        """Validate occasion is in allowed list."""
        if not isinstance(value, str):
            raise ValidationError(
                message="L'occasion doit être un texte",
                error_code="INVALID_OCCASION_TYPE"
            )
        
        value_lower = value.lower().strip()
        
        if value_lower not in OccasionValidator.VALID_OCCASIONS:
            occasions_str = ", ".join(OccasionValidator.VALID_OCCASIONS)
            raise ValidationError(
                message=f"Occasion invalide. Valeurs acceptées: {occasions_str}",
                error_code="INVALID_OCCASION"
            )
        
        return value_lower


class InterestValidator:
    """Validator for interest/hobby parameters."""
    
    MAX_INTERESTS = 10
    MAX_INTEREST_LENGTH = 50
    
    @staticmethod
    def validate_interests(values: List[str]) -> List[str]:
        """Validate interests list."""
        if not isinstance(values, list):
            raise ValidationError(
                message="Les intérêts doivent être une liste",
                error_code="INVALID_INTERESTS_TYPE"
            )
        
        if len(values) > InterestValidator.MAX_INTERESTS:
            raise ValidationError(
                message=f"Maximum {InterestValidator.MAX_INTERESTS} intérêts autorisés",
                error_code="TOO_MANY_INTERESTS"
            )
        
        cleaned_interests = []
        for interest in values:
            if not isinstance(interest, str):
                raise ValidationError(
                    message="Chaque intérêt doit être un texte",
                    error_code="INVALID_INTEREST_TYPE"
                )
            
            interest_cleaned = interest.strip().lower()
            
            if len(interest_cleaned) == 0:
                raise ValidationError(
                    message="Les intérêts ne peuvent pas être vides",
                    error_code="EMPTY_INTEREST"
                )
            
            if len(interest_cleaned) > InterestValidator.MAX_INTEREST_LENGTH:
                raise ValidationError(
                    message=f"Un intérêt ne peut pas dépasser {InterestValidator.MAX_INTEREST_LENGTH} caractères",
                    error_code="INTEREST_TOO_LONG"
                )
            
            if interest_cleaned not in cleaned_interests:
                cleaned_interests.append(interest_cleaned)
        
        return cleaned_interests


class RecommendationRequestValidator:
    """Compound validator for recommendation requests."""
    
    @staticmethod
    def validate_request(budget: float, age: int, occasion: str, 
                        interests: Optional[List[str]] = None) -> dict:
        """Validate complete recommendation request."""
        validated = {
            "budget": BudgetValidator.validate_budget(budget),
            "age": AgeValidator.validate_age(age),
            "occasion": OccasionValidator.validate_occasion(occasion),
            "interests": InterestValidator.validate_interests(interests or [])
        }
        return validated


def validate_pagination(skip: int = 0, limit: int = 20) -> tuple:
    """Validate pagination parameters."""
    MIN_SKIP = 0
    MIN_LIMIT = 1
    MAX_LIMIT = 100
    
    if not isinstance(skip, int) or skip < MIN_SKIP:
        raise ValidationError(
            message=f"Le paramètre 'skip' doit être >= {MIN_SKIP}",
            error_code="INVALID_SKIP"
        )
    
    if not isinstance(limit, int) or limit < MIN_LIMIT or limit > MAX_LIMIT:
        raise ValidationError(
            message=f"Le paramètre 'limit' doit être entre {MIN_LIMIT} et {MAX_LIMIT}",
            error_code="INVALID_LIMIT"
        )
    
    return skip, limit


def validate_search_query(query: str) -> str:
    """Validate search query string."""
    MIN_LENGTH = 1
    MAX_LENGTH = 200
    
    if not isinstance(query, str):
        raise ValidationError(
            message="La requête doit être un texte",
            error_code="INVALID_QUERY_TYPE"
        )
    
    query_cleaned = query.strip()
    
    if len(query_cleaned) < MIN_LENGTH:
        raise ValidationError(
            message="La requête doit contenir au moins 1 caractère",
            error_code="QUERY_TOO_SHORT"
        )
    
    if len(query_cleaned) > MAX_LENGTH:
        raise ValidationError(
            message=f"La requête ne peut pas dépasser {MAX_LENGTH} caractères",
            error_code="QUERY_TOO_LONG"
        )
    
    return query_cleaned
