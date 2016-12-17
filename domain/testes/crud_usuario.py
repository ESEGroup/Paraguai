#-*- coding: utf-8 -*-
import unittest
from domain.usuario import DTOUsuario, Usuario, IDUsuario
from domain.usuario.nivel_acesso import *
from domain.usuario import ServicoCRUDUsuario
from repositorios_memoria import RepositorioUsuarioEmMemoria

class TesteCRUDUsuario(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioUsuarioEmMemoria()
        self.servico = ServicoCRUDUsuario(self.repositorio)

    def test_criar_ok(self):
        dto = DTOUsuario("Bernardo", "contato@bamorim.com", "12345678", 0)
        usuario = self.servico.criar(dto)
        self.assertEqual(Usuario, usuario.__class__)
        self.assertEqual("Bernardo", usuario.nome)
        self.assertTrue(UsuarioComum(), usuario.nivelAcesso)
