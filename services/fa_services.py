"""
FastAPI Webhook Module
Author: @DanielChristello - 2024
Version: 0.4

Este servicio FastAPI está diseñado para manejar solicitudes de verificación de un webhook de Meta
1. Verificar la validez de las notificaciones entrantes.
2. Procesar los mensajes recibidos y extraer la información relevante.
3. Responder automáticamente a los mensajes entrantes.
+ Meta enviará notificaciones al webhook cuando recibas un mensaje en tu cuenta de WhatsApp Business.
+ Este endpoint recibirá los datos enviados por Meta, que incluyen información sobre los mensajes entrantes.
+ El servidor responderá automáticamente a los mensajes con un mensaje de bienvenida.
Documentación Meta: 
https://developers.facebook.com/docs/whatsapp/api/webhooks/inbound#verify-webhook
"""

from fastapi import FastAPI, Request                    # FastAPI class to handle the API requests and exceptios
from fastapi.responses import PlainTextResponse         # PlainTextResponse class to handle the responses of the API
import logging                                          # logging module to handle the logging of the application
from config_setup.settings import Settings              # Import the Settings class from the settings module
from config_setup.config_settings import get_settings   # Import the get_settings dependenciy for FastAPI use.
from services.wa_services import send_message_via_wa    # Import the send_message_via_wa function to send messages via WhatsApp
from schemas.webhook import WebhookPayload              # Import the WebhookPayload class to handle the payload of the webhook
from services.exceptions import MissingParametersException, InvalidTokenException, InvalidModeException, WebhookException
from services.exceptions_handler import validation_exception_handler, webhook_exception_handler, generic_exception_handler


# Configuración de logging
# Configura logging para registrar eventos importantes, como verificaciones exitosas o fallidas.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Define la aplicación FastAPI
app = FastAPI()
app.title = "ngrok FastAPI con Webhook"
app.version = "1.0"

# Configurar manejadores de excepciones
app.add_exception_handler(MissingParametersException, validation_exception_handler)
app.add_exception_handler(InvalidTokenException, validation_exception_handler)
app.add_exception_handler(InvalidModeException, validation_exception_handler)
app.add_exception_handler(WebhookException, webhook_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
    
@app.get("/", tags=["Home"])   # Tag and Decorator for the root path
def read_root():
    """
    Endpoint principal para comprobar que el servidor está activo.
    """    
    return {"title": app.title, "version": app.version, "message": "Server is running"}

@app.get("/webhook", tags=["Webhook"])
async def verify_webhook(request: Request, settings: Settings = get_settings()):
    """
        Validación del webhook: (Meta) necesita asegurarse de que este server es del propietario del servidor que manejará las notificaciones. 
        Más información en: https://developers.facebook.com/docs/whatsapp/api/webhooks/inbound#verify-webhook
    """

    mode = request.query_params.get("hub.mode")             # obtiene el valor del parámetro "hub.mode" de la solicitud enviado por meta
    token = request.query_params.get("hub.verify_token")    # obtiene el valor del parámetro "hub.verify_token" de la solicitud enviado por meta
    challenge = request.query_params.get("hub.challenge")   # obtiene el valor del parámetro "hub.challenge" de la solicitud enviado por meta

    if not all([mode, token, challenge]):
        logger.warning("Faltan parámetros en la solicitud GET.")
        raise MissingParametersException()

    if mode != "subscribe":
        logger.warning(f"Modo de verificación incorrecto: {mode}")
        raise InvalidModeException(provided_mode=mode)

    if token != settings.VERIFY_TOKEN:
        logger.warning(f"Token de verificación incorrecto. Meta: {token}. Local: {Settings.VERIFY_TOKEN}")
        raise InvalidTokenException(provided_token=token, expected_token=Settings.VERIFY_TOKEN)

    logger.info("Webhook verificado con éxito.")
    return PlainTextResponse(content=challenge, status_code=200)
    
@app.post("/webhook")
async def handle_messages(payload: WebhookPayload):
    """
    Maneja las notificaciones entrantes.
    """
    # Accede a los datos validados del payload
    for entry in payload.entry:
        for change in entry.changes:
            messages = change.value.get("messages", [])
            for message in messages:
                from_number = message.get("from")
                text_body = message.get("text", {}).get("body", "")
                logger.info(f"Mensaje recibido de {from_number}: {text_body}")
                send_message_via_wa(from_number, "Hola, ¿en qué puedo ayudarte?")
    return {"status": "processed"}

#..........................................................................
def start_fastapi():
    """
    Inicia el servidor FastAPI.
    """
    import uvicorn
    uvicorn.run("services.fa_services:app", host="0.0.0.0", port=5000, log_level="info")

#..........................................................................
# Para ejecutar la aplicación, ejecute el script start_ngrok_tunnel.py
# Test first locally with: http://localhost:5000/
