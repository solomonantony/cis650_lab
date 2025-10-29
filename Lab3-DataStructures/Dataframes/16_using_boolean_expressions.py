"""
One of pandas’ more powerful selection capabilities is Boolean indexing
Select all the A grades—that is, those that are greater than or equal to 90:
Pandas checks every grade to determine whether its value is greater than or equal to 90 and, if so, includes it in the new DataFrame.
Grades for which the condition is False are represented as NaN (not a number) in the new `DataFrame
NaN is pandas’ notation for missing values
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
using_True_False = df2[[True, True, False, True, False, True]]
print('using true false...\n', using_True_False)
less_than_150 = df2[df2.low<150]
print('less than 150...\n', less_than_150)

print(df2[df2.high <= 100][['color', 'concern', 'high']])
level = 75
print(df2[(df2.low < level) & (level <= df2.high)])
