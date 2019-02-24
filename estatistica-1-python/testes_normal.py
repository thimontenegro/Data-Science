# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:52:52 2019

@author: Thiag
"""

from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt


dados = norm.rvs(size = 100)

stats.probplot(dados, plot = plt)
stats.shapiro(dados)