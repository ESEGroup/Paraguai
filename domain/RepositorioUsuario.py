# -*- coding: utf-8 -*-

class RepositorioUsuario():
"""Essa classe abstrata representa um repositório de Usuários.
Esse repositório é a entidade que armazena Usuários no nosso sistema,
podendo ser um BD qualquer ou um armazenamento em memória"""

	def criarOuSalvar(self, _id=None, usuario):
		pass

	def obter(self, _id):
		pass

	def listar(self):
		pass
