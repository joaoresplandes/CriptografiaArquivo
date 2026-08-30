from Chave.caminho_chave import PathChave
from RotinaChave.rotina_chave import RotinaChave
from cryptography.fernet import Fernet
import os


class ExecutarChave:
    def __init__(self):
        self.__chave = os.path.join(PathChave.nm_arquivo_chave, 'chave.key')

    def executar(self):
        if not os.path.exists(self.__chave):
            chave = Fernet.generate_key()
            RotinaChave.salvar_chave_em_disco(chave_backup=chave, nm_arq_chave=self.__chave)
        else:
            chave = RotinaChave.carregar_chave_em_disco(nm_arquivo_chave=self.__chave)
        cipher_suite = Fernet(chave)

        return cipher_suite

    @staticmethod
    def executar_em_banco():
        if not RotinaChave().carregar_chave_de_banco():
            chave = Fernet.generate_key()
            RotinaChave().salvar_chave_em_banco(str(chave))
        else:
            chave = RotinaChave().carregar_chave_de_banco()
        cipher_suite = Fernet(chave)

        return cipher_suite
