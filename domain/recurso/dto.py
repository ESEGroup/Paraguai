class DTORecurso:
    """DTO para Recurso. É usada em cadastros
       e atualizações de Recursos.
       :param nome: Nome do usuário
       :param tipo: String com o tipo do recurso, podendo ser qualquer um dos listados em TipoRecurso.TIPOS
       :param local: String com informações de onde o recurso se localiza
       """

    def __init__(self, nome=None, tipo=None, local=None):
        self.nome = nome
        self.tipo = tipo
        self.local = local

class DTOBuscaRecurso:
    """DTO para Busca de Recurso onde os campos são tratados como E.
       :param nome: Nome do usuário para filtrar
       :param tipo: String com o tipo do recurso, podendo ser qualquer um dos listados em TipoRecurso.TIPOS
       :param local: String com informações de onde o recurso se localiza
       :param intervalos: Lista com DTOs de Intervalo de Tempo contendo os intervalos livres necessarios para o critério de busca
       """

    def __init__(self, nome=None, tipo=None, local=None, intervalos=[]):
        self.nome = nome
        self.tipo = tipo
        self.local = local
        self.intervalos = intervalos

class DTOIntervalo:
    """DTO para Intervalo de tempo, usado em agendamento e busca
       :param inicio: String contendo data no formato ISO8601
       :param fim: String contendo data no formato ISO8601
    """

    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

class DTOAgendamento:
    """DTO para Agendar Recurso
       :param idResponsavel: Int com o id do responsável pelo agendamento
       :param intervalo: DTOIntervaloDeTempo com o intervalo do agendamento"""

    def __init__(self, idResponsavel, intervalo):
        self.idResponsavel = idResponsavel
        self.intervalo = intervalo
