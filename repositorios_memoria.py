# -*- coding: utf-8 -*-

from domain.usuario import RepositorioUsuario, IDUsuario

class RepositorioUsuarioEmMemoria(RepositorioUsuario):
    """Essa classe modela um Repositório de Usuários em memória, para 
    armazenamento temporário e uso em mock tests.
    :param usuarios: Lista de Usuários armazenados (Usuario[])."""

    def __init__(self):
        self.usuarios = []

    def criar(self, usuario):
        novo_id = len(self.usuarios) + 1
        usuario.id = IDUsuario(novo_id)
        self.usuarios.append(usuario)

        return usuario


    def alterar(self, _id, usuario):
        usuarios[_id] = usuario
        return usuario


    def obter(self, _id):
        return usuarios[_id]


    def listar(self):
        return self.usuarios

        del self.usuarios[_id]
        return True
