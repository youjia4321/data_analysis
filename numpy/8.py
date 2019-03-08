import numpy as np
from numpy.linalg import inv, qr
s = np.random.randn(5, 5)
print(s)
print(inv(s))