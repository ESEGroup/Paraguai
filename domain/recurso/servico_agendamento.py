from domain.email import EmailAgendamentoCancelado, EmailAgendamentoConfirmado
from domain.intervalo import IntervaloDeTempo
from domain.excecoes import *
from .recurso import Recurso
from .tipo import TipoRecurso
from .filtro import FiltroRecurso
from .agendamento import Agendamento

class ServicoAgendamento():
    def __init__(self, repositorio, servicoEmail, repoUsuarios):
        self.repositorio = repositorio
        self.servicoEmail = servicoEmail
        self.repoUsuarios = repoUsuarios

    def agendar(self, IDRecurso, dto):
        recurso = self.repositorio.obter(IDRecurso)
        if not recurso:
            raise ExcecaoRecursoInexistente

        responsavel = self.repoUsuarios.obter(dto.idResponsavel)
        if not responsavel:
            raise ExcecaoUsuarioInexistente

        # Verificar se o recurso já tem um agendamento sobreposto
        for agendamento in recurso.agendamentos:
            if dto.intervalo.intercede(agendamento.intervalo):
                raise ExcecaoAgendamentoRecursoOcupado

        # Verificar se o recurso está indisponível
        if not recurso.utilizavel:
            raise ExcecaoAgendamentoRecursoInutilizavel

        novoAgendamento = Agendamento(dto.intervalo, dto.idResponsavel)
        recurso.agendamentos.append(novoAgendamento)

        self.repositorio.atualizar(recurso)

        self.servicoEmail.enviar(responsavel.email, EmailAgendamentoConfirmado(
            responsavel,
            recurso,
            novoAgendamento
        ))


    def remover(self, IDRecurso, dto):
        recurso = self.repositorio.obter(IDRecurso)
        if not recurso:
            raise ExcecaoRecursoInexistente

        responsavel = self.repoUsuarios.obter(dto.idResponsavel)
        if not responsavel:
            raise ExcecaoUsuarioInexistente

        agendamentoARemover = Agendamento(dto.intervalo, dto.idResponsavel)
        if(not agendamentoARemover in recurso.agendamentos):
            raise ExcecaoAgendamentoInexistente

        recurso.agendamentos.remove(agendamentoARemover)

        self.repositorio.atualizar(recurso)

        self.servicoEmail.enviar(responsavel.email, EmailAgendamentoCancelado(
            responsavel,
            recurso,
            agendamentoARemover
        ))
