from .recurso import Recurso
from .tipo import TipoRecurso
from .filtro import FiltroRecurso
from domain.IntervaloDeTempo import IntervaloDeTempo
from domain.agendamento import Agendamento
from domain.excecoes import *

class ServicoAgendamento():
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def listar(self):
        return [
          (agendamento,recurso)
          for recurso in self.repositorio.listar()
          for agendamento in recurso.agendamentos
        ]

    def listar_por_usuario(self, IDUsuario):
        return [
          (agendamento,recurso)
          for recurso in self.repositorio.listar()
          for agendamento in recurso.agendamentos
          if agendamento.responsavel == IDUsuario
        ]

    def agendar(self, IDRecurso, IDUsuario, intervalo):
        recurso = self.repositorio.obter(IDRecurso)
        if not recurso:
            raise ExcecaoRecursoInexistente

        # Verificar se o recurso já tem um agendamento sobreposto
        for agendamento in recurso.agendamentos:
            if intervalo.intercede(agendamento.intervalo):
                raise ExcecaoAgendamentoRecursoOcupado

        # Verificar se o recurso está indisponível
        if not recurso.utilizavel:
            raise ExcecaoAgendamentoRecursoIndisponivel

        novo_agendamento = Agendamento(intervalo, IDUsuario)
        recurso.agendamentos.append(novo_agendamento)
        self.repositorio.atualizar(recurso)


    def remover(self, IDRecurso, intervalo):
        recurso = self.repositorio.obter(IDRecurso)
        if not recurso:
            raise ExcecaoRecursoInexistente
        recurso.agendamentos = [
            agendamento
            for agendamento in recurso.agendamentos
            if not agendamento.intervalo.intercede(intervalo)
        ]
        self.repositorio.atualizar(recurso)
