from domain.email import *

class FormatadorEmail():
    def atende(self, email):
        email.__class__ == self.__class__.classe_atendida

    def formatar(self, email):
        pass

class FormatadorUsuarioCadastrado(FormatadorEmail):
    classe_atendida = EmailUsuarioCadastrado

    def formatar(self, email):
        usuario = email.usuario
        senha = email.senha

        """Prezado {},

        Você foi cadastrado com sucesso no Sistema de Agendamento UFRJ.

        Seguem abaixo os dados relacionados à sua conta:

        Nome completo: {}
        Nome de usuário: {}

        A senha associada à sua conta é {}.
        Solicitamos que você acesse o sistema e a altere assim que possível.

        Atenciosamente,
        Sistema de Agendamento UFRJ""".format(
            usuario.nome,
            usuario.nome,
            usuario.email,
            senha
        )


FORMATADORES_PADRAO = [FormatadorUsuarioCadastrado]
