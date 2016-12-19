from domain.excecoes import ExcecaoRecursoInexistente
from domain.usuario import Usuario
from domain.email import EmailRecursoInutilizavel
from datetime import datetime

class ServicoEstadoRecurso():
    def __init__(self, repo_recurso, repo_usuario, servico_email):
        self.repo_recurso = repo_recurso
        self.repo_usuario = repo_usuario
        self.servico_email = servico_email

    def alterar_estado(self, _id, utilizavel):
        """Altera o estado de um recurso pelo seu id para disponível ou não
        :param _id: Id do recurso a ser alterado
        :param utilizavel: Utilizável ou não (Booleano)"""

        recurso = self.repo_recurso.obter(_id)
        if not recurso:
            raise ExcecaoRecursoInexistente
        recurso.utilizavel = utilizavel

        if not utilizavel:
            self.cancelar_agendamentos(recurso)

        self.repo_recurso.atualizar(recurso)

    def cancelar_agendamentos(self, recurso):
        agora = datetime.now()
        agendamentosRemovidos = [a for a in recurso.agendamentos if a.intervalo.inicio >= agora]
        agendamentosMantidos = [a for a in recurso.agendamentos if a.intervalo.inicio < agora]

        recurso.agendamentos = agendamentosMantidos

        self.enviar_emails(recurso, agendamentosRemovidos)

    def enviar_emails(self, recurso, agendamentos):
        id_usuarios = set([a.idResponsavel for a in agendamentos])
        usuarios = [self.repo_usuario.obter(i) for i in id_usuarios]
        usuarios = [u for u in usuarios if u]
        emails = [EmailRecursoInutilizavel(
            u,
            recurso,
            list(filter(lambda a: a.idResponsavel == u.id, agendamentos))
        ) for u in usuarios]

        for email in emails:
            self.servico_email.enviar(email.usuario.email, email)
