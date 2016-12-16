# -*- coding: utf-8 -*-

"""
app_test_usuario.py

Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)

Descrição: Implementa um app em Flask para testar as operações
           de CRUD em Usuários.
Atributos: usuarios - Tipo: Usuario[]
"""

from flask import Flask, render_template, request, redirect

from domain.modelo.usuario.usuario import Usuario
from .repositorio_usuario_em_memoria import RepositorioUsuarioEmMemoria
from domain.servicos_app.crud_usuario import ServicoCRUDUsuario

App = Flask(__name__)

#instanciando o adapter
repositorio_usuario = RepositorioUsuarioEmMemoria()

# Instanciando serviço hexagonal
crud_recurso = ServicoCRUDRecurso(repositorio_recurso)

@App.route("/admin/usuarios", methods=["GET"])
def index():
    return render_template("usuarios.html", recursos=crud_recurso.todos())

@App.route("/admin/usuarios/1", methods=["GET"])
def novo_recurso():
    return render_template("form_recurso.html", recurso=Recurso())

@App.route("/recursos", methods=["POST"])
def criar_recurso():
    recurso = crud_recurso.criar(request.form["nome"])
    return redirect("/")

