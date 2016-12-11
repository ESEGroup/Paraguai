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
    app.register_blueprint(view_recursos, url_prefix='/recursos')

    return app
