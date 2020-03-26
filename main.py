import urllib.request
import json

def fahrenheitToCelcius(temperature):
	celcius = (temperature-32)/1.8000
	return celcius

api_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
city = "Kolkata"
apikey = "7b09572fed2b8b1141cd8d2dc9b61270"
#This is the url from where we will extract data
url = api_endpoint + "?q=" + city + "&APPID=" + apikey  
# urlopen function opens the url and stores it in response
response = urllib.request.urlopen(url)
# Store the json data
data = response.read()
# Now, we will parse the json data to use it later
parseResponse = json.loads(data)

temperature = parseResponse['list'][0]['main']['temp']
weather = parseResponse['list'][0]['weather'][0]['description']

print("%.3f degree celcius" % (fahrenheitToCelcius(temperature)))
print(city + " has a " + weather)