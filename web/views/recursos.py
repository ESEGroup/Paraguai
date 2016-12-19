from flask import Blueprint, render_template, current_app, request, url_for, redirect
from domain.recurso import Recurso, TipoRecurso, DTORecurso

view_recursos = Blueprint('recursos', __name__)

@view_recursos.route("/")
def index():
    recursos = current_app.crud_recurso.listar()
    print(recursos)
    return render_template("recursos/index.html", recursos=recursos)

@view_recursos.route("/novo")
def novo():
    tipos = [(tipo, tipo.capitalize()) for tipo in TipoRecurso.TIPOS]
    return render_template("recursos/novo.html", dto_recurso=DTORecurso(), tipos_recurso=tipos)

@view_recursos.route("/<id>")
def detalhes(id):
    return render_template("recursos/detalhes.html")

@view_recursos.route("/<id>/editar")
def editar(id):
    recurso = current_app.crud_recurso.obter(id)
    tipos = [(tipo, tipo.capitalize()) for tipo in TipoRecurso.TIPOS]
    dto = DTORecurso(recurso.nome, recurso.tipo.nome, recurso.local)
    return render_template("recursos/editar.html", dto_recurso=dto, tipos_recurso=tipos, id_recurso=id)

@view_recursos.route("/<id>", methods=["POST"])
def alterar(id):
    dto = DTORecurso(request.form["nome"], request.form["tipo"], request.form["local"])
    current_app.crud_recurso.alterar(id, dto)
    return redirect(url_for('recursos.index'))

@view_recursos.route("/", methods=["POST"])
def criar():
    dto = DTORecurso(request.form["nome"], request.form["tipo"], request.form["local"])
    current_app.crud_recurso.criar(dto)
    return redirect(url_for('recursos.index'))
