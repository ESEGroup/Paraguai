from flask import Flask, render_template, request, redirect, send_from_directory
from domain import ServicoCRUDRecurso, Recurso, TipoRecurso
from .RepositorioRecursoEmMemoria import RepositorioRecursoEmMemoria
from .FormulariosDeRecurso import FormulariosDeRecurso
App = Flask(__name__)

# Instanciando adapters
repositorio_recurso = RepositorioRecursoEmMemoria()

# Instanciando serviço hexagonal
crud_recurso = ServicoCRUDRecurso(repositorio_recurso)
form_recurso = FormulariosDeRecurso(repositorio_recurso)
# Criando menu
def gerarMenu():
    menu = [("Listar Recursos","/"),
            ("Buscar Recurso","/recursos/buscar/"),
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
# -----------------------------------------------
# Paginas Recurso
@App.route("/recursos/buscar/")
def lista_recurso():
    return render_template("form_buscar_recurso.html", tipos_recurso=[(tipo.nome,tipo.id) for tipo in crud_recurso.metadados["tipos"]], menu=gerarMenu())

# UC01 - Buscar Recurso
@App.route("/recursos/", methods=["GET"])
def resultado_busca_recurso():
    # try:
    (id, nome, tipo, intervalos, local) = form_recurso.busca(request.args)
    # except:
    #     # TODO - Mensagens de erro para busca
    #     return redirect("/recursos/buscar")
    return render_template("recursos.html", recursos=crud_recurso.buscar(id, nome, tipo, intervalos, local), menu=gerarMenu())

@App.route("/recursos/<id>")
def recurso(id):
    if not id:
        # TODO - Add 404
        return redirect("/recursos/buscar/")
    return render_template("recursos.html", recursos=crud_recurso.todos(), menu=gerarMenu())

@App.route("/admin/recursos/novo")
def novo_recurso():
    return render_template("form_recurso.html", tipos_recurso=[(tipo.nome,tipo.id) for tipo in crud_recurso.tipos()], recurso=Recurso(), menu=gerarMenu())

@App.route("/admin/recursos/novo", methods=["POST"])
def criar_recurso():
    recurso = crud_recurso.criar(request.form)
    return redirect("/")

# Adicionar verificação de permissão em algum ponto
@App.route("/admin/buscarUsuario")
def form_busca_usuario():
    return render_template("form_buscar_usuario.html", menu=gerarMenu(), departamento=[("DEL",1),("PESC",2),("IF",3)])

