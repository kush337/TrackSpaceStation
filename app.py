from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
	iss_response = requests.get('http://api.open-notify.org/iss-now.json')
	json_data = iss_response.content
	json_dict = json.loads(json_data)

	lat = json_dict['iss_position']['latitude']
	lon = json_dict['iss_position']['longitude'] 	
	return render_template('index.html', lat=lat, lon=lon)


if __name__ == '__main__':
	app.run(debug=True)