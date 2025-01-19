# exception_handlers.py
"""
Este archivo define manejadores para transformar excepciones en respuestas HTTP estructuradas.
"""
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from services.exceptions import WebhookException

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Maneja errores de validación de FastAPI.
    """
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation Error",
            "details": exc.errors(),
            "body": exc.body,
        },
    )

async def handle_exception(request: Request, status_code: int, detail: str, extra_data: dict = None):
    return JSONResponse(
        status_code=status_code,
        content={
            "error": detail,
            "extra_data": extra_data or {},
        },
    )

async def webhook_exception_handler(request: Request, exc: WebhookException):
    """
    Manejador de excepciones personalizado para WebhookException.
    Este manejador genera una respuesta JSON estructurada para las excepciones relacionadas con webhooks.

    Args:
        request (Request): La solicitud que originó la excepción.
        exc (WebhookException): La excepción lanzada.
    
    Returns:
        JSONResponse: Respuesta con código de estado y contenido detallado de la excepción.
    """
    # Verifica si `extra_data` existe y es un diccionario
    extra_data = exc.extra_data if isinstance(exc.extra_data, dict) else {}

    # Construye la respuesta JSON
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "Webhook Error",
            "details": exc.detail,
            "extra_data": extra_data
        },
    )

async def generic_exception_handler(request: Request, exc: Exception):
    debug_mode = True  # Cambia esto a False en producción
    extra_data = {"message": str(exc)}
    if debug_mode:
        extra_data["trace"] = repr(exc)
    return await handle_exception(request, 500, "Internal Server Error", extra_data)
