"""
You can select a subset of rows and columns and assign to new dataframe
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
df_subset = df2.loc[0:2, ['color', 'concern']]
print(df_subset)
