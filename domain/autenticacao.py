class ServicoAutenticacao():
    def __init__(self,repositorio):
        self.repositorio = repositorio

    def autenticar(self, email, senha):
        usuario = self.repositorio.obter_por_email(email)
        print(usuario)
        if not usuario:
            return None

        if not usuario.senhaCriptografada.verificar(senha):
            return None

        return usuario
