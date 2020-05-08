def recurse(subreddit, hot_list=[])def recurse(subreddit, hot_list=[])
"""Write a function that queries the Reddit
   API and prints the titles of the first 10
   hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ function that return the first 10 hot post"""
    url = 'https://www.reddit.com/r/{}/.json'
    headers = {'user-agent': 'X-Modhash'}
    url_format = requests.get(url.format(subreddit), headers=headers).json()
    try:
        for i in range(10):
            title = url_format['data']['children'][i]['data']['title']
            print(title)
    except:
        print(None)
