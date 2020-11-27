#first its necessary to install package pip install pandas and then import statement 
import pandas as pd

serie = pd.Series([4, 7, 6, 2, 1])

print(serie)

#get a specific element

print(serie.loc[2])