from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URLs of the other services
PRODUCT_SERVICE_URL = 'http://localhost:5001/product/'
RECOMMENDATION_SERVICE_URL = 'http://localhost:5002/recommendation/'
REVIEW_SERVICE_URL = 'http://localhost:5003/review/'

@app.route('/product-composite/<int:product_id>', methods=['GET'])
def get_product_composite(product_id):
    try:
        # Fetch product details
        product_response = requests.get(f"{PRODUCT_SERVICE_URL}{product_id}")
        if product_response.status_code != 200:
            return jsonify({"error": "Product service error"}), product_response.status_code
        product = product_response.json()

        # Fetch recommendations
        recommendations_response = requests.get(f"{RECOMMENDATION_SERVICE_URL}{product_id}")
        if recommendations_response.status_code != 200:
            return jsonify({"error": "Recommendation service error"}), recommendations_response.status_code
        recommendations = recommendations_response.json()

        # Fetch reviews
        reviews_response = requests.get(f"{REVIEW_SERVICE_URL}{product_id}")
        if reviews_response.status_code != 200:
            return jsonify({"error": "Review service error"}), reviews_response.status_code
        reviews = reviews_response.json()

        # Aggregate the data
        composite = {
            "product": product,
            "recommendations": recommendations,
            "reviews": reviews
        }

        return jsonify(composite), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
