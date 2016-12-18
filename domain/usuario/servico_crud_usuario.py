#-*- coding: utf-8 -*-
from .usuario import Usuario
from .nivel_acesso import *
from .senha_criptografada import *
from domain.excecoes import *

class ServicoCRUDUsuario():
    """Essa classe modela um serviço CRUD para Usuários, que independe da
    implementação do armazenamento.
    :param repositorio: Objeto de RepositorioUsuario"""

    def __init__(self, repositorio):
        self.repositorio = repositorio


    def criar(self, dados):
        """Cria um Usuário. Implementa o UC12 (Adicionar Usuário).
        :param dados: Objeto de DTOUsuario com os dados a serem inseridos."""

        escolha = {
            0: UsuarioComum(),
            1: SistemaManutencao(),
            2: Administrador(),
        }

        try:
            nivelAcesso = escolha[dados.nivelAcesso]
        except KeyError:
            raise ExcecaoNivelAcessoInvalido

        senhaCriptografada = SenhaCriptografada(dados.senha)
        usuario = Usuario(dados.nome, dados.email, senhaCriptografada, nivelAcesso)

        if self.repositorio.obter_por_email(dados.email):
            raise ExcecaoUsuarioJaExistente

        return self.repositorio.criar(usuario)


    def alterar(self, _id, dados):
        """Atualiza os dados de um Usuário. Implementa o UC13 (Alterar Usuário).
        :param _id: Número inteiro que representa o ID do Usuário desejado.
        :param dados: Objeto de DTOUsuario com os dados a serem inseridos."""

        usuario = self.repositorio.obter(_id)
        if not usuario:
            raise ExcecaoUsuarioInexistente

        #Usuário que possui o e-mail para o qual se deseja alterar
        usuarioDoEmail = self.repositorio.obter_por_email(dados.email)

        if usuarioDoEmail and usuarioDoEmail.id != _id:
            raise ExcecaoUsuarioJaExistente

        escolha = {
            0: UsuarioComum(),
            1: SistemaManutencao(),
            2: Administrador(),
        }

        try:
            usuario.nivelAcesso = escolha[dados.nivelAcesso]
        except KeyError:
            raise ExcecaoNivelAcessoInvalido            

        usuario.nome = dados.nome
        usuario.email = dados.email

        if dados.senha:
            usuario.senhaCriptografada = SenhaCriptografada(dados.senha)
              

        return self.repositorio.alterar(_id, usuario)


    def listar(self):
        """Lista todos os Usuários, retornando uma lista de objetos de Usuario.
        Implementa parte do UC04 (Buscar Usuário)."""
        
        #Não lista Usuários vazios (removidos)
        return list( filter( lambda r: r, self.repositorio.listar() ) )


    def obter(self, _id):
        """Busca pelo Usuário de um ID fornecido e o retorna. Implementa
        parte do UC04 (Buscar Usuário).
        :param _id: Número inteiro que representa o ID do Usuário desejado."""

        usuario = self.repositorio.obter(_id)

        if not usuario:
            raise ExcecaoUsuarioInexistente

        return usuario


    def remover(self, _id):
        """Remove o Usuário que possui o ID fornecido e o retorna, além de
        cancelar todos os seus Agendamentos. Implementa o UCXXX (Remover Usuário).
        :param _id: Número inteiro que representa o ID do Usuário desejado."""
        
        #TODO: buscar por agendamentos associados ao Usuário com id _id

        if not self.repositorio.obter(_id):
            raise ExcecaoUsuarioInexistente

        #TODO: cancela todos os agendamentos da lista

        return (self.repositorio.remover(_id), True)
