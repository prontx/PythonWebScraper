# Webscraper Application Implemented Using Python
# translator.py - contains function definition for script mode 4.
#                 Asks for a source language, word/phrase to be translated,
#                 returns the translation to the destination language.
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import re

# To keep track of invalid inputs, once the number reaches 10 the application exits
invalidEntryCounter = 0

def translate():
    print('Enter the language you want a translation from: ')
    inputToBeChecked = input()

    # For global variables to be changed in all scopes
    global invalidEntryCounter

    # Handling cases when more than five digits are input
    if len(inputToBeChecked) > 5:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    # Making sure the input is a string, possibly with whitespaces
    if re.match('[A-Z]*', inputToBeChecked):
        sourceLanguage = str(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    print('Enter the word you want to translate: ')
    inputToBeChecked = input()

    # Handling cases when more than a thousand digits are input
    if len(inputToBeChecked) > 1000:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    # Making sure the input is a string, possibly with whitespaces
    if re.match('[A-Z]*', inputToBeChecked):
        sourceWord = str(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    print('Enter the language you want a translation to: ')
    inputToBeChecked = input()

    # Handling cases when more than five digits are input
    if len(inputToBeChecked) > 5:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    # Making sure the input is a string, possibly with whitespaces
    if re.match('[A-Z]*', inputToBeChecked):
        destinationLanguage = str(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return


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

if __name__ == "__main__":
    translate()