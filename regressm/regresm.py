# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:10:23 2022

@author: camac
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


datos = pd.read_csv('C:/ppp/MK.csv')
datos.info()
datos.describe().T

datos.isnull().sum()

for i in datos.columns:
    sns.boxplot(datos[i])
    plt.show()
    
for i in datos.columns:
    sns.distplot(datos[i])
    plt.show()    

fig, axs = plt.subplots(1, 3, sharey=True)
datos.plot(kind='scatter', x='youtube', y='sales', ax=axs[0], figsize=(16, 8))
datos.plot(kind='scatter', x='facebook', y='sales', ax=axs[1])
datos.plot(kind='scatter', x='newspaper', y='sales', ax=axs[2])    

sns.heatmap(datos.corr(), annot=True)
feature_cols = ['youtube', 'facebook', 'newspaper']
X = datos[feature_cols]
y = datos.sales
scaler =StandardScaler()

X_scaled = scaler.fit_transform(X)
X = preprocessing.normalize(X_scaled)
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=10)
print ("Training shape:",x_train.shape)
print ("Testing shape:",x_test.shape)
print("Training shape:",y_train.shape)
print("Testing shape:",y_test.shape)

def plotScatterMatrix(df, plotSize, textSize):
    df = df.select_dtypes(include =[np.number]) 
    df = df.dropna('columns')
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    columnNames = list(df)
    if len(columnNames) > 10: # reduce the number of columns for matrix inversion of kernel density plots
        columnNames = columnNames[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show()
plotScatterMatrix(datos, 12, 10)


rg = LinearRegression()
rg.fit(X, y)

rg.score(x_train,y_train)

pred = rg.predict(x_test)
print("Predicted medv for test:")
pred

rg.score(x_test,y_test)

print("RMSE:",np.sqrt(metrics.mean_squared_error(y_test,pred)))
print("MAE:",metrics.mean_absolute_error(y_test,pred))
print("Predicted medv for test:")
