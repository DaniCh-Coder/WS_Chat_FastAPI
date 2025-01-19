"""
Este módulo contiene funciones para enviar mensajes de WhatsApp Business API.
..........................................................................
├── main.py                # Define las rutas y controladores de la API
├── services/
│   ├── __init__.py        # Inicializa el paquete de servicios
│   ├── whatsapp_service.py # Contiene la lógica relacionada con WhatsApp
│   └── utils.py           # Funciones utilitarias genéricas
├── schemas/
│   ├── __init__.py        # Inicializa el paquete de esquemas
│   ├── webhook.py         # Define esquemas de validación de entrada
├── config/
│   ├── __init__.py        # Inicializa el paquete de configuración
│   └── settings.py        # Manejo de configuración de la aplicación
"""
import requests
import logging
import json
from config_setup.settings import settings
from fastapi import HTTPException

logger = logging.getLogger(__name__)

def get_from_number(from_number: str) -> str:
    """
    Verifica si el número de teléfono del remitente es el número de teléfono de WhatsApp Business API.
    Si es así, cambia el FORMATO del número de teléfono del remitente al número de teléfono de WhatsApp Business API.
    """
    if from_number == settings.RECIPIENT_WAID_1:
        from_number = settings.RECIPIENT_ITEM_1
        logger.info(f"RECIPIENT_WAID_1: {settings.RECIPIENT_WAID_1} detectado, cambiando a RECIPIENT_ITEM_1: {settings.RECIPIENT_ITEM_1}")
    else:
        logger.info(f"RECIPIENT_WAID_1: {settings.RECIPIENT_WAID_1} no detectado.")
    return from_number        

def send_message_via_wa(to: str, response_message: str, language: str = "es"):
    """
    Envia un mensaje usando la API de WhatsApp Business.
    """
    to = get_from_number(to)    # controla si reqiere cambiar el formato del número de teléfono del remitente
    url = f"{settings.META_URL}/{settings.META_API_VER}/{settings.PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {settings.ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": response_message},
    }
    try:
        logger.info(f"Enviando mensaje a {to} : {response_message} con payload: {json.dumps(payload, indent=2)}")
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        logger.info(f"Mensaje enviado exitosamente a {to}.")
    except requests.exceptions.HTTPError as e:
        logger.error(f"Error HTTP al enviar el mensaje a {to}: {response.status_code} - {response.text}")
        if response.status_code == 400:
            logger.error(f"Detalles del error: {response.json().get('error', {}).get('error_data', {}).get('details')}")
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Error de conexión al enviar el mensaje a {to}: {str(e)}")
        raise HTTPException(status_code=500, detail="Error de conexión con el servidor de WhatsApp")
    except requests.exceptions.Timeout as e:
        logger.error(f"Tiempo de espera agotado al enviar el mensaje a {to}: {str(e)}")
        raise HTTPException(status_code=500, detail="Tiempo de espera agotado")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error inesperado al enviar el mensaje a {to}: {str(e)}")
        raise HTTPException(status_code=500, detail="Error inesperado al enviar el mensaje")
