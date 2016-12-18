from flask import Blueprint, render_template, current_app, request, url_for, redirect
from domain.usuario import Usuario, DTOUsuario, SenhaCriptografada

view_usuarios = Blueprint('usuarios', __name__)

@view_usuarios.route("/")
def index():
    usuarios = current_app.crud_usuario.listar()
    print(usuarios)
    return render_template("usuarios/index.html", usuarios=usuarios)

@view_usuarios.route("/novo")
def novo():
    return render_template("usuarios/novo.html", dto_usuario=DTOUsuario())

@view_usuarios.route("/<id_usuario>")
def detalhes(id_usuario):
    return render_template("usuarios/detalhes.html", id_usuario=id_usuario)

@view_usuarios.route("/<id_usuario>/editar")
def editar(id_usuario):
    usuario = current_app.crud_usuario.obter(id)

    #a senha do usuário está criptografada, não dá pra recuperar em texto
    #plano. Usando o digest para comparar
    dto = DTOUsuario(usuario.nome, usuario.email, None, usuario.nivelAcesso)
    digest = usuario.senhaCriptografada.digest	
    return render_template("usuarios/editar.html", id_usuario=id_usuario, dto_usuario=dto, digest=digest)

@view_usuarios.route("/<id_usuario>", methods=["POST"])
def alterar(id_usuario):
    dto = DTOUsuario(request.form["nome"], request.form["email"], request.form["senha"], request.form["nivelAcesso"])
    current_app.crud_usuario.alterar(id_usuario, dto)
    return redirect(url_for('recursos.index'))

@view_usuarios.route("/", methods=["POST"])
def criar():
    dto = DTOUsuario(request.form["nome"], request.form["email"], request.form["senha"], request.form["nivelAcesso"])
    current_app.crud_recurso.criar(dto)
    return redirect(url_for('recursos.index'))
