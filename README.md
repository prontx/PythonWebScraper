# PythonWebScraper
A simple web scraper application in Python.

The application is run using the **main.py** file. The user is free to select an application mode. Based on provided information the script runs a loop
and with each iteration the selected mode is executed.

The modes are:
```
1) Jobfinder mode -  asks for wished position and 
                     work location, scrapes data from 
                     indeed.com to find the corresponding offers.
                     Sample input: 
                     $ Software Developer
                     $ Brno
                     
2) COVID mode -      asks for country name, then 
                     scrapes data from worldometers.info to
                     print new COVID statistics in a given country.
                     Sample input: 
                     $ Finland
                     
3) Weather mode -    asks for city name, then using the geopy 
                     API prints the current weather 
                     forecast for the given city.
                     Sample input: 
                     $ Tokyo
                     
4) Translator mode - asks for a language user needs a translation 
                     from, the word itself, and the destination 
                     language, uses Google Translate 
                     API to print the result.
                     Sample input: 
                     $ en
                     $ What's the weather today?
                     $ es
                     
5) Reddit mode 1   - asks for a subreddit name, then for number of 
                     posts to be printed, uses PRAW API to 
                     achieve the result.
                     Sample input: 
                     $ AskReddit
                     $ 3
                     
6) Reddit mode 2   - asks for a post URL, prints all the comments.
                     Sample input:
                     $ https://www.reddit.com/r/AskReddit/comments/pamk79/what_would_you_rename_america_if_you_could_rename/
                     
7) Help mode       - prints the manual.
```
