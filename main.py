from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db


# Write your flask code here

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

@app.route("/homepage", methods=["GET"])
def hello():
    return "Welcome!"

if __name__ == "__main__": 
    app.debug = True
    app.run() 