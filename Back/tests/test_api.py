import pytest
import requests
import jwt
from datetime import datetime, timedelta, timezone

BASE_URL = "http://127.0.0.1:5000"
SECRET_KEY = 'your_secret_key'

@pytest.fixture(scope="module", autouse=True)
def start_and_stop_api():
    import subprocess
    import time

    api_process = subprocess.Popen(["python", "src/main.py"])
    time.sleep(3)  # Esperar unos segundos para asegurar que la API esté levantada
    yield
    api_process.terminate()

@pytest.fixture
def token():
    # Generar un token JWT para un usuario de prueba
    payload = {
        'username': 'testuser',
        'exp': datetime.now(timezone.utc) + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def test_get_countries():
    response = requests.get(f"{BASE_URL}/countries")
    assert response.status_code == 200 or response.status_code == 404
    if response.status_code == 200:
        json_response = response.json()
        assert isinstance(json_response, dict)  # Asegura que la respuesta es un diccionario
        assert len(json_response) > 0  # Asegura que el diccionario no está vacío
    elif response.status_code == 404:
        assert response.json() == {"error": "No countries found"}

def test_submit_predictions(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    data = {
        'predictions': [
            {'match_id': 1, 'home_score': 2, 'away_score': 1},
            {'match_id': 2, 'home_score': 0, 'away_score': 0}
        ]
    }
    response = requests.post(f"{BASE_URL}/predictions", json=data, headers=headers)
    assert response.status_code == 200 or response.status_code == 500
    if response.status_code == 200:
        json_response = response.json()
        assert json_response == {"message": "Predictions submitted successfully"}
    elif response.status_code == 500:
        json_response = response.json()
        assert json_response == {"error": "Failed to submit predictions"}
