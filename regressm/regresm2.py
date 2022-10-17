# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 21:37:19 2022

@author: camac
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

data = pd.read_csv('C:/ppp/MK.csv')

data.info()
data.describe().T
data.hist()
plt.show()

#Checking for missing value
data.isnull().sum()

#Checking for duplicate value
row,col = data.shape

data.drop_duplicates(inplace=True)

if data.shape==(row,col):
    print('The dataset doesn\'t have any duplicates')
else:
    print('The dataset have duplicates')
    
#Checking for outlier
ax = data[['youtube', 'facebook','newspaper']].plot(kind='box', title='boxplot', showmeans=True)    
#Removal of outlier
df = data.copy()

for i in ['youtube','facebook','newspaper']:
    Q1 = df[i].quantile(0.25)
    Q3 = df[i].quantile(0.75)
    IQR = Q3 - Q1
    df = df[df[i] <= (Q3+(1.5*IQR))]
    df = df[df[i] >= (Q1-(1.5*IQR))]
    df = df.reset_index(drop=True)
    (df.head())
print('Before removal of outliers, The dataset had {} samples.'.format(data.shape[0]))
print('After removal of outliers, The dataset now has {} samples.'.format(df.shape[0]))
# the independent variables set

X = df[['youtube', 'facebook','newspaper']]
  
# VIF dataframe
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
  
# calculating VIF for each feature
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
for i in range(len(X.columns))]
  
print(vif_data)

fig, axs = plt.subplots(1, 3, sharey=True, figsize=(24, 8))

sns.heatmap(data.corr(), annot=True)
sns.regplot(x=df["youtube"],y=df["sales"],data=df,ax=axs[0])
sns.regplot(x=df["facebook"],y=df["sales"],data=df,ax=axs[1])
sns.regplot(x=df["newspaper"],y=df["sales"],data=df,ax=axs[2])
plt.ylim(0,)


x = df.drop(['sales'],axis=1)

x = df.drop(['sales'],axis=1)
y = df['sales']
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=100)

#Standardization data
std = StandardScaler()

x_train_std = std.fit_transform(x_train)
x_train_std = pd.DataFrame(x_train_std, columns=X.columns)

x_test_std = std.transform(x_test)
x_test_std = pd.DataFrame(x_test_std, columns=X.columns)
ax = x_train_std.plot(kind='box', title='Boxplot (Training data)', showmeans=True)
ax = x_test_std.plot(kind='box', title='Boxplot (Testing data)', showmeans=True)

y_train_shape = y_train.values.reshape(-1,1)

y_train_shape = y_train.values.reshape(-1,1)

# Add a constant to get an intercept
x_train_sm = sm.add_constant(x_train_std['youtube'])


# Fit the resgression line using 'OLS'
lr = sm.OLS(y_train_shape, x_train_sm).fit()
print(lr.params)
print(lr.summary())

# Add a constant to get an intercept
x_train_sm1 = sm.add_constant(x_train_std[['youtube','facebook']])

# Fit the resgression line using 'OLS'
lr1 = sm.OLS(y_train_shape, x_train_sm1).fit()
print(lr1.params)
print(lr1.summary())

# Add a constant to get an intercept
x_train_sm2 = sm.add_constant(x_train_std[['youtube','facebook','newspaper']])

# Fit the resgression line using 'OLS'
lr2 = sm.OLS(y_train_shape, x_train_sm2).fit()
print(lr2.params)
print(lr2.summary())

#One Variable (Youtube)

y_test_shape = y_train.values.reshape(-1,1)

x_test_sm = sm.add_constant(x_test_std['youtube'])

# Predict the y values corresponding to X_test_sm
y_pred = lr.predict(x_test_sm)


MRSE = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE Test:", MRSE)                      
r_squared = r2_score(y_test, y_pred)
print("r_squared :", r_squared) 

# Add a constant to get an intercept
x_train_sm1 = sm.add_constant(x_train_std[['youtube','facebook']])

# Fit the resgression line using 'OLS'
lr1 = sm.OLS(y_train_shape, x_train_sm1).fit()
print(lr1.params)
print(lr1.summary())

# Add a constant to get an intercept
x_train_sm2 = sm.add_constant(x_train_std[['youtube','facebook','newspaper']])

# Fit the resgression line using 'OLS'
lr2 = sm.OLS(y_train_shape, x_train_sm2).fit()
print(lr2.params)
print(lr2.summary())

y_test_shape = y_train.values.reshape(-1,1)

x_test_sm2 = sm.add_constant(x_test_std[['youtube','facebook','newspaper']])

# Predict the y values corresponding to X_test_sm
y_pred2 = lr2.predict(x_test_sm2)


MRSE = np.sqrt(mean_squared_error(y_test, y_pred2))
print("RMSE Test:", MRSE)                      
r_squared = r2_score(y_test, y_pred2)
print("r_squared :", r_squared) 