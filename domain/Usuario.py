# -*- coding: utf-8 -*-

class Usuario():
"""Essa classe modela um Usuário para o nosso sistema.
Possui campos de e-mail e telefone, e é associado a um objeto
de NivelDeAcesso e a um objeto de SenhaCriptografada."""

	def __init__(self, nome=None, email=None, nivelAcesso, senhaCriptografada):
		self.nome = nome
		self.email = email
		self.nivelAcesso = nivelAcesso
		self.senhaCriptografada = senhaCriptografada

	def nivelDeAcesso():
		return self.nivelAcesso
