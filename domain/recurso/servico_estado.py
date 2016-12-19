from domain.excecoes import ExcecaoRecursoInexistente

class ServicoEstadoRecurso():
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def alterar_estado(self, _id, utilizavel):
        """Altera o estado de um recurso pelo seu id para disponível ou não
        :param _id: Id do recurso a ser alterado
        :param utilizavel: Utilizável ou não (Booleano)"""

        recurso = self.repositorio.obter(_id)
        if not recurso:
            raise ExcecaoRecursoInexistente
        recurso.utilizavel = utilizavel
        self.repositorio.salvar(recurso)
