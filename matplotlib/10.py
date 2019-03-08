# 从网页中加载json数据
import json
import requests
import matplotlib.pyplot as plt


url = 'https://api.douban.com/v2/book/1220562'
data = requests.get(url).text

# print(data)
#用josn将字符串数据转化为python字典
formData = json.loads(data)
# print(formData)

#获取字典中key值为tags对应的数据
tags=formData["tags"]
x= []
y= []


plt.figure(1)
ax1 = plt.subplot()
i = 1
for tag in tags:

    print("{}----{}".format(tag["name"],tag["count"]))
    x.append(tag["name"])
    y.append(tag["count"])
    ax1.text(tag["name"], tag["count"], tag["count"])
    i += 1
    

ax1.bar(x,y,label='Book Search')
ax1.set_title('Book search rankings')
ax1.legend()
plt.show()
