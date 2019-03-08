import numpy as np
from scipy import stats
from scipy.stats import chisquare

observed = np.array([15, 95])
# 观测值:110学生中化妆的女生95人，化妆的男生15人
expcted = np.array([55, 55])
# 理论值:110学生中化妆的女生55人，化妆的男生55人
s = chisquare(observed, expcted)
print(s)
