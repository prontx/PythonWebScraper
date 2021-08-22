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
    data = data["current"]
    print()

    currentTemp = data["temp"]
    print(f'\tCurrent temperature is: {currentTemp}°C')

    feelsLike = data["feels_like"]
    print(f'\tWeather feels like:     {feelsLike}°C')

    pressure = data["pressure"]
    print(f'\tThe pressure is:        {pressure}')

    humidity = data["humidity"]
    print(f'\tThe humidity is:        {humidity}')

    clouds = data["clouds"]
    print(f'\tClouds:                 {clouds}')

    windSpeed = data["wind_speed"]
    print(f'\tWind speed:             {windSpeed}')

    currentWeather = data["weather"][0]["main"]
    print(f'\tCurrent weather:        {currentWeather}')

    print()
