#-*- coding: utf-8 -*-

###########################################
# crud_usuario.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe ServicoCRUDUsuario.
#            Essa classe modela um serviço CRUD para Usuários,
#            que independe da implementação do armazenamento.
#            Seus métodos criam, alteram, buscam e listam Usuários.
#
# Atributos: repositorio - Tipo: RepositorioUsuario(domain.model.usuario.repositorio_usuario)
###########################################

class ServicoCRUDUsuario():

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

		return self.repositorio.todos()

	#UC04 - Buscar Usuario
	#param: _id: IDUsuario
	def obter(self, _id):

		return self.repositorio.obter(_id)

	#tem que remover o Usuário e tirar seus Agendamentos (que ainda estão indefinidos)
	def remover(self, _id):
		pass



