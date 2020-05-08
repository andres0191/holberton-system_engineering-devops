#!/usr/bin/python3
""" Write a recursive function that queries the
    Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """function that realized get for reddit"""
    url = 'https://www.reddit.com/r/{}/.json'
    headers = {'user-agent': 'X-Modhash'}
    limit = {'limit': 101}
    if after is not None:
        limit['after'] = after
    url_format = requests.get(url.format(subreddit),
                              headers=headers, params=limit).json()
    for i in range(len(url_format['data']['children'])):
        hot_list.append(url_format['data']['children'][i]['data']['title'])
    if url_format['data']['after'] is not None:
        recurse(subreddit, hot_list, url_format['data']['after'])
    return hot_list
