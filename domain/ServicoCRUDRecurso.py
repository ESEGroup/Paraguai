from domain import Recurso

class ServicoCRUDRecurso():
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def criar(self, nome):
        recurso = Recurso(name)
        self.repositorio.criar(recurso)

    def todos(self):
        return self.repositorio.todos()
