#-*- coding: utf-8 -*-

import hashlib

class SenhaCriptografada():
    """Essa classe modela uma senha criptografada (em hash SHA-1)
       para ser usada na autenticação de Usuários."""

    def __init__(self, senha):
        """Construtor: converte uma senha em hash e armazena o hash.
        :param senha: String que representa a senha não criptografada."""

        self.digest = hashlib.sha1(senha).hexdigest()

    def verificar(self, senha):
        """Verifica se uma senha em texto plano é compatível
        com o hash armazenado. Usado em autenticações.
        :param senha: String que representa a senha a ser comparada"""

        digestSenha = hashlib.sha1(senha).hexdigest()
        return self.digest == digestSenha
