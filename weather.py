# Webscraper Application Implemented Using Python
# weather.py - contains function definition for script mode 3
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import json
import os
from geopy.geocoders import Nominatim
from dotenv import load_dotenv

load_dotenv()
USER_AGENT = os.getenv('USER_AGENT')
API_KEY    = os.getenv('API_KEY')

def weatherInCity():
    print('Enter the city you want the forecast for: ')
    city = str(input())
    geolocator = Nominatim(user_agent=USER_AGENT)
    location = geolocator.geocode(city)
    latitude = location.raw['lat']
    longitude = location.raw['lon']
    apiKey = API_KEY
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (latitude, longitude, apiKey)
    response = requests.get(url)
    data = json.loads(response.text)
    currentTemp = data["current"]["temp"]
    print(f'\tCurrent temperature in {city} is: {currentTemp}°C')
    print()
