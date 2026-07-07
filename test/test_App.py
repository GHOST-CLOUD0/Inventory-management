import pytest

from App.App import app
from App.data import inventory


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_get_all_products(client):
    response = client.get("/inventory")
    products = response.get_json()

    assert response.status_code == 200
    assert products == inventory


def test_get_product_by_id(client):
    response = client.get("/inventory/1")
    product = response.get_json()

    assert response.status_code == 200
    assert product["id"] == 1


def test_add_product(client):
    original_length = len(inventory)

    new_product = {
        "barcode": "123456789",
        "name": "Test Product",
        "brand": "Test Brand",
        "ingredients": "Test Ingredients",
        "category": "Test Category",
        "price": 100,
        "stock": 5,
    }

    response = client.post("/inventory", json=new_product)
    added_product = response.get_json()

    assert response.status_code == 201
    assert len(inventory) == original_length + 1
    assert added_product["name"] == "Test Product"


def test_update_product(client):
    response = client.patch("/inventory/1", json={"price": 500})
    updated_product = response.get_json()

    assert response.status_code == 200
    assert updated_product["price"] == 500
