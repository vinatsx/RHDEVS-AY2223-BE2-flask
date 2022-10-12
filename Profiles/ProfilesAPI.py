from flask import Flask, request, make_response, Blueprint
from flask_cors import cross_origin
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:id>", methods = ["GET"])
@cross_origin(supports_credentials=True)
def getProfile(id):
  if id > len(db) - 1:
    return make_response({"status" : "failed", "message" : "Profile does not exist"})
  return make_response({"status" : "success", "data" : db[id]})

@profiles_api.route("/profiles", methods = ["POST"])
@cross_origin(supports_credentials=True)
def newProfile():
  name = request.args.get('name')
  db.append({"name" : name})
  return make_response({"status" : "success", "data" : db})

@profiles_api.route("/<int:id>", methods = ["DELETE"])
@cross_origin(supports_credentials=True)
def deleteProfile(id):
  if id > len(db) - 1:
    return make_response({"status" : "failed", "message" : "Profile does not exist"})
  db.remove(db[id])
  return make_response({"status" : "success", "data" : db})

@profiles_api.route("/<int:id>/score", methods = ["GET"])
@cross_origin(supports_credentials=True)
def getScore(id):
  data = []
  rawMinScore = request.args.get('minScore')
  if rawMinScore == "" or rawMinScore is None:
    minScore = 0
  else:
    minScore = int(request.args.get('minScore'))
  for score in db[id]["scores"]:
    if score > minScore:
      data.append(score)
  return make_response({"status" : "success", "data" : data})