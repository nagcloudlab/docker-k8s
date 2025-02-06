import socket
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

# MySQL Connection Config
DB_CONFIG = {
    "host": "mysql",  # Use MySQL service name in Kubernetes
    "user": "root",
    "password": "password",
    "database": "mydb"
}

def get_db_connection():
    """Returns a new database connection"""
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/api/info', methods=['GET'])
def get_info():
    """Returns Pod hostname and IP"""
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return jsonify({"hostname": hostname, "ip": ip}), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    """Fetches all users from MySQL"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        conn.close()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
