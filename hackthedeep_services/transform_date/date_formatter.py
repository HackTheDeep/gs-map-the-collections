from datetime import datetime
from dateutil.parser import parse

def guess_date(string_date):
	str_date=str(string_date)
	#print ("str_date" , str_date)
	str_date.replace(" ","")
	for fmt in ["%Y/%m/%d", "%d-%m-%Y", "%Y%m%d","%B,%Y","%B%d,%Y","%B-%y","%d-%b-%y","%Y","%b-%y","%m/%d/%Y"]:
		try:
			return datetime.strptime(str_date, fmt).date()
		except ValueError:
			continue
	return str_date

def format_date(str_date):
	dt=guess_date(str_date)
	#print ("guess_date", dt)

	if dt is str_date:
		return "Unresolved"
	desired_date_format="%Y-%B-%d"
	#print ("desired_date_format:" , desired_date_format)
	ret_date=dt.strftime(desired_date_format)
	#print ("ret_date:" , ret_date)
	return ret_date