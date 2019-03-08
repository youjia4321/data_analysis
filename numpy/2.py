from numpy import random
import numpy as np
personals = np.array(['Manu', 'Jeevan', 'Prakash', 'Manu', 'Prakash', 'Jeevan', 'Prakash'])
print(personals)
random_no = random.randn(7, 4) # 6行4列的随机数值
print(random_no)
random_no[personals =='Manu']
print("+++++++++++++\n", random_no[personals =='Manu', 2:]) 