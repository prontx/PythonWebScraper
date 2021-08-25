# Webscraper Application Implemented Using Python
# reddit.py - contains function definition for script modes 5 and 6
#             Mode 5 prints best posts on a given subreddit,
#             mode 6 prints the comments to a given post.
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import praw
import os
from dotenv import load_dotenv
import re

load_dotenv()
CLIENT_ID         = os.getenv('CLIENT_ID')
CLIENT_SECRET     = os.getenv('CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

# To keep track of invalid inputs, once the number reaches 10 the application exits
invalidEntryCounter = 0

def mostPopularPosts():
    print()
    print('Enter a subreddit that interests you: ')

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
        enteredSubreddit = str(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    print()
    print('Enter a number of top posts you wish to see: ')

    inputToBeChecked = input()

    # Handling cases when more than three digits are input
    if len(inputToBeChecked) > 3:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    # Making sure the input is an integer, possibly with whitespaces
    if re.match('[0-9]*', inputToBeChecked):
        enteredNumberOfPosts = int(inputToBeChecked)
    else:
        print('Cannot have that input, try again\n')
        invalidEntryCounter += 1
        if invalidEntryCounter == 10:
            print('Too many invalid entries, exiting the app')
            exit(1)
        return

    newPosts = reddit.subreddit(enteredSubreddit).top(limit=enteredNumberOfPosts)
    if newPosts:
        postCounter = 0
        print()
        for newPost in newPosts:
            postCounter += 1
            print(str(postCounter) + " " + newPost.title)
            print('\t' + str(newPost.score))
            print()
    else:
        print('Something went wrong\n')
        exit(1)


def postComments():
    print()
    print('Please enter the URL of the post you wish to scrape: ')
    link = str(input())
    submission = reddit.submission(url=link)
    if submission:
        submission.comments.replace_more(limit=0)
    else:
        print('Something went wrong\n')
        exit(1)
    print()
    for top_level_comment in submission.comments():
        print(top_level_comment.body)
    print()    

if __name__ == "__main__":
    mostPopularPosts()
    postComments()