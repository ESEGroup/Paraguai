from .recurso import Recurso
from .tipo import TipoRecurso
from .filtro import FiltroRecurso
from domain import IntervaloDeTempo
from domain.excecoes import ExcecaoRecursoInexistente

class ServicoCRUDRecurso():
    def __init__(self, repositorio):
        self.repositorio = repositorio

    # UC07 - Cadastrar Recurso
    def criar(self, dto):
        tipo = TipoRecurso(dto.tipo)
        novoRecurso = Recurso(
                      nome = dto.nome,
                      local = dto.local,
                      tipo = tipo)
        return self.repositorio.criar(novoRecurso)

    # UC08 - Alterar recurso
    def alterar(self, id, dto):
        """
        Recebe um id e um dicionário com os dados a serem alterados
        """
        recurso = self.repositorio.obter(id)
        if recurso == None:
            raise ExcecaoRecursoInexistente

        if dto.tipo:
            tipo = TipoRecurso(dto.tipo)
            recurso.tipo = tipo
        if dto.nome:
            recurso.nome = dto.nome
        if dto.local:
            recurso.local = dto.local

        return self.repositorio.criarOuSalvar(recurso)

    def obter(self,id):
        return self.repositorio.obter(id)

    # UC01 - Buscar Recurso
    def buscar(self, nome=None, tipoNome = None, intervalosLivres = [], local = None):
        """
        :param tipoID: ID do TipoRecurso correspondente
        :param intervalosLivres: Lista de intervalos livres desejados contendo tuplas (inicio,fim) ou intervalos
        """
        intervalosLivres = [IntervaloDeTempo(inicio,fim) for (inicio,fim) in intervalosLivres]
        tipo = tipoNome and TipoRecurso(tipoNome)
        filtro = FiltroRecurso(nome,tipo,local,intervalosLivres)
        return self.repositorio.buscar(filtro)

    def listar(self):
        return self.repositorio.listar()

    def remover(self, id):
        if self.repositorio.obter(id) == None:
            raise ExcecaoRecursoInexistente

        self.repositorio.remover(id)
