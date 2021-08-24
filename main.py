# Webscraper Application Implemented Using Python
# main.py - main script that runs the application
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import jobfinder    as jf
import covid        as c
import weather      as w
import translator   as t
import reddit       as r
import re

# Prints the manual
def printHelp():
    print('''
        1) Jobfinder mode  -  asks for wished position and 
                              work location, scrapes data from 
                              indeed.com to find the corresponding offers.
                     
        2) COVID mode      -  asks for country name, then 
                              scrapes data from worldometers.info to
                              print new COVID statistics in a given country.
                     
        3) Weather mode    -  asks for city name, then using the geopy 
                              API prints the current weather 
                              forecast for the given city.
                     
        4) Translator mode -  asks for a language user needs a translation 
                              from, the word itself, and the destination 
                              language, uses Google Translate 
                              API to print the result.
                     
        5) Reddit mode 1   -  asks for a subreddit name, then for number of 
                              posts to be printed, uses PRAW API to 
                              achieve the result.
                     
        6) Reddit mode 2   -  asks for a post URL, prints all the comments.

        7) Help mode       -  prints the manual.    
    ''')

# To keep track of the session number and thus enable easier mode implementation
sessionCounter      = 0
# To keep track of invalid inputs, once the number reaches 10 the application exits
invalidEntryCounter = 0
def runnerFunction():
    while 1:
        # For global variables to be changed in all scopes
        global sessionCounter
        global invalidEntryCounter

        if sessionCounter == 0:
            print('Hello! Please select script mode: ')
        else: 
            print('Please select script mode or finish the app if you wish: ')
        inputToBeChecked = input()

        # Handling cases when more than one digit is input
        if len(inputToBeChecked) > 1:
            print('Cannot have that input, try again\n')
            invalidEntryCounter += 1
            if invalidEntryCounter == 10:
                print('Too many invalid entries, exiting the app')
                exit(1)
            continue

        # Using regular expressions to ensure input is an integer
        if re.match('^[0-9]$', inputToBeChecked):
            modeNumber = int(inputToBeChecked)
            if modeNumber == 1:
                jf.jobFinder()
            elif modeNumber == 2:
                c.covidStats()
            elif modeNumber == 3:
                w.weatherInCity()
            elif modeNumber == 4:
                t.translate()
            elif modeNumber == 5:
                r.mostPopularPosts()
            elif modeNumber == 6:
                r.postComments()
            elif modeNumber == 7:
                printHelp()
            sessionCounter += 1
        else:
            print('You have not entered an integer, please try again\n')
            invalidEntryCounter += 1
            if invalidEntryCounter == 10:
                print('Too many invalid entries, exiting the app')
                exit(1)
            continue

if __name__ == "__main__":
    runnerFunction()