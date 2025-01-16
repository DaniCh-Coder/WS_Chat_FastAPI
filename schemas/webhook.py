"""
    This module defines the Pydantic models for the webhook payload.
    These models are used to validate and parse the incoming webhook data.
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
from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    from_: str
    text: Optional[dict]

class Change(BaseModel):
    value: dict

class Entry(BaseModel):
    changes: List[Change]

class WebhookPayload(BaseModel):
    entry: List[Entry]
