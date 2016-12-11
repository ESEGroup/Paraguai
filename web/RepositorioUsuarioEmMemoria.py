from domain import RepositorioUsuario, Usuario

class RepositorioUsuarioEmMemoria(RepositorioUsuario):
    def __init__(self):
        self.usuarios = []

    def criar(self, usuario):
        usuario.id = len(self.usuarios) + 1
        self.usuarios.append(usuario)
        return usuario

    def todos(self):
        return self.usuarios
