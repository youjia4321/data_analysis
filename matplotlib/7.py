import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure(1)
ghj =[5, 10 ,15, 20, 25]
it =[ 1, 2, 3, 4, 5]
plt.subplot(211)
plt.bar(ghj, it)
plt.xlabel('ghj')
plt.ylabel('it')
plt.title('ghj')
plt.grid(True)


df = pd.DataFrame(np.random.rand(10, 2), columns=list('ab'))
plt.subplot(212)
plt.scatter(df['a'], df['b'])
plt.xlabel('a')
plt.ylabel('b')
plt.grid(True)

arr = np.arange(100).reshape((10,10))
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")

from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("right", "5%", pad="3%")
plt.colorbar(im, cax=cax)

plt.tight_layout()
plt.show()
