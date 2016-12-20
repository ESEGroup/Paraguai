from domain.email import EmailAgendamentoCancelado, EmailAgendamentoConfirmado
from domain.intervalo import IntervaloDeTempo
from domain.excecoes import *
from domain.iso8601 import from_iso
from .recurso import Recurso
from .tipo import TipoRecurso
from .filtro import FiltroRecurso
from .agendamento import Agendamento
import pprint

def dto_to_intervalo(dto):
    return IntervaloDeTempo(from_iso(dto.inicio), from_iso(dto.fim))

class ServicoAgendamento():
    def __init__(self, repositorio, servicoEmail, repoUsuarios):
        self.repositorio = repositorio
        self.servicoEmail = servicoEmail
        self.repoUsuarios = repoUsuarios

    def agendar(self, IDRecurso, dto):
        intervalo = dto_to_intervalo(dto.intervalo)
        recurso = self.repositorio.obter(IDRecurso)
        if not recurso:
            raise ExcecaoRecursoInexistente

        responsavel = self.repoUsuarios.obter(dto.idResponsavel)
        if not responsavel:
            raise ExcecaoUsuarioInexistente

        # Verificar se o recurso já tem um agendamento sobreposto
        for agendamento in recurso.agendamentos:
            if intervalo.intercede(agendamento.intervalo):
                raise ExcecaoAgendamentoRecursoOcupado

        # Verificar se o recurso está indisponível
        if not recurso.utilizavel:
            raise ExcecaoAgendamentoRecursoInutilizavel

        novoAgendamento = Agendamento(intervalo, dto.idResponsavel)
        recurso.agendamentos.append(novoAgendamento)

        self.repositorio.atualizar(recurso)

        self.servicoEmail.enviar(responsavel.email, EmailAgendamentoConfirmado(
            responsavel,
            recurso,
            novoAgendamento
        ))


    def remover(self, IDRecurso, dto):
        intervalo = dto_to_intervalo(dto.intervalo)
        recurso = self.repositorio.obter(IDRecurso)
        if not recurso:
            raise ExcecaoRecursoInexistente

        agendamentoARemover = Agendamento(intervalo, dto.idResponsavel)
        if(not agendamentoARemover in recurso.agendamentos):
            raise ExcecaoAgendamentoInexistente

        responsavel = self.repoUsuarios.obter(dto.idResponsavel)
        if not responsavel:
            raise ExcecaoUsuarioInexistente

        recurso.agendamentos.remove(agendamentoARemover)

        self.repositorio.atualizar(recurso)

        self.servicoEmail.enviar(responsavel.email, EmailAgendamentoCancelado(
            responsavel,
            recurso,
            agendamentoARemover
        ))

