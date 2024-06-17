import subprocess

def start_api():
    # Iniciar la API en un proceso separado
    api_process = subprocess.Popen(["python", "src/Api/API.py"])
    return api_process

if __name__ == "__main__":
    api_process = start_api()

    try:
        # Mantener el script en ejecución para mantener la API en funcionamiento
        api_process.wait()
    except KeyboardInterrupt:
        # Terminar el proceso de la API al recibir una interrupción del teclado (Ctrl+C)
        api_process.terminate()
