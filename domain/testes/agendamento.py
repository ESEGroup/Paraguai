#-*- coding: utf-8 -8-
import unittest
from domain.recurso import DTOAgendamento, ServicoAgendamento, DTOIntervalo
from domain.excecoes import ExcecaoAgendamentoRecursoOcupado, ExcecaoAgendamentoRecursoInutilizavel
from repositorios_memoria import RepositorioRecursoEmMemoria, RepositorioUsuarioEmMemoria
from . import fabricas
from .suporte import ServicoEmailEmMemoria
from datetime import timedelta
from domain.email import *
from domain.iso8601 import from_iso

class TesteAgendamento(unittest.TestCase):
    def setUp(self):
        self.repo_recursos = RepositorioRecursoEmMemoria()
        self.repo_usuarios = RepositorioUsuarioEmMemoria()
        self.servico_email = ServicoEmailEmMemoria()
        self.servico = ServicoAgendamento(
            self.repo_recursos,
            self.servico_email,
            self.repo_usuarios
        )
        self.usuario = self.repo_usuarios.inserir(fabricas.admin('admin@admin.com'))
        self.recurso = self.repo_recursos.inserir(fabricas.recurso())

    def get_recurso(self):
        return self.repo_recursos.obter(self.recurso.id)

    def test_ok(self):
        intervalo = DTOIntervalo(
            "2016-12-19T12:00:00Z",
            "2016-12-19T13:00:00Z"
        )
        dto = DTOAgendamento(self.usuario.id, intervalo)
        self.servico.agendar(self.recurso.id, dto)

        novoRecurso = self.get_recurso()
        self.assertEqual(1, len(novoRecurso.agendamentos))
        self.assertEqual(from_iso(intervalo.inicio), novoRecurso.agendamentos[-1].intervalo.inicio)

        self.assertEqual(1, len(self.servico_email.emails))
        ultimoDest, ultimoEmail = self.servico_email.emails[-1]
        self.assertEqual(self.usuario.email, ultimoDest)
        self.assertEqual(EmailAgendamentoConfirmado, ultimoEmail.__class__)

    def test_conflito(self):
        dto = DTOAgendamento(self.usuario.id, DTOIntervalo(
            "2016-12-19T12:00:00Z",
            "2016-12-19T13:00:00Z"
        ))
        self.servico.agendar(self.recurso.id, dto)

        total = len(self.get_recurso().agendamentos)
        with self.assertRaises(ExcecaoAgendamentoRecursoOcupado):
            self.servico.agendar(self.recurso.id, dto)

        self.assertEqual(total, len(self.get_recurso().agendamentos))

    def test_inutilizavel(self):
        self.recurso.utilizavel = False
        self.repo_recursos.atualizar(self.recurso)

        dto = DTOAgendamento(self.usuario.id, DTOIntervalo(
            "2016-12-19T12:00:00Z",
            "2016-12-19T13:00:00Z"
        ))
        with self.assertRaises(ExcecaoAgendamentoRecursoInutilizavel):
            self.servico.agendar(self.recurso.id, dto)

    def test_remover(self):
        intervalo = DTOIntervalo(
            "2016-12-19T12:00:00Z",
            "2016-12-19T13:00:00Z"
        )
        dto = DTOAgendamento(self.usuario.id, intervalo)
        self.servico.agendar(self.recurso.id, dto)

        agendamentosAntes = len(self.get_recurso().agendamentos)
        emailsAntes = len(self.servico_email.emails)
        self.servico.remover(self.recurso.id, dto)
        agendamentosDepois = len(self.get_recurso().agendamentos)

        self.assertEqual(agendamentosDepois, agendamentosAntes - 1)

        self.assertEqual(emailsAntes + 1, len(self.servico_email.emails))
        ultimoDest, ultimoEmail = self.servico_email.emails[-1]
        self.assertEqual(self.usuario.email, ultimoDest)
        self.assertEqual(EmailAgendamentoCancelado, ultimoEmail.__class__)
