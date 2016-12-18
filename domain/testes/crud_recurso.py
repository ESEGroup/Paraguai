#-*- coding: utf-8 -8-
import unittest
from domain.recurso import Recurso, ServicoCRUDRecurso, TipoRecurso, DTORecurso, DTOBuscaRecurso
from domain.excecoes import ExcecaoRecursoInexistente
from repositorios_memoria import RepositorioRecursoEmMemoria

class TesteCRUDRecurso(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioRecursoEmMemoria()
        self.servico = ServicoCRUDRecurso(self.repositorio)

    def test_criar_ok(self):
        dto = DTORecurso("Projetor 1", "projetor", "h201")
        total_anterior = len(self.repositorio.recursos)
        recurso = self.servico.criar(dto)

        self.assertEqual(Recurso, recurso.__class__)
        self.assertEqual("Projetor 1", recurso.nome)
        self.assertEqual("h201", recurso.local)
        self.assertEqual(TipoRecurso("projetor"), recurso.tipo)
        self.assertEqual([], recurso.agendamentos)

        # Verificar que foi salvo no repositorio

        self.assertEqual(total_anterior + 1, len(self.repositorio.recursos))
        self.assertEqual(recurso, self.repositorio.obter(recurso.id))

    def test_alterar(self):
        dto = DTORecurso("Projetor 1", "projetor", "h201")
        recurso = self.servico.criar(dto)

        dto.nome = "Projetor Novo"
        self.servico.alterar(int(recurso.id), dto)

        recurso_novo = self.repositorio.obter(recurso.id)
        self.assertEqual("Projetor Novo", recurso_novo.nome)

    def test_inexistente(self):
        dto = DTORecurso("Projetor 1", "projetor", "h201")
        with self.assertRaises(ExcecaoRecursoInexistente):
            self.servico.alterar(1234, dto)

        with self.assertRaises(ExcecaoRecursoInexistente):
            self.servico.remover(1234)

    def test_remover(self):
        dto = DTORecurso("Projetor 1", "projetor", "h201")
        recurso = self.servico.criar(dto)

        self.servico.remover(recurso.id)

        self.assertEqual(None, self.repositorio.obter(recurso.id))

    def test_listar(self):
        dto1 = DTORecurso("Projetor 1", "projetor", "h201")
        dto2 = DTORecurso("Projetor 2", "projetor", "h201")

        self.servico.criar(dto1)
        self.servico.criar(dto2)

        nomes = list(map(lambda r: r.nome, self.servico.listar()))
        self.assertIn(dto1.nome, nomes)
        self.assertIn(dto2.nome, nomes)

    def test_buscar(self):
        dto1 = DTORecurso("Projetor 1", "projetor", "h201")
        dto2 = DTORecurso("Projetor 2", "projetor", "h201")
        dto3 = DTORecurso("Projetor 2", "projetor", "h202")

        self.servico.criar(dto1)
        self.servico.criar(dto2)
        self.servico.criar(dto3)

        busca = DTOBuscaRecurso(nome = "Projetor 2", local="h201")
        recursos = self.servico.buscar(busca)
        self.assertEqual(1, len(recursos))
        self.assertEqual("Projetor 2", recursos[0].nome)
        self.assertEqual("h201", recursos[0].local)
