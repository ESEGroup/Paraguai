# -*- coding: utf-8 -*-

###########################################
# UsuarioComum.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe UsuarioComum.
#            Essa classe modela o nível de acesso de um
#            Usuário comum. Qualquer Usuário possui a permissão
#            de um Usuário comum.
#
# Atributos: descricao - Tipo: string
#
# Dependências: domain.NivelAcesso
###########################################


from domain import NivelAcesso

class UsuarioComum(NivelAcesso):
	def __init__(self):
		self.descricao="Usuário Comum"