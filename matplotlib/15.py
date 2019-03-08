import pandas as pd
import matplotlib.pyplot as plt

data = {"a": 26, "b": 73, "c": 100}

d = pd.Series(data)
print(d)

df = pd.DataFrame(d)

plt.bar(['a', 'b', 'c'], df[0])
plt.show()
