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


if __name__ == '__main__':
	app.run(debug=True)
