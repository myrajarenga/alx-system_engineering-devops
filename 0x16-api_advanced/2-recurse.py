#!/usr/bin/python3
""" a script for a recursive function that queries the Reddit API and returns a list\
containing the titles of all hot articles for a given subreddi"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ function takes in a subreddit name and an optional empty list to start with"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else None
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children')
            for child in children:
                hot_list.append(child.get('data').get('title'))
            after = data.get('after')
            if after:
                recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None
