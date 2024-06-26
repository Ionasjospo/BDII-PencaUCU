import subprocess

def start_api():
    api_process = subprocess.Popen(["python", "src/Api/API.py"])
    return api_process

if __name__ == "__main__":
    api_process = start_api()

    try:
        api_process.wait()
    except KeyboardInterrupt:
        api_process.terminate()
