from re import U
from threading import local
from flask import Blueprint, request, make_response
from flask_cors import cross_origin
import sys
from db import db

sys.path.append("../")

auth_api = Blueprint("auth", __name__)

local_array = {}

@auth_api.route("/register", methods=["POST"])
@cross_origin(supports_credentials=True)
def registerUser():
    username = request.args.get("username")
    hashedPassword = request.args.get("hashedPassword")
    local_array[username] = hashedPassword

    response = {"status": "success"}

    return make_response(response)

@auth_api.route("/login", methods=["POST"])
def loginUser():
    username = request.args.get("username")
    hashedPassword = request.args.get("hashedPassword")

    if local_array[username] == hashedPassword:
        response = {"status": "successful login"}
    else:
        response = {"status": "failed", "error": "username and password do not match!"}

    return make_response(response)