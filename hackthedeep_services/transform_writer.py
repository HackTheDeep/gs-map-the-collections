import csv
import json
def convert_csv_to_json():
	with open('test.csv', 'rb') as csvfile:
		converted_dict = csv.DictReader(csvfile)
		fieldnames = ['localityBaySoundHarbor'
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
		,'trackingCatSuffix'
		]
		output = []
		for row in converted_dict:
			new_map = {}
			for key in row:
				if key.strip() in fieldnames:
					new_map[key] = row[key]
			output.append(new_map)
		out = json.dumps(output)
		print out
convert_csv_to_json()
			