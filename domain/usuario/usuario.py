# -*- coding: utf-8 -*-

from .nivel_acesso import *

class Usuario():
    """Modela os usuários do SAGR UFRJ.
    :param nome: Nome do Usuário
    :param email: Endereço de e-mail do Usuário
    :param nivelAcesso: Nível de acesso do Usuário (objeto de NivelAcesso)
    :param senha: Senha do Usuário, já criptografada (objeto de SenhaCriptografada)
    :param id: ID do Usuário (objeto de IDUsuario)
    """

    def __init__(self, nome, email, senhaCriptografada, nivelAcesso, id_usuario=None):
        self.nome = nome
        self.email = email
        self.nivelAcesso = nivelAcesso

        #criptografa a senha passada na criação
        self.senhaCriptografada = senhaCriptografada

        self.id = id_usuario

    def nivelDeAcesso(self):
        """Retorna o nível de acesso do Usuário (um objeto de NivelAcesso)."""
        return self.nivelAcesso
