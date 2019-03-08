#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

myfont = matplotlib.font_manager.FontProperties(fname="msyh.ttf")


x = np.arange(-10, 11)
y = x**2
plt.plot( x, y, 'r--',label='quxian')
plt.xlabel("这里是x坐标", FontProperties=myfont)
plt.ylabel("这里是y坐标", FontProperties=myfont)
plt.grid(True)
plt.legend()
plt.show()


# plt.axis([0, 6, 0, 20])
# The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax]
