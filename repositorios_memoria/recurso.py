from domain.recurso import RepositorioRecurso
from .base import RepositorioEmMemoria

class RepositorioRecursoEmMemoria(RepositorioEmMemoria, RepositorioRecurso):
    def buscar(self, recursoFiltro):
        return list(filter(lambda r: recursoFiltro.atende(r), self.listar()))
