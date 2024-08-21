import tkinter as tk
from functools import partial

class Calculadora:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("250x250")

        self.entrada = tk.Entry(self.janela, width=20)
        self.entrada.grid(row=0, column=0, columnspan=4)

        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for botao in botoes:
            cmd = partial(self.click_botao, botao)
            tk.Button(self.janela, text=botao, width=5, command=cmd).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.janela, text="C", width=10, command=self.limpar).grid(row=row_val, column=0, columnspan=4)

        self.janela.mainloop()

    def click_botao(self, botao):
        if botao == '=':
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(resultado))
            except Exception as e:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Erro")
        else:
            self.entrada.insert(tk.END, botao)

    def limpar(self):
        self.entrada.delete(0, tk.END)

if __name__ == "__main__":
    calculadora = Calculadora()