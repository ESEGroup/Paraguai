from domain import RepositorioRecurso, Recurso

class RepositorioRecursoEmMemoria(RepositorioRecurso):
    def __init__(self):
        teste = Recurso("Recurso Teste")
        teste.id = 1
        self.recursos = [teste]

    def criar(self, recurso):
        recurso.id = len(self.recursos) + 1
        self.recursos.append(recurso)
        return recurso

    def todos(self):
        return self.recursos
