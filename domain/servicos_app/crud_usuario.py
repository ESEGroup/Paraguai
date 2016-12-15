#-*- coding: utf-8 -*-
"""
crud_usuario.py

Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)

Descrição: Implementa a classe ServicoCRUDUsuario.
"""

class ServicoCRUDUsuario():
	"""Essa classe modela um serviço CRUD para Usuários, que independe da
	implementação do armazenamento.
	:param repositorio: Objeto de RepositorioUsuario"""

	def __init__(self, repositorio):

		self.repositorio = repositorio


	def criar(self, dados):
		"""Cria um Usuário. Implementa o UC12 (Adicionar Usuário).
		:param dados: Objeto de DTOUsuario com os dados a serem inseridos."""

		return self.repositorio.criar(dados)


	def alterar(self, _id, dados):
		"""Atualiza os dados de um Usuário. Implementa o UC13 (Alterar Usuário).
		:param _id: Número inteiro que representa o ID do Usuário desejado.
		:param dados: Objeto de DTOUsuario com os dados a serem inseridos."""		

		return self.repositorio.alterar(_id, dados)


	def listar(self):
		"""Lista todos os Úsuários, retornando uma lista de objetos de Usuario. 
		Implementa parte do UC04 (Buscar Usuário)."""

		return self.repositorio.todos()


	def obter(self, _id):
		"""Busca pelo Usuário de um ID fornecido e o retorna. Implementa 
		parte do UC04 (Buscar Usuário).
		:param _id: Número inteiro que representa o ID do Usuário desejado."""		

		return self.repositorio.obter(_id)

	
	def remover(self, _id):
		"""Remove o Usuário que possui o ID fornecido e o retorna, além de 
		cancelar todos os seus Agendamentos. Implementa o UCXXX (Remover Usuário).
		:param _id: Número inteiro que representa o ID do Usuário desejado."""			
		
		#busca por agendamentos associados ao Usuário com id _id

		#cancela todos os agendamentos da lista

		return (self.repositorio.remover(_id), true)
		



