from BancoDados.Rotina.rotina import Rotina
import getpass
import platform


class LogExecucao:

    @staticmethod
    def gerar_log():
        """
        Gera o um log de informação para cada uso da função
        :return:
        """
        nome_arquivo = 'log.txt'
        with open(nome_arquivo, 'w') as arq_log:
            arq_log.write(f'Detalhes do Sistema:\n\n')
            arq_log.write(f'Sistema Operacional: {platform.system()}\n')
            arq_log.write(f'Versao do Sistema: {platform.version()}\n')
            arq_log.write(f'Arquitetura do Sistema: {platform.architecture()}\n')
            arq_log.write(f'Nome do Computador: {platform.node()}\n') # obter o nome do computador
            arq_log.write(f'Plataforma: {platform.platform()}\n')
            arq_log.write(f'Usuario: {getpass.getuser()}\n')

    @staticmethod
    def gerar_log_em_banco(destino):
        Rotina().adicionar_logs(
            sis_operacional=str(platform.system()),
            ver_sistema=str(platform.version()),
            arquit_sistema=str(platform.architecture()[0]),
            nm_pc=str(platform.node()),
            plataform=str(platform.platform().split('.')[0]),
            user=str(getpass.getuser()),
            destino_arquiv=str(destino)
        )
