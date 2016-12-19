from .formatado import ServicoEmailFormatado
from .gmail import ServicoEmailGmail
from .formatadores import *

formatadores = [
    usuario_cadastrado,
    usuario_alterado,
    usuario_removido
]

class ServicoEmailConsole(ServicoEmailFormatado):
    def enviar_formatado(self, destino, assunto, corpo):
        print('Enviando Email para ' + destino + ' com assunto "' + assunto + '" e com corpo: \n\n' + corpo)
