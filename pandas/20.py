import pandas as pd
import numpy as np
import os

df = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))

print(df)

plt = df.plot(kind='bar').get_figure() 
plt.savefig(os.getcwd()+'/pngs/20plot.png') 

plt = df.plot(kind='bar', stacked=True).get_figure() # 堆积直方图
plt.savefig(os.getcwd()+'/pngs/20plot1.png')

plt = df.plot(kind='barh', stacked=True).get_figure() # 水平方向的柱形图
plt.savefig(os.getcwd()+'/pngs/20plot2.png')
