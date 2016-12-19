import json
from flask import Blueprint, render_template, current_app, request, session, url_for, redirect, g
from domain.recurso import Recurso, TipoRecurso, DTORecurso, DTOBuscaRecurso
from domain.iso8601 import to_iso
from domain.usuario.nivel_acesso import Administrador
from ..excecoes import ExcecaoParaguaiWeb

view_recursos = Blueprint('recursos', __name__)

def agendamentos_to_cal(list_agendamentos, userID = None):
    dict_agenda = [
    {
        "title" : current_app.crud_usuario.obter(int(agendamento.idResponsavel)).nome,
        "start" : to_iso(agendamento.intervalo.inicio).replace("Z","",1),
        "end" : to_iso(agendamento.intervalo.fim).replace("Z","",1),
        "editable" : bool(
            (g.nivelAcesso == Administrador()) or
            (agendamento.idResponsavel == userID)
        )
    }
    for agendamento in list_agendamentos
    ]
    return json.dumps(dict_agenda)

def validar_datepicker(data_str):
    if not data_str:
        return
    string_proc = data_str.strip().replace(" ","T",1) + ":00Z"
    try:
        from_iso(string_proc)
    except ValueError:
        raise ExcecaoParaguaiWeb("Data com formato inválido!")
    return string_proc

@view_recursos.route("/")
def index():
    recursos = current_app.crud_recurso.listar()
    print(recursos)
    return render_template("recursos/index.html", recursos=recursos)

@view_recursos.route("/buscar")
def pagina_busca():
    tipos = [(tipo, tipo.capitalize()) for tipo in TipoRecurso.TIPOS]
    return render_template("recursos/buscar.html", dto_recurso=DTORecurso(), tipos_recurso=tipos)

@view_recursos.route("/buscar", methods=["POST"])
def buscar():
    dto = DTOBuscaRecurso(request.form["nome"], request.form["tipo"], request.form["local"])
    intervalo = (validar_datepicker(request.form["start"]),
                 validar_datepicker(request.form["end"]))
    if not None in intervalo:
        dto.intervalos.append(intervalo)
    recursos = current_app.crud_recurso.buscar(dto)
    return render_template("recursos/index.html", recursos=recursos)

@view_recursos.route("/novo")
def novo():
    tipos = [(tipo, tipo.capitalize()) for tipo in TipoRecurso.TIPOS]
    return render_template("recursos/novo.html", dto_recurso=DTORecurso(), tipos_recurso=tipos)

@view_recursos.route("/<id>")
def detalhes(id):
    recurso = current_app.crud_recurso.obter(int(id))
    agendamentos = agendamentos_to_cal(recurso.agendamentos, session["id_usuario"])
    print(agendamentos)
    return render_template("recursos/detalhes.html", agendamentos = agendamentos, recurso = recurso)

@view_recursos.route("/<id>/editar")
def editar(id):
    recurso = current_app.crud_recurso.obter(int(id))
    tipos = [(tipo, tipo.capitalize()) for tipo in TipoRecurso.TIPOS]
    dto = DTORecurso(recurso.nome, recurso.tipo.nome, recurso.local)
    return render_template("recursos/editar.html", dto_recurso=dto, tipos_recurso=tipos, id_recurso=id)

@view_recursos.route("/<id>", methods=["POST"])
def alterar(id):
    dto = DTORecurso(request.form["nome"], request.form["tipo"], request.form["local"])
    current_app.crud_recurso.alterar(int(id), dto)
    return redirect(url_for('recursos.index'))

@view_recursos.route("/", methods=["POST"])
def criar():
    dto = DTORecurso(request.form["nome"], request.form["tipo"], request.form["local"])
    current_app.crud_recurso.criar(dto)
    return redirect(url_for('recursos.index'))
