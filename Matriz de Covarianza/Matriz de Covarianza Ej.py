# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:30:23 2022

@author: camac
"""

import pandas as pd
import matplotlib.pyplot as plt
#quitar notación cientifica



# Contexto:
#   (0) PIB
#   (1) Gastos mensuales en inflacin 
#   (2) Gastos mensuales en TIIE
#   (3) Gastos mensuales en FIX

datos = pd.read_csv('C:/ppp/2.csv')
datos = pd.DataFrame(datos)
print(datos)
datos.aggregate(["std", "var"])



def subgrafica_std(datos, columna, fig, posicion): 
    ax = fig.add_subplot(1, 4, posicion)    
    
    # calculando media y desviación estándar
    media = datos[columna].mean() 
    std = datos[columna].std()
   
    # graficando datos
    ax.scatter(range(len(datos[columna])), datos[columna],
               marker="D", s=50, color="purple")
    
    # graficando media y desviación estándar 
    ax.axhline(y=media+std, color="gray", linestyle="--", linewidth=3)
    ax.axhline(y=media, color="teal", linestyle=":",  linewidth=6)
    ax.axhline(y=media-std, color="gray", linestyle="--", linewidth=3)

    # presentación de gráfica
    ax.set_title("Dev std: " + columna.capitalize(), fontsize=20)
    ax.set_xticks(range(len(datos[columna])))
    ax.get_xaxis().set_visible(False)


# Desviaciones estándar para todas las columnas    
fig = plt.figure(figsize=(18, 5))     

subgrafica_std(datos, "PIB", fig, 1)
subgrafica_std(datos, "Inflacin", fig, 2)
subgrafica_std(datos, "TIIE", fig, 3)
subgrafica_std(datos, "FIX", fig, 4)

plt.show()
#Matriz de Covarianza
print(datos.var())
datos.cov()

#Grafica de covarianza
def subgrafica_dispersion(datos, col_a, col_b, fig, posicion, texto): 
    ax = fig.add_subplot(1, 3, posicion)    
    ax.scatter(datos[col_a], datos[col_b], marker="8", s=50, color="purple")
    ax.set_xlabel(col_a.capitalize(), fontsize=20, color="darkblue")
    ax.set_ylabel(col_b.capitalize(), fontsize=20, color="darkblue")
    ax.text(54, 0, texto, fontsize=28, color="red")
    

# Impresión de matrices de covarianza

print(datos[["PIB", "Inflacin"]].cov(), "\n")
print(datos[["PIB", "TIIE"]].cov(), "\n")
print(datos[["PIB", "FIX"]].cov(), "\n")

# Gráficas

fig = plt.figure(figsize=(20,6))
subgrafica_dispersion(datos, "PIB", "Inflacin", fig, 1, "Positiva")     
subgrafica_dispersion(datos, "PIB", "TIIE", fig, 2, "Negativa")     
subgrafica_dispersion(datos, "PIB", "FIX", fig, 3, "~ Cero")     
plt.show()


# Impresión de matrices de covarianza

print("\n"*3)
print(datos[["Inflacin", "TIIE"]].cov(), "\n")
print(datos[["Inflacin", "FIX"]].cov(), "\n")
print(datos[["TIIE", "FIX"]].cov(), "\n")

# Gráficas

fig = plt.figure(figsize=(20, 6))
subgrafica_dispersion(datos, "Inflacin", "TIIE", fig, 1, "Negativa")     
subgrafica_dispersion(datos, "Inflacin", "FIX", fig, 2, "~ Cero")     
subgrafica_dispersion(datos, "TIIE", "FIX", fig, 3, "~ Cero") 
plt.show()

