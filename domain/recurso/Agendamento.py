from domain import IntervaloDeTempo
class Agendamento():
    def __init__(self, intervalo, IDUsuario = None):
        self.intervalo = intervalo
        self.responsavel = IDUsuario
