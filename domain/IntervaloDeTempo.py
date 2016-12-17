from datetime import datetime
class IntervaloDeTempo():
    def __init__(self,inicio=None, fim=None):
        try:
            self.inicio = datetime.strptime(inicio,'%Y-%m-%d %H:%M')
        except:
            if ( type(inicio) is datetime):
                self.inicio = inicio
            else:
                print(type(inicio))
                raise ValueError("Inicio do intervalo de tempo inválido")

        try:
            self.fim = datetime.strptime(fim,'%Y-%m-%d %H:%M')
        except:
            if ( type(fim) is datetime):
                self.fim = fim
            else:
                print( type(fim))
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