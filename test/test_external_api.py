import requests
from unittest.mock import patch
from App.External_API import fetch_products

@patch("App.External_API.requests.get")
def test_fetch_product_success(mock_get):
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "name": "Mock Product",
            "brands": "Mock Brand",
            "ingredient": "Mock Ingredients",
            "categories": "Mock Categories"
        }
    }
    
    product = fetch_products("123456789")
    
    assert product["name"] == "Mock Product"
    assert product["brands"] == "Mock Brand"

@patch("App.External_API.requests.get")     
def test_fetch_product_not_found(mock_get):
    mock_get.return_value.json.return_value = {"status": 0}
    product = fetch_products("000000000")
    assert product == {}
    
@patch("App.External_API.requests.get") 
def test_fetch_product_http_error(mock_get):
    mock_get.return_value.status_code = 404
    product = fetch_products("123456789")
    assert product == {}  