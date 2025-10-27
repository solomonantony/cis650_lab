"""
To get a single cell value, can use .iloc[rowNumber][colNumber]
Or, use [colname][rowname]
DataFrame method at[row_name,col_name] and iat[row_num, col_num] attributes get a single value from a DataFrame
"""
import pandas as pd #alias
import functions
# define the dictionary of parallel lists
aqi = {
    'color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
    'concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups',
                'Unhealthy', 'Very Unhealthy', 'Hazardous'],
    'low': [0,  51,  101, 151, 201, 301],
    'high':[50, 100, 150, 200, 300, 999]
    }
df2 = pd.DataFrame(aqi)
print(df2.iloc[1][1])
