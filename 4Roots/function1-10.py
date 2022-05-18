import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.10)
y = x * 3

print("Point x:{}".format(x))
print("Point y:{}".format(y))

plt.plot(x,y)
plt.show()