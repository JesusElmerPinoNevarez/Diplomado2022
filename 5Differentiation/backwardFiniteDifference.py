from math import sin

def f(x):
  return ((sin(2*x))**3)/(x**4+1)

x0 = 2.45
h1 = 0.5
r1 = (f(x0)-f(x0-h1))/h1
print('R1 = {}'.format(r1))

h2 = 0.3
r2 = (f(x0)-f(x0-h2))/h2
print('R2 = {}'.format(r2))

h3 = 0.1
r3 = (f(x0)-f(x0-h3))/h3
print('R3 = {}'.format(r3))

h4 = 0.00001
r4 = (f(x0)-f(x0-h4))/h4
print('R4 = {}'.format(r4))

h5 = 0.0000001
r5 = (f(x0)-f(x0-h5))/h5
print('R5 = {}'.format(r5))

h6 = 0.0000000001
r6 = (f(x0)-f(x0-h6))/h6
print('R6 = {}'.format(r6))