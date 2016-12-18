from .tipo import TipoRecurso
from domain.support import ID

class IDRecurso(ID):
    pass

class Recurso():
    def __init__(self, nome, tipo, local, agendamentos=[], id=None):
        self.id = id
        self.nome = nome
        self.local = local
        self.tipo = tipo
        self.agendamentos = agendamentos
