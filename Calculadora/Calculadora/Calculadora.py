
from tkinter import *

ventana=Tk()  
ventana.title("Calculadora")

i = 0

#Crear pantalla 
e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan=5, padx=7, pady=7)
 
#funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
def borrar():
    e_texto.delete(0, END)
    i = 0 
def hacer_operacin():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion) 
    e_texto.delete(0, END)
    e_texto.insert(0,resultado)
    i = 0
#1
boton1 = Button(ventana, text="1", width="5", height="3", command = lambda: click_boton(1))
boton1.grid(row="1", column=1)
boton2 = Button(ventana, text="2", width="5", height="3", command = lambda: click_boton(2))
boton2.grid(row="1", column=2)
boton3 = Button(ventana, text="3", width="5", height="3", command = lambda: click_boton(3))
boton3.grid(row="1", column=3)

#2
boton4 = Button(ventana, text="4", width="5", height="3",command = lambda: click_boton(4))
boton4.grid(row="2", column=1)
boton5 = Button(ventana, text="5", width="5", height="3",command = lambda: click_boton(5))
boton5.grid(row="2", column=2)
boton6 = Button(ventana, text="6", width="5", height="3",command = lambda: click_boton(6))
boton6.grid(row="2", column=3)
#3
boton7 = Button(ventana, text="7", width="5", height="3",command = lambda: click_boton(7))
boton7.grid(row="3", column=1)
boton8 = Button(ventana, text="8", width="5", height="3",command = lambda: click_boton(8))
boton8.grid(row="3", column=2)
boton9 = Button(ventana, text="9", width="5", height="3",command = lambda: click_boton(9))
boton9.grid(row="3", column=3)
#cero
boton0 = Button(ventana, text="0", width="7", height="3",command = lambda: click_boton(0))
boton0.grid(row="4", column=1)
#fun
boton_borrar = Button(ventana, text="AC", width="5", height="3",command = lambda: borrar())
boton_borrar.grid(row="1", column=4)
boton_par1 = Button(ventana, text="(", width="5", height="3",command = lambda: click_boton("("))
boton_par1.grid(row="2", column=4)
boton_par2 = Button(ventana, text=")", width="5", height="3",command = lambda: click_boton(")"))
boton_par2.grid(row="3", column=4)
boton_multi = Button(ventana, text=" *", width="5", height="3",command = lambda: click_boton("*"))
boton_multi.grid(row="5", column=4)
boton_resta = Button(ventana, text="-", width="5", height="3",command = lambda: click_boton("-"))
boton_resta.grid(row="4", column=4)
boton_div = Button(ventana, text="/", width="5", height="3",command = lambda: click_boton("/"))
boton_div.grid(row="5", column=4)
boton_sum = Button(ventana, text="+", width="5", height="3",command = lambda: click_boton("+"))
boton_sum.grid(row="4", column=3)
#ig
boton_igual = Button(ventana, text="=", width="5", height="3",command = lambda: hacer_operacin())
boton_igual.grid(row="6", column=3)






ventana.mainloop() 
