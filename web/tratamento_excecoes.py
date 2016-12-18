from flask import flash, redirect, url_for
from web.excecoes import *
from domain.excecoes import *

def registrar_capturas(app):
    @app.errorhandler(ExcecaoNaoAutenticado)
    def nao_autenticado(erro):
        flash("Você precisa estar logado para acessar essa página.")
        return redirect(url_for('sessoes.login'));