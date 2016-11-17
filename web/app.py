from flask import Flask, render_template, request, redirect, send_from_directory
from domain import ServicoCRUDRecurso, Recurso, TipoRecurso
from .RepositorioRecursoEmMemoria import RepositorioRecursoEmMemoria
App = Flask(__name__)

# Instanciando adapters
repositorio_recurso = RepositorioRecursoEmMemoria()

# Instanciando serviço hexagonal
crud_recurso = ServicoCRUDRecurso(repositorio_recurso)

# Criando menu
def gerarMenu():
    menu = [("Listar Recursos","/"),
            ("Buscar Recurso","/recursos/buscar"),
            ("Criar Novo Recurso","/recursos/novo")]
    return [(label,url,url == request.url_rule.rule) for (label,url) in menu]

@App.route("/")
def index():
    return render_template("recursos.html", recursos=crud_recurso.todos(), menu=gerarMenu())

@App.route("/css/<path>")
def serve_stylesheet(path):
    return send_from_directory("./css",path)

@App.route("/js/<path>")
def serve_script(path):
    return send_from_directory("./js",path)

@App.route("/recursos/listar")
def lista_recurso():
    return render_template("recursos.html", recursos=crud_recurso.todos(), menu=gerarMenu())

@App.route("/recursos/listar", methods=["POST"])
def lista_busca_recurso():
    return render_template("recursos.html", recursos=crud_recurso.todos(), menu=gerarMenu())

@App.route("/recursos/novo")
def novo_recurso():
    return render_template("form_recurso.html", tipos_recurso=[(tipo.nome,tipo.id) for tipo in crud_recurso.tipos()], recurso=Recurso(), menu=gerarMenu())

@App.route("/recursos/buscar")
def form_busca_recurso():
    return render_template("form_buscar_recurso.html", tipos_recurso=[(tipo.nome,tipo.id) for tipo in crud_recurso.tipos()], menu=gerarMenu())

@App.route("/recursos/buscar/", methods=["POST"])
def form_busca_recurso_por_id():
    # TODO - Melhore-me
    if not request.form["id-recurso"]:
        return redirect("/")
    return redirect("/recurso/" + request.form["id-recurso"])

@App.route("/recurso/<id>")
def recurso(id):
    if not id:
        # TODO - Add 404
        return redirect("/recursos/buscar/")
    return render_template("recursos.html", recursos=crud_recurso.todos(), menu=gerarMenu())

@App.route("/recursos", methods=["POST"])
def criar_recurso():
    recurso = crud_recurso.criar(request.form)
    return redirect("/")

