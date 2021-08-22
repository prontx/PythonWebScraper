# Webscraper Application Implemented Using Python
# covid.py - contains function definition for script mode 2
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup

def covidStats():
    link = "https://www.worldometers.info/coronavirus/"
    print('Enter the country: ')
    country = str(input())
    unparsedPage = requests.get(link)
    parsedPage = BeautifulSoup(unparsedPage.content, 'html.parser')
    selectedCountry = parsedPage.find("a", text=country)
    parentElement = selectedCountry.parent.parent
    statistics = parentElement.find_all("td")
    print()
    counter = 0    
    for element in statistics:
        if counter == 1:
            print('\t' + 'Country name:                       ' + element.text)
        elif counter == 2:
            print('\t' + 'Total number of cases:              ' + element.text)
        elif counter == 3:
            print('\t' + 'Number of new cases:                ' + element.text)
        elif counter == 4:
            print('\t' + 'Total number of deaths:             ' + element.text)
        elif counter == 5:
            print('\t' + 'New deaths:                         ' + element.text)
        elif counter == 6:
            print('\t' + 'Total recovered:                    ' + element.text)
        elif counter == 7:
            print('\t' + 'New recovered:                      ' + element.text)
        elif counter == 8:
            print('\t' + 'Active cases:                       ' + element.text)
        elif counter == 9:
            print('\t' + 'Serious/critical:                   ' + element.text)
        elif counter == 10:
            print('\t' + 'Total # of cases per 1M population: ' + element.text)
        elif counter == 11:
            print('\t' + 'Total number of tests:              ' + element.text)
        elif counter == 12:
            print('\t' + 'Number of tests per 1M population:  ' + element.text)
        counter += 1
    print()