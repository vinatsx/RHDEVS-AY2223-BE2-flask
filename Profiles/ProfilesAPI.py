from flask import Blueprint, make_response, request
import sys
from db import db
from flask_cors import cross_origin

sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)


@profiles_api.route("/<int:id>", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_profile(id):
    try:
        data = {'name': db[id]['name'], 'scores': db[id]['scores']}
        response = {'status': 'success', 'data': data}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500

    return make_response(response)


@profiles_api.route("/profiles", methods=["POST"])
@cross_origin(supports_credentials=True)
def create_new_profile():
    try:
        data = request.get_json()
        db.append(data)
        response = {'status': 'success'}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500

    return make_response(response)


@profiles_api.route("/<int:id>", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_profile(id):
    try:
        id = int(id)
        deleted = db[id]
        new_db = [profile for profile in db if profile != deleted]
        response = {'deleted': deleted, 'new_db': new_db, 'status': 'success'}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500

    return make_response(response)


@profiles_api.route("/<int:id>/score", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_min_score(id):
    try:
        minScore = request.args.get('minScore')
        if minScore is None:
            data = {'scores': db[id]['scores']}
        else:
            minScore = int(minScore)
            data = {'scores': [score for score in db[id]['scores'] if score > minScore]}
        response = {'status': 'success', 'data': data}
    except Exception as e:
        return {"err": "An error has occured", "status": " failed"}, 500

    return make_response(response)
