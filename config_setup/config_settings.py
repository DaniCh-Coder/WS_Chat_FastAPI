# Config Settings
from config_setup.settings import Settings
'''Esta función crea y devuelve una instancia de la clase Settings.
    El propósito de usar una función en lugar de instanciar la clase directamente en el código principal es:
        Modularidad: Centraliza la creación de la configuración en un solo lugar.
        Reutilización: Puedes usar esta función en varias partes de tu código sin necesidad de repetir lógica o inicializar la configuración en múltiples lugares.
        Integración con FastAPI: Si estás utilizando FastAPI, puedes usar esta función como dependencia, lo que permite que el framework maneje su ciclo de vida.
'''
def get_settings():
    return Settings()