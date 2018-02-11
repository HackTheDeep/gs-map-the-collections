from datetime import datetime
from dateutil.parser import parse
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"

@app.route('/clean')
def clean():
	return "transform endpoint"

@app.route('/enrich')
def enrich():
	return "enrich endpoint"

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

if __name__ == '__main__':
	app.run(debug=True)
