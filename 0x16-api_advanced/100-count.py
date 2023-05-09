#!/usr/bin/python3
""" script for recursive function that queries the Reddit API"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API and counts the occurrences of given
    keywords in the titles of all hot articles.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of words to count the occurrences
        of in the titles of all hot articles.
        after (str): The fullname of the last item already seen by
        the function. Used for pagination.
        counts (dict): A dictionary to store the counts of each word.

    Returns:
        None
    """
    """
    Base case: if subreddit is invalid or no more posts, print
    the counts in the required format and return
    """
    if subreddit is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
        return

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    """check if subreddit is invalid"""
    if response.status_code != 200:
        print(None)
        return

    """Get data from the response"""
    data = response.json()["data"]
    after = data["after"]
    posts = data["children"]

    """
    Count the occurrences of each word in the
    titles of all hot articles
    """
    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            if title.count(word) > 0:
                counts[word] = counts.get(word, 0) + title.count(word)

    """
    Recursively call the function with the fullname
    of the last item already seen by the function
    """
    count_words(subreddit, word_list, after, counts)
