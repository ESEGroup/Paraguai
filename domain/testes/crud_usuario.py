#-*- coding: utf-8 -*-
import unittest
from domain.usuario import DTOUsuario, Usuario
from domain.usuario.nivel_acesso import *
from domain.usuario import ServicoCRUDUsuario
from domain.excecoes import *
from repositorios_memoria import RepositorioUsuarioEmMemoria
from .suporte import ServicoEmailEmMemoria
from domain.email import *

class TesteCRUDUsuario(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioUsuarioEmMemoria([])
        self.servico_email = ServicoEmailEmMemoria()
        self.servico = ServicoCRUDUsuario(self.repositorio, self.servico_email)

    def dto(self):
        return DTOUsuario("Bernardo", "contato@bamorim.com", "12345678", 0)

    def test_criar_ok(self):
        dto = self.dto()
        total_anterior = len(self.repositorio.listar())
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
        self.assertEqual(total_anterior + 1, len(self.repositorio.listar()))
        self.assertEqual(usuario.id, self.repositorio.obter(usuario.id).id)

        # Verifica que um email foi enviado ao novo usuário
        self.assertEqual(1,len(self.servico_email.emails))
        ultimoDestinatario, ultimoEmail = self.servico_email.emails[-1]
        self.assertEqual(usuario.email, ultimoDestinatario)
        self.assertIsInstance(ultimoEmail, EmailUsuarioCadastrado)
        self.assertEqual(dto.senha, ultimoEmail.senha)
        self.assertEqual(usuario, ultimoEmail.usuario)

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
        id = usuario.id

        dto = DTOUsuario("Novo Nome", "novo@email.com")
        self.servico.alterar(id, dto)

        novo_usuario = self.servico.obter(id)

        # Muda só nome e email
        self.assertEqual("Novo Nome", novo_usuario.nome)
        self.assertEqual("novo@email.com", novo_usuario.email)

        # Senha continua igual
        self.assertTrue(novo_usuario.senhaCriptografada.verificar("12345678"))

        # Um email foi enviado
        ultimoDestinatario, ultimoEmail = self.servico_email.emails[-1]
        self.assertEqual("novo@email.com", ultimoDestinatario)
        self.assertIsInstance(ultimoEmail, EmailUsuarioAlterado)
        self.assertEqual(usuario.id, ultimoEmail.usuario.id)

    def test_alterar_senha(self):
        dto = self.dto()
        usuario = self.servico.criar(dto)
        id = usuario.id

        dto = DTOUsuario(senha="novasenha")
        self.servico.alterar(id, dto)

        novo_usuario = self.servico.obter(id)

        # Senha continua igual
        self.assertFalse(novo_usuario.senhaCriptografada.verificar("12345678"))
        self.assertTrue(novo_usuario.senhaCriptografada.verificar("novasenha"))

    def test_inexistente(self):
        with self.assertRaises(ExcecaoUsuarioInexistente):
            self.assertEqual(None,self.servico.obter(1234))

        with self.assertRaises(ExcecaoUsuarioInexistente):
            self.servico.remover(1234)

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

    def test_remover(self):
        usuario = self.servico.criar(self.dto())

        self.servico.remover(usuario.id)
        self.assertEqual(None, self.repositorio.obter(usuario.id))

        # Um email foi enviado
        ultimoDestinatario, ultimoEmail = self.servico_email.emails[-1]
        self.assertEqual(usuario.email, ultimoDestinatario)
        self.assertIsInstance(ultimoEmail, EmailUsuarioRemovido)
        self.assertEqual(usuario.id, ultimoEmail.usuario.id)

    def test_remocao_dupla(self):
        id = self.servico.criar(self.dto()).id

        self.servico.remover(id)
        with self.assertRaises(ExcecaoUsuarioInexistente):
            self.servico.remover(id)
