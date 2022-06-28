import json
from flask import Blueprint, render_template, request


ul = Blueprint("user_login", __name__)


@ul.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "GET":
        return render_template("users/login.html")
    if request.method == "POST":
        return json.dumps({"name": 1})


@ul.route('/register', methods=["GET", "POST"])
def user_register():
    if request.method == "GET":
        return render_template("users/register.html")
    if request.method == "POST":
        return json.dumps({"name": 1})
