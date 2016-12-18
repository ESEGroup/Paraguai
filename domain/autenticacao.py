from domain.usuario.nivel_acesso import *

MAPEAMENTO = [
    ('admin', Administrador()),
    ('usuario', UsuarioComum())
]

def string_to_nivel_acesso(string):
    try:
        return list(map(lambda kv: kv[1], filter(lambda kv: kv[0] == string, MAPEAMENTO)))[0]
    except IndexError:
        return None

def nivel_acesso_to_string(nivel):
    try:
        return list(map(lambda kv: kv[0], filter(lambda kv: kv[1] == nivel, MAPEAMENTO)))[0]
    except IndexError:
        return None

class ServicoAutenticacao():
    def __init__(self,repositorio):
        self.repositorio = repositorio

    def nivel(self, concessao):
        return string_to_nivel_acesso(concessao['acesso'])

    def usuario(self, concessao):
        if 'id' in concessao:
            return self.repositorio.obter(concessao['id'])

    def autenticar(self, email, senha):
        usuario = self.repositorio.obter_por_email(email)
        print(usuario)
        if not usuario:
            return None

        if not usuario.senhaCriptografada.verificar(senha):
            return None

        return {'id': usuario.id, 'acesso': nivel_acesso_to_string(usuario.nivelAcesso)}
