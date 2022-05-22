from random import choice

def throwCoin():
    return choice(['aguila', 'sello'])

def evaluateCoinThrows(times):
    values = {}
    for iteration in range(times):
        coin = throwCoin()
        values[coin] = values.get(coin, 0) + 1
    return values
  
print(evaluateCoinThrows(1220))