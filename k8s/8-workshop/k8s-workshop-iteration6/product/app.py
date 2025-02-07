from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Dummy product data
    product = {
        "id": product_id,
        "name": "Smartphone",
        "description": "A high-end smartphone with a great camera.",
        "service_address": f"{os.getenv('POD_NAME')} ({os.getenv('POD_IP')})"
    }
    return jsonify(product), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
