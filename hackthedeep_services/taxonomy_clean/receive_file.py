import os, sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import worms_taxonomy_check
from worms_taxonomy_check import get_taxonomy_list_batch

def taxonomy_clean(file):
	wb = pd.read_csv(file, na_filter=False)

	dataframe = wb[['Family Name in Database', 'Genus Name', 'Species Name in Database', 'Species Author Name - Last 1 ']]
	family_name_changed = []
	species_name_changed = []
	genus_name_changed = []
	author_name_changed = []
	unresolved = []

	rows_to_parse = []
	for row in dataframe.itertuples():
		rows_to_parse.append([row._1, row._2, row._3, row._4])

	results = get_taxonomy_list_batch(rows_to_parse)

	for result in results:
		if ('error' in result):
			unresolved.append(result['error'])
			family_name_changed.append('')
			species_name_changed.append('')
			genus_name_changed.append('')
			author_name_changed.append('')
		else:
			if ('family' in result):
				family_name_changed.append(result['family'])
			else:
				family_name_changed.append('')
			if ('species' in result):
				species_name_changed.append(result['species'])
			else:
				species_name_changed.append('')
			if ('genus' in result):
				genus_name_changed.append(result['genus'])
			else:
				genus_name_changed.append('')
			if ('author_name' in result):
				author_name_changed.append(result['author_name'])
			else:
				author_name_changed.append('')
			unresolved.append('')

	wb['New_Family Name in Database'] = family_name_changed
	wb['New_Species Name in Database'] = species_name_changed
	wb['New_Genus Name'] = genus_name_changed
	wb['New_Species Author Name - Last 1 '] = author_name_changed
	wb['Unresolved_Taxonomy'] = unresolved

	wb.to_csv(file, index=False)

	return file
