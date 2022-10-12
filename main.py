from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db, AUTH_SECRET_KEY

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")
app.config['SECRET_KEY'] = AUTH_SECRET_KEY

@app.route("/", methods = ["GET"])
def hello():
  return "hello"

if __name__ == "__main__":
  app.run("localhost", port = 8080)