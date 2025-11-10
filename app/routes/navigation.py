from flask import Blueprint, render_template


bp = Blueprint("navigation", __name__)

@bp.route("/about", methods=["GET"])
def get_about():
    return render_template("about.html")

@bp.route("/homepage", methods=["GET"])
def get_homepage():
    return render_template("homepage.html")

@bp.route("/contact", methods=["GET"])
def get_contact():
    return render_template("contact.html")

@bp.route("/projects", methods=["GET"])
def get_projects():
    return render_template("projects.html")
