from domain import Recurso, TipoRecurso
from .IntervaloDeTempo import IntervaloDeTempo
from .Agendamento import Agendamento

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
    def buscar(self, id, nome, tipoID, intervalosLivres, localizacao):
        """
        :param tipoID: ID do TipoRecurso correspondente
        :param intervalosLivres: Lista de intervalos livres desejados contendo tuplas (inicio,fim) ou intervalos
        """
        print("Intervalos livres desejados : ", len(intervalosLivres))
        intervalosLivres = [IntervaloDeTempo(inicio,fim) for (inicio,fim) in intervalosLivres]
        agendamentos = [Agendamento(intervalo) for intervalo in intervalosLivres if type(intervalo) is IntervaloDeTempo]

        tipo = self.repositorio.tipo_por_id(tipoID)
        filtro = Recurso(nome,tipo,localizacao,agendamentos)
        filtro.id = id
        return self.repositorio.buscar(filtro)

    def todos(self):
        return self.repositorio.todos()

    def metadados(self):
        return self.metadados