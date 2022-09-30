# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:30:28 2022

@author: camac
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datos = pd.read_csv('C:/ppp/2.csv')

plt.hist(datos, bins=4)
plt.show

