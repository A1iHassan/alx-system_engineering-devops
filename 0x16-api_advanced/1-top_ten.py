#!/usr/bin/python3
"""task 1 answer"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    sub_data = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_data.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_data.json().get("data").get("children")]
