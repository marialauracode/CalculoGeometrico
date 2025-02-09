from tkinter import *

def calculoRetangulo():
    try:
        comprimento = float(entradaComprimento.get())
        largura = float(entradaLargura.get())
        calculo = comprimento * largura
        label_resultado_calculo.config(text=f"{calculo}")

    except ValueError:
        label_resultado_calculo.config(text=f"{calculo}")

def limparEntrada():
    entradaComprimento.delete(0, END)
    entradaLargura.delete(0, END)
    label_resultado_calculo.config(text="0")

window = Tk()
window.geometry('300x300')
window.title("Cálculo da Área do Retângulo")  

label_comprimento = Label(window, text="Comprimento do Retângulo:")
label_comprimento.pack()
entradaComprimento = Entry(window)
entradaComprimento.pack(pady=5)

label_largura = Label(window, text="Largura do Retângulo:")
label_largura.pack()
entradaLargura = Entry(window)
entradaLargura.pack(pady=5)

botao_calcular = Button(window, text="Calcular", command=calculoRetangulo)
botao_calcular.pack(pady=5)

botao_limpar = Button(window, text="Limpar", command=limparEntrada)
botao_limpar.pack(pady=5)

label_resultado = Label(window, text="Resultado: ", fg="black")
label_resultado.pack(pady=2)

label_resultado_calculo = Label(window, text="0", fg="red")
label_resultado_calculo.pack()

window.mainloop()

