# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:07:37 2022

@author: camac
"""

import pandas as pd
import matplotlib.pyplot as plt
#quitar notación cientifica
pd.options.display.float_format = '{:.2f}'.format


# Contexto:
#   (0) Edad,  
#   (1) Gastos mensuales en Medicina, 
#   (2) Gastos mensuales en Educación, y
#   (3) Gastos mensuales en Cacahuates

datos = {"edad" : [35, 50, 22, 45, 18, 75, 55, 20, 23, 49],
         "medicina" : [200, 1500, 150, 250, 0, 2500, 1400, 50, 0, 600],
         "educacion" : [1200, 0, 7500, 2200, 8300, 0, 0, 4900, 5100, 800],
         "cacahuates" : [10, 15, 0, 10, 20, 10, 20, 10, 15, 0]}

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
               marker="D", s=150, color="purple")
    
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

subgrafica_std(datos, "edad", fig, 1)
subgrafica_std(datos, "medicina", fig, 2)
subgrafica_std(datos, "educacion", fig, 3)
subgrafica_std(datos, "cacahuates", fig, 4)

plt.show()

#Matriz de Covarianza
print(datos.var())
datos.cov()
def subgrafica_dispersion(datos, col_a, col_b, fig, posicion, texto): 
    ax = fig.add_subplot(1, 3, posicion)    
    ax.scatter(datos[col_a], datos[col_b], marker="8", s=250, color="purple")
    ax.set_xlabel(col_a.capitalize(), fontsize=20, color="darkblue")
    ax.set_ylabel(col_b.capitalize(), fontsize=20, color="darkblue")
    ax.text(54, 0, texto, fontsize=28, color="red")
    

# Impresión de matrices de covarianza

print(datos[["edad", "medicina"]].cov(), "\n")
print(datos[["edad", "educacion"]].cov(), "\n")
print(datos[["edad", "cacahuates"]].cov(), "\n")

# Gráficas

fig = plt.figure(figsize=(20, 6))
subgrafica_dispersion(datos, "edad", "medicina", fig, 1, "Positiva")     
subgrafica_dispersion(datos, "edad", "educacion", fig, 2, "Negativa")     
subgrafica_dispersion(datos, "edad", "cacahuates", fig, 3, "~ Cero")     
plt.show()


# Impresión de matrices de covarianza

print("\n"*3)
print(datos[["medicina", "educacion"]].cov(), "\n")
print(datos[["medicina", "cacahuates"]].cov(), "\n")
print(datos[["educacion", "cacahuates"]].cov(), "\n")

# Gráficas

fig = plt.figure(figsize=(20, 6))
subgrafica_dispersion(datos, "medicina", "educacion", fig, 1, "Negativa")     
subgrafica_dispersion(datos, "medicina", "cacahuates", fig, 2, "~ Cero")     
subgrafica_dispersion(datos, "educacion", "cacahuates", fig, 3, "~ Cero") 
plt.show()