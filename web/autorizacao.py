from domain.usuario.nivel_acesso import *
from web.excecoes import ExcecaoNaoAutorizado
from functools import wraps
from flask import g

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
