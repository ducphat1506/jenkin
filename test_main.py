import requests

def test_get_version():
    response = requests.get("http://localhost:8000/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0"}

def test_check_prime():
    response = requests.get("http://localhost:8000/check_prime?number=7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}
