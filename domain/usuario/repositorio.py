# -*- coding: utf-8 -*-

class RepositorioUsuario():
    """Essa classe abstrata modela um Repositório de Usuários,
       ou seja, uma estrutura de armazenamento de Usuários (por
       exemplo, um BD ou armazenamento em arquivo de texto),
       para implementar o CRUD."""

    def inserir(self, usuario):
        """Cria um Usuário no Repositório. Deve retornar um objeto de Usuário com os dados fornecidos ou levantar uma exceção em caso de falha
        :param usuario: Usuario a ser salvo"""

    def atualizar(self, usuario):
        """Altera os dados de um Usuário do Repositório. Não retorna nada. Em caso de falha levanta uma exceção
        :param usuario: Usuário a ser persistido"""

    def obter(self, _id):
        """Busca um Usuário do Repositório com um ID específico e deve retorná-lo.
        :param _id: Número inteiro (int) que representa o ID do Usuário a ser buscado."""

    def obter_por_email(self, email):
        """Busca um Usuário do Repositório com um email específico e deve retorná-lo.
        :param email: String com o email do usuário a ser buscado"""

    def listar(self):
        """Retorna todos os Usuários armazenados no Repositório em uma lista."""

    def remover(self, _id):
        """Remove o Usuário com o ID fornecido do Repositório, se ele existir, e deve retornar um
        booleano indicando se a operação foi realizada com sucesso (true) ou não (false).
        :param _id: Número inteiro (int) que representa o ID do Usuário a ser buscado."""
