class TipoRecurso():
    def __init__(self,id,nome=None):
        self.id = id
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return (self.id, self.nome)

    def __eq__(self,other):
        if (other is None):
            return False
        return self.id == other.id

    def validarId(self):
        # TODO - Criar validação de tipo de recurso
        return True

    def validar(self):
        return ( bool(self.nome) and isinstance(self.nome,str) and self.validarId())