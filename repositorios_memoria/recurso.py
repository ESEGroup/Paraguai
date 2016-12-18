from difflib import SequenceMatcher
from itertools import product
from domain.recurso import RepositorioRecurso

class RepositorioRecursoEmMemoria(RepositorioRecurso):
    def __init__(self):
        self.recursos = []

    def criar(self, recurso):
        recurso.id = len(self.recursos) + 1
        self.recursos.append(recurso)
        return recurso

    def remover(self, id):
        try:
            self.recursos[int(id)-1] = None
            return True
        except IndexError:
            return False

    def obter(self, identificador):
        try:
            return self.recursos[int(identificador)-1]
        except:
            return None

    def buscar(self, recursoFiltro):
        return list(filter(lambda r: recursoFiltro.atende(r), self.recursos))

    def listar(self):
        return self.recursos
