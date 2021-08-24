# Webscraper Application Implemented Using Python
# jobfinder.py - contains function definition for script mode 1.
#                Asks for job name, job location, prints open positions
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import re

# To keep track of invalid inputs, once the number reaches 10 the application exits
invalidEntryCounter = 0

def jobFinder():
    # Basic link that will be added to later on
    link = 'https://www.linkedin.com/jobs/search?'
    print('Enter the job you are looking for: ')

    inputToBeChecked = input()

    # For global variables to be changed in all scopes
    global invalidEntryCounter

    # Handling cases when more than thirty digits are input
    if len(inputToBeChecked) > 30:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    # Making sure the input is a string, possibly with whitespaces
    if re.match('[A-Z]*', inputToBeChecked):
        jobName = str(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    print('Enter the location you would want to work from: ')

    inputToBeChecked = input()

    # Handling cases when more than thirty digits are input
    if len(inputToBeChecked) > 30:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    # Making sure the input is a string, possibly with whitespaces
    if re.match('[A-Z]*', inputToBeChecked):
        jobPreferredLocation = str(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    # Personalizing the URL
    link += f'keywords = {jobName}&location={jobPreferredLocation}'
    searchResult = requests.get(link)
    if searchResult:
        parsedPage = BeautifulSoup(searchResult.content, 'html.parser')
    else:
        print('Something went wrong\n')
        exit(1)
    # Returns a list of active positions
    if parsedPage:
        jobPositions = parsedPage.find_all("div", class_="base-card base-card--link base-search-card base-search-card--link job-search-card")
    else:
        print('Something went wrong\n')
        exit(1)
    # A counter to keep track of job number
    jobCounter = 0
    print()
    for jobPosition in jobPositions:
        jobCounter += 1
        positionName = jobPosition.find("span", class_="screen-reader-text")
        print(str(jobCounter) + ' ' + positionName.text.strip()) 
        organisationName = jobPosition.find("a", class_="hidden-nested-link")
        print('\t' + organisationName.text.strip())
        jobLocation = jobPosition.find("span", class_="job-search-card__location")
        print('\t' + jobLocation.text.strip())
        jobDescription = jobPosition.find("p", class_="job-search-card__snippet")
        print('\t' + jobDescription.text.strip())
        print()
