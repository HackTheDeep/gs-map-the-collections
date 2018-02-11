import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

wb = pd.read_csv('/Volumes/Macintosh HD 2/HACK THE DEEP/Test.csv')

df1 = wb[['Family Name in Database', 'Genus Name', 'Species Name in Database']]
print(df1)