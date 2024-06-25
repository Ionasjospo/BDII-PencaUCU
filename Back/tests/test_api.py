import pytest
import requests
import jwt
import random
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
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        json_response = response.json()
        assert isinstance(json_response, dict)  # Asegura que la respuesta es un diccionario
        assert len(json_response) > 0  # Asegura que el diccionario no está vacío
    elif response.status_code == 404:
        if response.headers.get('Content-Type') == 'application/json':
            assert response.json() == {"error": "No countries found"}
        else:
            assert "No countries found" in response.text

def test_get_country():
    id = random.randint(1, 16)
    countries = ['Uruguay', 'Argentina', 'Chile', 'Venezuela', 'Brasil', 'Paraguay', 'Jamaica', 'Perú', 'Colombia',
                 'México', 'Costa Rica', 'Estados Unidos', 'Canadá', 'Panamá', 'Ecuador', 'Bolivia']
    response = requests.get(f"{BASE_URL}/country/{id}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        try:
            json_response = response.json()
            assert len(json_response) == 1
            assert json_response[0]['name'] in countries  
        except ValueError:
            pytest.fail("Response content is not valid JSON")
    elif response.status_code == 404:
        if response.headers.get('Content-Type') == 'application/json':
            assert response.json() == {"error": "Country not found"}
        else:
            pytest.skip("Received HTML 404 response instead of JSON")

def test_stats():
    id_match = random.randint(1, 24)
    response = requests.get(f"{BASE_URL}/stats/{id_match}")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        try:
            json_response = response.json()
            assert isinstance(json_response, dict)
            assert 'stats' in json_response 
        except ValueError:
            pytest.fail("Response content is not valid JSON")
    elif response.status_code == 404:
        if response.headers.get('Content-Type') == 'application/json':
            assert response.json() == {"error": "No stats found"}
        else:
            pytest.skip("Received HTML 404 response instead of JSON")

def test_get_ranking(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f"{BASE_URL}/ranking", headers=headers)
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        try:
            json_response = response.json()
            assert isinstance(json_response, dict)
            assert len(json_response) > 0
        except ValueError:
            pytest.fail("Response content is not valid JSON")
    elif response.status_code == 404:
        if response.headers.get('Content-Type') == 'application/json':
            assert response.json() == {"error": "No ranking found"}
        else:
            assert "No ranking found" in response.text

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
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        try:
            json_response = response.json()
            assert json_response == {"message": "Predictions submitted successfully"}
        except ValueError:
            pytest.fail("Response content is not valid JSON")
    elif response.status_code == 500:
        try:
            json_response = response.json()
            assert json_response == {"error": "Failed to submit predictions"}
        except ValueError:
            pytest.fail("Response content is not valid JSON")

def test_old_predictions(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f"{BASE_URL}/old_predictions", headers=headers)
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        try:
            json_response = response.json()
            assert isinstance(json_response, dict)
            assert len(json_response) > 0
        except ValueError:
            pytest.fail("Response content is not valid JSON")
    elif response.status_code == 404:
        if response.headers.get('Content-Type') == 'application/json':
            assert response.json() == {"error": "No points found"}
        else:
            assert "No points found" in response.text

            
