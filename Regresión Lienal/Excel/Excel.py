import pandas as pd

#datos= pd.read_csv('dirección de archivo')"
datos= pd.read_csv('C:/ppp/1.csv')

#Gráfica ejemplo
"""import matplotlib.pyplot as plt
plt.ylabel("FIX")
plt.xlabel("TIIE")
plt.scatter(datos["FIX"], datos["TIIE"], color="black")
plt.show()"""
#cualquier grafica 
"""import matplotlib.pyplot as plt
plt.ylabel("nombre")
plt.xlabel("nombre")
plt.scatter(datos["nombre"], datos["nombre"], color="black")
plt.show()"""
#regresión ejemplo
from sklearn import linear_model
regresion = linear_model.LinearRegression()
tipo = datos["FIX"].values.reshape((-1,1))
modelo = regresion.fit(tipo, datos["TIIE"])
print("Interseccion (b)", modelo.intercept_)
print("Pendiente (m)", modelo.coef_)

"""regresión para cualquiera
from sklearn import linear_model
regresion = linear_model.LinearRegression()
tipo = datos["nombre"].values.reshape((-1,1))
modelo = regresion.fit(tipo, datos["nombre"])
print("Interseccion (b)", modelo.intercept_)
print("Pendiente (m)", modelo.coef_)"""

#predicción
"""entrada = [[],[],[],[]]
modelo.predict(entrada)
#Gráfica
plt.scatter(entrada, modelo.predict(entrada), color="pink")
plt.plt(entrada, modelo.predict(entrada), color"green")
plt.ylabel("FIX")
plt.xlabel("TIIE")
plt.scatter(datos["FIX"], datos["TIIE"], color="black")
plt.show()"""
