from domain import Recurso

class ServicoCRUDRecurso():
    def __init__(self, repositorio):
        self.repositorio = repositorio

    # UC07 - Cadastrar Recurso
    def criar(self, nome):
        recurso = Recurso(nome)
        return self.repositorio.criar(recurso)

    # UC01 - Buscar Recurso
    def buscar(self, categoria=None):
        pass

    def todos(self):
        return self.repositorio.todos()

    def tipos(self):
        return self.repositorio.tipos()