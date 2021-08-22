# Webscraper Application Implemented Using Python
# translator.py - contains function definition for script mode 4
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup

def translate():
    print('Enter the language you want a translation from: ')
    sourceLanguage = str(input())
    print('Enter the word you want to translate: ')
    sourceWord = str(input())
    print('Enter the language you want a translation to: ')
    destinationLanguage = str(input())

    import http.client
    conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")
    payload = "q=" + sourceWord + "&format=text&target=" + destinationLanguage +"&source=" + sourceLanguage
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-key': "03e84d1cebmsh8393172a48e2fb0p137f01jsn5239041898af",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }
    conn.request("POST", "/language/translate/v2", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode('utf-8')
    # Turns the decoded string into dictionary for to be easier to process later
    result = eval(result)
    # Gets the translation itself
    result = result["data"]["translations"][0]["translatedText"]
    print(f'The translation of your word/phrase is: {result}')
    print()