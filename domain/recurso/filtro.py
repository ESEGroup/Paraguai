class FiltroRecurso():
    """ Representa um filtro de recurso que pode conter:
    Nome, Tipo, Localização e Intervalos
    """

    def __init__(self, nome, tipo, local, intervalos):
        self.nome = nome
        self.tipo = tipo
        self.local = local
        self.intervalos = intervalos

    def atende(self, recurso):
        """ Diz se um recurso atende aos critérios do filtro ou não """
        return (
            self.atende_nome(recurso) and
            self.atende_tipo(recurso) and
            self.atende_local(recurso) and
            self.atende_intervalos(recurso)
        )

    def atende_nome(self, recurso):
        if not self.nome:
            return True
        return recurso.nome == self.nome

    def atende_tipo(self, recurso):
        if not self.tipo:
            return True
        return recurso.tipo == self.tipo

    def atende_local(self, recurso):
        if not self.local:
            return True
        return recurso.local == self.local

    def atende_intervalos(self, recurso):
        return not any( a.intervalo.intercede(i) for a in recurso.agendamentos for i in self.intervalos)
