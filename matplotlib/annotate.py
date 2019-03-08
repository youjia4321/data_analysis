import numpy as np
import matplotlib.pyplot as plt


x = np.random.randint(0, 10, size = 10)
x[5] = 30
plt.plot(x)
plt.ylim([-2, 35])
plt.annotate('this point is important', xy = (5, 30), xytext = (7, 31), arrowprops={'width': 4, 'shrink':.01})
plt.show()