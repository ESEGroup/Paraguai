# -*- coding: utf-8 -*-

from domain import SenhaCriptografada, Administrador, UsuarioComum, SistemaManutencao

class Usuario():
"""Essa classe modela um Usuário para o nosso sistema.
Possui campos de e-mail e telefone, e é associado a um objeto
de NivelDeAcesso e a um objeto de SenhaCriptografada."""

	def __init__(self, nome=None, email=None, nivelAcesso=None, senha, _id):
		self.nome = nome
		self.email = email
		self.nivelAcesso = nivelAcesso

		escolha = {
			0: UsuarioComum(),
			1: SistemaManutencao(),
			2: Administrador(),
		}

		self.nivelAcesso = escolha.get(nivelAcesso)

		#criptografa a senha passada na criação
		self.senhaCriptografada = SenhaCriptografada(senha)

		#_id deve ser um IDUsuario
		self.id = _id

	def nivelDeAcesso():
		return self.nivelAcesso
