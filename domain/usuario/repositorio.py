# -*- coding: utf-8 -*-

class RepositorioUsuario():
    """Essa classe abstrata modela um Repositório de Usuários,
       ou seja, uma estrutura de armazenamento de Usuários (por
       exemplo, um BD ou armazenamento em arquivo de texto),
       para implementar o CRUD."""

    def criar(self, usuario):
        """Cria um Usuário no Repositório. Deve retornar um objeto de Usuário com os dados fornecidos
        se a criação for realizada com sucesso. Caso ocorra uma falha, deverá retornar um objeto vazio.
        :param usuario: Objeto de DTOUsuario que possui os dados a serem carregados."""
        pass

    def alterar(self, _id, usuario):
        """Altera os dados de um Usuário do Repositório. Deve retornar um objeto de Usuário com
        os dados fornecidos se a alteração for realizada com sucesso. Caso ocorra uma falha, deve
        retornar um objeto vazio.
        :param _id: Número inteiro que representa o ID do Usuário a ser buscado.
        :param usuario: Objeto de DTOUsuario que possui os dados a serem carregados."""
        pass

    def obter(self, _id):
        """Busca um Usuário do Repositório com um ID específico e deve retorná-lo.
        :param _id: Número inteiro (int) que representa o ID do Usuário a ser buscado."""
        pass

    def obter_por_email(self, email):
        """Busca um Usuário do Repositório com um email específico e deve retorná-lo.
        :param email: String com o email do usuário a ser buscado"""
        pass

    def listar(self):
        """Retorna todos os Usuários armazenados no Repositório em uma lista."""
        pass

    def remover(self, _id):
        """Remove o Usuário com o ID fornecido do Repositório, se ele existir, e deve retornar um
        booleano indicando se a operação foi realizada com sucesso (true) ou não (false).
        :param _id: Número inteiro (int) que representa o ID do Usuário a ser buscado."""
        pass
