#first its necessary to install package pip install pandas and then import statement 
import pandas as pd

serie = pd.Series([4, 7, 6, 2, 1])

print(serie)

#get a specific element

print(serie.loc[2])

#adding specific index to serie

serie2 = pd.Series([1, 2, 3], index = [10, 11, 12])
print(serie2)