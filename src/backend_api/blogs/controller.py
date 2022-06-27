from flask import Blueprint, request, render_template


bg = Blueprint("blogs", __name__)


@bg.route("/blogs/<blog_id>", methods=["GET", "POST"])
def operate_blogs(blog_id):
    if request.method == "GET":
        if not isinstance(blog_id, int):
            
        print(blog_id)
        return blog_id
        # return render_template("tem÷plates/blog_editor/")
    if request.method == "POST":
        pass


# @bg.route("/blogs/<blog_id>")
# def 
