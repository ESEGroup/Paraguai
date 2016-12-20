from flask import Blueprint, jsonify, current_app, request, g
from web.autorizacao import requer_acesso
from web.autenticacao import requer_usuario
from domain.recurso import DTOAgendamento, DTOIntervalo
from domain.usuario.nivel_acesso import *
from domain.iso8601 import to_iso
from domain.excecoes import *

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

def return_recurso(id):
    recurso = current_app.crud_recurso.obter(id)
    return jsonify({'recurso': recurso_to_dict(recurso)})

def erro(txt, code=400):
    response = jsonify({'erro': txt})
    response.status_code = code
    return response

@api.route("/recursos")
@requer_usuario
def listar_recurso():
    recursos = current_app.crud_recurso.listar()
    json = {
        'recursos': [recurso_to_dict(r) for r in recursos]
    }
    return jsonify(json)

@api.route("/recursos/<id>")
@requer_acesso(SistemaManutencao(), Administrador())
def obter_recurso(id):
    return return_recurso(int(id))

@api.route("/recursos/<id_recurso>/estado", methods=['POST'])
@requer_acesso(SistemaManutencao(), Administrador())
def alterar_estado(id_recurso):
    entrada = request.get_json()
    current_app.estado_recurso.alterar_estado(int(id_recurso), entrada['utilizavel'])
    return return_recurso(id_recurso)

@api.route("/recursos/<id_recurso>/agendamentos", methods=['POST'])
@requer_usuario
def agendar(id_recurso):
    id = int(id_recurso)
    entrada = request.get_json()
    try:
        dto = DTOAgendamento(
            idResponsavel = g.usuario.id,
            intervalo = DTOIntervalo(
                entrada['agendamento']['intervalo']['inicio'],
                entrada['agendamento']['intervalo']['fim']
            )
        )

        current_app.agendamento.agendar(id, dto)
        return return_recurso(id)

    except ExcecaoAgendamentoRecursoOcupado:
        return erro('Recurso não disponível para o intervalo desejado')

    except ExcecaoAgendamentoRecursoInutilizavel:
        return erro('Recurso está marcado como inutilizável')

    except KeyError:
        return erro('Formato de entrada inválido')

@api.route("/recursos/<id_recurso>/cancelar_agendamento", methods=['POST'])
@requer_usuario
def cancelar_agendamento(id_recurso):
    id = int(id_recurso)
    entrada = request.get_json()
    try:
        dto = DTOAgendamento(
            idResponsavel = int(entrada['agendamento']['idResponsavel']),
            intervalo = DTOIntervalo(
                entrada['agendamento']['intervalo']['inicio'],
                entrada['agendamento']['intervalo']['fim']
            )
        )

        if dto.idResponsavel != g.usuario.id and g.nivelAcesso != Administrador():
            raise ExcecaoNaoAutorizado

        current_app.agendamento.remover(id, dto)
        return return_recurso(id)

    except ExcecaoAgendamentoInexistente:
        return erro('Não existe agendamento igual ao especificado')

    except KeyError:
        return erro('Formato de entrada inválido')
