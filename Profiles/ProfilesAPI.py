from flask import Blueprint, make_response, request, jsonify
import sys
sys.path.append("hw2/RHDEVS-AY2223-BE2-flask/")
from db import db

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:id>", methods = ["GET"])
def getProfile(id):
    if id > len(db) - 1:
        return make_response({"status": "error", "message": "no such ID"})
    else:
        profile = db[id]
        response = {"status": "success", "data": profile}
        return make_response(response)

@profiles_api.route("/profiles", methods = ["POST"])
def createProfile():
    data = {}
    newname = request.args.get('name')
    data['name'] = newname
    db.append(data)
    return make_response({"status": "success", "details": data})

@profiles_api.route("/<int:id>", methods = ["DELETE"])
def delProfile(id):
    if id > len(db) - 1:
        return make_response({"status": "error", "message": "no such ID"})
    else:
        del db[id]
        response = {"status": "success", "details": db}
        return make_response(response)

@profiles_api.route("/<int:id>/score", methods = ["GET"])
def getScore(id):
    if id > len(db) - 1:
        return make_response({"status": "error", "message": "no such ID"})
    else:
        minScore = request.args.get('minScore')
        if minScore == '':
            response = {"status": "success", "scores": db[id]['scores']}
            return make_response(response)
        else:
            filtered_scores = []
            for score in db[id]['scores']:
                if score > int(minScore):
                    filtered_scores.append(score)

            response = {"status": "success", "scores": filtered_scores}
            return make_response(response)