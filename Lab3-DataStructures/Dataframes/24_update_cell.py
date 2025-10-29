"""
use the dataframe's .at property
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
print('before update..', dfAQI)
dfAQI.at[2, 'concern'] = 'Unhealthy For Some'
print('after update...', dfAQI)
