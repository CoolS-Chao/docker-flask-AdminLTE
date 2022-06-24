from flask import Blueprint, request


bg = Blueprint("blogs", __name__)


@bg.route("/api/<version>/blogs")
def operate_blogs():
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@bg.route("/api/<version_string>/blogs/<blog_id>")
def 
