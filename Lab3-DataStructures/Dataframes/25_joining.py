"""
Join is based on index value by default
"""
import pandas as pd #alias
aqi = {
    'color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
    'concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups',
                'Unhealthy', 'Very Unhealthy', 'Hazardous'],
    'low': [0,  51,  101, 151, 201, 301],
    'high':[50, 100, 150, 200, 300, 999]
    }
df1 = pd.DataFrame(aqi)
print('first data frame...', df1)
df2 = pd.read_csv('C:/Users/santony/Desktop/cis650_lab-7/Lab3-DataStructures/Dataframes/aquidays.txt')
print('second dataframe...', df2)
#joining
result_df = df1.join(df2, lsuffix='_df1', rsuffix='_df2')
print('result of first joining...\n', result_df.columns)
print('joined..', result_df)
# change the index of the two dataframes
new_df1 = df1.set_index(['color'])
print('new df1.../n', new_df1)
new_df2 = df2.set_index(['color'])
print('new df2\n', new_df2)
result2_df = new_df1.join(new_df2, lsuffix='_newdf1', rsuffix='_newdf2' )
print('result2 \n', result2_df)
