from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
import mysql.connector
from mysql.connector import Error
from db import create_connection
import bcrypt
import os
import requests
from dotenv import load_dotenv


app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    api_key_encrypted = os.getenv("API_PASSWORD")

    print(bcrypt.checkpw(password.encode('utf-8'), api_key_encrypted.encode('utf-8')))
    if username != os.getenv("API_USER"):
        return False
    if not bcrypt.checkpw(password.encode('utf-8'), api_key_encrypted.encode('utf-8')):
        return False
    return True


@app.route('/registerdata', methods=['POST'])
@auth.login_required
def insert_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided in request body"}), 400

    register_url = "http://localhost:5001/registerdata"
    try:
        response = requests.post(register_url, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return jsonify({"message": "Data inserted successfully"})
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to insert data: {e}"}), 500


@app.route('/logindata', methods=['POST'])
@auth.login_required
def login_data():
    # Extract data from the request
    data = request.json
    if not data:
        return jsonify({"error": "No data provided in request body"}), 400

    # Call the login service to handle login
    login_url = "http://localhost:5001/logindata"
    response = requests.post(login_url, json=data)

    # Check the response from the login service
    if response.status_code == 200:
        return jsonify({"message": "User logged in successfully"})
    elif response.status_code == 401:
        return jsonify({"error": "Invalid username or password"}), 401
    else:
        return jsonify({"error": "Failed to log in"}), 500


@app.route('/userdata', methods=['POST'])
@auth.login_required
def user_data():
    # Extract data from the request
    data = request.json
    if not data:
        return jsonify({"error": "No data provided in request body"}), 400

    # Call the login service to handle login
    user_url = "http://localhost:5001/userdata"
    response = requests.post(user_url, json=data)

    # Check the response from the login service
    if response.status_code == 200:
        # If the login service returns user data, return it
        user_data = response.json()  # Assuming the user data is returned as JSON
        return jsonify(user_data)
    elif response.status_code == 401:
        return jsonify({"error": "Unauthorized"}), 401  # Fix for unauthorized error
    else:
        return jsonify({"error": "Failed to retrieve user data"}), 500  # Fix for generic error




if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)

