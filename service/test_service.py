from fastapi.testclient import TestClient
from .main import service
import random

client = TestClient(service)


def test_get_items():
    item_id = random.randint(0,100)
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id}
