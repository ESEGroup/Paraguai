# -*- coding: utf-8 -*-

###########################################
# nivel_acesso.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe NivelAcesso, que é abstrata e modela
#            um nível de acesso ao SAGR, além de todas as classes que herdam
#            dela (Administrador, SistemaManutencao, UsuarioComum).
#            
#            Estabelece uma relação de composição com Usuário (é contido por Usuário).
#
###########################################

from domain.support import ValueObject

class NivelAcesso(ValueObject):
	pass

class Administrador(NivelAcesso):
	pass

class SistemaManutencao(NivelAcesso):
	pass

class UsuarioComum(NivelAcesso):
	pass