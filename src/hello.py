# This is the first python code

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, .01)
plt.plot(x, np.sin(x))
plt.show()

l1 = [0]*10
print(l1)

for ind in range(1, 3):
    l1[ind*2] = 1

print(l1)
