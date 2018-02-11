import pandas as pd
import requests
from autocorrect import spell
import re

geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
google_api_key = 'AIzaSyCDj2fjKj5aq2TPMI-LTqCpk18pAxiTw8Q'
batch_size = 10000


def get_file_data(fileName):
	df = pd.read_excel(fileName)
	data = df[['Tracking Number', 'Continent', 'Country', 'Department / Province / State', 'County', 'City/Town/Hamlet', 'Specific Locale']]
	data.to_csv('data/DirtyDataLocationSubset.csv', index=False)
	return(data)



def make_request_to_geo(relativeUrl, option):
	relativeUrl = relativeUrl.replace("nan", "")
	option = option.replace("nan", "")
	params = {'address': relativeUrl, 'key': google_api_key}
	params2 = {'address': option, 'key': google_api_key}
	print(relativeUrl)
	try:
		r = requests.get(url = geocode_url, params = params)
		s = requests.get(url = geocode_url, params = params2)
		r.raise_for_status()
	except requests.exceptions.HTTPError as err:
		return {'error': 'Error in request'}

	if (r.status_code == 204):
		return {'error': 'None Found'}

	data = r.json()
	data2 = s.json()
	try: 
		if (len(data)):
			print(str(data["results"][0]["geometry"]["location"]["lat"]), str(data["results"][0]["geometry"]["location"]["lng"]))
			return (str(data["results"][0]["geometry"]["location"]["lat"]), str(data["results"][0]["geometry"]["location"]["lng"]))
	except:
		try: 
			if (len(data2)):
				print(str(data2["results"][0]["geometry"]["location"]["lat"]), str(data2["results"][0]["geometry"]["location"]["lng"]))
				return (str(data2["results"][0]["geometry"]["location"]["lat"]), str(data2["results"][0]["geometry"]["location"]["lng"]))
		except: 
			return ("", "")
	return ("", "")


	return {'error': 'None Found'}


def clean_file(data):
	data['new_continent'] = data['Continent'].apply(lambda x: clean_data(str(x)))
	data["new_country"] = data["Country"].apply(lambda x: clean_data(str(x)))
	data['new_department / Province / State'] = data['Department / Province / State'].apply(lambda x: clean_data(str(x)))
	data['new_county'] = data['County'].apply(lambda x: clean_data(str(x)))
	data['new_city/Town/Hamlet'] = data['City/Town/Hamlet'].apply(lambda x: clean_data(str(x)))
	data['new_specific Locale'] = data['Specific Locale'].apply(lambda x: clean_data(str(x)))

	data.to_csv('data/CleanDataLocationSubset.csv', index=False)
	return(data)


def clean_data(data):
	if data == "NaN" or data == "nan":
		return ""
	if len(data.split()) > 3:
		return ""
	data = re.sub('[^0-9a-zA-Z\s]+', '', data)
	return "" if spell(data) == "NaN" or spell(data) == "nan" else spell(data)


def get_geo_location(df):
	#df['new_coordinates'] = df.apply(lambda row: make_request_to_geo(s = '{} {} {} {} {} {}'.format(row['Continent'], row['Country'], row['Department / Province / State'], row['County'], row['City/Town/Hamlet'],row['Specific Locale']), s), axis=1)
	df['new_coordinates'] = df.apply(lambda row: make_request_to_geo('{} {} {} {} {} {}'.format(row['new_continent'], row['new_country'], row['new_department / Province / State'], row['new_county'], row['new_city/Town/Hamlet'],row['new_specific Locale']), '{} {} {} {}'.format(row['new_country'], row['new_department / Province / State'], row['new_county'], row['new_city/Town/Hamlet'])), axis=1)
	df['new_longitude'] = df["new_coordinates"].apply(lambda x: "" if x == None or x == () else x[0])
	df['new_latitude'] = df["new_coordinates"].apply(lambda x: "" if x == None or x == () else x[1])
	return(df)

def combine_location_data(dirtyData, geoLocation):
	data = pd.merge(dirtyData, geoLocation, on=['Tracking Number','Tracking Number'])
	data.to_csv('data/CleanedDataSet.csv', index=False)
	return(data)


def main(fileName):
	dirtyData = pd.read_excel(fileName)
	df = get_file_data(fileName)
	df = clean_file(df)
	df = get_geo_location(df)
	return(combine_location_data(dirtyData, df))





#make_request_to_geo()
#make_request_to_geo("USA")
# clean_file()
# df = get_geo_location()
# data = combine_location_data(df)
# print(data)

print(main("data/DirtyDataSmallSubset.xlsx"))
