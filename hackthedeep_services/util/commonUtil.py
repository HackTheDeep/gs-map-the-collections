import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def new_column_mapping(dirty_filename, clean_filename):
	wb_dirty_file = pd.read_excel(dirty_filename, na_filter=False)
	dirty_columns=list(wb_dirty_file.columns.values)
	print(len(dirty_columns))	
	wb_clean_file = pd.read_excel(clean_filename, na_filter=False)
	clean_columns=list(wb_clean_file.columns.values)
	print(len(clean_columns))
	if(len(dirty_columns) == len(clean_columns)):
		return clean_columns
	return []

# print(new_column_mapping("C:\\Users\\bpala\\OneDrive\\Documents\\GitHub\\gs-map-the-collections\\hackthedeep_services\\date-clean\\CleanedDataSet.xlsx",
# 	"C:\\Users\\bpala\\OneDrive\\Documents\\GitHub\\gs-map-the-collections\\hackthedeep_services\\date-clean\\DirtyDataSmallSubset.xlsx"))		
