from domain.support import ValueObject

class TipoRecurso(ValueObject):
    TIPOS = ["sala", "projetor", "computador", "ar-condicionado"]

    def __init__(self,nome):
        if not nome in TipoRecurso.TIPOS:
            raise ValueError("Tipo de Recurso inválido")

        self.nome = nome
