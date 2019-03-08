import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
myfont = matplotlib.font_manager.FontProperties(fname="/home/xjm/Desktop/projects/DataAnalysis/matplotlib/msyh.ttf")



def read():
    with open('/home/xjm/Desktop/projects/DataAnalysis/weiqiAnalysis/mianyang.json', 'r') as f:
        data = json.loads(f.read())
        df = pd.DataFrame(data)
        year = df['SPT'].str.split('-').str.get(1)
        df['SPT'] = year
        return df

def mian():
    # df = parse()
    df = read()
    grouped = df.groupby('SPT').count().reset_index() # 以月份分组求出各参数的总和
    plt.figure(1,figsize=(16,9))
    ax1 = plt.subplot()
    ax1.plot(grouped['SPT'], grouped['PARNM'], 'o--')
    ax1.set_xlabel('月份', FontProperties=myfont)
    ax1.set_ylabel('总参数量', FontProperties=myfont)
    ax1.set_title('月总参数量', FontProperties=myfont)
    for i in grouped.index:
       ax1.text(grouped['SPT'][i], grouped['PARNM'][i]+1, grouped['PARNM'][i])
    plt.savefig('year.png')
    df1 = df.set_index(['PARNM', 'SPT'])
    grouped1 = df1.groupby(level=['PARNM', 'SPT'])['MTDA']  # 以PARNM,SPT为索引值选择出MTDA这一列参数
    plt.figure(2, figsize=(16,9))
    faverage = grouped1.mean()
    faverage.plot(kind='bar')
    plt.ylabel('参数含量',  FontProperties=myfont)
    plt.xlabel('参数/月份',  FontProperties=myfont)
    plt.title('平均值',  FontProperties=myfont)
    plt.savefig('average.png')
    plt.figure(3,figsize=(16,9))
    fmin = grouped1.min()
    fmin.plot(kind='bar')
    plt.ylabel('参数含量',  FontProperties=myfont)
    plt.xlabel('参数/月份',  FontProperties=myfont)
    plt.title('最小值',  FontProperties=myfont)
    plt.savefig('min.png')
    plt.figure(4,figsize=(16,9))
    fmax = grouped1.max()
    fmax.plot(kind='bar')
    plt.ylabel('参数含量',  FontProperties=myfont)
    plt.xlabel('参数/月份',  FontProperties=myfont)
    plt.title('最大值',  FontProperties=myfont)
    plt.savefig('max.png')
    plt.figure(5,figsize=(16,9))
    fsum = grouped1.sum()
    fsum.plot(kind='bar')
    plt.ylabel('参数含量',  FontProperties=myfont)
    plt.xlabel('参数/月份',  FontProperties=myfont)
    plt.title('总和',  FontProperties=myfont)
    plt.savefig('sum.png')
    plt.figure(6,figsize=(16,9))
    fstd = grouped1.std()
    fstd.plot(kind='bar')
    plt.ylabel('参数含量',  FontProperties=myfont)
    plt.xlabel('参数/月份',  FontProperties=myfont)
    plt.title('标准差',  FontProperties=myfont)
    plt.savefig('std.png')
    plt.show()
if __name__ == "__main__":
    mian()
