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
        total_anterior = len(self.repositorio.usuarios)
        usuario = self.servico.criar(dto)

        self.assertEqual(Usuario, usuario.__class__)
        self.assertEqual("Bernardo", usuario.nome)
        self.assertTrue(UsuarioComum(), usuario.nivelAcesso)

        # Verificar que inseriu no repositorio
        self.assertEqual(total_anterior + 1, len(self.repositorio.usuarios))
        self.assertEqual(usuario, self.repositorio.obter(usuario.id))
