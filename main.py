# Webscraper Application Implemented Using Python
# main.py - runner script
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import jobfinder as jf
import covid as c

def runnerFunction():
    print('Hello! Please select script mode: ')
    modeNumber = int(input())
    if modeNumber == 1:
        jf.jobFinder()
    elif modeNumber == 2:
        c.covidStats()

if __name__ == "__main__":
    runnerFunction()