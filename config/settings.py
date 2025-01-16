"""
Este módulo contiene la configuración de la aplicación.
Construye una clase con todas las variables de entorno necesarias y valida su debida existencia.
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
import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Settings:
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
    META_API_VER = os.getenv("META_API_VER")
    META_URL = os.getenv("META_URL")
    RECIPIENT_ITEM_1 = os.getenv("RECIPIENT_ITEM_1")
    RECIPIENT_WAID_1 = os.getenv("RECIPIENT_WAID_1")

    @staticmethod
    def validate():
        required_vars = [
            Settings.VERIFY_TOKEN,
            Settings.ACCESS_TOKEN,
            Settings.PHONE_NUMBER_ID,
            Settings.META_API_VER,
            Settings.META_URL,
        ]
        if not all(required_vars):
            raise ValueError("Faltan variables de entorno necesarias.")

# Validar configuración al iniciar
Settings.validate()
