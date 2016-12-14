# -*- coding: utf-8 -*-

###########################################
# IDUsuario.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe IDUsuario.
#            Essa classe é um value object que representa o ID de
#            um usuário.
#
# Atributos: idUnico - Tipo: int
###########################################

class IDUsuario():

	def __init__(self, idUnico):
		#Construtor. Armazena um id fornecido
		#Parâmetros: idUnico - Tipo: int

		self.idUnico = idUnico