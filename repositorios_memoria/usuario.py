# -*- coding: utf-8 -*-

from domain.usuario import RepositorioUsuario

class RepositorioUsuarioEmMemoria(RepositorioUsuario):
    """Essa classe modela um Repositório de Usuários em memória, para 
    armazenamento temporário e uso em mock tests.
    :param usuarios: Lista de Usuários armazenados (Usuario[])."""

    def __init__(self, usuarios=[]):
        self.usuarios = usuarios

    def criar(self, usuario):
        """Cria um novo Usuário.
        :param usuario: Objeto de Usuario com os dados do novo Usuário."""
        novo_id = len(self.usuarios) + 1
        usuario.id = novo_id
        self.usuarios.append(usuario)

        return usuario


    def alterar(self, _id, usuario):
        """Altera um Usuário já existente.
        :param _id: ID do Usuário a ser alterado
        :param usuario: Objeto de Usuario com os novos dados"""
        self.usuarios[_id-1] = usuario
        return usuario


    def obter(self, _id):
        """Busca e retorna um objeto de Usuario associado a um ID fornecido.
        Pode levantar uma exceção do tipo IndexError caso não seja encontrado
        nenhum Usuário associado ao ID dado.
        :param _id: ID do Usuario buscado"""
        try:
            return self.usuarios[_id-1]
        except IndexError:
            return None

    def obter_por_email(self, email):
        """Busca e retorna um objeto de Usuario associado a um endereço de e-mail
        fornecido. Pode levantar uma exceção do tipo IndexError caso não seja
        encontrado nenhum Usuário associado ao e-mail dado."""
        try:
            return list(filter(lambda u: u.email == email, self.usuarios))[0]
        except IndexError:
            return None

    def listar(self):
        """Retorna uma lista de todos os Usuários armazenados no Repositório."""
        return self.usuarios

    def remover(self, _id):
        """Remove o Usuário associado ao ID fornecido, se ele existir.
        Pode causar um IndexError, caso não exista um Usuário com o ID fornecido.
        :param _id: ID do Usuário a ser deletado."""
        del self.usuarios[_id-1]
        
        for i in range(0, len(self.usuarios)):
            self.usuarios[i].id = i+1

        return True
