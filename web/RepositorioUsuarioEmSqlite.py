# -*- coding: utf-8 -*-

###########################################
# RepositorioUsuarioEmSqlite.py
#
# Autor: Lucas de Carvalho (Lucas-CG) (lucas.gomes@poli.ufrj.br)
#
# Descrição: Implementa a classe RepositorioUsuarioEmMemoria.
#            Essa classe modela um Repositório de Usuários em um banco
#            de dados SQLite, usando o framework Flask-SQLAlchemy.
#            Ainda não concluído.
#
# Atributos: ???
#
# Dependências: ???
###########################################

from domain import RepositorioUsuario, Usuario

class RepositorioUsuarioEmSqlite(RepositorioUsuario):
    def __init__(self):
        #self.usuarios = []
        pass

    #param: dados: DTOUsuario
    def criar(self, dados):
        #_id = len(self.usuarios) + 1
        #usuario = Usuario(dados.nome, dados.email, 1, dados.senha, _id)       
        #self.usuarios.append(usuario)
        #return usuario
        pass

    def listar(self):
        #return self.usuarios
        pass
