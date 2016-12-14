#-*- coding: utf-8 -*-

###########################################
# ServicoAplicacaoUsuario.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe ServicoAplicacaoUsuario.
#            Essa classe modela um serviço CRUD para Usuários,
#            que independe da implementação do armazenamento.
#            Seus métodos criam, alteram, buscam e listam Usuários.
#
# Atributos: repositorio - Tipo: domain.RepositorioUsuario
###########################################

class ServicoAplicacaoUsuario():

	def __init__(self, repositorio):

		self.repositorio = repositorio

	#UC12 - Adicionar Usuario
	#parâmetros: dados: DTOUsuario
	def criar(self, dados):

		return self.repositorio.criarOuSalvar(dados)

	#UC13 - Alterar Usuario
	#parâmetros: _id: IDUsuario, dados: DTOUsuario
	def alterar(self, _id, dados):

		return self.repositorio.criarOuSalvar(_id, dados)

	def listar(self):

		return self.repositorio.listar()

	#UC04 - Buscar Usuario
	#param: _id: IDUsuario
	def obter(self, _id):

		return self.repositorio.obter(_id)


