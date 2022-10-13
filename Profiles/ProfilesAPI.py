import profile
from urllib import response
from flask import Blueprint, make_response, request
from flask_cors import cross_origin
import sys
from db import db

sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:id>", methods=["GET"])
@cross_origin(supports_credentials=True)
def getUserInfo(id):
    data = db[id]
    response = {"status": "success", "data": data}

    return make_response(response)

@profiles_api.route("/profiles", methods=["POST"])
@cross_origin(supports_credentials=True)
def createProfile():
    data = request.args
    db.append(data)
    response = {"status": "success"}

    return make_response(response)

@profiles_api.route("/<int:id>", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def deleteProfile(id):
    del db[id]
    response = {"status": "success"}

    return make_response(response)

@profiles_api.route("<int:id>/score", methods=["GET"])
@cross_origin(supports_credentials=True)
def getMinScore(id):
    minScore = request.args.get("minScore")
    if minScore is None: 
        data = {"scores": db[id]["scores"]}
    else:
        minScore = int(minScore)
        data = {"scores": [score for score in db[id]["scores"] if score > minScore]}
    
    response = {"status": "success", "data": data}

    return make_response(response)
