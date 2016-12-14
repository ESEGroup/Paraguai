# -*- coding: utf-8 -*-

###########################################
# Administrador.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe Administrador.
#            Essa classe modela o nível de acesso de um
#            Administrador. Administradores podem efetuar o CRUD
#            de quaisquer Usuários e Recursos, além de terem acesso
#            aos comandos de um Usuário comum e poderem alterar/remover
#            Agendamentos de outros Usuários.
#
# Atributos: descricao - Tipo: string
#
# Dependências: domain.NivelAcesso
###########################################

from domain import NivelAcesso

class Administrador(NivelAcesso):
	def __init__(self):
		self.descricao="Administrador"