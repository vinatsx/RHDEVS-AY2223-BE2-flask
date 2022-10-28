from flask import Blueprint, make_response, request, jsonify, current_app
import sys
sys.path.append("hw2/RHDEVS-AY2223-BE2-flask/")
from db import db, creds
import jwt

auth_api = Blueprint("auth", __name__)

@auth_api.route("/register", methods = ["POST"])
def registerUser():
    username = request.args.get('username')
    passwordHash = request.args.get('passwordHash')

    if (username == '') or (passwordHash == ''):
        return make_response({"status": "error", "message": "Username or password is empty."})
    else:
        user = {"username": username, "passwordHash": passwordHash}
        creds.append(user)
        return make_response({"status": "success", "message": "User registered"})

@auth_api.route("/login", methods = ["POST"])
def login():
    username = request.args.get('username')
    passwordHash = request.args.get('passwordHash')
    user = {"username": username, "passwordHash": passwordHash}

    if user in creds:
        token = jwt.encode({"username": username, "passwordHash": passwordHash},
                            "SECRET_KEY", algorithm = "HS256")
        return make_response({"status": "success", "token": token})
    else:
        return make_response({"status": "error", "message": "User does not exist."})
