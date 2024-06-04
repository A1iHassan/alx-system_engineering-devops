#!/usr/bin/python3
"""task 1 answer"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    subs_data = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                             .format(subreddit),
                             headers={"User-Agent": "My-User-Agent"},
                             allow_redirects=False)
    if subs_data.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in subs_data.json().get("data").get("children")]
