class ExcecaoParaguai(Exception):
    pass

class ExcecaoRegraDeNegocio(ExcecaoParaguai):
    pass

class ExcecaoNivelAcessoInvalido(ExcecaoParaguai):
    pass

class ExcecaoUsuarioJaExistente(ExcecaoParaguai):
    pass

class ExcecaoEntidadeInexistente(ExcecaoParaguai):
    pass

class ExcecaoUsuarioInexistente(ExcecaoEntidadeInexistente):
    pass

class ExcecaoRecursoInexistente(ExcecaoEntidadeInexistente):
    pass

# Não herda da ExcecaoEntidadeInexistente porque Agendamento é um ValueObject
class ExcecaoAgendamentoInexistente(ExcecaoParaguai):
    pass

class ExcecaoAgendamentoRecursoOcupado(ExcecaoRegraDeNegocio):
    pass

class ExcecaoAgendamentoUsuarioOcupado(ExcecaoRegraDeNegocio):
    pass

class ExcecaoAgendamentoRecursoInutilizavel(ExcecaoRegraDeNegocio):
    pass
