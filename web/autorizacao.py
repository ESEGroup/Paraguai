from domain.usuario.nivel_acesso import *
from web.excecoes import ExcecaoNaoAutorizado
from functools import wraps
from flask import g

def requer_acesso(*niveis):
    def decorador(f):
        @wraps(f)
        def decorado(*args, **kwargs):
            if g.nivelAcesso not in niveis:
                raise ExcecaoNaoAutorizado
            return f(*args, **kwargs)
        return decorado
    return decorador
