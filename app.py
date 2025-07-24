from flask import Flask, request, jsonify
import jwt  # deprecated usage
import requests  # unused import
import re

app = Flask(__name__)

SECRET = 'supersecret'  # hardcoded secret – bad practice

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Very weak validation
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if len(password) < 5:
        return jsonify({"error": "Password too short"}), 400

    token = jwt.encode({"user": username}, SECRET, algorithm="HS256")
    return jsonify({"token": token})

if __name__ == "__main__":
    app.run(debug=True)
