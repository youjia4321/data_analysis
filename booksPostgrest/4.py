import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(1,5, figsize=(15,3))
n = np.array([0,1,2,3,4,5])
x = np.array([1,2,3,4,5])
axes[0].scatter(x, 0.25*np.random.randn(len(x)))
axes[0].set_title("scatter")

axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")

axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes[2].set_title("bar")

axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)
axes[3].set_title("fill_between")

N = 15
A = np.random.random(N)
B= np.random.random(N)
X = np.arange(N)
axes[4].bar(X, A, color ='.75', hatch ='\\')
design = {
'facecolor' : 'y',
'edgecolor' : 'g', 
'boxstyle' : 'round' 
}
axes[4].bar(X, A+B , bottom = A, color ='r', alpha=.4 ,hatch ='/')
axes[4].set_title("bewteen")
axes[4].text(10, 2, 'Matplotlib', bbox=design)
plt.show()
