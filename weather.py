# Webscraper Application Implemented Using Python
# weather.py - contains function definition for script mode 3.
#              Asks for a city name, then prints weather forecast.
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import json
import os
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import re

# Enables processing the local .env file,
# then looks up key-value pairs in it and assigns 
# them to variables.
load_dotenv()
USER_AGENT = os.getenv('USER_AGENT')
API_KEY    = os.getenv('API_KEY')

# To keep track of invalid inputs, once the number reaches 10 the application exits
invalidEntryCounter = 0

def weatherInCity():
    print('Enter the city you want the forecast for: ')

    inputToBeChecked = input()

    # For global variables to be changed in all scopes
    global invalidEntryCounter

    # Handling cases when more than twenty digits are input
    if len(inputToBeChecked) > 20:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    # Making sure the input is a string, possibly with whitespaces
    if re.match('[A-Z]*', inputToBeChecked):
        city = str(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    geolocator = Nominatim(user_agent=USER_AGENT)
    if geolocator:
        location = geolocator.geocode(city)
    else:
        print('Something went wrong\n')
        exit(1)
    if location:
        latitude = location.raw['lat']
        longitude = location.raw['lon']
    else:
        print('Something went wrong\n')
        exit(1)
    apiKey = API_KEY
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (latitude, longitude, apiKey)
    response = requests.get(url)
    if response:
        data = json.loads(response.text)
        data = data["current"]
        print()
    else:
        print('Something went wrong\n')
        exit(1)

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
