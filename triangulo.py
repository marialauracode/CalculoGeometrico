from tkinter import *

def calculoTriangulo():
    try: 
     base = float(entradaBase.get())
     altura = float(entradaAltura.get())
     calculo = ((base*altura)/2)
     label_resultado_calculo.config(text=f"{calculo}")

    except ValueError:
       label_resultado_calculo.config(text="ERRO: Entradas inválidas") 

def limparEntrada():
   entradaBase.delete(0, END)
   entradaAltura.delete(0, END)
   label_resultado_calculo.config(text="0")  

window = Tk()      
window.geometry('300x300')
window.title("Cálculo da Área do Triângulo")

label_base = Label(window, text="Base do Triângulo:")
label_base.pack()
entradaBase = Entry(window)
entradaBase.pack(pady=5)

label_altura = Label(window, text="Altura do Triângulo:")
label_altura.pack()
entradaAltura = Entry(window)
entradaAltura.pack(pady=5)

botao_calcular = Button(window, text="Calcular", command=calculoTriangulo)
botao_calcular.pack(pady=5)

botao_limpar = Button(window, text="Limpar", command=limparEntrada)
botao_limpar.pack(pady=5)

label_resultado = Label(window, text="Resultado: ", fg="black")
label_resultado.pack()

label_resultado_calculo = Label(window, text="0", fg="red")
label_resultado_calculo.pack()


window.mainloop()