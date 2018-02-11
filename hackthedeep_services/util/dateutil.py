from datetime import datetime
from dateutil.parser import parse
from autocorrect import spell
def guess_date(str_date):
	str_date.replace(" ","")
	for fmt in ["%Y/%m/%d", "%d-%m-%Y", "%Y%m%d","%B,%Y","%B%d,%Y","%B-%y","%d-%b-%y","%Y","%b-%y","%m/%d/%Y"]:
		try:
			return datetime.strptime(str_date, fmt).date()
		except ValueError:
			continue
	return str_date

def format_to_date(str_date):
	dt=guess_date(str_date)
	print ("guess_date", dt)
	if dt is str_date:
		return "Unresolved"
	desired_date_format="%Y-%B-%d"
	return dt.strftime(desired_date_format)

def cleanDate(date_str):
	strData = date_str.split(' ')
	x = spell(strData[0])
	date_str.replace(strData[0],x)
	if("summer of" in date_str.lower()):	
		return (date_str.replace("summer of","June"))
	if("summer" in date_str.lower()):	
		return (date_str.replace("summer","June"))
	elif ("winter of" in date_str.lower()):
		return (date_str.replace("winter of","December"))	
	elif ("winter" in date_str.lower()):
		return (date_str.replace("winter","December"))
	elif ("christmas" in date_str.lower()):
		return (date_str.replace("winter","December"))
	elif ("xmas" in date_str.lower()):
		return (date_str.replace("winter","December"))
	elif ("spring" in date_str.lower()):
		return (date_str.replace("spring","March"))
	elif ("spring of" in date_str.lower()):
		return (date_str.replace("spring of","June"))
	return date_str
		
