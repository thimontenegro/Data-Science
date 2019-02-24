# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:52:35 2019

@author: Thiag
"""

import matplotlib.pyplot as plt
import pandas as pd
from pyod.models.knn import KNN

iris = pd.read_csv('iris.csv')
plt.boxplot(iris.iloc[:,1], showfliers = False)
outliers = iris[(iris['sepal width'] > 4) | (iris['sepal width'] < 2.1)]

t = iris.iloc[:,1]
t = t.reshape(-1,1)

detector = KNN()
detector.fit(t)

previsoes = detector.labels_()