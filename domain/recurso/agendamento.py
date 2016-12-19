from domain.intervalo import IntervaloDeTempo
class Agendamento():
    def __init__(self, intervalo, IDUsuario):
        self.intervalo = intervalo
        self.idResponsavel = IDUsuario
