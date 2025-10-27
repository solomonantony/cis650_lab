import pandas as pd #alias
import functions
adict = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
df2 = pd.DataFrame(adict)
print(df2.head())
print(df2.info())
print(len(df2))
print(df2.shape)