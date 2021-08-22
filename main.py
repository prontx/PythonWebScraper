# Webscraper Application Implemented Using Python
# main.py - runner script
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import jobfinder as jf
import covid as c
import weather as w

sessionCounter = 0
def runnerFunction():
    while 1:
        global sessionCounter
        if sessionCounter == 0:
            print('Hello! Please select script mode: ')
        else: 
            print('Please select script mode or finish the app if you wish: ')
        modeNumber = int(input())
        if modeNumber == 1:
            jf.jobFinder()
        elif modeNumber == 2:
            c.covidStats()
        elif modeNumber == 3:
            w.weatherInCity()
        sessionCounter += 1

if __name__ == "__main__":
    runnerFunction()