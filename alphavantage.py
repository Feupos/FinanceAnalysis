import pandas as pd
import urllib
import json

API_KEY = open("alphavantage-key").read()

def stock_time_series(function, symbol):

	url_request = 'https://www.alphavantage.co/query?'\
			'function=' + function +\
			'&symbol=' + symbol +\
			'&apikey=' + API_KEY

	#data = pd.read_json(url_request)

	with urllib.request.urlopen(url_request) as url:
	    data = json.loads(url.read().decode())
	
	return data

def main():
	print('Alpha Vantage Python API')

if __name__ == "__main__":
    main()