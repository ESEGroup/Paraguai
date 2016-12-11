from flask import Flask
from domain import ServicoCRUDRecurso
from web.repositorios.recurso import RepositorioRecursoEmMemoria

def create_app():
    app = Flask(__name__)

    # Instanciando adapters
    app.repositorio_recurso = RepositorioRecursoEmMemoria()

    # Instanciando serviço hexagonal
    app.crud_recurso = ServicoCRUDRecurso(app.repositorio_recurso)

    from web.views.recursos import view_recursos
    app.register_blueprint(view_recursos, url_prefix="/recursos")

    from web.views.usuarios import view_usuarios
    app.register_blueprint(view_usuarios, url_prefix="/usuarios")

    from web.views.sessoes import view_sessoes
    app.register_blueprint(view_sessoes)

    return app
