import numpy as np
import matplotlib.pyplot as plt

def show_rose(values, title):
    # 玫瑰图花瓣的个数8, 45度
    n = 8
    angle = np.arange(0, 2*np.pi, 2*np.pi/n)

    # 绘制的数据values
    radius = np.array(values)

    # axis代表的x,y, axes代表画面
    plt.axes([0,0,.9,.9], polar=True)

    color = np.random.random(size=24).reshape((8,3))
    # print(color)

    plt.bar(angle, radius, color=color)

    plt.title(title, loc='left')
    # plt.grid(False)

x = [5,12,24,9,11,4,0,1]
# 风向数据,用wind = np.load('xx.npy')加载数据,在使用values, degree = np.histogram(wind, 8, [0, 360])处理wind数据,分为8份,范围在0~360之间
show_rose(x, 'Ravenna')
plt.show()