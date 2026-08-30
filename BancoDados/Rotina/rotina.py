from sqlalchemy import text
from BancoDados.Comum.comum import Conexao
from datetime import datetime

class Rotina:
    def __init__(self):
        self._cursor = Conexao().connect()
        self.data_criacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def finalizar_cursor(self):
        self._cursor.commit()
        self._cursor.close()

    def adicionar_logs(self, sis_operacional, ver_sistema, arquit_sistema, nm_pc, plataform, user, destino_arquiv):
        self._cursor.execute(
            text(
                '''Insert Into Logs (sis_operacional, ver_sistema, arquit_sistema, nm_pc, plataform, usuario, destino_arquivo, data_update) 
                VALUES (:sis_oper, :ver_sis, :arq_sis, :nm_pc, :plataform, :usuario, :destino, :update)'''
            ),
            {
                'sis_oper':str(sis_operacional),
                'ver_sis': str(ver_sistema),
                'arq_sis': str(arquit_sistema),
                'nm_pc': str(nm_pc),
                'plataform':str(plataform),
                'usuario': str(user),
                'destino': str(f'r{destino_arquiv}'),
                'update': str(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            }
        )
        self.finalizar_cursor()

    def adicionar_chave_banco(self, chave):
        self._cursor.execute(
            text('Insert Into chave_cripto(chave, data_criacao) VALUES (:chave, :data_criacao)'),
                {
                    'chave':str(chave),
                    'data_criacao':str(self.data_criacao)
                })
        self.finalizar_cursor()

    def visualizar_chave_banco(self):
        resultado = self._cursor.execute(text(f'Select top(1) chave from chave_cripto')).fetchone()
        self._cursor.close()
        try:
            return resultado[0]
        except TypeError:
            return False
