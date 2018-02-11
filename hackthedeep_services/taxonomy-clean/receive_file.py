import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import worms_taxonomy_check
from worms_taxonomy_check import get_taxonomy_for_species
import numpy as np

wb = pd.read_csv('/Volumes/Macintosh HD 2/HACK THE DEEP/Test.csv', na_filter=False)

dataframe = wb[['Family Name in Database', 'Genus Name', 'Species Name in Database', 'Species Author Name - Last 1 ']]

for row in dataframe.itertuples():
	print get_taxonomy_for_species(row._1, row._2, row._3, row._4)
