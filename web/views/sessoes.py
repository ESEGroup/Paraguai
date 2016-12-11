from flask import Blueprint, render_template

view_sessoes = Blueprint('sessoes', __name__)

@view_sessoes.route("/login")
def login():
    return render_template("sessoes/login.html")
