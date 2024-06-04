#!/usr/bin/python3
"""task 2 answer"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""
    import requests

    subs_data = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                             params={"count": count, "after": after},
                             headers={"User-Agent": "My-User-Agent"},
                             allow_redirects=False)
    if subs_data.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in subs_data.json()
                        .get("data")
                        .get("children")]

    info = subs_data.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
