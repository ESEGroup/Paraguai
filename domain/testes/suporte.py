from domain.email import ServicoEmail

class ServicoEmailEmMemoria(ServicoEmail):
    def __init__(self):
        self.emails = []

    def enviar(self, destinatario, email):
        self.emails.append((destinatario, email))
