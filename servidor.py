from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SECRET_KEY = os.environ.get("INTERNAL_SECRET")  

@app.route('/token', methods=['GET'])
def get_token():
    client_key = request.headers.get('X-Internal-Key')

    if client_key != SECRET_KEY:
        return jsonify({"error": "Acceso no autorizado"}), 401

    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        return jsonify({"error": "Token no disponible"}), 500

    return jsonify({"token": token}), 200
