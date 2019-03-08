import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')[:50]

print(df)


plt.plot(df['tip'], df['total_bill'], 'ob')
plt.show()