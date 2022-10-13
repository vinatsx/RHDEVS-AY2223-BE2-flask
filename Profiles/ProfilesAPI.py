# Profile API here
from flask import Blueprint, make_response, request
import sys
from db import db #importing db variable from db file
from flask_cors import cross_origin
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)


@profiles_api.route("/<int:id>", methods = ["GET"])
@cross_origin(supports_credentials=True)
def get_profile(id):
    try:
        data = {"name":db[id]['name'], "scores":db[id]['scores']}
        response ={"status":"success","data":data}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500
    
    return make_response(response)


@profiles_api.route("/profiles", methods = ["POST"])
@cross_origin(supports_credentials=True)
def create_new_profile():
    try:
        name = request.get_json()
        db.append(name)
        response = {'status': 'success'}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500

    return make_response(response)


@profiles_api.route("/<int:id>", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_profile(id):
    try:
        deleted = db[id]
        new_db = db.pop(id)
        response = {'deleted': deleted, 'new_db': new_db, 'status': 'success'}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500

    return make_response(response)   



@profiles_api.route("/<int:id>/score", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_min_score(id):
    try:
        minScore = request.args.get('minScore')    #request.args returns a "dictionary" object for you, score?minScore=3 so request.arg converts the url into  a dict object and looks for the ? sign which indicates a paramter
        if minScore is None:
            data = {'scores': db[id]['scores']}
        else:
            minScore = int(minScore)
            data = {'scores': [score for score in db[id]['scores'] if score > minScore]}
        response = {'status': 'success', 'data': data}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500

    return make_response(response)


