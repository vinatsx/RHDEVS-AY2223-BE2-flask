from flask import Blueprint, make_response, request, current_app
import sys
from db import creds
from flask_cors import cross_origin
import jwt
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

@auth_api.route("/register", methods = ["POST"])
@cross_origin(supports_credentials=True)
def registerUser():
    try:
        formData = request.args
        username = formData.get('username')
        passwordHash = formData.get('passwordHash')
        data = {"username": username, "passwordHash": passwordHash}
        creds.append(data)
        response = {"status": "success", "user_info": data}
    except Exception as e:
        return {"err": "haha fail", "status": "failed"},500
    return make_response(response)


@auth_api.route("/login", methods = ["POST"])
@cross_origin(supports_credentials=True)
def login():
    try:
        formData = request.get_json()  # returns {"username":   , "passwordHash":   }
        if formData in creds:
            token = jwt.encode(formData, current_app.config["SECRET_KEY"], algorithm="HS256")
        response = {"status": "success", "message": "Login successful!", "token": token}
    except Exception as e:
        return {"err": "error", "status": "failed"},500
    return make_response(response)
