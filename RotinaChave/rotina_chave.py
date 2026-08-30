from BancoDados.Rotina.rotina import Rotina


class RotinaChave:

    @staticmethod
    def salvar_chave_em_disco(chave_backup, nm_arq_chave):
        """
        Salva a chave criptografada em um local especifico
        :param chave_backup: chave criptografada pelo metodo Fernet.generate_key
        :param nm_arq_chave: local onde a chave será salva
        :return:
        """
        with open(nm_arq_chave, 'wb') as arquivo_chave:
            arquivo_chave.write(chave_backup)

    # função para carregar a chave de criptografia do backup em disco
    @staticmethod
    def carregar_chave_em_disco(nm_arquivo_chave):
        """
        Carrega a chave em memoria para ser usada no processo
        :param nm_arquivo_chave: caminho de origem da chave
        :return: chave criptografada
        """
        with open(nm_arquivo_chave, 'rb') as arquivo_chave:
            return arquivo_chave.read()

    @staticmethod
    def salvar_chave_em_banco(chave_backup: str):
        chave_backup = chave_backup[2:len(chave_backup)-1]
        Rotina().adicionar_chave_banco(chave_backup)


    @staticmethod
    def carregar_chave_de_banco():
        chave = Rotina().visualizar_chave_banco()

        return chave


