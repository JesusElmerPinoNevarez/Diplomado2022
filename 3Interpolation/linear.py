Xn = [-4, 1]
Yn = [-2, 5]
X = ""
Y = 3.7

def interpolation(Xn, Yn, X, Y):
  output = ""
  if X:
    output = Yn[0] + (X - Xn[0]) * ((Yn[1] - Yn[0])/(Xn[1] - Xn[0]))
  elif Y:
    output = Xn[0] + (Y - Yn[0]) * ((Xn[1] - Xn[0])/(Yn[1] - Yn[0]))
  return output

print("Result of",("Y" if X else "X"),"is:",round(interpolation(Xn, Yn, X, Y), 4))