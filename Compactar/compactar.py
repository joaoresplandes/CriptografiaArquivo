from zipfile import ZipFile
import os
from RotinaChave.gerar_chave import ExecutarChave


class Compactar:
    def __init__(self):
        self.cipher_suite = ExecutarChave().executar_em_banco()

    def compactar_arquivo(self, lista_arquivos, nm_arq_backup):
        with ZipFile(nm_arq_backup, 'w') as arquivo_zip:
            for arquivo in lista_arquivos:
                with open(arquivo, 'rb') as arquivo_bite:
                    conteudo = arquivo_bite.read()
                    conteudo_criptografado = self.cipher_suite.encrypt(conteudo)

                nome_arquivo = os.path.basename(arquivo)
                arquivo_zip.writestr(nome_arquivo, conteudo_criptografado)

class Descompactar:
    pass
