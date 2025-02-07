from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Get MongoDB URI from environment variable
MONGODB_URI = os.getenv('MONGODB_URI', 'default-url')

# Initialize MongoDB client
client = MongoClient(MONGODB_URI)
db = client.productdb
products_collection = db.products

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products_collection.find_one({"id": product_id}, {"_id": 0})
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    # Pre-populate with sample data if collection is empty
    if products_collection.count_documents({}) == 0:
        sample_products = [
            {"id": 1, "name": "Smartphone", "description": "A high-end smartphone with a great camera."},
            {"id": 2, "name": "Laptop", "description": "A powerful laptop suitable for all your needs."}
        ]
        products_collection.insert_many(sample_products)
    app.run(host='0.0.0.0', port=5001, debug=True)
