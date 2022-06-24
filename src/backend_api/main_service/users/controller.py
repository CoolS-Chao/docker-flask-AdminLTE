from flask import Blueprint, request


user = Blueprint("user_login", __name__)


@user.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass
