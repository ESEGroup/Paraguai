from datetime import datetime
class IntervaloDeTempo():
    def __init__(self,inicio=None, fim=None):
        if(type(inicio) is not datetime):
            raise ValueError("Inicio do intervalo de tempo inválido")

        if(type(fim) is not datetime):
            raise ValueError("Fim do intervalo de tempo inválido")

        if (self.inicio >= self.fim):
            print(inicio)
            print(fim)
            raise ValueError("Fim antes do Início")

    def intercede(self,outro):
        if (self.inicio <= outro.inicio):
            return bool(
                (outro.inicio < self.fim and self.fim <= outro.fim) or
                (outro.fim <= self.fim)
            )
        else:
            return outro.intercede(self)
