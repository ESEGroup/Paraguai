from domain.email import *
from datetime import datetime

def formata(classe):
    def decorador(f):
        f.aceita = lambda email: email.__class__ == classe
        return f
    return decorador

def formata_intervalo(intervalo):
    return "{} até {}".format(
        datetime.strftime(intervalo.inicio, "%d/%m/%Y das %H:%M"),
        datetime.strftime(intervalo.fim, "as %H:%M")
    )

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

@formata(EmailRecursoInutilizavel)
def recurso_inutilizavel(email):
    plural = len(email.agendamentosCancelados) > 1
    if plural:
        assunto = "Seus agendamentos do recurso {} foram cancelados"
    else:
        assunto = "Seu agendamento do recurso {} foi cancelado"

    assunto = assunto.format(email.recurso.nome)

    corpo_por_agendamento = [
        formata_intervalo(a.intervalo) for a in email.agendamentosCancelados
    ]
    corpo_agendamentos = str.join('\n', corpo_por_agendamento)

    s = "s" if plural else ""
    corpo = """Prezado {},

    {}
    {} apresentou inconformidade e se encontra em reparo.

    Seguem abaixo os dados relacionados ao{} agendamento{} cancelado{}:

    Recurso: {}
    Categoria: {}

    Período{}:
    {}

    Atenciosamente,
    Sistema de Agendamento UFRJ
    """.format(
        email.usuario.nome,
        assunto,
        email.recurso.nome,
        s,s,s,
        email.recurso.nome,
        email.recurso.tipo.nome,
        s,
        corpo_agendamentos
    )

    return (assunto, corpo)

@formata(EmailAgendamentoConfirmado)
def agendamento_confirmado(email):
    assunto = "Confirmação de agendamento de recurso"
    corpo = """Prezado {},

    Seu agendamento foi efetuado com sucesso! Seguem abaixo os dados relacionados:

    Recurso: {}
    Categoria: {}
    Período: {}

    Atenciosamente,
    Sistema de Agendamento UFRJ""".format(
        email.usuario.nome,
        email.recurso.nome,
        email.recurso.tipo.nome,
        formata_intervalo(email.agendamento.intervalo)
    )

    return (assunto, corpo)

@formata(EmailAgendamentoCancelado)
def agendamento_cancelado(email):
    assunto = "Confirmação de cancelamento de agendamento"
    corpo = """Prezado {},

    Esta é uma mensagem de confirmação de que o agendamento a seguir foi cancelado:

    Recurso: {}
    Categoria: {}
    Periodo: {}

    Atenciosamente,
    Sistema de Agendamento UFRJ""".format(
        email.usuario.nome,
        email.recurso.nome,
        email.recurso.tipo.nome,
        formata_intervalo(email.agendamento.intervalo)
    )

    return (assunto, corpo)
