import numpy as np
import matplotlib.pyplot as plt
# 给出均值为mean，标准差为stdev的高斯随机数（场），当size赋值时，例如：size=100，表示返回100个高斯随机数。
x1 = np.random.normal(10, 1, 100)
x2 = np.random.normal(20, 1, 100)
x3 = np.random.normal(30, 1, 100)
plt.plot(x1)
plt.plot(x2)
plt.plot(x3)
# plt.legend(['x1','x2','x3'], ncol = 3, mode = 'expand', loc=(0.02, 1.02))
plt.legend(['x1','x2','x3'])
plt.show()