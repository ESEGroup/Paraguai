"""Fornece dados de teste para os CRUDs de Usuário e Recurso."""

from domain.recurso import Recurso, TipoRecurso, Agendamento
from domain.intervalo import IntervaloDeTempo
from domain.usuario import Usuario, SenhaCriptografada
from domain.usuario.nivel_acesso import *
from domain.usuario.senha_criptografada import SenhaCriptografada

from datetime import datetime, timedelta

def email_para(nome):
    return nome.lower() + "@paraguai.com"

def base_user(i, nome, email, pw=None, nivel=None):
    return Usuario(
        nome = nome,
        email = email,
        senhaCriptografada = SenhaCriptografada(pw or nome.lower()),
        nivelAcesso = nivel,
        id = int(i)
    )

def adm(i, nome):
    return base_user(i, nome, email_para(nome), nome.lower(), Administrador())

def usr(i, nome):
    return base_user(i, nome, email_para(nome), nome.lower(), UsuarioComum())

def sis(i, nome, pw):
    return base_user(i, nome, None, pw, SistemaManutencao())

usuarios = [
    adm(1, "Bernardo"),
    adm(2, "Lucas"),
    adm(3, "Olavo"),
    adm(4, "Varlen"),
    adm(5, "Felipe"),
    usr(6, "Plebeu"),
    sis(7, "Sistema de Manutencao", "019j3elkda")
]

# ---- RECURSO ----

tipos = [
    TipoRecurso("sala"),
    TipoRecurso("projetor")
]

def rec(id, nome, tipo, local,agendamentos=[]):
    return Recurso(nome, tipos[tipo], local, id=id, agendamentos=agendamentos)

recursos = [
    rec(1, "Sala H-201",0,"Fundão,CT,Bloco H", agendamentos=[
        Agendamento(
            idResponsavel = usuarios[0].id,
            intervalo = IntervaloDeTempo(
                inicio = datetime.now()+timedelta(weeks=1),
                fim = datetime.now()+timedelta(weeks=1)+timedelta(hours=2)
            )
        ),
        Agendamento(
            idResponsavel = usuarios[1].id,
            intervalo = IntervaloDeTempo(
                inicio = datetime.now()+timedelta(weeks=-1),
                fim = datetime.now()+timedelta(weeks=-1)+timedelta(hours=2)
            )
        )
    ]),
    rec(2, "Sala H-204",0,"Fundão,CT,Bloco H"),
    rec(3, "Projetor AB-Z",1,"Fundão,CT,Sala D-201"),
    rec(4, "Projetor AB-X",1,"Fundão,CCMN,Sala F-102"),
]
