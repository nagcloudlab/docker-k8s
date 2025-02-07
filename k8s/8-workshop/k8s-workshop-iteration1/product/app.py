from flask import Flask, jsonify

app = Flask(__name__)

# Mock product data
PRODUCTS = {
    1: {
        "id": 1,
        "name": "Smartphone",
        "description": "A high-end smartphone with a great camera."
    },
    2: {
        "id": 2,
        "name": "Laptop",
        "description": "A powerful laptop suitable for all your needs."
    }
}

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = PRODUCTS.get(product_id)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
