from flask import Flask, jsonify

app = Flask(__name__)

# Mock recommendation data
RECOMMENDATIONS = {
    1: [
        {"id": 101, "name": "Wireless Earbuds"},
        {"id": 102, "name": "Smartwatch"}
    ],
    2: [
        {"id": 201, "name": "Mouse"},
        {"id": 202, "name": "Keyboard"}
    ]
}

@app.route('/recommendation/<int:product_id>', methods=['GET'])
def get_recommendations(product_id):
    recommendations = RECOMMENDATIONS.get(product_id, [])
    return jsonify(recommendations), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
