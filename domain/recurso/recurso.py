from .tipo import TipoRecurso

class Recurso():
    def __init__(self, nome=None, tipo=None, local=None, agendamentos=[]):
        self.id = None
        self.nome = nome
        self.localizacao = local
        if not tipo:
            tipo = TipoRecurso(0)
        self.tipo = tipo
        self.agendamentos = agendamentos

    def __str__(self):
        return nome
