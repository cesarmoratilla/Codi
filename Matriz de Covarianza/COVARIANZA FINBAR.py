# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:19:57 2022

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

datos = pd.read_csv('C:/ppp/finban.csv')
datos = pd.DataFrame(datos)
print(datos)
datos.aggregate(["std", "var"])



def subgrafica_std(datos, columna, fig, posicion): 
    ax = fig.add_subplot(1, 5, posicion)    
    
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
fig = plt.figure(figsize=(18, 6))     

subgrafica_std(datos, "IPC", fig, 1)
subgrafica_std(datos, "ALFAA", fig, 2)
subgrafica_std(datos, "GCARSOA1", fig, 3)
subgrafica_std(datos, "WMT", fig, 4)
subgrafica_std(datos, "GFINBURO", fig, 5)
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

print(datos[["IPC", "ALFAA"]].cov(), "\n")
print(datos[["IPC", "GCARSOA1"]].cov(), "\n")
print(datos[["IPC", "WMT"]].cov(), "\n")
print(datos[["IPC", "GFINBURO"]].cov(), "\n")
print(datos[["GCARSOA1", "GFINBURO"]].cov(), "\n")
# Gráficas

fig = plt.figure(figsize=(20, 6))
subgrafica_dispersion(datos, "IPC", "ALFAA", fig, 1, "Negativa")     
subgrafica_dispersion(datos, "IPC", "GCARSOA1", fig, 2, "~ Cero")     
subgrafica_dispersion(datos, "IPC", "GFINBURO", fig, 3, "~ Cero") 
subgrafica_dispersion(datos, "IPC", "WMT", fig, 3, "~ Cero") 

plt.show()

