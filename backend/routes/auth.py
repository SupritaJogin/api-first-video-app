from flask import Blueprint, request, jsonify
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# Dummy user database
users = {
    "admin": {
        "name": "Admin",
        "email": "admin@example.com",
        "password_hash": generate_password_hash("1234"),
        "role": "student"
    }
}

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users:
        return jsonify({"message":"User already exists"}), 400
    users[username] = {
        "name": data.get("name"),
        "email": data.get("email"),
        "password_hash": generate_password_hash(password),
        "role": "student"
    }
    return jsonify({"message":"Signup successful"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"message":"Invalid credentials"}), 401
    token = jwt.encode({
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, "secret123", algorithm="HS256")
    return jsonify({"token": token})

@auth_bp.route("/me", methods=["GET"])
def profile():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"message":"Token missing"}), 401
    token = auth_header.split(" ")[1]
    try:
        data = jwt.decode(token, "secret123", algorithms=["HS256"])
        username = data["user"]
        user = users.get(username)
        return jsonify({
            "status":"authorized",
            "role": user["role"],
            "user": username
        })
    except:
        return jsonify({"message":"Token is invalid"}), 401
