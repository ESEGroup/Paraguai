class DTORecurso:
    """Essa classe modela um Data Transmission Object para Recurso. É usada em cadastros
       e atualizações de Recursos.
       :param nome: Nome do usuário
       :param tipo: String com o tipo do recurso, podendo ser qualquer um dos listados em TipoRecurso.TIPOS
       :param local: String com informações de onde o recurso se localiza
       """

    def __init__(self, nome=None, tipo=None, local=None):
        self.nome = nome
        self.tipo = tipo
        self.local = local
