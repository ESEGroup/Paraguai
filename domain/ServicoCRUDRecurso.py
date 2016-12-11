from domain import Recurso, TipoRecurso

class ServicoCRUDRecurso():
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.metadados = self.repositorio.metadados()

    # UC07 - Cadastrar Recurso
    def criar(self, fonte):
        # TODO - Validar criação
        tipoRecurso = self.repositorio.tipoPorId(id = fonte["categoria"])
        novoRecurso = Recurso(nome = fonte["nome"],
                      local = fonte["local"],
                      tipo = tipoRecurso )
        return self.repositorio.criar(novoRecurso)

    # UC01 - Buscar Recurso
    def buscar(self, categoria=None):
        pass

    def todos(self):
        return self.repositorio.todos()

    def metadados(self):
        return self.metadados