# -*- coding: utf-8 -*-

###########################################
# Usuario.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe Usuario.
#            Essa classe modela os usuários do SAGRE UFRJ.
#            Cada Usuário contém um nome, um endereço de e-mail,
#            um nível de acesso, uma senha criptografada e um ID.
#
#
# Atributos: nome - Tipo: string
#            email - Tipo: string
#            nivelAcesso - Tipo: domain.NivelAcesso (composição)
#            senhaCriptografada - Tipo: domain.SenhaCriptografada (composição)
#            id - Tipo: domain.IDUsuario (composição)
#
# Dependências: domain.[SenhaCriptografada, IDUsuario,
#               Administrador, UsuarioComum, SistemaManutencao]
###########################################


from domain import NivelAcesso, SenhaCriptografada, IDUsuario, Administrador, UsuarioComum, SistemaManutencao

class Usuario():

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
		return self.nivelAcesso
