from flask import Blueprint, render_template, current_app, request, url_for, redirect
from domain.usuario import Usuario, DTOUsuario
from domain.usuario.nivel_acesso import *
from web.autenticacao import requer_usuario
from web.autorizacao import requer_acesso

view_usuarios = Blueprint('usuarios', __name__)

niveisAcesso = [
    (0, "Usuário Comum"),
    (2, "Administrador")
]

def nivelAcessoToStr(nivel):
    if nivel == Administrador():
        return "Administrador"
    if nivel == UsuarioComum():
        return "Usuário Comum"

@view_usuarios.route("/")
@requer_usuario
@requer_acesso(Administrador())
def index():
    usuarios = current_app.crud_usuario.listar()
    usuarios = [u for u in usuarios if u.nivelAcesso != SistemaManutencao()]
    usuarios = [{
        'id': u.id,
        'nome': u.nome,
        'email': u.email,
        'nivel': nivelAcessoToStr(u.nivelAcesso)
    } for u in usuarios]
    return render_template("usuarios/index.html", usuarios=usuarios)

@view_usuarios.route("/novo")
@requer_usuario
@requer_acesso(Administrador())
def novo():
    return render_template("usuarios/novo.html", dto_usuario=DTOUsuario(), niveisAcesso=niveisAcesso)


@view_usuarios.route("/<id_usuario>/editar")
@requer_usuario
@requer_acesso(Administrador())
def editar(id_usuario):
    usuario = current_app.crud_usuario.obter(int(id_usuario))
    dto = DTOUsuario(usuario.nome, usuario.email, None, None)

    return render_template("usuarios/editar.html", id_usuario=id_usuario, dto_usuario=dto, niveisAcesso=niveisAcesso)

@view_usuarios.route("/<id_usuario>", methods=["POST"])
@requer_usuario
@requer_acesso(Administrador())
def alterar(id_usuario):
    dto = DTOUsuario(request.form["nome"], request.form["email"], request.form["senha"], int(request.form["nivelAcesso"]))
    current_app.crud_usuario.alterar(int(id_usuario), dto)

    return redirect(url_for('usuarios.index'))

@view_usuarios.route("/", methods=["POST"])
@requer_usuario
@requer_acesso(Administrador())
def criar():
    dto = DTOUsuario(request.form["nome"], request.form["email"], request.form["senha"], int(request.form["nivelAcesso"]))
    current_app.crud_usuario.criar(dto)
    return redirect(url_for('usuarios.index'))

@view_usuarios.route("/<id_usuario>/remover")
@requer_usuario
@requer_acesso(Administrador())
def remover(id_usuario):
    usuario = current_app.crud_usuario.remover(int(id_usuario))
    return redirect(url_for('usuarios.index'))
