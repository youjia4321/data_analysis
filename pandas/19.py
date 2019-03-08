# coding:utf8
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt


data_url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'

df = pd.read_csv(data_url)[:50]

print(df.head())

lm = ols('tip~total_bill', df).fit()

plt.plot(df['total_bill'], df['tip'], 'ob')

plt.plot(df['total_bill'], lm.fittedvalues, 'r', linewidth=2)

plt.show()