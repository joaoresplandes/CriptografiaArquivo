from Comum.diretorios import Diretorios
from shutil import move
from datetime import datetime
import os


class SubRotinas:

    @staticmethod
    def verifica_diretorio(arquivo: str):
        """
        Verifica se o arquivo em questão esta em diretorio destino, caso sim o remove, para não haver duplicidade
        :param arquivo: nome_arquivo
        :return:
        """
        if arquivo in os.listdir(Diretorios.destino):
            os.remove(os.path.join(Diretorios.destino, arquivo))

    @staticmethod
    def mover_arquivo_backup(arquivo_backup: str, destino: str):
        """
        Se a pasta de destino não existir, a cria. E move o arquino da pasta de origem para a pasta de destino
        :param arquivo_backup: caminho absoluto do arquivo de inicio
        :param destino: caminho de destino para onde o arquivo deve ser movido
        :return:
        """
        if not os.path.exists(destino):
            os.makedirs(destino)

        move(arquivo_backup, destino)

    @staticmethod
    def buscar_arquivos_csv(caminho_origem: str) -> list:
        """
        Lista todos os arquivos da pasta caminho_origem, onde contem todos os arquivos a serem compactados
        :param caminho_origem: caminho origem dos arquivos
        :return: lista com os caminhos absolutos dos arquivos
        """
        lista_arquivos = []
        for arquivo in os.listdir(caminho_origem):
            if arquivo.endswith('.csv'):
                lista_arquivos.append(rf'{caminho_origem}/{arquivo}')
        return lista_arquivos

    @staticmethod
    def data_arquivo():
        """
        Gera a data de hoje no padrao brasileiro para colocar no nome do arquivo
        :return: data e hora em string
        """
        data_arquivo = datetime.now().strftime("%d%m%Y_%H%M%S")

        return data_arquivo
