#-*- coding: utf-8 -*-
import unittest
from domain.usuario import DTOUsuario, Usuario, IDUsuario
from domain.usuario.nivel_acesso import *
from domain.usuario import ServicoCRUDUsuario
from domain.excecoes import *
from repositorios_memoria import RepositorioUsuarioEmMemoria

class TesteCRUDUsuario(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioUsuarioEmMemoria()
        self.servico = ServicoCRUDUsuario(self.repositorio)

    def dto(self):
        return DTOUsuario("Bernardo", "contato@bamorim.com", "12345678", 0)

    def test_criar_ok(self):
        dto = self.dto()
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
        dto = self.dto()
        self.assertEqual(UsuarioComum(), self.servico.criar(dto).nivelAcesso)

        dto.email = "_"+dto.email
        dto.nivelAcesso = 1
        self.assertEqual(SistemaManutencao(), self.servico.criar(dto).nivelAcesso)

        dto.email = "_"+dto.email
        dto.nivelAcesso = 2
        self.assertEqual(Administrador(), self.servico.criar(dto).nivelAcesso)

        with self.assertRaises(ExcecaoNivelAcessoInvalido):
            dto.email = "_"+dto.email
            dto.nivelAcesso = 3
            self.servico.criar(dto)

    def test_usuario_mesmo_email(self):
        dto = self.dto()
        self.servico.criar(dto)
        with self.assertRaises(ExcecaoUsuarioJaExistente):
            self.servico.criar(dto)

    def test_alterar_sem_senha(self):
        dto = self.dto()
        usuario = self.servico.criar(dto)
        id = usuario.id.id

        dto = DTOUsuario("Novo Nome", "novo@email.com")
        self.servico.alterar(id, dto)

        novo_usuario = self.servico.obter(id)

        # Muda só nome e email
        self.assertEqual("Novo Nome", novo_usuario.nome)
        self.assertEqual("novo@email.com", novo_usuario.email)

        # Senha continua igual
        self.assertTrue(novo_usuario.senhaCriptografada.verificar("12345678"))

    def test_alterar_senha(self):
        dto = self.dto()
        usuario = self.servico.criar(dto)
        id = usuario.id.id

        dto = DTOUsuario(senha="novasenha")
        self.servico.alterar(id, dto)

        novo_usuario = self.servico.obter(id)

        # Senha continua igual
        self.assertFalse(novo_usuario.senhaCriptografada.verificar("12345678"))
        self.assertTrue(novo_usuario.senhaCriptografada.verificar("novasenha"))

    def test_inexistente(self):
        self.assertEqual(None,self.servico.obter(1234))

        with self.assertRaises(ExcecaoUsuarioInexistente):
            self.servico.alterar(1234,self.dto())

    def test_listar(self):
        dto = self.dto()
        dto2 = self.dto()
        dto2.email = "_"+dto2.email
        self.servico.criar(dto)
        self.servico.criar(dto2)

        usuarios = self.servico.listar()
        emails = map(lambda u: u.email, usuarios)
        self.assertIn(dto.email, emails)
        self.assertIn(dto2.email, emails)
