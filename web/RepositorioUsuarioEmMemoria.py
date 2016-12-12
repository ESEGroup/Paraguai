from domain import RepositorioUsuario, Usuario

class RepositorioUsuarioEmMemoria(RepositorioUsuario):
    def __init__(self):
        self.usuarios = []

    #param: dados: DTOUsuario
    def criar(self, dados):
        _id = len(self.usuarios) + 1
        usuario = Usuario(dados.nome, dados.email, 1, dados.senha, _id)       
        self.usuarios.append(usuario)
        return usuario

    def todos(self):
        return self.usuarios
