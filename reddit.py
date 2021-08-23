# Webscraper Application Implemented Using Python
# reddit.py - contains function definition for script modes 5 and 6
# Author: Matsvei Hauryliuk, FIT VUT Student
# Github: @prontx

import requests
from bs4 import BeautifulSoup
import praw
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID         = os.getenv('CLIENT_ID')
CLIENT_SECRET     = os.getenv('CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

def mostPopularPosts():
    print()
    print('Enter a subreddit that interests you: ')
    enteredSubreddit = str(input())
    print()
    print('Enter a number of top posts you wish to see: ')
    enteredNumberOfPosts = int(input())

    newPosts = reddit.subreddit(enteredSubreddit).top(limit=enteredNumberOfPosts)
    postCounter = 0
    print()
    for newPost in newPosts:
        postCounter += 1
        print(str(postCounter) + " " + newPost.title)
        print('\t' + str(newPost.score))
        print()


def postComments():
    print()
    print('Please enter the URL of the post you wish to scrape: ')
    link = str(input())
    submission = reddit.submission(url=link)
    submission.comments.replace_more(limit=0)
    print()
    for top_level_comment in submission.comments():
        print(top_level_comment.body)
    print()    