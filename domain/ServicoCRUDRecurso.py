from domain import Recurso, TipoRecurso
from .IntervaloDeTempo import IntervaloDeTempo
from .Agendamento import Agendamento

class ServicoCRUDRecurso():
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.metadados = self.repositorio.metadados()

    # UC07 - Cadastrar Recurso
    def criar(self, fonte):
        # TODO - Validar criação -> Externalizar o processamento do form
        tipoRecurso = self.repositorio.tipo_por_id(id = fonte["categoria"])
        novoRecurso = Recurso(nome = fonte["nome"],
                      local = fonte["local"],
                      tipo = tipoRecurso )
        return self.repositorio.criarOuSalvar(novoRecurso)

    # UC08 - Alterar recurso
    def alterar(self, fonte):
        """
        Recebe um dicionário com id e os dados a serem alterados
        """
        if not fonte["id"]:
            return None
        recurso = self.repositorio.recurso_por_id(fonte["id"])

        # -x-v Refatorar esse trecho para fazer iterando pelas propriedades:
        if fonte["categoria"]:
            tipoRecurso = self.repositorio.tipo_por_id(id = fonte["categoria"])
            recurso.tipo = tipoRecurso
        if fonte["nome"]:
            recurso.nome = fonte["nome"]
        if fonte["local"]:
            recurso.local = fonte["local"]
        # -x-^

        return self.repositorio.criarOuSalvar(recurso)

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