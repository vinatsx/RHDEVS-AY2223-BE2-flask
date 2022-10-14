from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import authSecretKey

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

app.config['SECRET_KEY'] = authSecretKey

@app.route("/", methods = ["GET"])
def WelcomeMessage():
    return "Welcome back to JCRORHSUA LAND"

if __name__ == "__main__":
    app.run("localhost", port = 3000)