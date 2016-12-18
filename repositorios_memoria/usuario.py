# -*- coding: utf-8 -*-

from domain.usuario import RepositorioUsuario, IDUsuario

class RepositorioUsuarioEmMemoria(RepositorioUsuario):
    """Essa classe modela um Repositório de Usuários em memória, para 
    armazenamento temporário e uso em mock tests.
    :param usuarios: Lista de Usuários armazenados (Usuario[])."""

    def __init__(self, usuarios=[]):
        self.usuarios = usuarios

    def criar(self, usuario):
        novo_id = len(self.usuarios) + 1
        usuario.id = IDUsuario(novo_id)
        self.usuarios.append(usuario)

        return usuario


    def alterar(self, _id, usuario):
        id = _id.id-1
        self.usuarios[id] = usuario
        return usuario


    def obter(self, _id):
        try:
            return self.usuarios[_id.id-1]
        except IndexError:
            return None

    def obter_por_email(self, email):
        try:
            return list(filter(lambda u: u.email == email, self.usuarios))[0]
        except IndexError:
            return None

    def listar(self):
        return self.usuarios

    def remover(self, _id):
        self.usuarios[_id.id-1] = None
        return True
