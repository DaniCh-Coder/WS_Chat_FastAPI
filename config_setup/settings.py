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
from pydantic_settings import BaseSettings
from pydantic import Field, ValidationError

class Settings(BaseSettings):
    VERIFY_TOKEN: str = Field(..., description="Token para la verificación del webhook")
    ACCESS_TOKEN: str = Field(..., description="Token de acceso a la API de Meta")
    PHONE_NUMBER_ID: str = Field(..., description="ID del número de teléfono asociado a la cuenta de WhatsApp Business")
    META_API_VER: str = Field(..., description="Versión de la API de Meta utilizada")
    META_URL: str = Field(..., description="URL base de la API de Meta")
    RECIPIENT_ITEM_1: str = Field(None, description="ID del ítem del destinatario, si es requerido")
    RECIPIENT_WAID_1: str = Field(None, description="ID de WhatsApp del destinatario, si es requerido")
    APP_ID: str = Field(..., description="ID de la aplicación")
    NGROK_AUTH_TOKEN: str = Field(..., description="Token de autenticación de ngrok")
    NGROK_COMMAND: str = Field(..., description="Comando para ngrok")
    NGROK_TIMEOUT: int = Field(..., description="Tiempo de espera para ngrok")
    DEBUG: bool = Field(None, description="Modo de depuración")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Probar la configuración al iniciar
try:
    settings = Settings()
except ValidationError as e:
    raise ValueError(f"Error al cargar las variables de entorno: {e}")

# Ejemplo de acceso
if __name__ == "__main__":
    print(f"VERIFY_TOKEN: {settings.VERIFY_TOKEN}")
    print(f"ACCESS_TOKEN: {settings.ACCESS_TOKEN}")
    print(f"META_API_VER: {settings.META_API_VER}")
    print(f"META_URL: {settings.META_URL}")
    print(f"PHONE_NUMBER_ID: {settings.PHONE_NUMBER_ID}")
    print(f"RECIPIENT_ITEM_1: {settings.RECIPIENT_ITEM_1}")
    print(f"RECIPIENT_WAID_1: {settings.RECIPIENT_WAID_1}")
    print(f"APP_ID: {settings.APP_ID}")
    print(f"NGROK_AUTH_TOKEN: {settings.NGROK_AUTH_TOKEN}")
    print(f"NGROK_COMMAND: {settings.NGROK_COMMAND}")
    print(f"NGROK_TIMEOUT: {settings.NGROK_TIMEOUT}")
    print(f"DEBUG: {settings.DEBUG}")
   
