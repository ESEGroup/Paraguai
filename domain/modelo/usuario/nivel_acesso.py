# -*- coding: utf-8 -*-

from domain.support import ValueObject

class NivelAcesso(ValueObject):
    """Classe abstrata que modela um nível de acesso ao SAGR.
    Estabelece uma relação de composição com Usuário (é contido por Usuário)."""
    pass

class Administrador(NivelAcesso):
    """Nível de acesso de um Administrador. Garante acesso para visualizar e editar
    quaisquer Agendamentos, Recursos e Agendamentos."""
    pass

class SistemaManutencao(NivelAcesso):
    """Nível de acesso do Sistema de Manutenção. Garante acesso a quaisquer Recursos
    para agendar vistorias (equivalentes a Agendamentos) e alterar suas disponibilidades."""
    pass

class UsuarioComum(NivelAcesso):
    """Nível de acesso de um Usuário comum. Apenas possui acesso aos seus Agendamentos."""
    pass
