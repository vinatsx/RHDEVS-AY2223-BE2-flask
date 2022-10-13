from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db


# Write your flask code herepp
app = Flask(__name__)
app.config['SECRET_KEY'] = 'testsecretkey1'
app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

@app.route("/", methods = ["GET"])

def hello():
    return "hello"

if __name__ == "__main__":
    app.run()

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")