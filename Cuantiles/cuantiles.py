# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:48:13 2022

@author: camac
"""

import numpy as np
"""alturas = np.random.normal(prmedio, dvt, tamaño de muestra)"""
alturas = np.random.normal(1.75, 0.15, 100000)
"""np.quantile(alturas, [lo que queremos obtener])"""
np.quantile(alturas, [0, 1/4, 2/4, 3/4, 1])
import matplotlib.pyplot as plt

cuantiles = [(2, "Mediana"),
             (3, "Terciles"),
             (4, "Cuartiles"),
             (5, "Quintiles"),
             (10, "Deciles"),
             (100, "Percentiles")]

cortes = []
for cuantil in cuantiles:
    corte = []
    valor = 0
    for i in range(cuantil[0]-1):
        valor += 1/cuantil[0]
        corte.append(valor)         
    cortes.append(corte)

for i in range(len(cuantiles)):
    plt.figure(figsize=(7.5, 5))
    plt.title(cuantiles[i][1], size=22)
    plt.ylabel("Frecuencia", size=16)
    plt.xlabel("Alturas", size=16)
    plt.hist(alturas, 100, label="altura", color="pink")
    #print(np.quantile(alturas, [0] + cortes[i] + [1]))
    for corte in cortes[i]:
        plt.axvline(x = np.quantile(alturas, corte), label="%.2f" % corte, linewidth=3)
    if i < len(cuantiles) - 1:
        plt.legend()
    plt.show()
    print("\n"*4)