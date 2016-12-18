from domain.usuario.nivel_acesso import *
from web.excecoes import ExcesaoNaoAutorizado, ExcesaoNaoAutenticado
from functools import wraps
from flask import g, session, current_app

def carregar_usuario(f):
    @wraps(f)
    def decorado(*args, **kwargs):
        concessao = session.get('concessao')
        if concessao:
            g.usuario = current_app.autenticacao.usuario(concessao)
            g.nivelAcesso = current_app.autenticacao.nivel(concessao)
        else:
            g.usuario = None
            g.nivelAcesso = None
        return f(*args, **kwargs)
    return decorado

def requer_usuario(f):
    @wraps(f)
    def decorado(*args, **kwargs):
        concessao = session.get('concessao')
        if not g.usuario:
            raise ExcecaoNaoAutenticado
        return f(*args, **kwargs)
    return carregar_usuario(decorado)

def requer_acesso(niveis=[]):
    niveis = set(niveis)
    niveis.add(Administrador())

    def decorador(f):
        @wraps(f)
        def decorado(*args, **kwargs):
            if g.nivelAcesso not in niveis:
                raise ExcecaoNaoAutorizado
            return f(*args, **kwargs)
        return carregar_usuario(decorado)
    return decorador
