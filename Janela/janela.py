import tkinter as tk
from Janela.SubRotina.sub_rotina import SubRotina


class Janela:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def janela_backup(self):
        janela_principal = tk.Toplevel(self.root)
        janela_principal.title('Backup de Arquivos')

        tk.Button(
            janela_principal,
            text='Diretório de Origem',
            command=SubRotina.selecionar_diretorio_origem
        ).pack()
        janela_principal.protocol('WM_DELETE_WINDOW', self.root.quit)

        self.root.mainloop()