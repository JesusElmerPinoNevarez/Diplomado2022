import math

def f(x):
  return (2*(math.sin(math.sqrt(x)))-x)

a, b= 0, 1.9724
m = ((a+b)/2)

r1 = f(a)*(b-a)
print("Regla del rectángulo  I = {}".format(r1))

r2 = f(m)*(b-a)
print("Regla del punto medio I = {}".format(r2))

r3 = ((b-a)/2)*(f(a)+f(b))
print("Regla del trapecio I = {}".format(r3))

r4 = ((b-a)/6)*(f(a)+(4*f(m))+f(b))
print("Regla de Simpson I = {}".format(r4))