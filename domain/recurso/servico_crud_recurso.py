from .recurso import Recurso
from .tipo import TipoRecurso
from .filtro import FiltroRecurso
from domain import IntervaloDeTempo
from domain.excecoes import ExcecaoRecursoInexistente
from domain.iso8601 import from_iso

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
        return self.repositorio.inserir(novoRecurso)

    # UC08 - Alterar recurso
    def alterar(self, id, dto):
        """
        Recebe um id e um dicionário com os dados a serem alterados
        """
        recurso = self.repositorio.obter(id)
        if not recurso:
            raise ExcecaoRecursoInexistente

        if dto.tipo:
            tipo = TipoRecurso(dto.tipo)
            recurso.tipo = tipo
        if dto.nome:
            recurso.nome = dto.nome
        if dto.local:
            recurso.local = dto.local

        self.repositorio.atualizar(recurso)
        return True

    def obter(self,id):
        recurso = self.repositorio.obter(id)
        if not recurso:
            raise ExcecaoRecursoInexistente

        return recurso

    # UC01 - Buscar Recurso
    def buscar(self, dto):
        """
        :param tipoID: ID do TipoRecurso correspondente
        :param intervalosLivres: Lista de intervalos livres desejados contendo tuplas (inicio,fim) ou intervalos
        """
        intervalosLivres = [IntervaloDeTempo(from_iso(inicio),from_iso(fim)) for (inicio,fim) in dto.intervalos]
        tipo = dto.tipo and TipoRecurso(dto.tipo)
        filtro = FiltroRecurso(dto.nome,tipo,dto.local,intervalosLivres)
        return self.repositorio.buscar(filtro)

    def listar(self):
        return self.repositorio.listar()

    def remover(self, id):
        if not self.repositorio.obter(id):
            raise ExcecaoRecursoInexistente

        self.repositorio.remover(id)
