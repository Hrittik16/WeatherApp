import urllib.request
import json

def kelvinToCelcius(temperature):
	celcius = temperature - 273.15
	return celcius

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
city = "Kolkata"
apikey = "7b09572fed2b8b1141cd8d2dc9b61270"
#This is the url from where we will extract data
url = api_endpoint + "?q=" + city + "&appid=" + apikey  
# urlopen function opens the url and stores it in response
response = urllib.request.urlopen(url)
# Store the json data
data = response.read()
# Now, we will parse the json data to use it later
parseResponse = json.loads(data)

temperature = parseResponse['main']['temp']
weather = parseResponse['weather'][0]['description']

print("Weather in " + city)
print("%.2f degree celcius" % (kelvinToCelcius(temperature)))
print("Weather Status : " + weather)