import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 0.5)
y = np.random.rayleigh(3.4, 200)

plt.plot(x,y)
plt.show()