from flask import Blueprint, render_template

view_usuarios = Blueprint('usuarios', __name__)

@view_usuarios.route("/")
def index():
    return render_template("usuarios/index.html")

@view_usuarios.route("/novo")
def novo():
    return render_template("usuarios/form.html")

@view_usuarios.route("/<id_usuario>")
def detalhes(id_usuario):
    return render_template("usuarios/detalhes.html")
