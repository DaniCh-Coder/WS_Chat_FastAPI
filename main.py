'''
start_ngrok_tunnel.py
Este script:
1. Testea un tunel ngrok. 
2.Si no esta funcionando intenta crearlo.
3. Luego arranca el servidor FastAPI.
'''
import logging
import sys
import os

# Llama directamente a la función antes de las importaciones locales
def add_project_root_to_path():
    """
    Añade la raíz del proyecto a sys.path si no está ya incluido.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.append(project_root)
        logging.info(f"Ruta del proyecto añadida a sys.path: {sys.path} \n")
    else:
        logging.info(f"Ruta del proyecto correcta en sys.path: {sys.path} \n")

# Configuración del logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def start_ng_fa():
    """
    Punto de entrada principal del script.
    Verifica y maneja el estado de un túnel ngrok.
    """
    try:
        from utils.ngrok_utils import test_ngrok_tunnel, get_ngrok_tunnel
        from services.fa_services import start_fastapi

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
        # Revisa el path del proyecto
        add_project_root_to_path()

        # Llama al bucle asincrónico de forma correcta
        start_ng_fa()
    except Exception as e:
        logging.error(f"Error crítico al arrancar la aplicación: {e}")