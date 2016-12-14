# -*- coding: utf-8 -*-

###########################################
# SistemaManutencao.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe SistemaManutencao.
#            Essa classe modela o nível de acesso do Sistema de Manutenção,
#            que acessará o SAGRE para alterar o estado de Recursos (entre
#            Disponível e Indisponível) e agendar vistorias (que são equi-
#            valentes a Agendamentos).
#
# Atributos: descricao - Tipo: string
#
# Dependências: domain.NivelAcesso
###########################################

from domain import NivelAcesso

class SistemaManutencao(NivelAcesso):
	def __init__(self):
		self.description="Sistema de Manutenção"