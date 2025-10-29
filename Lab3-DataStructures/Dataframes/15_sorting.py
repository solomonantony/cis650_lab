"""
To sort a DataFrame, use the sort_values() method
The sort_values() method has the named parameter inplace
Can sort a DataFrame by its rows or columns, based on their indices or values
Sort the rows by their indices in descending order using sort_index and its keyword argument ascending=False
"""
import pandas as pd #alias
import functions
# define the dictionary
aqi = {
    'color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
    'concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups',
                'Unhealthy', 'Very Unhealthy', 'Hazardous'],
    'low': [0,  51,  101, 151, 201, 301],
    'high':[50, 100, 150, 200, 300, 999]
    }
df2 = pd.DataFrame(aqi)
print(df2.sort_values('color', ascending=False))
print(df2.sort_values('concern'))
