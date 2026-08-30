from Backup.LogExecucao.log_execucao import LogExecucao
from Backup.SubRotinasBackup.sub_rotinas import SubRotinas
from Backup.Alerta.alerta import Alerta
from Compactar.compactar import Compactar
import os


class Backup:
    def __init__(self):
        self.data_arquivo = SubRotinas.data_arquivo()

    def realizar_backup(self, origem, destino):
        lista_arquivo = SubRotinas.buscar_arquivos_csv(origem)

        if not lista_arquivo:
            Alerta.exibe_popup("Nenhum arquivo CSV encontrado", sucesso=False)
        else:
            caminho_final = rf'{origem}\backup_{self.data_arquivo}.zip'
            try:
                SubRotinas.verifica_diretorio(os.path.basename(caminho_final))
                Compactar().compactar_arquivo(lista_arquivos=lista_arquivo, nm_arq_backup=caminho_final)
                Alerta.exibe_popup('Compactação e criptografia realizadas com sucesso')
            except Exception as e:
                Alerta.exibe_popup('Erro na compactação e criptografia', sucesso=False)
            try:
                SubRotinas.mover_arquivo_backup(arquivo_backup=caminho_final, destino=destino)
                Alerta.exibe_popup('Backup realizado com sucesso')
                LogExecucao().gerar_log_em_banco(caminho_final)
            except Exception as e:
                Alerta.exibe_popup(f'Erro durante o backup: {str(e)}', sucesso=False)
