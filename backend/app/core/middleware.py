"""Middleware for error handling, request logging, and CORS configuration."""

import time
import logging
from typing import Callable
from uuid import uuid4

from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from .exceptions import TrouveUnCadeauException
from .schemas import ErrorResponse

# Configure logging
logger = logging.getLogger(__name__)


class ErrorHandlingMiddleware:
    """Middleware for centralized error handling."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request = Request(scope, receive)
        request_id = str(uuid4())
        scope["request_id"] = request_id

        try:
            await self.app(scope, receive, send)
        except TrouveUnCadeauException as exc:
            error_response = ErrorResponse(
                error=exc.error_code,
                message=exc.message,
                status_code=exc.status_code,
                request_id=request_id,
            )
            response = JSONResponse(
                status_code=exc.status_code,
                content=error_response.dict(),
            )
            await response(scope, receive, send)
            logger.error(
                f"TrouveUnCadeau Error: {exc.error_code} - {exc.message}",
                extra={"request_id": request_id, "status_code": exc.status_code},
            )
        except Exception as exc:
            error_response = ErrorResponse(
                error="INTERNAL_ERROR",
                message="Une erreur interne s'est produite",
                status_code=500,
                request_id=request_id,
            )
            response = JSONResponse(
                status_code=500,
                content=error_response.dict(),
            )
            await response(scope, receive, send)
            logger.exception(
                f"Unexpected error",
                extra={"request_id": request_id},
            )


class RequestLoggingMiddleware:
    """Middleware for logging HTTP requests and responses."""

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request = Request(scope, receive)
        request_id = str(uuid4())
        start_time = time.time()

        async def send_with_logging(message):
            if message["type"] == "http.response.start":
                status_code = message["status"]
                process_time = time.time() - start_time
                
                logger.info(
                    f"{request.method} {request.url.path} - {status_code}",
                    extra={
                        "request_id": request_id,
                        "method": request.method,
                        "path": request.url.path,
                        "status_code": status_code,
                        "process_time_ms": round(process_time * 1000, 2),
                    },
                )
            await send(message)

        await self.app(scope, receive, send_with_logging)


def get_cors_middleware(app, origins: list = None):
    """
    Configure CORS middleware for the FastAPI application.
    
    Args:
        app: FastAPI application instance
        origins: List of allowed origins (default: development origins)
    
    Returns:
        FastAPI app with CORS middleware configured
    """
    if origins is None:
        origins = [
            "http://localhost",
            "http://localhost:3000",
            "http://localhost:8000",
            "http://localhost:8501",  # Streamlit default port
            "http://127.0.0.1:8501",
            "http://127.0.0.1",
        ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    return app


def configure_middleware(app, enable_cors: bool = True, cors_origins: list = None):
    """
    Configure all middleware for the FastAPI application.
    
    Args:
        app: FastAPI application instance
        enable_cors: Whether to enable CORS (default: True)
        cors_origins: List of allowed CORS origins
    
    Returns:
        FastAPI app with all middleware configured
    """
    # Add custom middleware (order matters - added in reverse)
    app.add_middleware(RequestLoggingMiddleware)
    app.add_middleware(ErrorHandlingMiddleware)
    
    # Add CORS if enabled
    if enable_cors:
        get_cors_middleware(app, cors_origins)
    
    return app
