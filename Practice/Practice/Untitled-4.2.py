from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
next_id = 1

def response(status, data=None, message=""):
    return jsonify({
        "status": status,
        "data": data,
        "message": message
    })

@app.route("/users", methods=["GET"])
def get_users():
    return response("ok", users, "users list")

@app.route("/users", methods=["POST"])
def create_user():
    global next_id
    data = request.json
    user = {
        "id": next_id,
        "name": data.get("name")
    }
    users.append(user)
    next_id += 1
    return response("ok", user, "user created")

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return response("ok", user, "user found")
    return response("error", None, "user not found"), 404

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            return response("ok", user, "user updated")
    return response("error", None, "user not found"), 404

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return response("ok", None, "user deleted")
    return response("error", None, "user not found"), 404

if __name__ == "__main__":
    app.run(debug=True)
