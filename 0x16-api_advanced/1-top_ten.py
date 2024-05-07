#!/usr/bin/python3
""" script that queries the Reddit API and
    prints the titles of the first 10 subreddit
"""
import requests
from sys import argv


def top_ten(subreddit):
    """ returns the first 10 hot posts"""
    user = {'User-Agent': 'baby reindeer'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
