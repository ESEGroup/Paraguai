from flask import session, current_app, g
from functools import wraps
from web.excecoes import ExcecaoNaoAutenticado
from domain.usuario.nivel_acesso import Administrador

def registrar_precarregar_usuario(app):
    @app.before_request
    def precarregar_usuario():
        concessao = session.get('concessao')
        if concessao:
            g.usuario = current_app.autenticacao.usuario(concessao)
            g.nivelAcesso = current_app.autenticacao.nivel(concessao)
            g.admin = g.nivelAcesso == Administrador()
        else:
            g.usuario = None
            g.nivelAcesso = None
            g.admin = False

def requer_usuario(f):
    """Decorador que levanta uma exceção caso o usuário não esteja logado"""
    @wraps(f)
    def decorado(*args, **kwargs):
        concessao = session.get('concessao')
        if not g.usuario:
            raise ExcecaoNaoAutenticado
        return f(*args, **kwargs)
    return decorado
