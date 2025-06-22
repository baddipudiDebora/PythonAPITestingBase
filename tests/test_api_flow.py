import pytest
from utils.api_client import APIClient
from utils.payload_loader import load_payload

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="module")
def client():
    return APIClient(BASE_URL)

def test_create_resource_valid(client):
    payload = load_payload("test_data/single_object.json")
    print(client.base_url)
    response = client.post("/user", data=payload)
    assert response.status_code == 200
    assert "code" in response.json()
