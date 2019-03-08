import pandas as pd
import os

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(data_url)
# print(df[:7])
# print(df[df.tip>8])
# print(df.loc[[1,3,6],['tip', 'sex']])
# print(df.shape)
# print(df.index)
# print(df.loc[0])

counts1 = df['sex'].value_counts()
# print(counts1)
counts2 = df['day'].value_counts()
print(counts2)
# print(os.getcwd())
dec = os.getcwd()
plt = counts1.plot(kind='bar').get_figure()
plt.savefig(dec+'/pngs/9plot1.png')


