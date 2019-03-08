import pandas as pd
import numpy as np

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(data_url)

# print(df)
df.index.name = 'index'
dfs = df.loc[:20]
print(dfs)
d = dfs.pop('day')
dfs.insert(0,'day',d)
print(dfs)

df1 = dfs.drop(['sex', 'smoker'], axis=1)
print(df1)