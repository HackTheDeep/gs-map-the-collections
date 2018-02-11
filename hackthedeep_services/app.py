import StringIO
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
	f = request.files['data_file']
	if not f:
		return "No file"
	stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
	csv_input = csv.reader(stream)
	#print("file contents: ", file_contents)
	#print(type(file_contents))
	print(csv_input)
	for row in csv_input:
		print(row)

	stream.seek(0)
	result = transform(stream.read())
	result_after_taxonomy_clean = receive_file.taxonomy_clean(result)
	result_after_date_clean = date_transformer.transform_date(result_after_taxonomy_clean)
	return 'Successful'

if __name__ == '__main__':
	app.run(debug=True)
