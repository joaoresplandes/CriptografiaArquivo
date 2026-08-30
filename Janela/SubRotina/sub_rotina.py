from Comum.diretorios import Diretorios
from tkinter import filedialog
from Backup.backup import Backup

class SubRotina:

    @staticmethod
    def selecionar_diretorio_origem():
        diretorio_origem = filedialog.askdirectory(title='Selecioar o Diretório de Origem: ')
        if diretorio_origem:
            Backup().realizar_backup(origem=diretorio_origem, destino=Diretorios.destino)
