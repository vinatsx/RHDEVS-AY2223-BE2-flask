from flask import Blueprint, make_response, request, Flask
import sys
from db import db
from flask_cors import cross_origin
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:id>", methods = ["GET"])
@cross_origin(supports_credentials=True)
def getProfile(id):
    try:
        name = db[id]["name"]
        score = db[id]["scores"]
        data = {"name": name, "scores": score}
        response = {"status": "success", "data": data}
    except Exception as e:
        return {"err": "big error", "status": "failed"},500

    return make_response(response)


@profiles_api.route("/profiles", methods = ["POST"])
@cross_origin(supports_credentials=True)
def createProfile():
    try:
        formData = request.get_json()
        db.append(formData)
        response = {"status": "success", "updated_db": db}
    except Exception as e:
        return {"err": "big error u suck", "status": "failed"},500

    return make_response(response)


@profiles_api.route("/<int:id>", methods = ["DELETE"])
@cross_origin(supports_credentials=True)
def deleteProfile(id):
    try: 
        deleted_user = db[id]["name"]
        db.pop(id)
        response = {"status": "success", "deleted_user": deleted_user, "updated_db": db}
    except Exception as e:
        return {"err": "big fail", "status": "failed"},500

    return make_response(response)


@profiles_api.route("/<int:id>/score", methods = ["GET"])
@cross_origin(supports_credentials=True)
def getMinScore(id):
    try:
        formData = request.args
        min_score = formData['minScore']
        user_scores = db[id]['scores']
        if min_score is None:
            data = {"scores": user_scores}
        else:
            min_score = int(min_score)
            #list = []           i noob need visualise list comprehension
            #for i in user_scores:
                #if i > min_score:
                    #xs.append(i)
            above_min_score = [i for i in user_scores if i > min_score]
            data = {"scores": above_min_score}
        response = {"status": "success", "data": data}
    except Exception as e:
        return {"err": "im tired pls work", "status": "failed"},500

    return make_response(response)