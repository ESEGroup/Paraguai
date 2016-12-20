from flask import Blueprint, render_template, current_app
from web.autenticacao import requer_usuario

pages = Blueprint('pages', __name__)

@pages.route('/')
@requer_usuario
def index():
    recursos_total = len(current_app.crud_recurso.listar())
    return render_template("pages/index.html", recursos_total=recursos_total)
