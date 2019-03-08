import matplotlib.pyplot as plt
import matplotlib
plt.figure(figsize=(8,8))
GDP = [12406.8,13908.57,9386.87,9143.64]
myfont = matplotlib.font_manager.FontProperties(fname="msyh.ttf")
plt.subplot(211)
plt.bar(range(4), GDP, align = 'center',color='steelblue', alpha = 0.8)
plt.ylabel('GDP')
plt.title('四个直辖市GDP大比拼',FontProperties=myfont)
plt.xticks(range(4),['北京市','上海市','天津市','重庆市'], FontProperties=myfont)
plt.ylim([5000,15000])
for x,y in enumerate(GDP):
    plt.text(x,y+100,'%s' % round(y,1),ha='center')

plt.subplot(212)
GDP = [185691, 112182.8, 49386.4, 34666.3]
plt.bar(range(4), GDP, align='center',color='purple',alpha=0.3)
plt.ylabel('GDP')
plt.title('2017 World GDP Rank')
plt.xticks(range(4), ['USA', 'China', 'Japan', 'Germany'])
plt.ylim([10000, 200000])
for x,y in enumerate(GDP):
    plt.text(x,y+100,'%s' %round(y,1),ha='center')

plt.show()
