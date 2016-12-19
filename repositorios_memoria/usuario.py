# -*- coding: utf-8 -*-

from .base import RepositorioEmMemoria
from domain.usuario import RepositorioUsuario

class RepositorioUsuarioEmMemoria(RepositorioEmMemoria, RepositorioUsuario):
    """Essa classe modela um Repositório de Usuários em memória, para
    armazenamento temporário e uso em mock tests."""


    def obter_por_email(self, email):
        """Busca e retorna um objeto de Usuario associado a um endereço de e-mail
        fornecido. Pode levantar uma exceção do tipo IndexError caso não seja
        encontrado nenhum Usuário associado ao e-mail dado."""
        try:
            return list(filter(lambda u: u.email == email, self.listar()))[0]
        except IndexError:
            return None
