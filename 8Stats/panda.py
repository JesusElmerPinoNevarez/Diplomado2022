import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')

listOne = iris['sepal length'].tolist()
listTwo = iris['sepal width'].tolist()
tupleOne = tuple(iris['petal length'])
tupleTwo = tuple(iris['petal width'])
dictionary = dict(iris['class'])

print(listOne)
print(listTwo)
print(tupleOne)
print(tupleTwo)
print(dictionary)