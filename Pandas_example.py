#first its necessary to install package pip install pandas and then import statement 
import pandas as pd

serie = pd.Series([4, 7, 6, 2, 1])

print(serie)

#get a specific element 

print(serie.loc[2])

#adding specific index to serie

serie2 = pd.Series([1, 2, 3], index = [10, 11, 12])
print(serie2)


serie2 = pd.Series([1, 2, 3], index = ['a', 'b', 'c'])
print(serie2)

#adding a new value to an index

serie2.loc['c'] = 100
print(serie2)

#print only selected index
print(serie2.loc[['a', 'b']])

#using operator : 

serie3 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(serie3.loc[5:])