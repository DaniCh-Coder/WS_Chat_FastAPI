'''
start_ngrok_tunnel.py
Este script:
1. Testea un tunel ngrok. 
2.Si no esta funcionando intenta crearlo.
3. Luego arranca el servidor FastAPI.
--------------------------------------------------------------
my_project/
├── main.py          # Define la aplicación FastAPI y las rutas.
├── services.py      # Lógica de negocio (opcional).
├── run.py           # Arranque del servidor Uvicorn.
└── requirements.txt # Dependencias del proyecto.
'''
import logging
from utils.ngrok_utils import test_ngrok_tunnel, get_ngrok_tunnel
from services.fa_services import start_fastapi

# Configuración del logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def start_ng_fa():
    """
    Punto de entrada principal del script.
    Verifica y maneja el estado de un túnel ngrok.
    """
    try:
        result = test_ngrok_tunnel()
        logging.info(result)

        tunnel = get_ngrok_tunnel()
        logging.info(tunnel)
            
    except Exception as e:
        logging.error(f"Error inesperado en ejecución principal start_ng_fa -> ngrok_tunnel: {e}")
    
    try:
        # Llama a la función de arranque del server
        start_fastapi()
    except Exception as e:
        logging.error(f"Error inesperado en ejecución principal start_ng_fa -> start_fastapi: {e}")

if __name__ == "__main__":
    try:
        # Llama al bucle asincrónico de forma correcta
        start_ng_fa()
    except Exception as e:
        logging.error(f"Error crítico al arrancar la aplicación: {e}")