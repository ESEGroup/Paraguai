from flask import Flask, render_template, request, redirect
from domain import ServicoCRUDRecurso, Recurso
from .RepositorioRecursoEmMemoria import RepositorioRecursoEmMemoria
App = Flask(__name__)

# Instanciando adapters
repositorio_recurso = RepositorioRecursoEmMemoria()

# Instanciando serviço hexagonal
crud_recurso = ServicoCRUDRecurso(repositorio_recurso)

# Criando menu
def gerarMenu():
    menu = [("Listar","/"),
            ("Criar Novo Recurso","/recursos/novo")]
    return [(label,url,url == request.url_rule.rule) for (label,url) in menu]

@App.route("/")
def index():
    return render_template("recursos.html", recursos=crud_recurso.todos(), menu=gerarMenu())

@App.route("/recursos/novo")
def novo_recurso():
    return render_template("form_recurso.html", recurso=Recurso(), menu=gerarMenu())

@App.route("/recursos", methods=["POST"])
def criar_recurso():
    recurso = crud_recurso.criar(request.form["nome"])
    return redirect("/")

