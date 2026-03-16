import tkinter as tk

historico = []

def clicar(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        conta = entrada.get()
        resultado = eval(conta)

        historico.append(f"{conta} = {resultado}")
        atualizar_historico()

        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)

    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def atualizar_historico():
    caixa_historico.delete(0, tk.END)

    for item in historico:
        caixa_historico.insert(tk.END, item)

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("350x400")

entrada = tk.Entry(janela, font=("Arial",20))
entrada.pack(fill="x", padx=10, pady=10)

entrada.bind("<Return>", lambda event: calcular())

frame_botoes = tk.Frame(janela)
frame_botoes.pack()

botoes = [
["1","2","3","+"],
["4","5","6","-"],
["7","8","9","*"],
["0","C","=","/"]
]

for linha in botoes:

    frame_linha = tk.Frame(frame_botoes)
    frame_linha.pack()

    for botao in linha:

        if botao == "=":
            comando = calcular

        elif botao == "C":
            comando = limpar

        else:
            comando = lambda x=botao: clicar(x)

        tk.Button(
            frame_linha,
            text=botao,
            width=5,
            height=2,
            font=("Arial",14),
            command=comando
        ).pack(side="left", padx=2, pady=2)

caixa_historico = tk.Listbox(janela, height=8)
caixa_historico.pack(fill="both", padx=10, pady=10)

entrada.focus()

janela.mainloop()