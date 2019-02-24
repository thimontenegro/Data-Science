# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:23:20 2019

@author: Thiag
"""

import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[19,6],[43,32]])
chi2_contingency(novela)

exercicio= np.array([[41,34],[18,7]])
chi2_contingency(exercicio)