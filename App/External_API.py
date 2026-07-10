import requests

def fetch_products(barcode):
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return {}

    data = response.json()
    if data.get("status") != 1:
        return {}

    return data.get('product', {})

def search_products_by_name(product_name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": 5,
        "fields": "code,product_name,brands,categories",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return []

    products = response.json().get("products", [])

    return [
        product
        for product in products
        if product.get("code") and product.get("product_name")
    ]