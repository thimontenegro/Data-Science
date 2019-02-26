# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:50:11 2019

@author: Thiag
"""

import pandas as pd
import numpy as np

np.random.seed(2345)
amostra = np.random.choice(a = [0,1], size = 1000, replace = True, p=[0.5,0.5])
amostra

