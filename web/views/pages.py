from flask import Blueprint, render_template
from web.autenticacao import requer_usuario

pages = Blueprint('pages', __name__)

@pages.route('/')
@requer_usuario
def index():
    return render_template("pages/index.html")
