from pandas import *

var = Series(['Python', 'Java', 'c', 'c++', 'Php'], index =[5,4,3,2,1])
print(var)
var1 = var.reindex(['a','b','c','d','e'], fill_value=33)# reindex creates a new object 
var1.index.name = 'youjia'
print(var1.index)
print(var1)