import pandas as pd
import numpy
from pandas import Series, DataFrame

mjp = Series([5,4,3,2,1], index =['a','b','c','d','e'])
index = mjp.index
print(index)
print(DataFrame(mjp).T)
mjp.index = [list('abcde')]
print(mjp)
print(DataFrame(mjp).T)

s = [list('abrdy')]
player_1 =Series(mjp, index=s)
print(player_1)
print(pd.notnull(player_1))