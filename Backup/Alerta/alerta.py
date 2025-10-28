import tkinter as tk
from tkinter import messagebox


class Alerta:
    def __init__(self):
        self.root_alerta = tk.Tk() # cria o objeto tkinter
        self.root_alerta.withdraw() # some com a janela do tkinter

    @staticmethod
    def exibe_popup(mensagem, sucesso=True):
         if sucesso:
             messagebox.showinfo('Sucesso', message=mensagem) # cria um popup de sucesso
         else:
            messagebox.showerror('Erro', message=mensagem) # cria um popup de erro
