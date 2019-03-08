import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# 数据的直方图
n, bins, patches = plt.hist(x, 50, density=1, facecolor='r', alpha=0.75)


# for i in patches:
#     print(i)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100, \sigma=15$')
plt.text(40, .01, r'$\alpha_i >  \beta_i$')
plt.text(70, .01, r'$\sum_{i=0}^\infty x_i$')
plt.axis([0, 160, 0, 0.03])
plt.grid(True) # 显示网格
plt.show()