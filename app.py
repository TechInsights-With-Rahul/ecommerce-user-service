from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory user storage
users = {}


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


# Health check endpoint for readiness probe
@app.route('/ready', methods=['GET'])
def ready_check():
    return jsonify({"status": "ready"}), 200



@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    
    if username in users:
        return jsonify({"message": "User already exists!"}), 400
    
    users[username] = {
        "email": data.get('email')
    }
    
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    
    if not user:
        return jsonify({"message": "User not found!"}), 404
    
    return jsonify({"username": username, "email": user["email"]}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

