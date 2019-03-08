import pandas as pd
import numpy as np

import pandas.util.testing as tm
import os
# 在pandas的DataFrame中经常使用多个索引，在pandas中成为MultiIndex对象
# 创建两个<type 'numpy.ndarray'>对象，分别为colors和foods

colors = tm.np.random.choice(['red', 'green'], size=5)
foods = tm.np.random.choice(['eggs','hom'], size=5)
# print(colors)
# print(foods)
# print(type(foods))

index = pd.MultiIndex.from_arrays([colors, foods], names=['color', 'food'])

df = pd.DataFrame(np.arange(10).reshape((5, 2)), columns=['熟食', '生食'], index=index)
grouped = df.groupby(level=['color','food'])

# for name,gorup in grouped:
#     print(name)
#     print(gorup)

print(grouped.aggregate(np.sum).reset_index()) # 将color和food索引转化为列变量
print(df.groupby(level=['color','food'],as_index=False).sum()) 
print(grouped.size()) # 返回各组的数据量
print(grouped.describe()) # 描述性统计