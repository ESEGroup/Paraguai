from flask import Blueprint, jsonify, current_app, request
from web.autorizacao import requer_acesso
from domain.usuario.nivel_acesso import *
from domain.iso8601 import to_iso

api = Blueprint('api', __name__)

def recurso_to_dict(recurso):
    print(recurso.__dict__)
    return {
        'nome': recurso.nome,
        'categoria': recurso.tipo.nome,
        'utilizavel': recurso.utilizavel,
        'agendamentos': [agendamento_to_dict(a) for a in recurso.agendamentos]
    }

def agendamento_to_dict(agendamento):
    return {
        'idResponsavel': agendamento.idResponsavel,
        'intervalo': intervalo_to_dict(agendamento.intervalo)
    }

def intervalo_to_dict(intervalo):
    return {
        'inicio': to_iso(intervalo.inicio),
        'fim': to_iso(intervalo.inicio)
    }

@api.route("/recursos/<id>")
@requer_acesso(SistemaManutencao(), Administrador())
def obter_recurso(id):
    recursos = current_app.crud_recurso.listar()
    json = {
        'recursos': [recurso_to_dict(r) for r in recursos]
    }
    return jsonify(json)

@api.route("/recursos/<id_recurso>/estado", methods=['POST'])
@requer_acesso(SistemaManutencao(), Administrador())
def alterar_estado(id_recurso):
    entrada = request.get_json()
    current_app.estado_recurso.alterar_estado(int(id_recurso), entrada['utilizavel'])
    return jsonify({'status': 'ok'})
