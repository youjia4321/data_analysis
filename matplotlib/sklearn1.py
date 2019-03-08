import numpy as np
# 机器学习的模型
from sklearn.svm import SVR
import matplotlib.pyplot as plt


x = np.array([71,47,8,14,37,250,315,357,121,200])
y = np.array([33.85, 33.43, 32.79, 32.81, 32.74, 34.81,34.31,34.69,34.18,33.92])

x1 = np.array([71,47,8,14,37]).reshape((5,1))
y1 = np.array([33.85, 33.43, 32.79, 32.81, 32.74]).reshape((5,1))

x2 = np.array([250,315,71,357,121,200]).reshape((6,1))
y2 = np.array([34.81,34.31,33.85,34.69,34.18,33.92]).reshape((6,1))

fig, axes = plt.subplots()

axes.scatter(x, y)
# 创建算法
svr1 = SVR(kernel='linear')
svr2 = SVR(kernel='linear')

# 将数据交给算法fit
svr1.fit(x1,y1)
svr2.fit(x2,y2)

# 预测数据
x_test1 = np.linspace(0, 100, 20).reshape((20,1))
x_test2 = np.linspace(50, 350, 20).reshape((20,1))
y1_ = svr1.predict(x_test1)
y2_ = svr2.predict(x_test2)

axes.plot(x_test1, y1_)
axes.plot(x_test2, y2_)

plt.show()