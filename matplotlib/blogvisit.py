import json
import requests
import matplotlib.pyplot as plt
import matplotlib

myfont = matplotlib.font_manager.FontProperties(fname="msyh.ttf")
url = 'http://localhost:3000/books'
resp = requests.get(url)
data = json.loads(resp.text)

# print(data)
x = []
y = []


plt.figure(1, figsize=(9, 9))

ax1 = plt.subplot2grid((2,2),(0,0) ,colspan=2)
for visit in data[:10]:
    x.append(visit['name'])
    y.append(visit['price'])
    ax1.text(visit['name'], visit['price']+1, "$"+str(visit['price']))
plt.plot(x, y, label="name--price")
ax1.set_title("图书价格", FontProperties=myfont)
ax1.set_ylabel('价格(单位/元)', FontProperties=myfont)
ax1.set_xlabel("图书名", FontProperties=myfont)
ax1.legend()
# ax.annoate()
a = []
b = []
ax2 = plt.subplot(223)
for visit in data[20:50]:
    a.append(visit['price'])
    b.append(visit['views'])
    ax2.text(visit['price'], visit['views']+3, str(visit['views']))
    # ax2.text(visit['price'], -6, str(visit['price']))
ax2.scatter(a,b, label="price--views", color='r')
ax2.set_xlabel("图书价格", FontProperties=myfont)
ax2.set_ylabel("浏览量(单位/次)", FontProperties=myfont)
ax2.set_title("图书浏览量", FontProperties=myfont)
ax2.legend()
# plt.axis([0,max(a)+10,0,max(b)+10])
# plt.show()

ax3 = plt.subplot(224)
q = []
w = []
for visit in data[30:40]:
    q.append(visit['name'])
    w.append(visit['popularity'])
    ax3.text(visit['name'], visit['popularity'], str(visit['popularity'])+"%")
ax3.scatter(q,w)
ax3.set_ylabel("图书推荐度", FontProperties=myfont)
plt.show()

