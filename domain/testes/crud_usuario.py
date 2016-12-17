#-*- coding: utf-8 -*-
import unittest
from domain.usuario import DTOUsuario, Usuario, IDUsuario
from domain.usuario.nivel_acesso import *
from domain.usuario import ServicoCRUDUsuario
from domain.excecoes import ExcecaoNivelAcessoInvalido
from repositorios_memoria import RepositorioUsuarioEmMemoria

class TesteCRUDUsuario(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioUsuarioEmMemoria()
        self.servico = ServicoCRUDUsuario(self.repositorio)

    def test_criar_ok(self):
        dto = DTOUsuario("Bernardo", "contato@bamorim.com", "12345678", 0)
        total_anterior = len(self.repositorio.usuarios)
        usuario = self.servico.criar(dto)

        # Verificar que foi criado um Usuario
        self.assertEqual(Usuario, usuario.__class__)
        self.assertEqual("Bernardo", usuario.nome)
        self.assertEqual("contato@bamorim.com", usuario.email)

        # Verificar que foi criado usuario com nível de acesso correto
        self.assertTrue(UsuarioComum(), usuario.nivelAcesso)

        # Verificar que foi criada uma senha criptografada
        self.assertTrue(usuario.senhaCriptografada.verificar("12345678"))
        self.assertFalse(usuario.senhaCriptografada.verificar("outrasenha"))

        # Verificar que inseriu no repositorio
        self.assertEqual(total_anterior + 1, len(self.repositorio.usuarios))
        self.assertEqual(usuario, self.repositorio.obter(usuario.id))

    def test_nivel_acesso(self):
        dto = DTOUsuario("Bernardo", "contato@bamorim.com", "12345678", 0)
        self.assertEqual(UsuarioComum(), self.servico.criar(dto).nivelAcesso)
        dto.nivelAcesso = 1
        self.assertEqual(SistemaManutencao(), self.servico.criar(dto).nivelAcesso)
        dto.nivelAcesso = 2
        self.assertEqual(Administrador(), self.servico.criar(dto).nivelAcesso)
        dto.nivelAcesso = 3

        with self.assertRaises(ExcecaoNivelAcessoInvalido):
            self.servico.criar(dto)
