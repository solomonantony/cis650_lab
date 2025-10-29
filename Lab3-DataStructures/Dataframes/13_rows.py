"""
DataFrames support indexing capabilities with [], but pandas documentation recommends using the attributes loc, iloc, at and iat
Access by index name: .loc[ ]
Access by row number: .iloc[ ]
"""
import pandas as pd #alias
import functions
# define the dictionary of parallel lists
grades = {
    'color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
    'concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups',
                'Unhealthy', 'Very Unhealthy', 'Hazardous'],
    'low': [0,  51,  101, 151, 201, 301],
    'high':[50, 100, 150, 200, 300, 999]
    }
df2=pd.DataFrame(grades)
print(df2.loc[0])

