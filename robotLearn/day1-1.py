import numpy as np
from sklearn import preprocessing  # 数据预处理
input_data = np.array([[2.1, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [0.5, -7.9, 5.6],
                      [5.9, 2.3, -5.8]])

# 这是当需要将数值转换为布尔值时使用的预处理技术。我们可以用一种内置的方法来二值化输入数据，比如说用0.5作为阈值，方法如下 (所有高于0.5(阈值)的值将被转换为1，并且所有低于0.5的值将被转换为0。)

data_binarized = preprocessing.Binarizer(threshold = 0.5).transform(input_data)
print("\nBinarized data:\n", data_binarized)

# 平均值和标准偏差 - (axis=0为列)

print("Mean = ", input_data.mean(axis = 0))
print("Std deviation = ", input_data.std(axis = 0))

# 删除输入数据的平均值和标准偏差 -(scale 零均值单位方差)

data_scaled = preprocessing.scale(input_data)
print(data_scaled)
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis = 0))

# 最小最大缩放

data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print ("\nMin max scaled data:\n", data_scaled_minmax)

'''
def featureScaling(arr):
    scaler = preprocessing.MinMaxScaler()
    result = scaler.fit_transform(arr)
    return result

# tests of your feature scaler--line below is input data
data = np.array([[640.], [1440.], [1920.]])
print(featureScaling(data))
'''

# L1标准化它也被称为最小绝对偏差。 这种标准化会修改这些值，以便绝对值的总和在每行中总是最多为1。 它可以在以下Python代码，使用上面的输入数据来实现 -# Normalize data
data_normalized_l1 = preprocessing.normalize(input_data, norm = 'l1')
print("\nL1 normalized data:\n", data_normalized_l1)


# PythonL2标准化它也被称为最小二乘。这种归正常化修改了这些值，以便每一行中的平方和总是最多为1。它可以在以下Python代码，使用上面的输入数据来实现 -# Normalize data
data_normalized_l2 = preprocessing.normalize(input_data, norm = 'l2')
print("\nL2 normalized data:\n", data_normalized_l2)