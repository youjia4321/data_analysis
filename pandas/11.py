import pandas as pd
import numpy as np

df = pd.DataFrame({'A':['foo','bar','foo','bar','foo','bar','foo','foo'],'B':['one','one','two','three','two','two','one','three'],'C': np.random.randn(8), 'D': np.arange(8)})

print(df)

# print(df.groupby('A').first())
# print(df.groupby(['A','B']).first())

# 我们还可以根据列来分组，先创建一个get_type函数，如果列名为abem中之一，就分为组别vowel，反之为consonant

def get_type(letter):
    if letter.lower() in 'abem':
        return 'vowel'
    else:
        return 'consonant'

gropued = df.groupby(get_type, axis=1)
print(gropued.first())