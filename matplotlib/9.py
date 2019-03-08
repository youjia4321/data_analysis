import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
from pandas import Series,DataFrame

plt.figure(1)
ax1 = plt.subplot(211)
s1 = pd.Series(np.random.randn(20).cumsum(),
              index=np.arange(0,40,2))


# print(s1)
# ax1=s1.plot(label = "random number", title = "random sum")
ax1.bar(s1.index, s1, label='random number', color='g')
for i in s1.index:
    x = i
    y = s1[i]
    ax1.text(x, y+.1, '%.3f' % y)
ax1.set_title('random sum')
ax1.set_xlabel('position')
ax1.set_ylabel('sum')
ax1.legend()
plt.grid()

plt.subplot(212)
s2 = pd.Series(np.random.randn(20).cumsum(),#累加
              index=np.arange(0,20))
# print(s2)
ax2=s1.plot(label = "random number sum", style="ko-")

ax2.legend()
plt.grid()
plt.show()
