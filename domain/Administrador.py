# -*- coding: utf-8 -*-

from domain import NivelAcesso

class Administrador(NivelAcesso):
	def __init__(self):
		self.description="Administrador"