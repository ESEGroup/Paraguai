from domain.email import *

class ServicoEmailFormatado(ServicoEmail):
    def __init__(self, formatadores):
        self.formatadores = formatadores

    def formatador(email):
        formatadores = list(filter(lambda f: f.aceita(email), self.formatadores))
        if not formatadores:
            return None

        return formatadores[0]

    def formatar(email):
        formatador = self.formatador(email)
        if not formatador:
            return None

        return formatador.formatar(email)

class ServicoEmailConsole(ServicoEmailFormatado):
    def enviar(self, destino, email):
        corpo = self.formatar(email)
        if not corpo:
            print("Nenhum formatador disponível para a classe %s" % email.__class__.__name__)
        print("Enviando Email para " + destino + " com corpo: \n\n" + corpo)
