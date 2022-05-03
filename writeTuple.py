import pickle

#tupleList = '845807', 'Macho', 284, 'Angus', '28/04/2022'
tupleList = input('Insert a tuple list:')

with open('tupleList.bin','wb') as fh:
  pickle.dump(tupleList, fh)

if tupleList:
  print('Done...')
else:
  print('Tuple list is empty')