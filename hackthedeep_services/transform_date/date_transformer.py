import os, sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import date_formatter 
from date_formatter import format_date
import numpy as np


def transform_date(file):
	wb = pd.read_csv(file, na_filter=False)
	date_columns= []
	columns=list(wb.columns.values)

	for column in columns:
		if ('date' in column.lower()):
			date_columns.append(column)
	
	data_columns.remove("update") 
	
	dataframe=wb[data_columns]
	
	rows_to_parse = []

	for row in dataframe.itertuples():
		for column in date_columns:
			wb['New_'+ column] = format_date(row[column])

	output_file="/data/transformed_date.csv"
	output_file=wb.to_csv(output_file, index=False)

	return output_file

if __name__ == '__main__':
    filename = sys.argv[1]
    transform_date(filename)