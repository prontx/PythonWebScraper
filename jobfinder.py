# Webscraper Application Implemented Using Python
# jobfinder.py - contains function definition for script mode 1
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup

def jobFinder():
    # Basic link that will be added to later on
    link = 'https://www.linkedin.com/jobs/search?'
    print('Enter the job you are looking for: ')
    jobName = str(input())
    print('Enter the location you would want to work from: ')
    jobPreferredLocation = str(input())
    # Personalizing the URL
    link += f'keywords = {jobName}&location={jobPreferredLocation}'
    searchResult = requests.get(link)
    parsedPage = BeautifulSoup(searchResult.content, 'html.parser')
    # Returns a list of active positions
    jobPositions = parsedPage.find_all("div", class_="base-card base-card--link base-search-card base-search-card--link job-search-card")
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
