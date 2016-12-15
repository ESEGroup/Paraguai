# -*- coding: utf-8 -*-

###########################################
# RepositorioUsuarioEmMemoria.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe RepositorioUsuarioEmMemoria.
#            Essa classe modela um Repositório de Usuários em memória,
#            para armazenamento temporário e uso em mock tests.
#
# Atributos: usuarios - Tipo: Usuario[]
#
# Dependências: domain.RepositorioUsuario, domain.Usuario
###########################################

import domain.RepositorioUsuario
import domain.Usuario

class RepositorioUsuarioEmMemoria(RepositorioUsuario):
    def __init__(self):

        self.usuarios = []

    #parâmetros: dados: DTOUsuario
    def criar(self, usuario):

        _id = len(self.usuarios) + 1

        usuario = Usuario(dados.nome, dados.email, 1, dados.senha, _id)       
        self.usuarios.append(usuario)

        return usuario

    def atualizar(self, _id, usuario):

        _id = len(self.usuarios) + 1

        usuario = Usuario(dados.nome, dados.email, 1, dados.senha, _id)       
        self.usuarios.append(usuario)

        return usuario

    #_id: - Tipo: int
    def obter(self, _id):

        return usuarios[_id]


    def listar(self):

        return self.usuarios
