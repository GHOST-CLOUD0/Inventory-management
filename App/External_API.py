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
