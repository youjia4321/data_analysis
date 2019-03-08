import pandas as pd

gh = pd.Series(['Dhoni', 'Sachin', 'Kohli'], index =[0,2,4])
# print(gh)
# s = gh.reindex(range(7), method='bfill')
# print(s)

import numpy as np
fp = pd.DataFrame(np.random.randn(9).reshape((3,3)),index =['a','b','c'], columns =['Gujarat','Tamil Nadu', 'Kerala'])
print(fp.shape)
print(fp.sort_values(by='Kerala'))

fp1 =fp.reindex(['a', 'b', 'c', 'd'], columns = ['Gujarat','Assam','Kerala']) 
print(fp1)
s = fp1.drop(['Kerala'], axis=1)
print(s)