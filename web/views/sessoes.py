from flask import Blueprint, render_template, current_app, request, flash, session, redirect, url_for

view_sessoes = Blueprint('sessoes', __name__)

@view_sessoes.route("/login")
def login():
    return render_template("sessoes/login.html")

@view_sessoes.route("/login", methods=["POST"])
def autenticar():
    usuario = current_app.autenticacao.autenticar(request.form['email'], request.form['senha'])

    if usuario:
        session['id_usuario'] = usuario.id
        flash('Autenticação bem sucedida')
        return redirect(url_for('pages.index'))
    else:
        flash('Usuário ou Senha Inválidos')
        return "Invalido"
        return redirect(url_for('sessoes.login'))

@view_sessoes.route("/logout")
def logout():
    session.pop('id_usuario', None)
    return redirect(url_for('sessoes.login'))
