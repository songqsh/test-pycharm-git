# This is the first python code

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, .01)
plt.plot(x, np.sin(x))
plt.show()