import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt


def read():
    with open('mianyang.json', 'r') as f:
        data = json.loads(f.read())
        df = pd.DataFrame(data)
        return df


def element(df, str, minD, maxD):
    try:
        new_df = df[df['PARNM']==str]
        new_df.index = new_df['MTDA']
        print('该值%s的范围为(%d~%d)' % (str, minD, maxD))
        for i in new_df.index:
            if (i > maxD) or (i < minD): 
                print('数值异常!!!  发生在%s, %s为%s' % (new_df['SPT'][i], str,  i))
    except:
        print("没有此项参数")


if __name__ == "__main__":
    df = read()
    element(df, 'pH值', 6, 8)
    element(df, '溶解氧', 3, 4)
