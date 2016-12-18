"""Fornece dados de teste para os CRUDs de Usuário e Recurso."""

from domain.recurso import Recurso, TipoRecurso
from domain.usuario import Usuario
from domain.usuario.nivel_acesso import *
from domain.usuario.senha_criptografada import SenhaCriptografada

def email_para(nome):
    return nome.lower() + "@paraguai.com"

def base_user(i, nome, email=None, nivel=None):
    return Usuario(nome, email or email_para(nome), SenhaCriptografada(nome.lower()), nivel, int(i))

def adm(i, nome, email=None):
    return base_user(i, nome, email, Administrador())

def usr(i, nome, email=None):
    return base_user(i, nome, email, UsuarioComum())

def sis(i, nome, email=None):
    return base_user(i, nome, email, SistemaManutencao())

usuarios = [
    adm(1, "Bernardo"),
    adm(2, "Lucas"),
    adm(3, "Olavo"),
    adm(4, "Varlen"),
    adm(5, "Felipe"),
    usr(6, "Plebeu"),
    sis(7, "Breno")
]

# ---- RECURSO ----

tipos = [
    TipoRecurso("sala"),
    TipoRecurso("projetor")
]

def rec(id, nome, tipo, local):
    return Recurso(nome, tipos[tipo], local, id=id)

recursos = [
    rec(1, "Sala H-201",0,"Fundão,CT,Bloco H"),
    rec(2, "Sala H-204",0,"Fundão,CT,Bloco H"),
    rec(3, "Projetor AB-Z",1,"Fundão,CT,Sala D-201"),
    rec(4, "Projetor AB-X",1,"Fundão,CCMN,Sala F-102"),
]
