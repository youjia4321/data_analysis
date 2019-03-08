import pandas as pd
import numpy as np

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(data_url)

# print(df)
df.index.name = 'index'
dfs = df.loc[:20]
# print(dfs['sex'].str.len())
# print(dfs['sex'].str.lower())
# print(dfs['sex'].str.split('a').str.get(0))

dfs1 = dfs['sex'].str.replace('^Female$', 'Man', case=False) # 替换

dfs2 = dfs1.str.replace('^Male$', 'Woman', case=False)

# print(dfs2)

print(dfs['sex'].str.extract('^(?P<upper>[FM])(?P<lower>.*?)$')) # ?P<upper> 输出的结果包含列名
'''
      upper lower
index
0       Fem   ale
1         M   ale
2         M   ale
'''
