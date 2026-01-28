from flask import Flask, request, jsonify
import jwt
import bcrypt
import datetime
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

users = {}

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"status": "error", "data": None, "message": "token required"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            user = users.get(data["username"])
            if not user:
                raise Exception()
        except:
            return jsonify({"status": "error", "data": None, "message": "invalid token"}), 401
        return f(*args, **kwargs)
    return wrapper

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    password_hash = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    users[data["username"]] = password_hash
    return jsonify({"status": "ok", "data": None, "message": "user registered"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    password_hash = users.get(data["username"])
    if not password_hash or not bcrypt.checkpw(data["password"].encode(), password_hash):
        return jsonify({"status": "error", "data": None, "message": "invalid credentials"}), 401
    token = jwt.encode({
        "username": data["username"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, app.config["SECRET_KEY"], algorithm="HS256")
    return jsonify({"status": "ok", "data": {"token": token}, "message": "login success"})

@app.route("/profile", methods=["GET"])
@token_required
def profile():
    return jsonify({"status": "ok", "data": {"profile": "private data"}, "message": "access granted"})

if __name__ == "__main__":
    app.run(debug=True)
