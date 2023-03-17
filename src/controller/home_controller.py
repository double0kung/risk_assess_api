from flask import Blueprint

home = Blueprint('home', __name__, url_prefix="/")

@home.get("/")
def get_home_page():
    return { "message": "Welcome to Risk Assess App"}