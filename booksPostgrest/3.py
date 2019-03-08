import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
myfont = matplotlib.font_manager.FontProperties(fname="msyh.ttf")
df = pd.read_csv("test.csv")

df_house_count = df.groupby('Region')['Price'].count().reset_index()

ax1 = plt.subplot()
sns.barplot(x='Region', y='Price', palette="Greens_d", data=df_house_count, ax=ax1)
ax1.set_title('北京各大区二手房数量对比',fontsize=15, FontProperties=myfont)
ax1.set_xlabel('区域', FontProperties=myfont)
ax1.set_ylabel('数量', FontProperties=myfont)
ax1.set_xticklabels(["东北", "东南", "东城", "北城", "南城", "西城"], FontProperties=myfont)
plt.show()