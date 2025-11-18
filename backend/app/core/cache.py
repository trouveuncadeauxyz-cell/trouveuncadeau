"""Caching layer for performance optimization."""

from typing import Any, Dict, Optional, Callable
from datetime import datetime, timedelta
from functools import wraps
import json
import logging
import hashlib

logger = logging.getLogger(__name__)


class InMemoryCache:
    """Simple in-memory cache with TTL support."""
    
    def __init__(self):
        self.cache: Dict[str, Dict[str, Any]] = {}
    
    def set(self, key: str, value: Any, ttl_seconds: int = 3600):
        """Store value in cache with TTL."""
        self.cache[key] = {
            'value': value,
            'expires_at': datetime.utcnow() + timedelta(seconds=ttl_seconds)
        }
        logger.debug(f"Cache set: {key} (TTL: {ttl_seconds}s)")
    
    def get(self, key: str) -> Optional[Any]:
        """Retrieve value from cache if not expired."""
        if key not in self.cache:
            return None
        
        entry = self.cache[key]
        if datetime.utcnow() > entry['expires_at']:
            del self.cache[key]
            logger.debug(f"Cache expired: {key}")
            return None
        
        logger.debug(f"Cache hit: {key}")
        return entry['value']
    
    def delete(self, key: str):
        """Remove value from cache."""
        if key in self.cache:
            del self.cache[key]
            logger.debug(f"Cache deleted: {key}")
    
    def clear(self):
        """Clear entire cache."""
        self.cache.clear()
        logger.info("Cache cleared")
    
    def cleanup_expired(self):
        """Remove expired entries."""
        now = datetime.utcnow()
        expired_keys = [
            key for key, entry in self.cache.items()
            if now > entry['expires_at']
        ]
        
        for key in expired_keys:
            del self.cache[key]
        
        if expired_keys:
            logger.debug(f"Cleaned up {len(expired_keys)} expired entries")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        self.cleanup_expired()
        return {
            'total_entries': len(self.cache),
            'memory_used_mb': len(json.dumps(self.cache, default=str)) / (1024 * 1024)
        }


class CacheKey:
    """Utility for generating cache keys."""
    
    @staticmethod
    def product(product_id: str) -> str:
        return f"product:{product_id}"
    
    @staticmethod
    def products_all() -> str:
        return "products:all"
    
    @staticmethod
    def recommendation(budget: float, age: int, occasion: str) -> str:
        key_str = f"rec:{budget}:{age}:{occasion}"
        return hashlib.md5(key_str.encode()).hexdigest()
    
    @staticmethod
    def search(query: str) -> str:
        return f"search:{query.lower()}"


def cache_result(ttl_seconds: int = 3600, cache_obj: Optional[InMemoryCache] = None):
    """Decorator for caching function results."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            # Generate cache key from function name and arguments
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            cache_key = hashlib.md5(cache_key.encode()).hexdigest()
            
            # Try to get from cache
            if cache_obj:
                cached = cache_obj.get(cache_key)
                if cached is not None:
                    logger.debug(f"Cache hit for {func.__name__}")
                    return cached
            
            # Execute function
            result = await func(*args, **kwargs)
            
            # Store in cache
            if cache_obj:
                cache_obj.set(cache_key, result, ttl_seconds)
            
            return result
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            cache_key = hashlib.md5(cache_key.encode()).hexdigest()
            
            # Try to get from cache
            if cache_obj:
                cached = cache_obj.get(cache_key)
                if cached is not None:
                    logger.debug(f"Cache hit for {func.__name__}")
                    return cached
            
            # Execute function
            result = func(*args, **kwargs)
            
            # Store in cache
            if cache_obj:
                cache_obj.set(cache_key, result, ttl_seconds)
            
            return result
        
        # Return appropriate wrapper
        import asyncio
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


# Global cache instance
_cache = InMemoryCache()


def get_cache() -> InMemoryCache:
    """Get global cache instance."""
    return _cache


def clear_cache():
    """Clear global cache."""
    _cache.clear()


def cache_products(ttl_seconds: int = 1800):
    """Cache strategy for product lists (30 minutes)."""
    return cache_result(ttl_seconds=ttl_seconds, cache_obj=_cache)


def cache_recommendations(ttl_seconds: int = 900):
    """Cache strategy for recommendations (15 minutes)."""
    return cache_result(ttl_seconds=ttl_seconds, cache_obj=_cache)


def cache_search(ttl_seconds: int = 600):
    """Cache strategy for search results (10 minutes)."""
    return cache_result(ttl_seconds=ttl_seconds, cache_obj=_cache)
