###########################################
# support.py
#
# Autores: Bernardo Amorim (bamorim), Lucas de Carvalho (Lucas-CG)
#
# Descrição: Classes e funções utilitárias para
#            implementações do domínio.
#
###########################################

class ValueObject():
	def __eq__(self, other):
		self.__dict__ == other.__dict__ && seçf.__class__ == other.__class__

class ID(ValueObject):
	def __init__(self, id):
		self.id = id