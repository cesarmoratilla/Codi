# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:41:54 2022

@author: camac
"""

import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('C:/ppp/2.csv')
"""#Gráfico
plt.scatter(datos["x"], datos["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()"""
#Gráfico
plt.scatter(datos["FIX"], datos["TIIE"])
plt.xlabel("FIX")
plt.ylabel("TIIE")
plt.show()
#Gráfico2
plt.scatter(datos["FIX"], datos["PIB"])
plt.xlabel("FIX")
plt.ylabel("PIB")
plt.show()
#Gráfico3
plt.scatter(datos["FIX"], datos["Inflacin"])
plt.xlabel("FIX")
plt.ylabel("Inflacin")
plt.show()
#Gráfico4
plt.scatter(datos["Inflacin"], datos["PIB"])
plt.xlabel("Inflacin")
plt.ylabel("PIB")
plt.show()
#Gráfico4
plt.scatter(datos["TIIE"], datos["PIB"])
plt.xlabel("TIIE")
plt.ylabel("PIB")
plt.show()
#Correlación Pearson
datos.corr()
print(datos.corr()) # -1 (existe una relación fuerte entre las variables) #  (entre mas cerca del 0 hay menos relación)  # 1(existe una relación fuerte)
#Gráfica de correlaciónes de calor
matriz = datos.corr()
plt.matshow(matriz, cmap="bwr", vmin=-1, vmax=1)
plt.xticks(range(4), datos.columns, rotation=90)
plt.yticks(range(4), datos.columns)

for i in range(len(matriz.columns)):
    for j in range(len(matriz.columns)):
        plt.text(i, j, round(matriz.iloc[i, j], 2),
                ha= "center", va="center" )


plt.colorbar()
plt.show()
