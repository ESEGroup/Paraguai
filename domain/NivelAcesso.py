###########################################
# NivelAcesso.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe NivelAcesso.
#            Essa classe abstrata modela um nível de acesso ao SAGRE.
#            Todos os níveis de acesso devem herdar dessa classe.
#            Níveis de acesso afetam as permissões que um Usuário possui
#            sobre dados de outros Usuários, sobre Recursos e sobre Agendamentos.
#            
#            Estabelece uma relação de composição com Usuário (é contido por Usuário).
#
###########################################


class NivelAcesso:
	def __init__(self):
		pass