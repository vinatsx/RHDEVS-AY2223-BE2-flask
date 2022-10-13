from os import remove
from flask import Blueprint, request, make_response
from flask_cors import cross_origin
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:id>", methods = ["GET"])
@cross_origin(supports_credentials=True)

def get_name(id):
    if id > len(db) - 1:
        return make_response({"status":"error", "message":"no such id"})
    else:
        data = db[id]
        response = {"status":"success", "data":data}
        return make_response(response)



@profiles_api.route("/profiles", methods = ["POST"])
@cross_origin(supports_credentials=True)

def newprof():
    data = {}
    new_name = request.args.get('name')
    data['name']= new_name
    db.append(data)
    return make_response({"status":"success", "details":data})



@profiles_api.route("/<int:id>", methods = ["DELETE"])
@cross_origin(supports_credentials=True)

def delete_prof(id):
    if id > len(db) - 1:
        return make_response({"status":"error", "message":"no such id"})
    else:
        db.remove(db[id])
        response = {"status":"success", "data":db}
        return make_response(response)



@profiles_api.route("/<int:id>/score", methods = ["GET"])
@cross_origin(supports_credentials=True)
def get_min_score(id):
    data = []
    if id > len(db) - 1:
        return make_response({"status":"error", "message":"no such id"})
    minscore = request.args.get('minScore')
    if minscore == "" or minscore is None:
        minscore = 0
    else:
        c = int(minscore)
    for x in db[id]["scores"]:
        if x > c:
            data.append(x)
    response = {"status":"success", "data":data}
    return make_response(response)