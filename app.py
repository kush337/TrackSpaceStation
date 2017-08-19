from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
	response = requests.get('http://api.open-notify.org/iss-now.json')
	json_data = response.json()
	json_dict = json.loads(json_data) 	
	return json_dict


if __name__ == '__main__':
	app.run(debug=True)