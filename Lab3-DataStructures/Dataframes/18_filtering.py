"""
A filter expression returns a subset of rows
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
df_filtered = df2[df2.high <= 100][['color', 'concern', 'high']]
print(df_filtered)


