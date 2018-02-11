import csv
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import pandas as pd
import uuid
es = Elasticsearch()
def convert_csv_to_json(file):
	workbook = pd.read_csv(file, na_filter=False)
	doc_columns= []
	columns=list(workbook.columns.values)
	select_columns = [
		'LotIRN',
		'EMu Catalog IRN'
		]
	for column in columns:
		cleaned_column = column.strip()
		# print cleaned_column
		if ('new_' in cleaned_column.lower() or cleaned_column in select_columns):
			doc_columns.append(column)
	# print 'doc_columns'
	# print doc_columns
	# print 'workbook'
	# print workbook

	dataframe=workbook[doc_columns]
	# nt 'dataframe'
	# print dataframepri
	converted_dict = dataframe.to_dict('records')
	# print 'converted_dict'
	# print converted_dict
	output = []
	for row in converted_dict:
		# cleaned_row = {k.replace(" ",""): v for k,v in row.items()}
		# for k,v in cleaned_row.items():
		# 	if type(v) is str:
		# 		cleaned_row = k, v.replace(" ","")
		new_map = {}
		for key, value in row.items():
			cleaned_key = key.strip()
			if type(value) is str:
				cleaned_value = value.strip()
			else: 
				cleaned_value = value
			row[key] = cleaned_value
			new_map[cleaned_key] = row[key]
		output.append(new_map)
	return json.dumps(output)

def persist_doc_to_elasticsearch(documents):
	doc_list = json.loads(str(documents))
	# print doc_list
	#create index with specific mapping
	j = 0
	actions = []
	print len(doc_list)
	while (j < len(doc_list)):
		if 'LotIRN' in doc_list[j]:
			doc_id = doc_list[j]['LotIRN']
		elif 'EMu Catalog IRN' in doc_list[j]:
			doc_id = doc_list[j]['EMu Catalog IRN']
		else:
			continue;
		action = {
	        "_index": "collections-data3",
	        "_type": "collection",
	        "_id": doc_id,
	        "_source": doc_list[j]
	        }
		actions.append(action)
		j += 1	

	helpers.bulk(es, actions)

persist_doc_to_elasticsearch(convert_csv_to_json('CleanedDataSet.csv'))

def query_from_elasticsearch():
	res = es.search(index="collections-data3", body={"query": {"match_all": {}}})
	print("Got %d Hits:" % res['hits']['total'])
	print res
query_from_elasticsearch()
