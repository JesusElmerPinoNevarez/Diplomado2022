import pickle

with open('tupleList.bin','rb') as fh:
  tupleList = pickle.load(fh)

if tupleList:
  print(tupleList)
else:
  print('Tuple list is empty')