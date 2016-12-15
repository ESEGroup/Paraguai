#-*- coding: utf-8 -*-

###########################################
# senha_criptografada.py
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe SenhaCriptografada.
#            Essa classe modela uma senha criptografada (em hash SHA-1)
#            para ser usada na autenticação de Usuários.
#
# Atributos: digest - Tipo: string
#
# Dependências: hashlib
###########################################

import hashlib

class SenhaCriptografada():

	def __init__(self, senha):
		#Construtor: converte uma senha em hash e armazena o hash.
		#Parâmetros: senha - Tipo: string

		self.digest = hashlib.sha1(senha).hexdigest()

	def verificar(self, senha):
		#Verifica se uma senha em texto plano é compatível
		#com o hash armazenado.
		#Parâmetros: senha - Tipo: string

		digestSenha = hashlib.sha1(senha).hexdigest()
		return self.digest == digestSenha