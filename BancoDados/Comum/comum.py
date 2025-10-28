from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from urllib.parse import quote_plus


class User:
    # def __init__(self):
        # self.LOGIN = credenciais.login
        # self.PWD = credenciais.senha
    LOGIN = 'joao.silva'
    PWD = 'Joao133726@'


class DBCriptografia:
    def __init__(self):
        #  Dados de Conexão de Banco de dados
        self.NAME = 'Criptografia'
        self.PORT = '1433'
        # SERVER = 'PC_Dev'
        self.SERVER = 'localhost'
        self.DRIVER = 'ODBC Driver 17 for SQL Server'
        self.ENGINE = create_engine(
            f"mssql+pyodbc://{User.LOGIN}:{quote_plus(User.PWD)}@{quote_plus(self.SERVER)}:{self.PORT}/{self.NAME}?"
            f"driver={quote_plus(self.DRIVER)}"
        )

class Conexao:

    @staticmethod
    def connect():
        conector = DBCriptografia().ENGINE.connect()

        return conector

# if __name__ == '__main__':
#     try:
#         crds = Credenciais('Banco Dados')
#         con = Conexao(crds).connect()
#         print('Conexão bem sucedida')
#     except OperationalError as e:
#         print(f'Erro de conexão -> {e}')