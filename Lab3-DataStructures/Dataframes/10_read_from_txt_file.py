import pandas as pd
import os
os.chdir("C:/Users/santony/Documents/Learning/CIS650/cis650_lab/Lab3-DataStructures/Lab10-Dataframes/")
df = pd.read_csv('aqi.txt')
# Above assumes a comma-separated file
# Also assumes the first row in the file contains column headings
print(df)
