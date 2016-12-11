#-*- coding: utf-8 -*-

class ServicoAplicacaoUsuario():
	"""Essa classe modela um serviço CRUD para Usuários.
	Seus metodos criam, alteram, buscam e listam Usuários.
	Seu único atributo é "repositorio", que deve herdar de RepositorioUsuario"""

	def __init__(self, repositorio):
		self.repositorio = repositorio

	#UCXX - Criar Usuario
	#param: dados: DTOUsuario
	def criar(self, dados):
		return self.repositorio.criarOuSalvar(dados)

	#UCXX - Alterar Usuario
	#param: _id: IDUsuario, dados: DTOUsuario
	def alterar(self, _id, dados):
		return self.repositorio.criarOuSalvar(_id, dados)

	def listar(self):
		return self.repositorio.listar()

	#UCXX - Buscar Usuario
	#param: _id: IDUsuario
	def obter(self, _id):
		return self.repositorio.obter(_id)


