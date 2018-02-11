import StringIO
import io
import csv
from datetime import datetime
from dateutil.parser import parse
from flask import Flask
from flask import request
import os, sys
from taxonomy_clean import receive_file
from transform_date import date_transformer

app = Flask(__name__)


def transform(text_file_contents):
    return text_file_contents.replace("=", ",")

@app.route('/')
def index():
	return "Hello World!"

@app.route('/mapTheCollections', methods = ['POST'])
def mapTheCollections():
	file_as_string = request.json.get('filepath')
	arr_file = list(csv.reader(file_as_string.splitlines()))
	with open('result.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(arr_file)

	result_after_taxonomy_clean = receive_file.taxonomy_clean('result.csv')
	#result_after_date_clean = date_transformer.transform_date(result_after_taxonomy_clean)
	return 'Successful'

if __name__ == '__main__':
	app.run(debug=True)
