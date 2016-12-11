class ServicoAplicacaoUsuario:
	def __init__(self, repositorio):
		self.repositorio = repositorio

	#UCXX - Criar usuário
	#Dados é um UsuarioDTO
	def criar(self, dados):
		return self.repositorio.criar()
