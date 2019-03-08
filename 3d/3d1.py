from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-4, 4, 0.01)
y = np.arange(-4, 4, 0.01)

# plt.plot(x, y)
X, Y = np.meshgrid(x, y) # 生成网格点
# print(X)
def mk_Z(X, Y):
    return 3+0.5*np.sin(X)+np.cos(Y)-np.cos(2-X)
Z = mk_Z(X, Y)
plt.figure(figsize=(16,4))
axes = plt.subplot(131, projection = '3d')
axes.plot_surface(X, Y, Z)
axes2 = plt.subplot(132, projection = '3d')
s = axes2.plot_surface(X, Y, Z, cmap='rainbow')
# plt.colorbar(s, shrink=.5)
axes3 = plt.subplot(133, projection = '3d')
axes3.plot_surface(X, Y, Z, rstride = 50, cstride = 50, cmap='rainbow')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_zlabel('z')
plt.show()