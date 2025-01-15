import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Variables de la API de Meta extraídas del entorno
VERSION = os.getenv("META_API_VER")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
RECIPIENT_WAID = os.getenv("RECIPIENT_WAID")

# Fundamental recargar las variables de entorno cada vez que se ejecuta el script (por ejemplo, en un entorno de desarrollo)
def force_load_env():
    """
    Fuerza la recarga de las variables de entorno del archivo .env
    """
    for key in os.environ.keys():
        if key.startswith("META_") or key in ["PHONE_NUMBER_ID", "ACCESS_TOKEN", "RECIPIENT_WAID"]:
            os.environ.pop(key)
    load_dotenv()

# Llama a esta función antes de usar las variables
force_load_env()

def send_whatsapp_message():
    """
    Envía un mensaje de WhatsApp usando la API de Meta.
    """
    # URL de la API de WhatsApp Business
    url = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"
    
    # Encabezados para la solicitud
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    
    # Datos del mensaje
    data = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_WAID,
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }
    
    # Enviar la solicitud POST
    response = requests.post(url, headers=headers, json=data)
    return response

# Ejecutar la función y manejar la respuesta
def main():
    force_load_env()
    response = send_whatsapp_message()
    
    if response.status_code == 200:
        print("Mensaje enviado exitosamente.")
        print(response.json())
    else:
        print(f"Error al enviar el mensaje: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    main()
