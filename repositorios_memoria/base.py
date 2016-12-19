import copy

class RepositorioEmMemoria():
    def __init__(self, entidades=[]):
        self.entidades = entidades

    def inserir(self, entidade):
        """Cria uma nova Entidade.
        :param entidade: Entidade a ser inserida"""
        novo_id = len(self.entidades) + 1
        entidade.id = novo_id
        self.entidades.append(entidade)

        return entidade

    def atualizar(self, entidade):
        """Persiste a entidade dado o seu próprio id
        :param entidade: Entidade a ser persistida"""
        self.entidades[entidade.id-1] = entidade

    def obter(self, _id):
        """Busca e retorna um objeto de Entidade associado a um ID fornecido.
        :param _id: ID do Entidade buscada"""
        try:
            return copy.deepcopy(self.entidades[_id-1])
        except IndexError:
            return None

    def listar(self):
        return copy.deepcopy(list(filter(lambda r: r, self.entidades)))

    def remover(self, _id):
        self.entidades[_id-1] = None
        return True
