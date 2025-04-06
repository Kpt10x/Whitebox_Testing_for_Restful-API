from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

# Configure logging
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests
logging.basicConfig(level=logging.DEBUG)

# Sample users database
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    if not request.is_json:
        return jsonify({"error": "Invalid input, expecting JSON"}), 400

    data = request.get_json()
    if "name" not in data or "age" not in data:
        return jsonify({"error": "Invalid input, missing fields"}), 400

    user_id = max(users.keys(), default=0) + 1
    users[user_id] = {"name": data["name"], "age": data["age"]}

    return jsonify({"message": "User created", "id": user_id}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if "name" not in data or "age" not in data:
        return jsonify({"error": "Invalid input, missing fields"}), 400

    users[user_id].update({"name": data["name"], "age": data["age"]})
    return jsonify({"message": "User updated", "id": user_id}), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted", "id": user_id}), 200

@app.route("/api/test", methods=["POST"])
def test_api():
    return jsonify({"message": "Test successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)
