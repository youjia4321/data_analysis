#encoding:utf8
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib

myfont = matplotlib.font_manager.FontProperties(fname="msyh.ttf")

plt.figure(1)
ax1 = plt.subplot(111)
data = np.array([15,10,25,15])
width = 0.5


x_bar = np.arange(4) 

rect = ax1.bar(x_bar, data, color='lightblue', label='13')
for rec in rect:
    x=rec.get_x() #获取所有x坐标的值
    height=rec.get_height()  #获取所在高度的值
    # print(x,height)
    ax1.text(x+0.2,.5+height,str(height)+'W')

ax1.set_xticks(x_bar)
ax1.set_xticklabels(["第一季度", "第二季度", "第三季度", "第三季度"], FontProperties=myfont)
ax1.set_xlabel("季度", FontProperties=myfont)

ax1.set_ylabel("销量(单位/万)", FontProperties=myfont)
ax1.set_title("2017年销售表", FontProperties=myfont)
ax1.grid(True)  #是否显示网格
ax1.set_ylim(0,28) #设置y的显示范围

# ax1.spines["right"].set_color("none")
# ax1.spines["top"].set_color("none")
plt.legend()
plt.show()

plt.subplot(211)
plt.plot([1,2,3], label="test1")
plt.plot([3,2,1], label="test2")
# 将图例放到这个子图上方，
# 扩展自身来完全利用提供的边界框。
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

plt.subplot(223)
plt.plot([1,2,3], label="test1")
plt.plot([3,2,1], label="test2")
# 将图例放到这个小型子图的右侧
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()

from numpy.random import randn

z = randn(10)
print(z)
red_dot, = plt.plot(z, "ro", markersize=15)
# 将白色十字放置在一些数据上
white_cross, = plt.plot(z[:5], "w+", markeredgewidth=3, markersize=15)

plt.legend([red_dot, (red_dot, white_cross)], ["Attr A", "Attr A+B"])
plt.show()



