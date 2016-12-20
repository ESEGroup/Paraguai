from flask import session, current_app, g, request
from functools import wraps
from web.excecoes import ExcecaoNaoAutenticado
from domain.usuario.nivel_acesso import Administrador

def registrar_precarregar_usuario(app):
    def get_usuario():
        id_usuario = session.get('id_usuario')
        if id_usuario:
            return current_app.repositorio_usuario.obter(id_usuario)

        try:
            id = int(request.args.get('authId'))
            pw = str(request.args.get('authToken'))
            print(id, pw)
            return current_app.autenticacao.autenticar_por_id(id, pw)
        except:
            return None

    @app.before_request
    def precarregar_usuario():
        usuario = get_usuario()

        if usuario:
            g.usuario = usuario
            g.nivelAcesso = usuario.nivelAcesso
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
