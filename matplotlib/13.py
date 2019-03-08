import matplotlib.pyplot as plt

plt.style.use('ggplot')

edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['Secondary','Junior College','Bachelor','Master','Others']

explode = [0,0.08,0,0,0]  # 用于突出显示大专学历人群
colors=['#FEB748','#EDD25D','#FE4F54','#51B4FF','#dd5555']
plt.axes(aspect='equal')
plt.pie(x = edu, explode=explode, labels=labels, colors=colors,autopct='%.1f%%',pctdistance=0.8, labeldistance = 1.15,wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},)
    # explode=explode, # 突出显示大专人群
    # labels=labels, # 添加教育水平标签
    # colors=colors, # 设置饼图的自定义填充色
    # utopct='%.1f%%', # 设置百分比的格式，这里保留一位小数
    # pctdistance=0.8,  # 设置百分比标签与圆心的距离
    # labeldistance = 1.15, # 设置教育水平标签与圆心的距离
    # startangle = 180, # 设置饼图的初始角度
    # radius = 1.5, # 设置饼图的半径
    # counterclock = False, # 是否逆时针，这里设置为顺时针方向
    # wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},# 设置饼图内外边界的属性值
    # textprops = {'fontsize':12, 'color':'k'}, # 设置文本标签的属性值
    # center = (1.8,1.8), # 设置饼图的原点
    # frame = 1# 是否显示饼图的图框，这里设置显示
plt.xticks(())
plt.yticks(())
plt.title('Zhima Credit Discredited User Analysis')
plt.show()