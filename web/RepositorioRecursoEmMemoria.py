from domain import RepositorioRecurso

class RepositorioRecursoEmMemoria(RepositorioRecurso):
    def __init__(self):
        self.recursos = []

    def criar(self, recurso):
        recurso.id = len(self.recursos) + 1
        self.recursos.append(recurso)
        return recurso

    def todos(self):
        return self.recursos
