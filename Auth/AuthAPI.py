from urllib import request
from flask import Blueprint, jsonify
from flask import Flask, request, make_response, current_app 
from flask_cors import cross_origin
import sys
from db import db, creds
import jwt
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

@auth_api.route('/register', methods = ["POST"])
def reg():

    def details(arg):
        username = arg.get('username')
        hashedpw = arg.get('pwhashed')

        if (username == '') or (hashedpw == ''):
            return jsonify({"Status" : "Failed" , "Message" : "Username or Password is not available"})
        else:
            creds.append({"username":username, "passwordHash":hashedpw})
            return jsonify({"Status" : "Success" , "Message" : "Registered"})

    if request.args.get('username'):
        return details(request.args)

    elif request.form.get('username'):
        return details(request.form)

    

@auth_api.route('/login', methods = ["POST"])
def login():

    def logindetails(argsform):
        username = argsform.get('username')
        hashedPassword = argsform.get('passwordHash')
        return username, hashedPassword

    if request.args.get('username'):
        det = logindetails(request.args)

    elif request.form.get('username'):
         det = logindetails(request.form)

    username = det[0]
    hashedPassword = det[1]

    checkuser = {"username":username, "passwordHash":hashedPassword} 
    if checkuser in creds:
        token = jwt.encode({'userID': username,
                            'passwordHash': hashedPassword
                            }, current_app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'Status':'Success', 'token': token})
    
    return jsonify({"Status" : "Failed" , "Message" : "Username or Password does not match"})






