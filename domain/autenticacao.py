class ServicoAutenticacao():
    def __init__(self,repositorio):
        self.repositorio = repositorio

    def autenticar_por_id(self, id, senha):
        usuario = self.repositorio.obter(id)
        return self.autenticar_usuario(usuario, senha)

    def autenticar(self, email, senha):
        usuario = self.repositorio.obter_por_email(email)
        return self.autenticar_usuario(usuario)

    def autenticar_usuario(self, usuario, senha):
        if not usuario:
            return None

        if not usuario.senhaCriptografada.verificar(senha):
            return None

        return usuario

