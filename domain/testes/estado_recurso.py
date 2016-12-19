#-*- coding: utf-8 -8-
import unittest
from domain.recurso import Recurso, TipoRecurso, ServicoEstadoRecurso
from domain.excecoes import ExcecaoRecursoInexistente
from repositorios_memoria import RepositorioRecursoEmMemoria

class TesteCRUDRecurso(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioRecursoEmMemoria()
        self.servico = ServicoEstadoRecurso(self.repositorio)

    def recurso(self, utilizavel=True):
        return Recurso(
            nome = 'Recurso',
            tipo = TipoRecurso('outros'),
            local = 'local',
            utilizavel = utilizavel
        )

    def test_alterar_inutilizavel(self):
        _id = self.repositorio.criar(self.recurso(True)).id

        self.servico.alterar_estado(_id, False)
        novoRecurso = self.repositorio.obter(_id)
        self.assertEqual(False, novoRecurso.utilizavel)

    def test_alterar_utilizavel
        _id = self.repositorio.criar(self.recurso(True)).id

        self.servico.alterar_estado(_id, True)
        novoRecurso = self.repositorio.obter(_id)
        self.assertEqual(True, novoRecurso.utilizavel)

    def test_inexistente(self):
        with self.assertRaises(ExcecaoRecursoInexistente):
            self.servico.alterar_estado(123, False)
