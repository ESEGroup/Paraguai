class DTOUsuario:
    """Essa classe modela um Data Transmission Object para Usuários. É usada em cadastros
       e atualizações de Usuários. A senha usada aqui é uma senha
       em texto plano não-criptografada.
       :param nome: Nome do usuário
       :param email: Endereço de e-mail
       :param senha: Senha em texto plano não criptografada
       :param nivelAcesso: Número inteiro que indica o nível de acesso (0: UsuarioComum, 1: SistemaDeManutencao, 2: Administrador)
       """

    def __init__(self, nome=None, email=None, senha=None, nivelAcesso=0):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.nivelAcesso = nivelAcesso
