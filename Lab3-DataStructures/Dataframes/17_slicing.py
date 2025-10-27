"""
Similar to lists, DataFrames provide slicing to get part of the data
Index can be a slice
When using slices containing labels with loc, the range specified includes the high index ('Test3'):
"""
import pandas as pd #alias
import functions
aqi = {
    'color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
    'concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups',
                'Unhealthy', 'Very Unhealthy', 'Hazardous'],
    'low': [0,  51,  101, 151, 201, 301],
    'high':[50, 100, 150, 200, 300, 999]
    }
df2 = pd.DataFrame(aqi)
print(df2)
print(df2.loc[0:1])