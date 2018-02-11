import os, sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import date_formatter 
from date_formatter import format_date
import numpy as np


def transform_date(file):
	
	wb = pd.read_csv(file, na_filter=False)
	#wb = pd.read_csv(file, na_filter=False)
	date_columns= []
	columns=list(wb.columns.values)
	
	for column in columns:
		if ('date' in column.lower()):
			if('updated' in column.lower()):
				continue
			else:
				date_columns.append(column)

	#print ("date_columns", date_columns)
	dataframe=wb[date_columns]
	
	rows_to_parse = []

	for row in dataframe.itertuples():
		for column in row:
			if column in [0, '']:
				continue
			if 'column == "NaT"':
				continue
			wb['New_'+ column] = format_date(column)

	wb.to_csv(file, index=False)
	return file

if __name__ == '__main__':
    filename = sys.argv[1]
    #print ("filename",filename)
    transform_date(filename)