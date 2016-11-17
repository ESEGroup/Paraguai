from .TipoRecurso import TipoRecurso
class Recurso():
    def __init__(self, nome=None, tipo=None, local=None):
        self.id = None
        self.nome = nome
        self.localizacao = None
        if not tipo:
            tipo = TipoRecurso()
        self.tipo = tipo

    def __str__(self):
        return nome
