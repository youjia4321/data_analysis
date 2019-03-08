import pandas as pd
import os


data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(data_url)

# print(df)

good = df[df.tip > 5]  # 筛选处itp>5的


good_counts = good['day'].value_counts()  # 然后计算周几绘制柱状图
counts = df['day'].value_counts()
print(good_counts)
print(counts)
per = good_counts/counts  # 筛选与总体的百分比
print(per)

# dec = os.getcwd()
# plt = per.plot(kind='bar').get_figure()
# plt.savefig(dec+'/pngs/10plot1.png')
print(df.groupby('day').first())
# print(df.replace([2,3,4],[200,300,400]))