# import csv
# import json
# from datetime import datetime
# from elasticsearch import Elasticsearch
# from elasticsearch import helpers
# import pandas as pd
print 'file start'

# def convert_csv_to_json(file):
# 	print 'hello'
# 	wb = pd.read_csv(file, na_filter=False)
# 	# with open('C:\Users\Myagmardorj\Desktop\CleanedDataSet.csv', 'rb') as csvfile:
# 	date_columns= []
# 	columns=list(wb.columns.values)

# 	for column in columns:
# 		if ('new_' in column.lower()):
# 			date_columns.append(column)
# 	dataframe=wb[date_columns]
# 	converted_dict = dataframe.to_dict('records')
# 	print converted_dict
# 	# with open('C:\Users\Myagmardorj\Desktop\BadData.csv', 'rb') as csvfile:
# 		# converted_dict = csv.DictReader(csvfile)
# 		# # change column names to match excel headers
# 		# select_columns = ['localityBaySoundHarbor'
# 		# ,'localityContinent'
# 		# ,'localityCounty' 
# 		# ,'localityCountry' 
# 		# ,'localityDeptProvinceState'
# 		# ,'localityIRN'
# 		# ,'localityIsland'
# 		# ,'localityIslandGroup'
# 		# ,'localityLakePondResevoir'
# 		# ,'localityLatitude'
# 		# ,'localityLongitude'
# 		# ,'localityNotes'
# 		# ,'localityOcean'
# 		# ,'localityPreciseLocation'
# 		# ,'localityRiver'
# 		# ,'localitySeaGulf'
# 		# ,'localityStream'
# 		# ,'localityTownship'
# 		# ,'localityVerbatim'
# 		# ,'locationCollectedDayfrom'
# 		# ,'locationCollectedDayTo'
# 		# ,'locationCollectedMonthFrom'
# 		# ,'locationCollectedMonthTo'
# 		# ,'locationCollectedYearFrom'
# 		# ,'locationCollectedYearTo'
# 		# ,'locationCollectedDatefrom'
# 		# ,'locationCollectedDateTo'
# 		# ,'locationCollection'
# 		# ,'locationDepthEnd'
# 		# ,'locationDepthStart'
# 		# ,'locationElevationFrom'
# 		# ,'locationElevationTo'
# 		# ,'locationElevationVerbatim'
# 		# ,'taxGroup'
# 		# ,'taxNameFamily'
# 		# ,'taxNameGenus'
# 		# ,'taxNameOrder'
# 		# ,'taxNameSpecies'
# 		# ,'taxNameSubspecies'
# 		# ,'taxonomyNumberOfSpecimens'
# 		# ,'trackingNumber'
# 		# ,'trackingCatNumber'
# 		# ,'trackingCatPrefix'
# 		# ,'trackingCatSuffix',
# 		# 'LotIRN',
# 		# 'EMu Catalog IRN'
# 		# ]
# 	output = []
# 	for row in converted_dict:
# 		cleaned_row = {k.replace(" ",""): v.replace(" ","") for k,v in row.items()}
# 		new_map = {}
# 		for key in cleaned_row:
# 			cleaned_key = key.strip()
# 			if cleaned_key in select_columns:
# 				new_map[cleaned_key] = cleaned_row[cleaned_key]
# 		output.append(new_map)
# 	return json.dumps(output)

# def persist_doc_to_elasticsearch(documents):
# 	doc_list = json.loads(str(documents))
# 	es = Elasticsearch()
# 	#create index with specific mapping
# 	j = 0
# 	actions = []
# 	while (j < len(doc_list)):
# 		if 'LotIRN' in doc_list[j]:
# 			doc_id = doc_list[j]['LotIRN']
# 		elif 'EMu Catalog IRN' in doc_list[j]:
# 			doc_id = doc_list[j]['EMu Catalog IRN']
# 		else:
# 			raise Exception('Id field not found')
# 		action = {
# 	        "_index": "collections-data",
# 	        "_type": "collection",
# 	        "_id": doc_id,
# 	        "_source": doc_list[j]
# 	        }
# 		actions.append(action)
# 		j += 1	

# 	helpers.bulk(es, actions)

# convert_csv_to_json('C:\\Users\\Myagmardorj\\Desktop\\Hack the deep\\gs-map-the-collections\\hackthedeep_services\\CleanedDataSet.csv')
# def query_from_elasticsearch():
# 	res = es.search(index="collections-data", body={"query": {"match_all": {}}})
# 	print("Got %d Hits:" % res['hits']['total'])
# 	print 'blah'
# # convert_csv_to_json('C:\Users\Myagmardorj\Desktop\Hack the deep\gs-map-the-collections\hackthedeep_services\CleanedDataSet.csv')

# # persist_doc_to_elasticsearch(convert_csv_to_json('C:\Users\Myagmardorj\Desktop\Hack the deep\gs-map-the-collections\hackthedeep_services\CleanedDataSet.csv'))
# # query_from_elasticsearch()
# # if __name__ == '__main__':
# #     filename = sys.argv[1]
# #     print 'hello'
# #     #print ("filename",filename)
# #     convert_csv_to_json(filename)