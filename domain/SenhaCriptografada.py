#-*- coding: utf-8 -*-
import hashlib

class SenhaCriptografada():
"""Essa classe modela uma senha criptografada, para
autenticação de Usuários."""

	def __init__(self, digest):
		self.digest = digest

	def verificar(self, senha)
		#Verifica se uma senha em texto plano é compatível
		#com o hash armazenado

		digestSenha = hashlib.sha1(senha).hexdigest()
		return self.digest == digestSenha