from domain.intervalo import IntervaloDeTempo
from domain.support import ValueObject

class Agendamento(ValueObject):
    def __init__(self, intervalo, idResponsavel):
        self.intervalo = intervalo
        self.idResponsavel = idResponsavel
