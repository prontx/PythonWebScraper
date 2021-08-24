# Webscraper Application Implemented Using Python
# covid.py - contains function definition for script mode 2.
#            Prints latest covid info about a country.
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import re

# To keep track of invalid inputs, once the number reaches 10 the application exits
invalidEntryCounter = 0

def covidStats():
    link = "https://www.worldometers.info/coronavirus/"
    print('Enter the country: ')
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
        country = str(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    unparsedPage = requests.get(link)
    parsedPage = BeautifulSoup(unparsedPage.content, 'html.parser')
    selectedCountry = parsedPage.find("a", text=country)

    if selectedCountry:
        parentElement = selectedCountry.parent.parent
    else:
        print('Something went wrong\n')
        exit(1)

    if parentElement:
        statistics = parentElement.find_all("td")
    else:
        print('Something went wrong\n')
        exit(1)

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

if __name__ == "__main__":
    covidStats()