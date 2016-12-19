from domain.email import *

def formata(classe):
    def decorador(f):
        f.aceita = lambda email: email.__class__ == classe
        return f
    return decorador

@formata(EmailUsuarioCadastrado)
def usuario_cadastrado(email):
    assunto = "Você foi cadastrado no Sistema de Agendamento UFRJ!"
    corpo = """Prezado {},

    Você foi cadastrado com sucesso no Sistema de Agendamento UFRJ.

    Seguem abaixo os dados relacionados à sua conta:

    Nome completo: {}
    Nome de usuário: {}

    A senha associada à sua conta é {}.
    Solicitamos que você acesse o sistema e a altere assim que possível.

    Atenciosamente,
    Sistema de Agendamento UFRJ""".format(
        email.usuario.nome,
        email.usuario.nome,
        email.usuario.email,
        email.senha
    )

    return (assunto, corpo)

@formata(EmailUsuarioAlterado)
def usuario_alterado(email):
    assunto = "Seu cadastro foi alterado por um administrador do sistema"
    corpo = """Prezado {},

    Seu cadastro foi alterado por um administrador do sistema.

    Seguem abaixo as informações da sua conta após a alteração:

    Nome completo: {}
    Nome de usuário: {}

    Atenciosamente,
    Sistema de Agendamento UFRJ""".format(
        email.usuario.nome,
        email.usuario.nome,
        email.usuario.email
    )

    return (assunto, corpo)

@formata(EmailUsuarioRemovido)
def usuario_removido(email):
    assunto = "Seu cadastro foi removido do sistema"
    corpo = """Prezado {},

    Seu cadastro foi removido do sistema por um administrador.

    Você não será mais capaz de acessar o sistema usando seus dados antigos.

    Atenciosamente,
    Sistema de Agendamento UFRJ""".format(
        email.usuario.nome
    )

    return (assunto,corpo)
