import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
myfont = matplotlib.font_manager.FontProperties(fname="/home/xjm/Desktop/projects/DataAnalysis/matplotlib/msyh.ttf")



def read(path):
    with open(path, 'r') as f:
        data = json.loads(f.read())
        df = pd.DataFrame(data)
        return df

def analysis(df):
    grouped = df.groupby('PARNM')['MTDA'].count().reset_index()
    print(grouped)
    fig, axes = plt.subplots(2,3, figsize=(14,9))
    axes[0][0].bar(grouped['PARNM'], grouped['MTDA'], color='r', alpha=.3, width=.5)
    axes[0][0].set_xticklabels(grouped['PARNM'], FontProperties=myfont)
    axes[0][0].set_title('PARNM参数的数量', FontProperties=myfont)
    axes[0][0].set_ylabel('数量', FontProperties=myfont)
    for i in grouped.index:
        axes[0][0].text(grouped['PARNM'][i], grouped['MTDA'][i], grouped['MTDA'][i])

    x = []
    a = []
    b = []
    c = [] 
    d = []
    o2 = df[df.PARNM=='溶解氧'].sort_values(by='SPT') # 按时间排序的溶解氧的曲线图
    te = df[df.PARNM=='温度'].sort_values(by='SPT')
    el = df[df.PARNM=='电导率'].sort_values(by='SPT')
    ph = df[df.PARNM=='pH值'].sort_values(by='SPT')
    nh4 = df[df.PARNM=='氨氮'].sort_values(by='SPT')
    print(o2, te, el, ph, nh4)
    for i in o2['SPT']:
        x.append(i.split(" ")[1])
    for i in el['SPT']:
        a.append(i.split(" ")[1])
    for i in ph['SPT']:
        b.append(i.split(" ")[1])
    for i in nh4['SPT']:
        c.append(i.split(" ")[1])
    for i in te['SPT']:
        d.append(i.split(" ")[1])
    axes[0][1].plot(x, o2['MTDA'], color='g', label='O2')
    
    axes[0][1].plot(d, te['MTDA'], color='r', label='Temperature')
    axes[0][1].set_title('溶解氧温度曲线', FontProperties=myfont)
    axes[0][1].set_ylabel('单位(mg/l,uS/cm)', FontProperties=myfont)
    
    axes[0][1].legend()
    axes[1][0].plot(x, o2['MTDA'], color='r',label='O2')
    axes[1][0].plot(b, ph['MTDA'], color='y',label='pH') 
    axes[1][0].plot(c, nh4['MTDA'], label='NH4')
    axes[1][0].set_title('pH,NH4,O2曲线', FontProperties=myfont)
    axes[1][0].set_ylabel('单位(PH,mg/l)', FontProperties=myfont)
    axes[1][0].legend()

    
    axes[1][1].set_ylabel('单位(℃)',FontProperties=myfont)
    axes[1][1].plot(a, el['MTDA'], label='Electrical')
    axes[1][1].set_title('电导率曲线', FontProperties=myfont)
    axes[1][1].legend()

    plt.savefig('1.png')
    plt.show()


def average(df):
    grouped = df.groupby('PARNM')['MTDA']
    count = grouped.agg([np.mean, np.sum, np.max, np.min, np.std]).reset_index()
    print(count)
    plt.figure(figsize=(14,9))
    ax1 = plt.subplot(231)
    ax1.plot(count['PARNM'], count['mean'], label='The average                                     ', color='r')
    ax1.set_xticklabels(count['PARNM'], FontProperties=myfont)
    ax1.legend()
    ax2 = plt.subplot(232)
    ax2.bar(count['PARNM'], count['sum'], label='The sum', color='y', alpha=.5)
    ax2.set_xticklabels(count['PARNM'], FontProperties=myfont)
    ax2.legend()
    ax3 = plt.subplot(233)
    ax3.plot(count['PARNM'], count['amax'], label='The max', color='g')
    ax3.set_xticklabels(count['PARNM'], FontProperties=myfont)
    ax3.legend()
    ax4 = plt.subplot(234)
    ax4.bar(count['PARNM'], count['amin'], label='The min', alpha=.5)
    ax4.set_xticklabels(count['PARNM'], FontProperties=myfont)
    ax4.legend()
    ax5 = plt.subplot(235)
    ax5.plot(count['PARNM'], count['std'], label='The std')
    ax5.set_xticklabels(count['PARNM'], FontProperties=myfont)
    ax5.legend()
    for i in count.index:
        ax1.text(count['PARNM'][i], count['mean'][i], '%.2f' % count['mean'][i])
    for i in count.index:
        ax2.text(count['PARNM'][i], count['sum'][i], '%.2f' % count['sum'][i])
    for i in count.index:
        ax3.text(count['PARNM'][i], count['amax'][i], '%.2f' % count['amax'][i])
    for i in count.index:
        ax4.text(count['PARNM'][i], count['amin'][i], '%.2f' % count['amin'][i])
    for i in count.index:
        ax5.text(count['PARNM'][i], count['std'][i], '%.2f' % count['std'][i])
    plt.show()

def main():
    # df = parse()
    # print(df)
    df = read("mianyang.json") # 7月份绵阳数据
    analysis(df) # 大概的曲线图
    average(df) # 各个参数的平均值 总和 最小值 最大值 标准差

if __name__ == "__main__":
    main()

