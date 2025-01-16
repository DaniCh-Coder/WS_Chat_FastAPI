# exceptions.py
"""
Modulo para el manejo de errores y excepciones
Este script define excepciones personalizadas para manejar errores relacionados con el Webhook y tiene las siguientes ventajas:
1. Claridad en los Errores: Cada tipo de error tiene una clase específica, lo que mejora la comprensión del flujo.
2. Facilidad de Depuración: Los metadatos adicionales (extra_data) ayudan a rastrear los valores erróneos.
3. Preparación para Pruebas: Las excepciones específicas pueden ser verificadas fácilmente en las pruebas unitarias.
Consistencia: Las excepciones personalizadas crean un estándar claro para manejar errores relacionados con el webhook.
"""
from fastapi import HTTPException

class WebhookException(HTTPException):
    """
    Excepción base para errores relacionados con el Webhook.
    """
    def __init__(self, status_code: int, detail: str, extra_data: dict = None):
        super().__init__(status_code=status_code, detail=detail)
        self.extra_data = extra_data or {}

class MissingParametersException(WebhookException):
    """
    Excepción para solicitudes con parámetros insuficientes.
    """
    def __init__(self):
        detail = "Parámetros insuficientes en la solicitud. Se requieren 'hub.mode', 'hub.verify_token', y 'hub.challenge'."
        super().__init__(status_code=400, detail=detail)

class InvalidTokenException(WebhookException):
    """
    Excepción para solicitudes con un token de verificación incorrecto.
    """
    def __init__(self, provided_token: str, expected_token: str):
        detail = f"Token de verificación incorrecto. Proporcionado: {provided_token}, Esperado: {expected_token}."
        extra_data = {"provided_token": provided_token, "expected_token": expected_token}
        super().__init__(status_code=403, detail=detail, extra_data=extra_data)

class InvalidModeException(WebhookException):
    """
    Excepción para solicitudes con un modo de verificación incorrecto.
    """
    def __init__(self, provided_mode: str):
        detail = f"Modo de verificación no válido: {provided_mode}. Solo se acepta 'subscribe'."
        extra_data = {"provided_mode": provided_mode}
        super().__init__(status_code=403, detail=detail, extra_data=extra_data)
