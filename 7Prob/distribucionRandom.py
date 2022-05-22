import random
import matplotlib.pyplot as plt

x = []
y = []

for n in range(100):
  x.append(n*0.1)
  y.append(random.uniform(0, 60))

plt.plot(x,y)
plt.show()