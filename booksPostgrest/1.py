import json
import requests
import matplotlib.pyplot as plt
import matplotlib

myfont = matplotlib.font_manager.FontProperties(fname="msyh.ttf")
url = 'http://localhost:3000/books?select=name,views'
resp = requests.get(url)
data = json.loads(resp.text)

plt.figure(1, figsize=(10,10))
ax1 = plt.subplot()
plt.figure(2, figsize=(10,10))
ax2 = plt.subplot()
x = []
y = []
for i in data[:20]:
    x.append(i['views'])
    y.append(i['name'].split(" ")[0])
    ax2.text(i['name'].split(" ")[0], i['views']+1, i['views'])
ax1.pie(x, autopct='%.1f%%', labels=y)



ax2.bar(y, x, alpha=0.5)
ax2.set_title("图书浏览量", FontProperties=myfont)
ax2.set_xlabel("书名", FontProperties=myfont)
ax2.set_ylabel("浏览次数", FontProperties=myfont)
plt.show()
