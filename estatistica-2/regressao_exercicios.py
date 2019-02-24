# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 01:50:51 2019

@author: Thiag
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv("women.csv")
base = base.drop(['Unnamed: 0'],axis = 1)

X = base.iloc[:,1].values
X = X.reshape(-1,1)
y = base.iloc[:,0].values


modelo = LinearRegression()
modelo.fit(X,y)
modelo.intercept_
modelo.coef_
plt.scatter(X,y)
plt.plot(X, modelo.predict(X), color='purple')


