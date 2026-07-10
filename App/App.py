from flask import Flask, request, jsonify
from App.data import inventory
from App.External_API import fetch_products, search_products_by_name

app = Flask(__name__)

@app.route('/product/<barcode>', methods=['GET'])
def get_product_from_api(barcode):
    product = fetch_products(barcode)
    if not product:
        return jsonify({"error": "product not found"}), 404
    return jsonify(product), 200

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    return jsonify(item) if item else ('Not Found', 404)

@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    data['id'] = max([item["id"]for item in inventory], default=0) + 1
    inventory.append(data)
    return jsonify(data), 201

@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    item.update(data)
    return jsonify(item), 200

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    inventory.remove(item)
    return "", 204
    
@app.route("/products/search", methods=["GET"])
def search_products():
    product_name = request.args.get("q", "").strip()

    if not product_name:
        return jsonify({"error": "Search term is required"}), 400

    products = search_products_by_name(product_name)

    return jsonify({
        "count": len(products),
        "results": products
    }), 200
    
@app.route('/inventory/import', methods=['POST'])
def import_inventory_item():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400

    barcode = data.get("barcode")
    if not barcode:
        return jsonify({"error": "Barcode is required"}), 400

    product = fetch_products(barcode)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    new_item = {
        "id": max([item["id"] for item in inventory], default=0) + 1,
        "barcode": barcode,
        "name": product.get("product_name", "Unknown Product"),
        "brand": product.get("brands", "Unknown Brand"),
        "ingredients": product.get("ingredients_text", ""),
        "category": product.get("categories", ""),
        "price": data.get("price", 0),
        "stock": data.get("stock", 0),
    }

    inventory.append(new_item)
    return jsonify(new_item), 201
if __name__ == '__main__':
    app.run(debug=True)
