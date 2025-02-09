from tkinter import *

def calculoQuadrado():
    try:
        lado = float(entrada.get())
        calculo = lado**2
        label_resultado_calculo.config(text=f"{calculo}")

    except ValueError: 
        label_resultado_calculo.config(text="ERRO: Entrada inválida")

def limparValor():
    entrada.delete(0, END)
    label_resultado_calculo.config(text="0")  


window = Tk()  
window.geometry('300x300')  
window.title("Cálculo da Área do Quadrado")

label_lado = Label(window, text= "Lado do Quadrado:")
label_lado.pack()
entrada = Entry(window)
entrada.pack(pady=5)

botao_calcular = Button(window, text="Calcular", command=calculoQuadrado)
botao_calcular.pack(pady=5)

botao_limpar = Button(window, text="Limpar",command=limparValor)
botao_limpar.pack(pady=5)

label_resultado = Label(window, text="Resultado: ", fg="black")
label_resultado.pack(pady=2)

label_resultado_calculo = Label(window, text="0", fg="red")
label_resultado_calculo.pack()

window.mainloop()



    