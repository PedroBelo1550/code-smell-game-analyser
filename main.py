import tkinter as tk
from tkinter import messagebox

from analyser import Analyser

def processar():
    entrada = entrada_url.get()

    print(entrada)
    Analyser.processar(entrada)

    # Aqui você pode processar a URL ou o caminho inserido
    messagebox.showinfo("Processado", f"URL ou caminho inserido: {entrada}, os dados estão disponíveis na pasta de download")

# Criar janela
janela = tk.Tk()
janela.title("Code smell analyser")

# Campo de entrada
label_url = tk.Label(janela, text="URL Git ou caminho:")
label_url.pack(pady=(10, 0))
entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(pady=(0, 10))

# Botão de processar
botao_processar = tk.Button(janela, text="Processar", command=processar)
botao_processar.pack()

# Executar janela
janela.mainloop()
