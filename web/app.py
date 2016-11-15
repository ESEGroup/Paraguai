from flask import Flask, render_template, request, redirect
from domain import ServicoCRUDRecurso, Recurso
from .RepositorioRecursoEmMemoria import RepositorioRecursoEmMemoria
App = Flask(__name__)

# Instanciando adapters
repositorio_recurso = RepositorioRecursoEmMemoria()

# Instanciando serviço hexagonal
crud_recurso = ServicoCRUDRecurso(repositorio_recurso)

@App.route("/")
def index():
    return render_template("recursos.html", recursos=crud_recurso.todos())

@App.route("/recursos/novo")
def novo_recurso():
    return render_template("form_recurso.html", recurso=Recurso())

@App.route("/recursos", methods=["POST"])
def criar_recurso():
    recurso = crud_recurso.criar(request.form["nome"])
    return redirect("/")

