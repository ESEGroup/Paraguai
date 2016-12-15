#-*- coding: utf-8 -*-

###########################################
# dto_usuario.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe DTOUsuario.
#            Essa classe modela um Data Transmission
#            Object para Usuários. É usada em cadastros
#            e atualizações de Usuários. A senha usada aqui
#            é uma senha em texto plano não-criptografada.
#
# Atributos: nome - Tipo: string
#            email - Tipo: string
#            senha - Tipo: string
#            nivelAcesso - Tipo: int
###########################################


class DTOUsuario:

	def __init__(self, nome=None, email=None, senha=None, nivelAcesso=None):
		
		self.nome = nome
		self.email = email
		self.senha = senha
		self.nivelAcesso = nivelAcesso