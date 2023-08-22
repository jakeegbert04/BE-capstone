from flask import  Blueprint
from controllers import auth_controller

auth = Blueprint("auth", __name__)

@auth.route("/user/auth", methods=["Post"])
def auth_token_add():
    return auth_controller.auth_token_add()