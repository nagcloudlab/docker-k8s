from flask import Flask, jsonify

app = Flask(__name__)

# Mock review data
REVIEWS = {
    1: [
        {"id": 1001, "comment": "Excellent product!", "rating": 5},
        {"id": 1002, "comment": "Good value for money.", "rating": 4}
    ],
    2: [
        {"id": 2001, "comment": "Not what I expected.", "rating": 2},
        {"id": 2002, "comment": "Could be better.", "rating": 3}
    ]
}

@app.route('/review/<int:product_id>', methods=['GET'])
def get_reviews(product_id):
    reviews = REVIEWS.get(product_id, [])
    return jsonify(reviews), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
