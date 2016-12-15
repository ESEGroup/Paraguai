# -*- coding: utf-8 -*-

"""
usuario.py

Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)

Descrição: Implementa as classes Usuario e IDUsuario.
"""

from senha_criptografada import *
from nivel_acesso import *
from domain.support import ID

class IDUsuario(ID):
	"Value Object que armazena o ID de um Usuário."
	pass

class Usuario():
	"""Modela os usuários do SAGR UFRJ.
	:param nome: Nome do Usuário
	:param email: Endereço de e-mail do Usuário
	:param nivelAcesso: Nível de acesso do Usuário (objeto de NivelAcesso)
	:param senha: Senha do Usuário, já criptografada (objeto de SenhaCriptografada)
	:param id: ID do Usuário (objeto de IDUsuario)
	"""

	def __init__(self, nome=None, email=None, escolhaNivelAcesso=None, senha, _id):
		
		self.nome = nome
		self.email = email

		escolha = {
			0: UsuarioComum(),
			1: SistemaManutencao(),
			2: Administrador(),
		}

		self.nivelAcesso = escolha.get(escolhaNivelAcesso)

		#criptografa a senha passada na criação
		self.senhaCriptografada = SenhaCriptografada(senha)

		self.id = IDUsuario(_id)

	def nivelDeAcesso():
		"""Retorna o nível de acesso do Usuário (um objeto de NivelAcesso)."""
		return self.nivelAcesso
