from datetime import datetime, timedelta
from domain.recurso import Recurso, Agendamento, TipoRecurso
from domain.intervalo import IntervaloDeTempo
from domain.usuario import Usuario
from domain.usuario.nivel_acesso import Administrador

def admin(email):
    return Usuario(
        nome='Admin',
        email=email,
        senhaCriptografada=None,
        nivelAcesso = Administrador()
    )

def intervalo(delta_semanas=0):
    now = datetime.now()
    hour = timedelta(hours=1)
    delta = timedelta(weeks=delta_semanas)
    return IntervaloDeTempo(now+delta, now+delta+hour)


def recurso(utilizavel=True, agendamentos=[]):
    return Recurso(
        nome = 'Recurso',
        tipo = TipoRecurso('outros'),
        local = 'local',
        utilizavel = utilizavel,
        agendamentos = [Agendamento(intervalo(semanas), idUsuario) for (idUsuario, semanas) in agendamentos]
    )
