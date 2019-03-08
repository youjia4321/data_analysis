import pandas as pd
import numpy as np

index = pd.date_range('1/29/2014', periods=15)
ts = pd.Series(np.arange(15), index=index)
# print(ts)

key = lambda x:x.month  # 计算每个index的月份
zscore = lambda x: (x-x.mean())/x.std()
tranformed = ts.groupby(key).transform(zscore)


print(tranformed.groupby(key).mean())
print(tranformed.groupby(key).std())          
