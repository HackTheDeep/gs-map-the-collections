import pandas as pd
import requests
from autocorrect import spell
import re

geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
google_api_key = 'AIzaSyCDj2fjKj5aq2TPMI-LTqCpk18pAxiTw8Q'
batch_size = 1000


def guess_date(string_date):
	str_date=str(string_date)
	str_date.replace(" ","")
	for fmt in ["%Y/%m/%d", "%d-%m-%Y", "%Y%m%d","%B,%Y","%B, %Y","%B%d,%Y","%B-%y","%d-%b-%y","%Y","%b-%y","%m/%d/%Y"]:
		print ("fmt", fmt )
		try:
			return datetime.strptime(str_date, fmt).date()
		except ValueError:
			continue
	print ("str_date2" , str_date)
	return str_date

def format1_date(str_date):
	dt=guess_date(str_date)
	
	if dt is str_date:
		return "Unresolved"
	desired_date_format="%Y-%B-%d"
	print ("desired_date_format:" , desired_date_format)
	ret_date=dt.strftime(desired_date_format)
	print ("ret_date:" , ret_date)
	return ret_date


def get_converted_date(df):
	df['new_Date Collection Verbatim DB'] = df['Date Collection Verbatim DB'].apply(lambda x: format1_date(str(x)))
	#data.to_csv('data/CleanDate.csv', index=False)
	return(df)

def combine_date_data(dirtyData, dateData):
	data = pd.merge(dirtyData, dateData[['Tracking Number', 'new_Date Collection Verbatim DB']], on=['Tracking Number'])
	#data.to_csv('data/CleanedDataSet1.csv', index=False)
	return(data)


def get_file_data(df):
	#df = pd.read_csv(fileName)
	data = df[['Tracking Number', 'Date Collection Verbatim DB','Continent', 'Country', 'Department / Province / State', 'County', 'City/Town/Hamlet', 'Specific Locale']]
	data.to_csv('data/__locationOnlyDirtyData.csv', index=False)
	return(data)



def make_request_to_geo(relativeUrl, option):
	relativeUrl = relativeUrl.replace("nan", "")
	option = option.replace("nan", "")
	params = {'address': relativeUrl, 'key': google_api_key}
	params2 = {'address': option, 'key': google_api_key}
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
	print("Cleaning File...\n")
	data['new_continent'] = data['Continent'].apply(lambda x: clean_data(str(x)))
	data["new_country"] = data["Country"].apply(lambda x: clean_data(str(x)))
	data['new_department / Province / State'] = data['Department / Province / State'].apply(lambda x: clean_data(str(x)))
	data['new_county'] = data['County'].apply(lambda x: clean_data(str(x)))
	data['new_city/Town/Hamlet'] = data['City/Town/Hamlet'].apply(lambda x: clean_data(str(x)))
	data['new_specific Locale'] = data['Specific Locale'].apply(lambda x: clean_data(str(x)))

	data.to_csv('data/__locationOnlyCleanData.csv', index=False)
	return(data)


def clean_data(data):
	if data == "NaN" or data == "nan":
		return ""
	if len(data.split()) > 3:
		return ""
	data = re.sub('[^0-9a-zA-Z\s]+', '', data)
	return "" if spell(data) == "NaN" or spell(data) == "nan" else spell(data)


def get_geo_location(df):
	print('Getting geographic coordinates...\n')
	df['new_coordinates'] = df.apply(lambda row: make_request_to_geo('{} {} {} {} {} {}'.format(row['new_continent'], row['new_country'], row['new_department / Province / State'], row['new_county'], row['new_city/Town/Hamlet'],row['new_specific Locale']), '{} {} {} {}'.format(row['new_country'], row['new_department / Province / State'], row['new_county'], row['new_city/Town/Hamlet'])), axis=1)
	df['new_latitude'] = df["new_coordinates"].apply(lambda x: "" if x == None or x == () else x[0])
	df['new_longitude'] = df["new_coordinates"].apply(lambda x: "" if x == None or x == () else x[1])
	return(df)

def combine_location_data(dirtyData, geoLocation):
	data = pd.merge(dirtyData, geoLocation[['Tracking Number', 'new_continent', 'new_country', 'new_department / Province / State', 'new_county', 'new_city/Town/Hamlet', 'new_specific Locale', 'new_coordinates', 'new_longitude', 'new_latitude']], on=['Tracking Number'])
	data.to_csv('data/CleanedDataSet.csv', index=False)
	return(data)

def runGeoreferencing(df):
	dirtyData = df
	df = get_file_data(df)
	df = clean_file(df)
	df = get_geo_location(df)
	df = get_converted_date(df)
	df = (combine_date_data(dirtyData,df))
	return(combine_location_data(dirtyData, df))





#make_request_to_geo()
#make_request_to_geo("USA")
# clean_file()
# df = get_geo_location()
# data = combine_location_data(df)
# print(data)

#df = pd.read_excel("data/DirtyDataSet.xlsx")
#runGeoreferencing(df)
