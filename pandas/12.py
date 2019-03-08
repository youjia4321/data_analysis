import pandas as pd
import numpy as np

import pandas.util.testing as tm
import os
# 在pandas的DataFrame中经常使用多个索引，在pandas中成为MultiIndex对象
# 创建两个<type 'numpy.ndarray'>对象，分别为colors和foods

colors = tm.np.random.choice(['red', 'green'], size=20)
foods = tm.np.random.choice(['eggs','hom'], size=20)
# print(colors)
# print(foods)
# print(type(foods))

index = pd.MultiIndex.from_arrays([colors, foods], names=['color', 'food'])

df = pd.DataFrame(np.arange(40).reshape((20, 2)), columns=['熟食', '生食'], index=index)
# print(df)

print(df.query('food=="eggs"'))
# grouped = df.groupby(level='color')
# print(grouped.mean())
# grouped1 = df.groupby(level='food')
# print(grouped1.mean())

# df.index.names = [None, None]
# print(df)
# print(df.query('ilevel_1=="eggs"'))

df1 = df.replace([8,10,12,14,16,18,20,22,24,28,30,32], [0,0,4,6,8,0,38,36,4,6,38,34])
# print(df1)
eggs = df1.query('food=="eggs"')
counts = eggs['熟食'].value_counts()
print(counts)
plt = counts.plot(kind='pie').get_figure()
dec = os.getcwd()
plt.savefig(dec+'/pngs/12plot.png')