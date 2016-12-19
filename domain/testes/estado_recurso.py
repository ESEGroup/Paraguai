#-*- coding: utf-8 -8-
import unittest
from domain.recurso import Recurso, TipoRecurso, ServicoEstadoRecurso, Agendamento
from domain.usuario import Usuario
from domain.intervalo import IntervaloDeTempo
from domain.excecoes import ExcecaoRecursoInexistente
from repositorios_memoria import RepositorioRecursoEmMemoria
from .suporte import ServicoEmailEmMemoria
from domain.email import EmailRecursoInutilizavel
from datetime import datetime, timedelta

class DummyRepoUsuario():
    def obter(self, id):
        return Usuario(
            nome = "Usuario " + str(id),
            email = str(id)+"@example.com",
            nivelAcesso = None,
            senhaCriptografada = None,
            id = id
        )

class TesteCRUDRecurso(unittest.TestCase):
    def setUp(self):
        self.repo_recurso = RepositorioRecursoEmMemoria()
        self.servico_email = ServicoEmailEmMemoria()
        self.servico = ServicoEstadoRecurso(
            self.repo_recurso,
            DummyRepoUsuario(),
            self.servico_email
        )

    def recurso(self, utilizavel=True, agendamentos=[]):
        now = datetime.now()
        hour = timedelta(hours=1)
        return Recurso(
            nome = 'Recurso',
            tipo = TipoRecurso('outros'),
            local = 'local',
            utilizavel = utilizavel,
            agendamentos = [Agendamento(IntervaloDeTempo(now+delta, now+delta+hour), idUsuario) for (idUsuario, delta) in agendamentos]
        )

    def test_alterar_inutilizavel(self):
        recurso = self.recurso(
            True,
            [
                (1, timedelta(weeks=1)),
                (1, timedelta(weeks=2)),
                (1, timedelta(weeks=-1)),
                (2, timedelta(weeks=-1)),
                (3, timedelta(weeks=1))
            ]
        )
        _id = self.repo_recurso.inserir(recurso).id

        self.servico.alterar_estado(_id, False)
        novoRecurso = self.repo_recurso.obter(_id)
        self.assertEqual(False, novoRecurso.utilizavel)

        self.assertEqual(2, len(novoRecurso.agendamentos))
        inicios = [a.intervalo.inicio for a in novoRecurso.agendamentos]
        self.assertTrue(all([i < datetime.now() for i in inicios]))

        emails = self.servico_email.emails
        self.assertEqual(2, len(emails))
        emails1 = [e for (d,e) in emails if d == "1@example.com"]
        emails3 = [e for (d,e) in emails if d == "3@example.com"]
        self.assertEqual(1,len(emails1))
        self.assertEqual(1,len(emails3))
        email1 = emails1[0]
        email3 = emails3[0]
        self.assertEqual(2,len(email1.agendamentosCancelados))
        self.assertEqual(1,len(email3.agendamentosCancelados))

    def test_alterar_utilizavel(self):
        _id = self.repo_recurso.inserir(self.recurso(True)).id

        self.servico.alterar_estado(_id, True)
        novoRecurso = self.repo_recurso.obter(_id)
        self.assertEqual(True, novoRecurso.utilizavel)

    def test_inexistente(self):
        with self.assertRaises(ExcecaoRecursoInexistente):
            self.servico.alterar_estado(123, False)
