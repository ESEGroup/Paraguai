# -*- coding: utf-8 -*-

###########################################
# RepositorioUsuario.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe RepositorioUsuario.
#            Essa classe abstrata modela um Repositório de Usuários,
#            ou seja, uma estrutura de armazenamento de Usuários (por
#            exemplo, um BD ou armazenamento em arquivo de texto),
#            para implementar o CRUD.
###########################################

class RepositorioUsuario():

	def criarOuSalvar(self, _id=None, usuario):
		#Cria ou atualiza um Usuário no Repositório.
		#Parâmetros: _id - Tipo: int; usuario - Tipo: domain.Usuario
		pass

	def obter(self, _id):
		#Obtém um Usuário com um ID específico.
		#Parâmetros: _id - Tipo: int
		pass

	def listar(self):
		#Lista todos os Usuários armazenados.
		pass
