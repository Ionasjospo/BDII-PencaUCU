import subprocess
import time

def start_api():
    api_process = subprocess.Popen(["python", "src/main.py"])
    time.sleep(5)
    return api_process

if __name__ == "__main__":
    api_process = start_api()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        api_process.terminate()
