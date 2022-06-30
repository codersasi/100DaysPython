import requests
from datetime import datetime
ENDPOINT = "http://api.sunrise-sunset.org/json"
params = {
    #Bangalore Lat/Long
    'lat': 12.971599,
    'lng': 77.594566,
    'formatted': 0
}
response = requests.get(ENDPOINT, params=params)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.now()
