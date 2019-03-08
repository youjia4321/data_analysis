import matplotlib.pyplot as plt
price = [39099, 5899, 13599, 12399, 68599]
plt.figure(1)
plt.subplot(211)
plt.barh(range(5),price,align='center',color='red',alpha=0.5)
plt.title('Dog Price Comparsion')
plt.xlabel('price')
plt.yticks(range(5),['Husky','French Bulldog','Golden Retriever','Labrador Retriever','Shiba Inu'])
plt.xlim([3000,80000])
for x,y in enumerate(price):
    print(x)
    plt.text(y+100,x,'%s' % y,va='center')
plt.show()

