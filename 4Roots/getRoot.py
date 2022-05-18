import matplotlib.pyplot as plt
from math import exp

def f(x):
  return exp(2-x)-7*x

def f2(x):
  return -exp(2-x)-7

x = [1.5]
x.append(x[0] - f(x[0]) / f2(x[0]))
x.append(x[1] - f(x[1]) / f2(x[1]))
x.append(x[2] - f(x[2]) / f2(x[2]))

print("x0 = ", x[0])
print("x1 = ", x[1])
print("x2 = ", x[2])
print("x3 = ", x[3])
print("Value = ", f(x[3]))
print('Roots is =', x[3])

x1 = [-2, -1, 0, 1, 2]
y = [68.59815, 27.085537, 7.38056, -4.281718, -13]

plt.plot(x1, y)
plt.show()

y1 = [-61.59815, -27.085537, -14.389056, -9.718282, -8]

plt.plot(x1, y1)
plt.show()

plt.plot(x, y1)
plt.show()