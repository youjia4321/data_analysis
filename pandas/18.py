import pandas as pd
import numpy as np
import os

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
dfs = pd.read_csv(data_url)

df = dfs[:50]
print(df)
plt = df.plot(kind='scatter', x='tip', y='total_bill').get_figure()
dec = os.getcwd()
plt.savefig(dec+'/pngs/18plot.png')

# def jitter(series, factor):
#     z = float(series.max())-float(series.min())
#     a = float(factor)*z/50
#     return series.apply(lambda x: x + np.random.uniform(-a, a))
#
#
# df2 = df
# df2['tip'] = jitter(df['tip'], 1)
# df2['total_bill'] = jitter(df['total_bill'], 1)
# print(df2)