import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(3,3, figsize=(15,15))
# print(axes)
x = np.array([1,2,3,4,5])
axes[0][0].scatter(x, 0.25*np.random.randn(len(x)))
axes[0][0].set_title("scatter")
# plt.show() 

X = np.linspace(-6, 100, 1024) # 其中x1、x2、N分别为起始值、终止值、元素个数。若默认N，默认点数为100。
print(X[99])
axes[0][1].plot(X, np.sinc(X), c = 'r')

X = np.linspace(-6, 6, 1024)
Y = np.sinc(X)
X_sub = np.linspace(-3, 3, 1024)
Y_sub = np.sinc(X_sub) 
axes[0][2].plot(X, Y, c = 'b') 
sub_axes = plt.axes([.3,.3,.10,.10])
sub_axes.plot(X_sub, Y_sub, c = 'k')

a = np.array([1,2,3,2,1,3,24,24,2,1,1])
axes[1][0].pie(a, autopct='%.1f%%')

plt.show()
T = np.linspace(0 , 2 * np.pi, 1024)
plt.axes(polar = True)
plt.plot(T, 1. + .25 * np.sin(16 * T), c= 'k')
plt.show()

