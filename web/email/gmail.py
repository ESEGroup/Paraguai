import smtplib
from .formatado import ServicoEmailFormatado

class ServicoEmailGmail(ServicoEmailFormatado):
    def __init__(self, formatadores, usuario, senha):
        self.formatadores = formatadores

        self.smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        self.usuario = usuario
        self.senha = senha

    def start_smtp(self):
        self.smtpserver.ehlo()
        self.smtpserver.starttls()
        self.smtpserver.login(self.usuario, self.senha)

    def stop_smtp(self):
        self.smtpserver.close()

    def criar_header(self, assunto):
        return 'To: ' + destino + '\nFrom: ' + self.usuario + '\nSubject:' + assunto + '\n'

    def enviar_formatado(self, destino, assunto, corpo):
        self.start_smtp()

        msg = criar_header(assunto) + '\n' + corpo
        msg = msg.encode('utf-8')

        self.smtpserver.sendmail(self.usuario, destino, msg)
        self.stop_smtp()
