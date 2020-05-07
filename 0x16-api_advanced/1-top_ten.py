#!/usr/bin/python3
"""Write a function that queries the Reddit
   API and prints the titles of the first 10
   hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/.json'
    headers = {'user-agent': 'X-Modhash'}
    url_format = requests.get(url.format(subreddit), headers=headers).json()
    if (url_format):
        for i in range(10):
            title = url_format['data']['children'][i]['data']['title']
            print (title)
    return (None)
