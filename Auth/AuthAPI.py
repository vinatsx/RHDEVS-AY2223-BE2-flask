# Score API here
from flask import Blueprint, request
import sys
from flask_cors import cross_origin
import jwt

sys.path.append("../")

auth_api = Blueprint("auth", __name__)


local = {}


@auth_api.route("/register", methods=["POST"])
@cross_origin(supports_credentials=True)
def register():
    try:
        username = request.args.get('username')
        password = request.args.get('password')
        local[username] = password
        return {'status': 'success'}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500
    

@auth_api.route("/login", methods=["POST"])
@cross_origin(supports_credentials=True)
def login():
    try:
        username = request.args.get('username')
        password_hash = request.args.get('passwordHash')
        if local.get(username) == None:
            return {"status": "failed", "err": "username and password does not match"}
        elif local[username] != password_hash:
            return {"status": "failed", "err": "username and password does not match"}
        else:
            key = 'secret'
            encoded = jwt.encode(local, key)
            return {"status": "success", "data": encoded}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500
