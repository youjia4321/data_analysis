from numpy import random
algebra = random.randn(7,4) # empty will return a matrix of size 7,4
for j in range(7):
    algebra[j] = j

print(algebra)
print(algebra[[6,1,4,3,5,0,2]])
print(algebra[[1,2,3,5]][:, [0,2,1,3]])