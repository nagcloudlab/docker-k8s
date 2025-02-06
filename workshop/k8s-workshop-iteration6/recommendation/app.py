from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Get MongoDB URI from environment variable
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://mongodb-recommendation:27017/recommendationdb')


# Initialize MongoDB client
client = MongoClient(MONGODB_URI)
db = client.recommendationdb
recommendations_collection = db.recommendations

@app.route('/recommendation/<int:product_id>', methods=['GET'])
def get_recommendations(product_id):
    recommendations = list(recommendations_collection.find({"product_id": product_id}, {"_id": 0}))
    return jsonify(recommendations), 200

if __name__ == '__main__':
    # Pre-populate with sample data if collection is empty
    if recommendations_collection.count_documents({}) == 0:
        sample_recommendations = [
            {"id": 101, "product_id": 1, "name": "Wireless Earbuds"},
            {"id": 102, "product_id": 1, "name": "Smartwatch"},
            {"id": 201, "product_id": 2, "name": "Mouse"},
            {"id": 202, "product_id": 2, "name": "Keyboard"}
        ]
        recommendations_collection.insert_many(sample_recommendations)
    app.run(host='0.0.0.0', port=5002, debug=True)
