class ExcecaoParaguai(Exception):
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
