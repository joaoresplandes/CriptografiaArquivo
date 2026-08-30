class Credenciais:
    def __init__(self, sistema):
        self.sistema = sistema
        self._login = self.obter_login()
        self._senha = self.obter_senha()

    @property
    def login(self):
        return self._login

    @property
    def senha(self):
        return self._senha

    def obter_login(self):
        login = input(f'Login do {self.sistema}: ')

        return login

    def obter_senha(self):
        senha = input(f'Senha do {self.sistema}: ')

        return senha
