from flask import Blueprint, render_template, current_app, request, url_for, redirect
from domain import Recurso

view_recursos = Blueprint('recursos', __name__, template_folder='templates')

@view_recursos.route("/")
def index():
    recursos = current_app.crud_recurso.todos()
    return render_template("recursos/index.html", recursos=recursos)

@view_recursos.route("/novo")
def novo_recurso():
    return render_template("recursos/form.html", recurso=Recurso())

@view_recursos.route("/", methods=["POST"])
def criar_recurso():
    current_app.crud_recurso.criar(request.form["nome"])
    return redirect(url_for('recursos.index'))
