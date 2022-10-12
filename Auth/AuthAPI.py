from flask import Flask, request, make_response, Blueprint, current_app
from flask_cors import cross_origin
import sys
from db import db, creds
import jwt
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

@auth_api.route("/register", methods = ["POST"])
@cross_origin(supports_credentials=True)
def register():
  username = request.args.get("username")
  passwordHash = request.args.get("passwordHash")
  creds.append({"username" : username, "passwordHash" : passwordHash})
  return make_response({"status":"success", "data" : creds})

@auth_api.route("/login", methods = ["POST"])
@cross_origin(supports_credentials=True)
def login():
  username = request.args.get("username")
  passwordHash = request.args.get("passwordHash")
  if {"username" : username, "passwordHash" : passwordHash} in creds:
    token = jwt.encode({"username" : username,
                        "passwordHash" : passwordHash
                        }, current_app.config["SECRET_KEY"], algorithm="HS256")
    return make_response({"status" : "success", "token" : token})
  return make_response({"status" : "failed", "message" : "Username or password does not match"})