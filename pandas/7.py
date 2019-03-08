from pandas import Series

var = Series(['Python', 'Java', 'c', 'c++', 'Php'], index =[5,4,3,2,1])
print(var)

print(var[4])
print(var[1:4])