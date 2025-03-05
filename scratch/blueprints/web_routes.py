from flask_smorest import Blueprint
from flask import render_template

web_bp = Blueprint("web_bp", __name__, template_folder="../templates")

@web_bp.route("/")
def home():
    return render_template("index.html", title="HELLO!")
