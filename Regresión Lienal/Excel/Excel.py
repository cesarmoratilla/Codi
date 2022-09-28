import pandas as pd

#datos= pd.read_csv('direcci�n de archivo')"
datos= pd.read_csv('C:/ppp/1.csv')

#Gr�fica ejemplo
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
#regresi�n ejemplo
from sklearn import linear_model
regresion = linear_model.LinearRegression()
tipo = datos["FIX"].values.reshape((-1,1))
modelo = regresion.fit(tipo, datos["TIIE"])
print("Interseccion (b)", modelo.intercept_)
print("Pendiente (m)", modelo.coef_)

"""regresi�n para cualquiera
from sklearn import linear_model
regresion = linear_model.LinearRegression()
tipo = datos["nombre"].values.reshape((-1,1))
modelo = regresion.fit(tipo, datos["nombre"])
print("Interseccion (b)", modelo.intercept_)
print("Pendiente (m)", modelo.coef_)"""

#predicci�n
"""entrada = [[],[],[],[]]
modelo.predict(entrada)
#Gr�fica
plt.scatter(entrada, modelo.predict(entrada), color="pink")
plt.plt(entrada, modelo.predict(entrada), color"green")
plt.ylabel("FIX")
plt.xlabel("TIIE")
plt.scatter(datos["FIX"], datos["TIIE"], color="black")
plt.show()"""
