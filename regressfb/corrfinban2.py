# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:10:35 2022

@author: camac
"""

import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('C:/ppp/fb2.csv')
"""#Gráfico
plt.scatter(datos["x"], datos["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()"""
#Gráfico
plt.scatter(datos["IPC"], datos["GMEX"])
plt.xlabel("IPC")
plt.ylabel("GMEX")
plt.show()
#Gráfico2
plt.scatter(datos["IPC"], datos["GMEXT"])
plt.xlabel("IPC")
plt.ylabel("GMEXT")
plt.show()
#Gráfico3
plt.scatter(datos["IPC"], datos["SCCO"])
plt.xlabel("IPC")
plt.ylabel("SCCO")
plt.show()
#Gráfico4
plt.scatter(datos["SCCO"], datos["GMEXT"])
plt.xlabel("SCCO")
plt.ylabel("GMEXT")
plt.show()
#Gráfico4
plt.scatter(datos["GMEX"], datos["GMEXT"])
plt.xlabel("GMEX")
plt.ylabel("GMEXT")
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
