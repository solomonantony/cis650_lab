"""
To access a particular DataFrame column, use square brackets [ ]
similar to Python list and dictionary item access
The result of column access is a pandas Series -- dfAQI.concern
can use this shorthand if column name is a valid variable name
Convert from Series to list using tolist() method
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
print('all the columns...\n', df2)
print('only two selected column...\n', df2[['low','high']])
