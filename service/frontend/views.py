from flask import Blueprint, render_template

blueprint = Blueprint("frontend", __name__)

@blueprint.route("/")
def index():
    return render_template("index.html")

@blueprint.route("/app.json")
def app_json():
    return {
        "name": "AOK Faucet",
        "icon": "https://faucet.aok.network/static/icon.png"
    }
