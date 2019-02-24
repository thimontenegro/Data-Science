# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 02:57:32 2019

@author: Thiago
"""

import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
base.shape
np.random.seed(2345)
amostra = np.random.choice(a =[0,1], size = 150, replace = True, p =[0.5,0.5])
np.random.choice(a = [0, 1], size = 50, replace = True, p = [0.5, 0.5, 0.2])
len(amostra[amostra == 0])

len(amostra[amostra == 1])