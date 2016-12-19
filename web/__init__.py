from flask import Flask
from domain.recurso import ServicoCRUDRecurso
from domain.usuario import ServicoCRUDUsuario
from domain.autenticacao import ServicoAutenticacao
from repositorios_memoria.recurso import RepositorioRecursoEmMemoria
from repositorios_memoria.usuario import RepositorioUsuarioEmMemoria
from web.mocks import recursos, usuarios
from web.tratamento_excecoes import registrar_capturas
from web.autenticacao import registrar_precarregar_usuario
from web.email import ServicoEmailConsole
from web.email.formatadores import FORMATADORES_PADRAO

def create_app():
    app = Flask(__name__)
    registrar_capturas(app)
    registrar_precarregar_usuario(app)

    app.secret_key = 'notthatsecret'

    # Instanciando adapters
    app.repositorio_recurso = RepositorioRecursoEmMemoria(recursos)
    app.repositorio_usuario = RepositorioUsuarioEmMemoria(usuarios)
    app.servico_email = ServicoEmailConsole(FORMATADORES_PADRAO)

    # Instanciando serviço hexagonal
    app.crud_recurso = ServicoCRUDRecurso(app.repositorio_recurso)
    app.crud_usuario = ServicoCRUDUsuario(app.repositorio_usuario,app.servico_email)

    # Instanciando serviço de autenticacao

    app.autenticacao = ServicoAutenticacao(app.repositorio_usuario)

    from web.views.pages import pages
    app.register_blueprint(pages)

    from web.views.recursos import view_recursos
    app.register_blueprint(view_recursos, url_prefix="/recursos")

    from web.views.usuarios import view_usuarios
    app.register_blueprint(view_usuarios, url_prefix="/usuarios")

    from web.views.assets import assets
    app.register_blueprint(assets, url_prefix="/public")

    from web.views.sessoes import view_sessoes
    app.register_blueprint(view_sessoes)

    return app
