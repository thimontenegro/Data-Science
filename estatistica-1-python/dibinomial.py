# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:19:29 2019

@author: Thiag
"""

from scipy.stats import binom
prob = binom.pmf(3,5,0.5)
print(prob)

prob = binom.pmf(0,4,0.25)
binom.pmf(1,4,0.25)
binom.pmf(2,4,0.25)
binom.pmf(3,4,0.25)
binom.pmf(4,4,0.25)

binom.cdf(4,4,0.25)

binom.pmf(7,12,0.25)