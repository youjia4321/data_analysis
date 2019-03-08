import pandas as pd
import numpy
from pandas import Series, DataFrame

mjp = Series([5,4,3,2,1])
# print(mjp)
# print(mjp.values)
# print(mjp.index)
print((mjp!=5).mean())
# mjp[1] = 10000000
# print(mjp[[1,3,4]])
# print(mjp[mjp<3])
print(numpy.mean(mjp))
print(5 in mjp)
print(DataFrame(mjp).T)