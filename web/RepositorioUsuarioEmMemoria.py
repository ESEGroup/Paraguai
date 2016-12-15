# -*- coding: utf-8 -*-

"""
RepositorioUsuarioEmMemoria.py

Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)

Descrição: Implementa a classe RepositorioUsuarioEmMemoria.
           Essa classe modela um Repositório de Usuários em memória,
           para armazenamento temporário e uso em mock tests.

Atributos: usuarios - Tipo: Usuario[]
"""

from domain.modelo.usuario.repositorio_usuario import RepositorioUsuario
import domain.modelo.usuario.usuario import Usuario

class RepositorioUsuarioEmMemoria(RepositorioUsuario):
    """Essa classe modela um Repositório de Usuários em memória, para 
    armazenamento temporário e uso em mock tests.
    :param usuarios: Lista de Usuários armazenados (Usuario[])."""

    def __init__(self):

        self.usuarios = []


    def criar(self, usuario):

        _id = len(self.usuarios) + 1

        usuario = Usuario(dados.nome, dados.email, 1, dados.senha, _id)       
        self.usuarios.append(usuario)

        return usuario


    def alterar(self, _id, usuario):

        _id = len(self.usuarios) + 1

        usuario = Usuario(dados.nome, dados.email, 1, dados.senha, _id)       
        self.usuarios.append(usuario)

        return usuario


    def obter(self, _id):

        return usuarios[_id]


    def listar(self):

        return self.usuarios
