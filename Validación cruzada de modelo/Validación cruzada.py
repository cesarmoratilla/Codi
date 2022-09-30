# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:12:31 2022

@author: camac
"""

#Validación cruzada de modelo de ML
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

modelo = pd.read_csv('C:/ppp/1.csv')
bosque = RandomForestClassifier()

bosque.fit(modelo[["FIX", "TIIE"]].values,
           modelo["PIB"].values)

"""           
print(bosque.score(modelo[["FIX", "TIIE"]].values, 
                   modelo["PIB"].values))
"""
print(cross_val_score(bosque,
                   modelo[["FIX", "TIIE"]].values, 
                   modelo["PIB"].values,
                   cv=5).mean())