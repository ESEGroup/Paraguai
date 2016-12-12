# -*- coding: utf-8 -*-

from domain import NivelAcesso

class UsuarioComum(NivelAcesso):
	def __init__(self):
		self.description="Usuário Comum"