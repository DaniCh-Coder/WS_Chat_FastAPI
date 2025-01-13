start_ngrok_doc
Documentación de start_ngr_ok.bat
El archivo de configuración de ngrok se llama config.yml y generalmente está ubicado en tu directorio de usuario:
En Linux/MacOS: ~/.ngrok2/config.yml
En Windows: %HOMEPATH%\.ngrok2\config.yml
Ejemplo: Config files read: [C:\Users\Dani\AppData\Local/ngrok/ngrok.yml]

Explicación del codigo bach start_ngr_ok.bat
@echo off: Desactiva la visualización de los comandos en la consola.
set SUBDOMAIN=xxxxxx-xxxxxx-xxxxxx.ngrok-free.app: Define el subdominio que se utilizará para el túnel de ngrok.
set PORT=5000: Define el puerto local que se expondrá a través de ngrok.
REM ngrok http --url xxxxxx-xxxxxx-xxxxxx.ngrok-free.app 5000: Línea comentada que muestra un ejemplo de cómo se puede ejecutar ngrok con un subdominio y puerto específicos.
ngrok http --url %SUBDOMAIN% %PORT%: Inicia ngrok con el subdominio y puerto especificados.
pause: Pausa la ejecución del script para mantener la ventana de la consola abierta y permitir al usuario ver la salida.
Uso
Para ejecutar este archivo .bat, simplemente haz doble clic sobre él o ejecútalo desde el terminal:

Asegúrate de que ngrok esté instalado y accesible en tu PATH. Si no lo está, puedes agregar la ruta completa al ejecutable de ngrok en el script.
Así también start_ngr_ok.bat esta ubicado y accesible en tu path para poder ser ejecutado desde tu línea de comando o desde la terminal de tu entorno virtual.
El archivo de configuración de ngrok se llama config.yml y generalmente está ubicado en tu directorio de usuario:
En Linux/MacOS: ~/.ngrok2/config.yml
En Windows: %HOMEPATH%\.ngrok2\config.yml
Ejemplo: Config files read: [C:\Users\Dani\AppData\Local/ngrok/ngrok.yml]