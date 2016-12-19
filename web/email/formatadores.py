from domain.email import *

def formata(classe):
    def decorador(f):
        f.aceita = lambda email: email.__class__ == classe
        return f
    return decorador

@formata(EmailUsuarioCadastrado)
def usuario_cadastrado(email):
    usuario = email.usuario
    senha = email.senha

    return """Prezado {},

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

FORMATADORES_PADRAO = [usuario_cadastrado]
