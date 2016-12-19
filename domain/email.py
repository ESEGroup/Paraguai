from domain.support import ValueObject

class EmailUsuarioCadastrado(ValueObject):
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class EmailUsuarioAlterado(ValueObject):
    def __init__(self, usuario):
        self.usuario = usuario

class EmailUsuarioRemovido(ValueObject):
    def __init__(self, usuario):
        self.usuario = usuario

class EmailRecursoInutilizavel(ValueObject):
    def __init__(self, usuario, recurso, agendamentosCancelados):
        self.usuario = usuario
        self.recurso = recurso
        self.agendamentosCancelados = agendamentosCancelados

class EmailAgendamento(ValueObject):
    def __init__(self, usuario, recurso, agendamento):
        self.usuario = usuario
        self.recurso = recurso
        self.agendamento = agendamento

class EmailAgendamentoConfirmado(EmailAgendamento):
    pass

class EmailAgendamentoCancelado(EmailAgendamento):
    pass

class ServicoEmail():
    def enviar(self, destinatario, email):
        """Envia um email para um destinatario com um assunto e um corpo (texto)
        :param destinatario: String contendo o email do destinatario
        :param email: Value Object contendo o email desejado (os dados que precisam ser carregados para a camada de visualização enviar o email)
        """
        pass
