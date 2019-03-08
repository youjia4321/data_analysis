import numpy as np
from sklearn import preprocessing

# 定义样本标签

input_labels = ['red','black','red','green','black','yellow','white']

# 创建和训练标签编码器对象

encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

# print(encoder)   # LabelEncoder() 训练标签编码器对象,通过编码随机排序列表来检查性能

test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels)
print("Encoded values =", list(encoded_values))

# 通过解码一组随机数来检查性能 -

encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("\nDecoded labels =", list(decoded_list))
