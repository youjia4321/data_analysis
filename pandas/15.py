import pandas as pd
import numpy as np

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(data_url)

# print(df)
df.index.name = 'index'
dfs = df.loc[:20]
grouped = dfs.groupby('day')


print(grouped['total_bill'].agg([np.sum,np.mean,np.std]))

print(np.sum(dfs['total_bill']))
# def sum():
#     return np.sum(grouped['total_bill'])


# print(grouped['total_bill'].agg({'C':'sum'})) 已经放弃使用并将在未来版本中删除
