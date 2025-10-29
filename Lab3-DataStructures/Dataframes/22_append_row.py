""""
Create a dataframe for the new row.  
Then use the dataframe's .concat method
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

print('before new row...', dfAQI)
new_row = pd.DataFrame({'color': 'Brown', 'concern': 'Worst', 'low': 1000, 'high': 9999}, index=[7])
new_df = pd.concat([dfAQI, new_row])
print('after new row...', new_df)

