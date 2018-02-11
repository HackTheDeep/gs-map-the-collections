import csv
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

def convert_csv_to_json():
	with open('test.csv', 'rb') as csvfile:
		converted_dict = csv.DictReader(csvfile)
		# change column names to match excel headers
		select_columns = ['localityBaySoundHarbor'
		,'localityContinent'
		,'localityCounty' 
		,'localityCountry' 
		,'localityDeptProvinceState'
		,'localityIRN'
		,'localityIsland'
		,'localityIslandGroup'
		,'localityLakePondResevoir'
		,'localityLatitude'
		,'localityLongitude'
		,'localityNotes'
		,'localityOcean'
		,'localityPreciseLocation'
		,'localityRiver'
		,'localitySeaGulf'
		,'localityStream'
		,'localityTownship'
		,'localityVerbatim'
		,'locationCollectedDayfrom'
		,'locationCollectedDayTo'
		,'locationCollectedMonthFrom'
		,'locationCollectedMonthTo'
		,'locationCollectedYearFrom'
		,'locationCollectedYearTo'
		,'locationCollectedDatefrom'
		,'locationCollectedDateTo'
		,'locationCollection'
		,'locationDepthEnd'
		,'locationDepthStart'
		,'locationElevationFrom'
		,'locationElevationTo'
		,'locationElevationVerbatim'
		,'taxGroup'
		,'taxNameFamily'
		,'taxNameGenus'
		,'taxNameOrder'
		,'taxNameSpecies'
		,'taxNameSubspecies'
		,'taxonomyNumberOfSpecimens'
		,'trackingNumber'
		,'trackingCatNumber'
		,'trackingCatPrefix'
		,'trackingCatSuffix',
		'LotIRN',
		'EMu Catalog IRN'
		]
		output = []
		for row in converted_dict:
			cleaned_row = {k.replace(" ",""): v.replace(" ","") for k,v in row.items()}
			new_map = {}
			for key in cleaned_row:
				cleaned_key = key.strip()
				if cleaned_key in select_columns:
					new_map[cleaned_key] = cleaned_row[cleaned_key]
			output.append(new_map)
		return json.dumps(output)

def persist_doc_to_elasticsearch(documents):
	doc_list = json.loads(str(documents))
	es = Elasticsearch()
	#create index with specific mapping
	j = 0
	actions = []
	while (j < len(doc_list)):
		if 'LotIRN' in doc_list[j]:
			doc_id = doc_list[j]['LotIRN']
		elif 'EMu Catalog IRN' in doc_list[j]:
			doc_id = doc_list[j]['EMu Catalog IRN']
		else:
			raise Exception('Id field not found')
		action = {
	        "_index": "collections-data",
	        "_type": "collection",
	        "_id": doc_id,
	        "_source": doc_list[j]
	        }
		actions.append(action)
		j += 1	

	helpers.bulk(es, actions)



def query_from_elasticsearch():
	res = es.search(index="collections-data", body={"query": {"match_all": {}}})
	print("Got %d Hits:" % res['hits']['total'])


persist_doc_to_elasticsearch(convert_csv_to_json())
			