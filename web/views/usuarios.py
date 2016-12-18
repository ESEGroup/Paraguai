from flask import Blueprint, render_template, current_app, request, url_for, redirect
from domain.usuario import Usuario, DTOUsuario

view_usuarios = Blueprint('usuarios', __name__)

@view_usuarios.route("/")
def index():
    usuarios = current_app.crud_usuario.listar()
    print(usuarios)
    return render_template("usuarios/index.html", usuarios=usuarios)

@view_usuarios.route("/novo")
def novo():
    return render_template("usuarios/form.html")

@view_usuarios.route("/<id_usuario>")
def detalhes(id_usuario):
    return render_template("usuarios/detalhes.html")


@view_usuarios.route("/showdetalhes")
def showdetalhes():
    return render_template("usuarios/detalhes.html")

@view_usuarios.route("/<id_usuario>/editar")
def editar(id_usuario):
    return render_template("usuarios/detalhes.html")
