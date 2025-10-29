"""
Maintaining DataFrame data Appending a column
a list can be appended to a DataFrame: df['new_colname'] = list
"""
import pandas as pd #alias
aqi = {
    'color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
    'concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups',
                'Unhealthy', 'Very Unhealthy', 'Hazardous'],
    'low': [0,  51,  101, 151, 201, 301],
    'high':[50, 100, 150, 200, 300, 999]
    }
dfAQI = pd.DataFrame(aqi)
dfAQI['rank'] = [1, 2, 3, 4, 5, 6]
print(dfAQI)
