from datetime import datetime
from dateutil.parser import parse
from flask import Flask
from flask import request
import os, sys
from taxonomy_clean import receive_file

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"

@app.route('/clean', methods = ['POST'])
def clean():
	if request.method == 'POST':
		data = request.get_json()
	receive_file.taxonomy_clean(data['filepath'])

if __name__ == '__main__':
	app.run(debug=True)
