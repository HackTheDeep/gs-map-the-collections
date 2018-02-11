import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

wb = pd.read_csv('/Volumes/Macintosh HD 2/HACK THE DEEP/Test.csv')

dataframe = wb[['Family Name in Database', 'Genus Name', 'Species Name in Database', 'Species Author Name - Last 1 ']]

for row in dataframe.itertuples():
	print row