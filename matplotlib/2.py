import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
print(t)
plt.figure(1)
plt.subplot(221)
plt.plot(t, t, 'r--')

plt.xlabel('x')
plt.ylabel('y')

plt.subplot(222)
plt.plot(t, t**2, 'bs')

plt.xlabel('x')
plt.ylabel('y')

plt.subplot(223)
plt.plot(t, t**3, 'g^')

plt.xlabel('x')
plt.ylabel('y')

plt.subplot(224)
plt.plot(t, t**4, 'ob')


plt.xlabel('x')
plt.ylabel('y')
plt.annotate('local min', xy=(0, 0), xytext=(1, 200), arrowprops=dict(facecolor='black', shrink=.01))
plt.show()

