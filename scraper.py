import requests
import datetime
import threading
currentDT = datetime.datetime.now()
from pprint import pprint

def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID={api, key}&units=metric');
	return res.json();
def print_weather(result,city):
	import time
	while True:
		import datetime
		currentDT = datetime.datetime.now()
		print("{}'s Current Temp: {},".format(city,result['main']['temp']), "{}'s Humidity: {}%, ".format(city,result['main']['humidity']), str(currentDT), file=open("officetemp.db", "a") )
		time.sleep(300)
def main():
	city='Melbourne'
	print()
	try:
	  query='q='+city; 
	  w_data=weather_data(query);
	  print_weather(w_data, city)
	  print()
	except:
	  print('City name not found...')

if __name__=='__main__':
	main()
