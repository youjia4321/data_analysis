import numpy as np
from numpy import random
x1= np.array([1,2,3,4,5])
y1 = np.array([6,7,8,9,10])
cond =[True, False, True, True, False]
z1 = [(x,y,z) for x,y,z in zip(x1, y1, cond)] 
print(z1)
s = np.where(cond, x1, y1)   # 如果cond为true,就取x值,否则取y值
print(s)


x = np.random.randn(12)
print(x)
print((x>0).sum())
