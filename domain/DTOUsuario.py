#-*- coding: utf-8 -*-

class DTOUsuario:
"""Essa classe modela um Data Transmission Object (DTO) para Usuários.
Usado em cadastros e atualizações de Usuários."""

	def __init__(self, nome=None, email=None, senha=None):
		self.nome = nome
		self.email = email
		self.senha = senha