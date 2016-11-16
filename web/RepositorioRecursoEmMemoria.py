from domain import RepositorioRecurso, Recurso, TipoRecurso

class RepositorioRecursoEmMemoria(RepositorioRecurso):
    def __init__(self):
        listaTipos = [(0,"Sala"),(1,"Projetor"),(2,"Microscópio")]
        self.listaTipoRecurso = [TipoRecurso.TipoRecurso(id = identificador, nome = recurso) for (identificador,recurso) in listaTipos ]

        teste = Recurso("Recurso Teste")
        teste.id = 1
        teste.tipo = self.listaTipoRecurso[0]
        self.recursos = [teste]

    def criar(self, recurso):
        recurso.id = len(self.recursos) + 1
        self.recursos.append(recurso)
        return recurso

    def todos(self):
        return self.recursos

    def tipos(self):
        return self.listaTipoRecurso

    def tipoPorId(self,id):
        pass

