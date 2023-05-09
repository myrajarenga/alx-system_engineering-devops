#!/usr/bin/python3
""" script to retrive no of subscriber in subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ return no of suns in subreddit"""

    url = "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit)
    headers = {'User-Agent': 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
