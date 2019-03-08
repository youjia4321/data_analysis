import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
myfont = matplotlib.font_manager.FontProperties(fname="msyh.ttf")
df = pd.read_csv("test.csv")
# print(df)
ax = plt.subplot(221)
ax.bar(df['Id'], df['Price'], color='r',alpha=0.5)
# print(df.index)
for i in df.index:
    ax.text(df['Id'][i], df['Price'][i]+5, df['Price'][i])
ax1 = plt.subplot(222)
ax1.pie(df['Size'], autopct='%.1f%%',labels=df['Id'],wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'})
df_house_count = df.groupby('Region')['Price'].count().reset_index()
print(df.groupby('Region').sum())
for name,group in df.groupby('Region'):
    print(name,group['Price'])

ax3 = plt.subplot(223)
# print(df_house_count)
ax3.bar(df_house_count['Region'], df_house_count['Price'])
for i in df_house_count['Price'].index:
    ax3.text(df_house_count['Region'][i], df_house_count['Price'][i]+0.1, df_house_count['Price'][i])

ax3.set_xticklabels(["东北", "东南", "东城", "北城", "南城", "西城"], FontProperties=myfont)
ax3.set_title('北京各大区二手房数量对比',FontProperties=myfont)
plt.show()